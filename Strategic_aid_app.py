from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load models and transformers
with open('scaler.pkl', 'rb') as file:
    scaler = pickle.load(file)

with open('pca.pkl', 'rb') as file:
    pca = pickle.load(file)

with open('country_to_int.pkl', 'rb') as file:
    country_to_int = pickle.load(file)

model_pickle = open("./clustering.pkl", "rb")
clf = pickle.load(model_pickle)

def binary_encode_country(country_name):
    # Check if country exists in the mapping
    if country_name not in country_to_int:
        return None

    # Get the integer representation of the country
    country_int = country_to_int[country_name]

    # Get the maximum number of bits (this should match your training max_bits)
    max_bits = max(country_to_int.values()).bit_length()

    # Create binary encoded features
    country_bits = [(country_int >> i) & 1 for i in range(max_bits)]

    return country_bits

def feature_engineering(data):
    life_expec_mean = 70.7838323353293
    gdpp_mean = 12157.125748502995
    child_mort_mean = 37.358682634730535

    # Child Well-being Index
    data['child_wellbeing_index'] = 1 / (data['child_mortality'] * data['total_fertility'])

    # Income vs. Cost of Living
    data['real_income'] = data['income'] / (1 + data['inflation'])

    # Life Expectancy Improvement Potential
    data['life_expectancy_potential'] = data['life_expectancy'] / data['health']

    # Additional features
    data['economic_dependence_ratio'] = data['exports'] / data['imports']
    data['health_spending_vs_gdp_ratio'] = data['health'] / data['gdpp']
    data['fertility_vs_mortality_ratio'] = data['total_fertility'] / data['child_mortality']

    data['high_childmort_rate'] = (data['child_mortality'] > child_mort_mean).astype(int)
    data['high_gdpp'] = (data['gdpp'] > gdpp_mean).astype(int)
    data['high_lif_expec'] = (data['life_expectancy'] > life_expec_mean).astype(int)

    return data

@app.route('/')
def home():
    return "Clustering API is running!"

@app.route("/allocate", methods=['POST'])
def prediction():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Extract and preprocess features
        features = {
            'child_mortality': data['child_mortality'],
            'exports': data['exports'],
            'health': data['health'],
            'imports': data['imports'],
            'income': data['income'],
            'inflation': data['inflation'],
            'life_expectancy': data['life_expectancy'],
            'total_fertility': data['total_fertility'],
            'gdpp': data['gdpp']
        }

        # Convert features to DataFrame
        features_df = pd.DataFrame([features])

        # Apply feature engineering
        features_df = feature_engineering(features_df)

        # Handle binary encoding for country
        country_bits = binary_encode_country(data['country'])
        if country_bits is None:
            return jsonify({'error': 'Invalid country name'}), 400

        # Append binary encoded country features
        for i, bit in enumerate(country_bits):
            features_df[f'country_bits_{i}'] = bit

        # Convert to array for further processing
        features_array = features_df.to_numpy()

        # Scale the features
        features_scaled = scaler.transform(features_array)

        # Apply PCA
        features_pca = pca.transform(features_scaled)

        # Predict cluster
        cluster = clf.predict(features_pca)[0]
        features_pca = pca.transform(features_scaled)
        print("values", features_pca)
        print("cluster", cluster)

        # Determine priority message
        if cluster == 0:
            return f"This is economically stable country, currently no aid needed"
           
        elif cluster == 1:
            return f"The aid allocation to this country should be on high priority, Help Needed"
            
        
        elif cluster == 2:
            return f"The aid allocation to this country should be on low priority, its an economically stable country"
            

    except Exception as e:
        return jsonify({'error': str(e)})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
