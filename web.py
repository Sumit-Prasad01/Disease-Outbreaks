import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Prediction of Disease Outbreaks",
                   layout="wide",
                   page_icon="doctor")

# diabetes_model = pickle.load(open(r"C:/Users/sumit/OneDrive/Desktop/Internship-Project/saved_models/diabetes_model.sav", "rb"))/

diabetes_model = pickle.load(open(r"C:\Users\sumit\OneDrive\Desktop\Internship-Project\saved_models\diabetes_model.sav", 'rb'))

# file_path=r"./saved_models/diabetes_model.sav"

# with open(file_path, "rb") as file:
#     diabetes_model = pickle.load(file)

print("Model loaded successfully")

# heart_model = pickle.load(open(r"C:/Users/sumit/OneDrive/Desktop/Internship-Project/training_models/heart_model/heart_model.ipynb", "rb"))

# parkinsons_model = pickle.load(open(r"//pass", "rb"))

with st.sidebar:
    selected = option_menu('Prediction of disease outbreaks', ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Disease Prediction'],
                           menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)



# For Diabetes Prediction
if selected == 'Diabetes Prediction':
    st.title("Diabetes Prediction with Ml")
    col1,col2,col3  = st.columns(3)
    with col1:
        Pregnencies = st.text_input('Number of pregnancies')
    with col2:
        Glucose = st.text_input('Glucose level')
    with col3:
        BloodPressure  = st.text_input('Vlood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin thickness value')
    with col2:
        Insulin = st.text_input('Insulin value')
    with col3:
        BMI = st.text_input('BMI value ')
    with col1:
        DiabetesPedegreeFunction = st.text_input('Diabetes Pedigree Function Value ')
    with col2:
        Age = st.text_input("Age of the person ")


# For Heart Disease Prediction
# For Parkinsons Disease Prediction