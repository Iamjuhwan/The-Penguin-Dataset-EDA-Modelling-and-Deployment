import joblib
import streamlit as st
import numpy as np

# Encoding dictionaries for categorical features
encoding_sex = {"Female": 0, "Male": 1}
encoding_clutch = {"No": 0, "Yes": 1}
encoding_island = {"Biscoe": 0, "Dream": 1, "Torgesen": 2}

# Streamlit UI components
st.title("A Penguin Prediction Web App") 
st.write("This Web App uses the *Palmer Archipelago Penguin Dataset* to predict the Specie of Penguins due to some of their features")

st.markdown('<h3 style="text-align: center;" class="title">Penguin Features</h3>', unsafe_allow_html=True)

# load the model
model = joblib.load(open('logistic 3.pkl', 'rb'))


#model = joblib.load('your_saved_model.pkl')
col1, col2 = st.columns(2)
with col1:
        body_mass = st.slider(
            "Body Mass (mm)", min_value=2700, max_value=6300, value=3000)
        flipper_Length = st.slider(
            "Flipper/Wing Length(mm)", min_value=172, max_value=231, value=200)
        culmen_Length = st.slider(
            "Culmen/Beak Length (mm)", min_value=32.1, max_value=59.6, value=40.0)
        culmen_Depth = st.slider(
            "Culmen/Beak Depth (mm)", min_value=13.1, max_value=29.5, value=20.0)    
    
with col2:
    sex = st.selectbox("Sex", list(encoding_sex.keys()),
                    help="Select Penguin's gender")
    island = st.selectbox("Island", list(encoding_island.keys()),
                    help='Select the Island the Penguin was located')
    clutch = st.selectbox("Clutch", list(encoding_clutch.keys()),
                    help='Select *Yes* or *No* depending on the presence of Clutch')
    Delta_15N = st.slider(
        "Culmen Depth (mm)", min_value=7.63220, max_value=10.02544, value=8.00000)         
    Delta_13C = st.slider(
        "Culmen Depth (mm)", min_value=-27.01854, max_value=-23.78767, value=-25.78767)         

# Encode categorical inputs
sex_encoded = encoding_sex.get(sex, -1)
clutch_encoded = encoding_clutch.get(clutch, -1)
island_encoded = encoding_island.get(island, -1)

# Create a feature vector for prediction
features = np.array([[island_encoded, clutch_encoded, culmen_Length, culmen_Depth, flipper_Length, body_mass, sex_encoded,  Delta_15N, Delta_13C]])

# Make a prediction
if st.button("Predict"):
    predictions = model.predict(features)

    if predictions == 0:
        st.write("Adelie")
    elif predictions == 1:
        st.write("Chinstrap")
    else:
        st.write("Torgesen")


# Display the app information
st.write("Please adjust the sliders and select categorical values to make predictions.")