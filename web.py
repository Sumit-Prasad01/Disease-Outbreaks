import os
import pickle # pre trained model loading
import streamlit as st    # web app
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")
# diabetes_model= pickle.load(open(r"C:\Users\padha\Documents\disease outbreaks\saved_models\saved_models\diabetes_model.sav",'rb'))

# heart_disease_model=pickle.load(open(r"C:\Users\padha\Documents\disease outbreaks\saved_models\saved_models\heart_disease_model.sav",'rb'))

# parkinsons_model= pickle.load(open(r"C:\Users\padha\Documents\disease outbreaks\saved_models\saved_models\parkinsons_model.sav",'rb'))

with st.sidebar:
    selected= option_menu('Prediction of disease outbreak system',
                          ['Diabetes Prediction','Heart Disease Prediction','Parkinsons Prediction'],
                          menu_icon='hospital-fill',icons=['activity','heart','person'],default_index=0)
    
# For Diabetes

if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using Ml')
    col1,col2,col3 = st.columns(3)
    with col1:
        Pregnancies= st.text_input('Number of Pregnancies')
    with col2:
        Glucose= st.text_input('Glucose level')
    with col3:
        Bloodpressure= st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin= st.text_input('Insulin level')
    with col3:
        BMI = st.text_input('BMI  value')
    with col1:
        DiabetesPedigreeFunction= st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age= st.text_input('Age of the person')

# diab_diagnosis = ''
# if st.button('Diabetes Test Result'):
#     user_input=[Pregnancies, Glucose, Bloodpressure, SkinThickness, Insulin,
#                       BMI, DiabetesPedigreeFunction, Age]
#     user_input= [float(x) for x in user_input]
#     diab_prediction= diabetes_model.predict([user_input])
#     if diab_prediction[0]==1:
#         diab_diagnosis= 'The person is diabetic'
#     else:
#         diab_diagnosis= 'The person is not diabetic'
# st.success(diab_diagnosis)
    

# For Heart Disease

if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.selectbox('Sex', ['Male', 'Female'])
    with col3:
        cp = st.selectbox('Chest Pain Type', ['Typical Angina', 'Atypical Angina', 'Non-anginal Pain', 'Asymptomatic'])
    
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol Level')
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', ['Yes', 'No'])
    
    with col1:
        restecg = st.selectbox('Resting Electrocardiographic Results', ['Normal', 'Having ST-T wave abnormality', 'Showing probable or definite left ventricular hypertrophy'])
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.selectbox('Exercise Induced Angina', ['Yes', 'No'])
    
    with col1:
        oldpeak = st.text_input('Depression Induced by Exercise Relative to Rest')
    with col2:
        slope = st.selectbox('Slope of the Peak Exercise ST Segment', ['Up', 'Flat', 'Down'])
    with col3:
        ca = st.selectbox('Number of Major Vessels Colored by Fluoroscopy', ['0', '1', '2', '3'])
    
    with col1:
        thal = st.selectbox('Thalassemia', ['Normal', 'Fixed Defect', 'Reversible Defect'])



# heart_diagnosis = ''

# if st.button('Diabetes Test Result'):
#     user_input = [
#         age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, 
#         oldpeak, slope, ca, thal
#     ]

#     sex_map = {'Male': 0, 'Female': 1}
#     cp_map = {'Typical Angina': 0, 'Atypical Angina': 1, 'Non-anginal Pain': 2, 'Asymptomatic': 3}
#     fbs_map = {'Yes': 1, 'No': 0}
#     restecg_map = {'Normal': 0, 'Having ST-T wave abnormality': 1, 'Showing probable or definite left ventricular hypertrophy': 2}
#     exang_map = {'Yes': 1, 'No': 0}
#     slope_map = {'Up': 0, 'Flat': 1, 'Down': 2}
#     ca_map = {'0': 0, '1': 1, '2': 2, '3': 3}
#     thal_map = {'Normal': 0, 'Fixed Defect': 1, 'Reversible Defect': 2}

#     user_input[1] = sex_map[sex]
#     user_input[2] = cp_map[cp]
#     user_input[5] = fbs_map[fbs]
#     user_input[6] = restecg_map[restecg]
#     user_input[8] = exang_map[exang]
#     user_input[10] = slope_map[slope]
#     user_input[11] = ca_map[ca]
#     user_input[12] = thal_map[thal]

#     user_input = [float(x) if isinstance(x, (int, float)) else x for x in user_input]

#     heart_prediction = heart_model.predict([user_input])

#     if heart_prediction[0] == 1:
#         heart_diagnosis = 'The person has heart disease.'
#     else:
#         heart_diagnosis = 'The person does not have heart disease.'

#     st.success(heart_diagnosis)



# For Parkinsons Disease

if selected == 'Parkinsons Prediction':
    st.title('Parkinsons Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        MDVP_Fo = st.text_input('MDVP:Fo (Hz)')
    with col2:
        MDVP_Fhi = st.text_input('MDVP:Fhi (Hz)')
    with col3:
        MDVP_Flo = st.text_input('MDVP:Flo (Hz)')
    
    with col1:
        MDVP_Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col2:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col3:
        MDVP_RAP = st.text_input('MDVP:RAP')
    
    with col1:
        MDVP_PPQ = st.text_input('MDVP:PPQ')
    with col2:
        Jitter_DDP = st.text_input('Jitter:DDP')
    with col3:
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
    
    with col1:
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col2:
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
    with col3:
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
    
    with col1:
        MDVP_APQ = st.text_input('MDVP:APQ')
    with col2:
        Shimmer_DDA = st.text_input('Shimmer:DDA')
    with col3:
        NHR = st.text_input('NHR')
    
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    
    with col1:
        spread1 = st.text_input('spread1')
    with col2:
        spread2 = st.text_input('spread2')
    with col3:
        D2 = st.text_input('D2')
    
    with col1:
        PPE = st.text_input('PPE')


# parkinsons_diagnosis = ''

# if st.button('Parkinson’s Test Result'):
#     user_input = [
#         MDVP_Fo, MDVP_Fhi, MDVP_Flo, MDVP_Jitter_percent, MDVP_Jitter_Abs, MDVP_RAP, 
#         MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, 
#         MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE
#     ]

#     user_input = [float(x) for x in user_input]

#     parkinsons_prediction = parkinsons_model.predict([user_input])

#     if parkinsons_prediction[0] == 1:
#         parkinsons_diagnosis = 'The person has Parkinson’s disease'
#     else:
#         parkinsons_diagnosis = 'The person does not have Parkinson’s disease'

#     st.success(parkinsons_diagnosis)
