import os
import pickle  
import streamlit as st  
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")

# File Paths

def load_model(file_name):
    return pickle.load(open(file_name, 'rb'))

diabetes_model = load_model(os.path.join('saved_models', 'diabetes_model.sav'))
heart_model = load_model(os.path.join('saved_models', 'heart_model.sav'))
parkinsons_model = load_model(os.path.join('saved_models', 'new_parkinsons_model.sav'))

with st.sidebar:
    selected = option_menu('Prediction of Disease Outbreak System',
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
                           menu_icon='hospital-fill', icons=['activity', 'heart', 'person'], default_index=0)

# Functions for Input Fields

def input_field(column, label):
    return column.text_input(label)

def selectbox_field(column, label, options):
    return column.selectbox(label, options)

# Functions for Prediction Logic

def diabetes_prediction():
    st.title('Diabetes Prediction using ML')
    col1, col2, col3 = st.columns(3)
    inputs = {}
    inputs['Pregnancies'] = input_field(col1, 'Number of Pregnancies')
    inputs['Glucose'] = input_field(col2, 'Glucose Level')
    inputs['Blood Pressure'] = input_field(col3, 'Blood Pressure Value')
    inputs['Skin Thickness'] = input_field(col1, 'Skin Thickness Value')
    inputs['Insulin'] = input_field(col2, 'Insulin Level')
    inputs['BMI'] = input_field(col3, 'BMI Value')
    inputs['Diabetes Pedigree Function'] = input_field(col1, 'Diabetes Pedigree Function Value')
    inputs['Age'] = input_field(col2, 'Age')

    if st.button('Diabetes Test Result'):
        user_input = [float(inputs[key]) for key in inputs]
        diab_prediction = diabetes_model.predict([user_input])
        diagnosis = 'The person is diabetic' if diab_prediction[0] == 1 else 'The person is not diabetic'
        st.success(diagnosis)

def heart_disease_prediction():
    st.title('Heart Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    inputs = {}
    inputs['Age'] = input_field(col1, 'Age')
    inputs['Sex'] = selectbox_field(col2, 'Sex', ['Male', 'Female'])
    inputs['Chest Pain Type'] = selectbox_field(col3, 'Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
    inputs['Resting Blood Pressure'] = input_field(col1, 'Resting Blood Pressure')
    inputs['Serum Cholesterol Level'] = input_field(col2, 'Serum Cholesterol Level')
    inputs['Fasting Blood Sugar'] = selectbox_field(col3, 'Fasting Blood Sugar > 120 mg/dl', ['Yes', 'No'])
    inputs['Resting ECG'] = selectbox_field(col1, 'Resting Electrocardiographic Results', ['Normal', 'Having ST-T wave abnormality', 'Showing probable or definite left ventricular hypertrophy'])
    inputs['Maximum Heart Rate Achieved'] = input_field(col2, 'Maximum Heart Rate Achieved')
    inputs['Exercise Induced Angina'] = selectbox_field(col3, 'Exercise Induced Angina', ['Yes', 'No'])
    inputs['Depression Induced by Exercise'] = input_field(col1, 'Depression Induced by Exercise Relative to Rest')
    inputs['Slope'] = selectbox_field(col2, 'Slope of the Peak Exercise ST Segment', ['Up', 'Flat', 'Down'])
    inputs['Number of Major Vessels'] = selectbox_field(col3, 'Number of Major Vessels Colored by Fluoroscopy', ['0', '1', '2', '3'])
    inputs['Thalassemia'] = selectbox_field(col1, 'Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])

    if st.button('Heart Disease Test Result'):
        sex_map = {'Male': 0, 'Female': 1}
        cp_map = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3}
        fbs_map = {'Yes': 1, 'No': 0}
        restecg_map = {'Normal': 0, 'Having ST-T wave abnormality': 1, 'Showing probable or definite left ventricular hypertrophy': 2}
        exang_map = {'Yes': 1, 'No': 0}
        slope_map = {'Up': 0, 'Flat': 1, 'Down': 2}
        ca_map = {'0': 0, '1': 1, '2': 2, '3': 3}
        thal_map = {'Normal': 0, 'Fixed Defect': 1, 'Reversible Defect': 2}

        user_input = [
            float(inputs['Age']), sex_map[inputs['Sex']], cp_map[inputs['Chest Pain Type']],
            float(inputs['Resting Blood Pressure']), float(inputs['Serum Cholesterol Level']), fbs_map[inputs['Fasting Blood Sugar']],
            restecg_map[inputs['Resting ECG']], float(inputs['Maximum Heart Rate Achieved']),
            exang_map[inputs['Exercise Induced Angina']], float(inputs['Depression Induced by Exercise']),
            slope_map[inputs['Slope']], ca_map[inputs['Number of Major Vessels']], thal_map[inputs['Thalassemia']]
        ]

        heart_prediction = heart_model.predict([user_input])
        diagnosis = 'The person has heart disease.' if heart_prediction[0] == 1 else 'The person does not have heart disease.'
        st.success(diagnosis)

def parkinsons_prediction():
    st.title('Parkinsons Disease Prediction using ML')
    col1, col2, col3 = st.columns(3)
    inputs = {}
    inputs['MDVP:Fo (Hz)'] = input_field(col1, 'MDVP:Fo (Hz)')
    inputs['MDVP:Fhi (Hz)'] = input_field(col2, 'MDVP:Fhi (Hz)')
    inputs['MDVP:Flo (Hz)'] = input_field(col3, 'MDVP:Flo (Hz)')
    inputs['MDVP:Jitter (%)'] = input_field(col1, 'MDVP:Jitter (%)')
    inputs['MDVP:Jitter (Abs)'] = input_field(col2, 'MDVP:Jitter (Abs)')
    inputs['MDVP:RAP'] = input_field(col3, 'MDVP:RAP')
    inputs['MDVP:PPQ'] = input_field(col1, 'MDVP:PPQ')
    inputs['Jitter:DDP'] = input_field(col2, 'Jitter:DDP')
    inputs['MDVP:Shimmer'] = input_field(col3, 'MDVP:Shimmer')
    inputs['MDVP:Shimmer (dB)'] = input_field(col1, 'MDVP:Shimmer (dB)')
    inputs['Shimmer:APQ3'] = input_field(col2, 'Shimmer:APQ3')
    inputs['Shimmer:APQ5'] = input_field(col3, 'Shimmer:APQ5')
    inputs['MDVP:APQ'] = input_field(col1, 'MDVP:APQ')
    inputs['Shimmer:DDA'] = input_field(col2, 'Shimmer:DDA')
    inputs['NHR'] = input_field(col3, 'NHR')
    inputs['HNR'] = input_field(col1, 'HNR')
    inputs['RPDE'] = input_field(col2, 'RPDE')
    inputs['DFA'] = input_field(col3, 'DFA')
    inputs['spread1'] = input_field(col1, 'spread1')
    inputs['spread2'] = input_field(col2, 'spread2')
    inputs['D2'] = input_field(col3, 'D2')
    inputs['PPE'] = input_field(col1, 'PPE')


    if st.button('Parkinson’s Test Result'):
        user_input = [float(inputs[key]) for key in inputs]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        diagnosis = 'The person has Parkinson’s disease' if parkinsons_prediction[0] == 1 else 'The person does not have Parkinson’s disease'
        st.success(diagnosis)

if selected == 'Diabetes Prediction':
    diabetes_prediction()
elif selected == 'Heart Disease Prediction':
    heart_disease_prediction()
elif selected == 'Parkinsons Prediction':
    parkinsons_prediction()
