import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Set page configuration
st.set_page_config(
    page_title="Student Dropout Prediction",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Create directories if they don't exist
if not os.path.exists("model"):
    os.makedirs("model")

def load_encoders_and_model():
    """
    Load the model, encoders, and scaler if they exist.
    If not, provide default versions for demonstration.
    """
    # Default model and encoders (for demonstration if files not found)
    model = None
    feature_names = None
    encoders = {}
    scaler = None
    
    try:
        # Try to load model and feature names
        model_files = [f for f in os.listdir("model") if f.endswith("_model.joblib")]
        if model_files:
            model = joblib.load(f"model/{model_files[0]}")
            feature_names = joblib.load("model/feature_names.joblib")
        
        # Load encoders for categorical features
        categorical_features = ['Gender', 'Scholarship_holder', 'Debtor', 
                              'Tuition_fees_up_to_date', 'Displaced', 
                              'Daytime_evening_attendance']
        
        for feature in categorical_features:
            encoder_path = f"model/encoder_{feature}.joblib"
            if os.path.exists(encoder_path):
                encoders[feature] = joblib.load(encoder_path)
            else:
                # Create default encoder
                encoders[feature] = LabelEncoder()
                if feature == 'Gender':
                    encoders[feature].classes_ = np.array(['Male', 'Female'])
                else:
                    encoders[feature].classes_ = np.array(['No', 'Yes'])
                if feature == 'Daytime_evening_attendance':
                    encoders[feature].classes_ = np.array(['Evening', 'Daytime'])
        
        # Load scaler
        scaler_path = "model/scaler_numerical_features.joblib"
        if os.path.exists(scaler_path):
            scaler = joblib.load(scaler_path)
        else:
            scaler = StandardScaler()
        
    except Exception as e:
        st.error(f"Error loading model components: {e}")
    
    return model, feature_names, encoders, scaler

def predict_dropout_risk(student_data, model, feature_names, encoders, scaler):
    """
    Predict the risk of a student dropping out.
    
    Parameters:
    -----------
    student_data : dict
        Dictionary containing student features
    model : sklearn model
        Loaded prediction model
    feature_names : list
        List of feature names in the correct order
    encoders : dict
        Dictionary of label encoders for categorical features
    scaler : sklearn scaler
        Scaler for numerical features
    
    Returns:
    --------
    dict
        Prediction results including probability and risk level
    """
    if model is None:
        return {
            'dropout_probability': 0.5,
            'graduate_probability': 0.5,
            'predicted_status': 'Demo Mode - No Model Loaded',
            'risk_level': 'Medium'
        }
    
    # Prepare the input data
    input_data = []
    
    # Encode categorical features
    categorical_features = ['Gender', 'Scholarship_holder', 'Debtor', 
                          'Tuition_fees_up_to_date', 'Displaced', 
                          'Daytime_evening_attendance']
    
    for feature in categorical_features:
        if feature in student_data and feature in encoders:
            try:
                student_data[feature] = encoders[feature].transform([student_data[feature]])[0]
            except:
                # Default to 0 if transformation fails
                student_data[feature] = 0
    
    # Scale numerical features
    numerical_features = [f for f in feature_names if f not in categorical_features]
    if len(numerical_features) > 0 and scaler is not None:
        numerical_values = [student_data.get(f, 0) for f in numerical_features]
        try:
            scaled_values = scaler.transform([numerical_values])[0]
            for i, feature in enumerate(numerical_features):
                student_data[feature] = scaled_values[i]
        except:
            # Use unscaled values if transformation fails
            pass
    
    # Create the input array in the correct order
    for feature in feature_names:
        input_data.append(student_data.get(feature, 0))
    
    # Make prediction
    input_array = np.array([input_data])
    
    # Predict both class and probability
    prediction = model.predict(input_array)[0]
    probability = model.predict_proba(input_array)[0]
    
    # Interpret the results
    result = {
        'dropout_probability': float(probability[0]),
        'graduate_probability': float(probability[1]),
        'predicted_status': 'Dropout' if prediction == 0 else 'Graduate',
        'risk_level': 'High' if probability[0] > 0.7 else 'Medium' if probability[0] > 0.3 else 'Low'
    }
    
    return result

def calculate_derived_features(data):
    """Calculate derived features from the input data"""
    # Average grade across semesters
    data['avg_grade'] = (data['Curricular_units_1st_sem_grade'] + 
                         data['Curricular_units_2nd_sem_grade']) / 2
    
    # Total approved units
    data['total_approved_units'] = (data['Curricular_units_1st_sem_approved'] + 
                                   data['Curricular_units_2nd_sem_approved'])
    
    # Total enrolled units
    data['total_enrolled_units'] = (data['Curricular_units_1st_sem_enrolled'] + 
                                   data['Curricular_units_2nd_sem_enrolled'])
    
    # Pass rate
    if data['total_enrolled_units'] > 0:
        data['pass_rate'] = (data['total_approved_units'] / 
                            data['total_enrolled_units']) * 100
    else:
        data['pass_rate'] = 0
    
    # Grade improvement
    data['grade_improvement'] = (data['Curricular_units_2nd_sem_grade'] - 
                                data['Curricular_units_1st_sem_grade'])
    
    # Performance drop indicator
    data['performance_drop'] = int((data['Curricular_units_2nd_sem_approved'] < 
                                  data['Curricular_units_1st_sem_approved']) and 
                                 (data['Curricular_units_2nd_sem_grade'] < 
                                  data['Curricular_units_1st_sem_grade']))
    
    # Approval rates
    if data['Curricular_units_1st_sem_enrolled'] > 0:
        data['approval_rate_1st_sem'] = data['Curricular_units_1st_sem_approved'] / data['Curricular_units_1st_sem_enrolled']
    else:
        data['approval_rate_1st_sem'] = 0
        
    if data['Curricular_units_2nd_sem_enrolled'] > 0:
        data['approval_rate_2nd_sem'] = data['Curricular_units_2nd_sem_approved'] / data['Curricular_units_2nd_sem_enrolled']
    else:
        data['approval_rate_2nd_sem'] = 0
    
    return data

def display_prediction_results(prediction):
    """Display the prediction results in a visually appealing way"""
    # Create columns for layout
    col1, col2 = st.columns(2)
    
    # Display prediction result
    with col1:
        st.subheader("Prediction Result")
        status_color = "green" if prediction['predicted_status'] == 'Graduate' else "red"
        st.markdown(f"<h3 style='color:{status_color};'>Predicted Status: {prediction['predicted_status']}</h3>", 
                    unsafe_allow_html=True)
        
        # Risk level with appropriate color
        risk_color = "green"
        if prediction['risk_level'] == 'Medium':
            risk_color = "orange"
        elif prediction['risk_level'] == 'High':
            risk_color = "red"
            
        st.markdown(f"<h4 style='color:{risk_color};'>Risk Level: {prediction['risk_level']}</h4>", 
                    unsafe_allow_html=True)
    
    # Display probability gauge chart
    with col2:
        st.subheader("Dropout Probability")
        
        # Create and display gauge chart using matplotlib
        fig, ax = plt.subplots(figsize=(4, 3))
        
        # Gauge chart settings
        dropout_prob = prediction['dropout_probability']
        gauge_colors = ['green', 'yellow', 'orange', 'red']
        
        # Create gauge segments
        ax.barh(0, 100, color='lightgray', height=0.5)
        
        # Add colored segments
        segment_width = 25
        for i, color in enumerate(gauge_colors):
            ax.barh(0, segment_width, left=i*segment_width, color=color, height=0.5, alpha=0.7)
        
        # Add pointer
        pointer_pos = dropout_prob * 100
        ax.plot([pointer_pos, pointer_pos], [-0.5, 0.5], color='black', linewidth=3)
        ax.plot([pointer_pos-3, pointer_pos, pointer_pos+3], [-0.5, 0, -0.5], color='black')
        
        # Format plot
        ax.set_xlim(0, 100)
        ax.set_ylim(-1, 1)
        ax.set_yticks([])
        ax.set_xticks([0, 25, 50, 75, 100])
        ax.set_xticklabels(['0%', '25%', '50%', '75%', '100%'])
        ax.set_title(f"Dropout Probability: {dropout_prob:.1%}")
        
        # Remove spines
        for spine in ax.spines.values():
            spine.set_visible(False)
            
        plt.tight_layout()
        
        # Display plot in Streamlit
        st.pyplot(fig)
    
    # Display detailed probabilities
    st.subheader("Probability Breakdown")
    prob_col1, prob_col2 = st.columns(2)
    
    with prob_col1:
        st.metric("Dropout Probability", f"{prediction['dropout_probability']:.1%}")
    
    with prob_col2:
        st.metric("Graduate Probability", f"{prediction['graduate_probability']:.1%}")

def main():
    # Load model components
    model, feature_names, encoders, scaler = load_encoders_and_model()
    
    # App title and description
    st.title("🎓 Student Dropout Prediction System")
    st.markdown("""
    This application predicts the likelihood of a student dropping out of their program based on 
    academic performance and demographic factors. Enter student information below to get a prediction.
    """)
    
    # Check if model is loaded
    if model is None:
        st.warning("⚠️ No model file found. Running in demonstration mode. Predictions will be random.")
    
    # Create tabs for different app sections
    tab1, tab2, tab3 = st.tabs(["Make Prediction", "Model Info", "About"])
    
    with tab1:
        st.header("Student Information")
        
        # Create form for user input
        with st.form("prediction_form"):
            # Create columns for better layout
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("Demographic Information")
                gender = st.selectbox("Gender", options=["Male", "Female"])
                scholarship = st.selectbox("Scholarship Holder", options=["No", "Yes"])
                debtor = st.selectbox("Debtor Status", options=["No", "Yes"])
                tuition_up_to_date = st.selectbox("Tuition Fees Up to Date", options=["Yes", "No"])
                displaced = st.selectbox("Displaced Student", options=["No", "Yes"])
                attendance = st.selectbox("Attendance Schedule", options=["Daytime", "Evening"])
                
                st.subheader("Admission Information")
                admission_grade = st.slider("Admission Grade", min_value=0, max_value=200, value=120)
                prev_qualification = st.slider("Previous Qualification Grade", min_value=0, max_value=200, value=130)
                
            with col2:
                st.subheader("First Semester Performance")
                units_1st_credited = st.slider("Curricular Units 1st Sem Credited", min_value=0, max_value=10, value=0)
                units_1st_enrolled = st.slider("Curricular Units 1st Sem Enrolled", min_value=0, max_value=10, value=6)
                units_1st_evaluations = st.slider("Curricular Units 1st Sem Evaluations", min_value=0, max_value=20, value=6)
                units_1st_approved = st.slider("Curricular Units 1st Sem Approved", min_value=0, max_value=10, value=5)
                units_1st_grade = st.slider("Curricular Units 1st Sem Grade", min_value=0, max_value=20, value=13)
                
                st.subheader("Second Semester Performance")
                units_2nd_credited = st.slider("Curricular Units 2nd Sem Credited", min_value=0, max_value=10, value=0)
                units_2nd_enrolled = st.slider("Curricular Units 2nd Sem Enrolled", min_value=0, max_value=10, value=6)
                units_2nd_evaluations = st.slider("Curricular Units 2nd Sem Evaluations", min_value=0, max_value=20, value=6)
                units_2nd_approved = st.slider("Curricular Units 2nd Sem Approved", min_value=0, max_value=10, value=5)
                units_2nd_grade = st.slider("Curricular Units 2nd Sem Grade", min_value=0, max_value=20, value=14)
            
            # Submit button
            submit_button = st.form_submit_button("Predict Dropout Risk")
            
            if submit_button:
                # Collect all input data
                student_data = {
                    'Gender': gender,
                    'Scholarship_holder': scholarship,
                    'Debtor': debtor,
                    'Tuition_fees_up_to_date': tuition_up_to_date,
                    'Displaced': displaced,
                    'Daytime_evening_attendance': attendance,
                    'Curricular_units_1st_sem_credited': units_1st_credited,
                    'Curricular_units_1st_sem_enrolled': units_1st_enrolled,
                    'Curricular_units_1st_sem_evaluations': units_1st_evaluations,
                    'Curricular_units_1st_sem_approved': units_1st_approved,
                    'Curricular_units_1st_sem_grade': units_1st_grade,
                    'Curricular_units_2nd_sem_credited': units_2nd_credited,
                    'Curricular_units_2nd_sem_enrolled': units_2nd_enrolled,
                    'Curricular_units_2nd_sem_evaluations': units_2nd_evaluations,
                    'Curricular_units_2nd_sem_approved': units_2nd_approved,
                    'Curricular_units_2nd_sem_grade': units_2nd_grade,
                    'Admission_grade': admission_grade,
                    'Previous_qualification_grade': prev_qualification
                }
                
                # Calculate derived features
                student_data = calculate_derived_features(student_data)
                
                # Make prediction
                if model is not None and feature_names is not None:
                    prediction = predict_dropout_risk(student_data, model, feature_names, encoders, scaler)
                    
                    # Display prediction results
                    display_prediction_results(prediction)
                    
                    # Recommendations based on prediction
                    st.subheader("Recommendations")
                    if prediction['risk_level'] == 'High':
                        st.error("⚠️ This student is at high risk of dropping out. Immediate intervention is recommended.")
                        st.markdown("""
                        **Suggested interventions:**
                        - Schedule an immediate academic counseling session
                        - Provide additional tutoring for challenging courses
                        - Check for financial assistance options if applicable
                        - Consider reducing course load for the next semester
                        - Regular follow-ups with academic advisor
                        """)
                    elif prediction['risk_level'] == 'Medium':
                        st.warning("⚠️ This student has some risk factors for dropping out. Monitoring is recommended.")
                        st.markdown("""
                        **Suggested interventions:**
                        - Schedule a check-in with academic advisor
                        - Identify and address specific challenge areas
                        - Consider peer mentoring or study groups
                        - Monitor academic progress closely next semester
                        """)
                    else:
                        st.success("✅ This student is likely to complete their program successfully.")
                        st.markdown("""
                        **Recommendations:**
                        - Continue with current academic plan
                        - Consider enrichment opportunities such as research or internships
                        - Regular check-ins with academic advisor for continued success
                        """)
                else:
                    st.error("Cannot make prediction: Model or feature names not loaded properly.")
    
    with tab2:
        st.header("Model Information")
        
        st.subheader("About the Prediction Model")
        st.write("""
        This application uses a machine learning model to predict the likelihood of student dropout. 
        The model was trained on historical student data with the following features:
        
        - **Academic Performance**: Course grades, number of courses passed/failed, etc.
        - **Financial Factors**: Scholarship status, debtor status, tuition payment status
        - **Demographic Information**: Gender, displacement status, etc.
        - **Enrollment Patterns**: Day/evening attendance, course load, etc.
        
        The model analyzes these factors to identify patterns associated with students who drop out versus those who graduate successfully.
        """)
        
        st.subheader("Key Dropout Risk Factors")
        st.markdown("""
        Based on the model's analysis, the following factors have the strongest influence on dropout prediction:
        
        1. **Academic Performance**: Low grades and failing courses, especially in the first semester
        2. **Financial Challenges**: Being a debtor or having unpaid tuition fees
        3. **Course Management**: Enrolling in many courses but completing few
        4. **Performance Decline**: Significant drop in performance between semesters
        """)
        
        st.subheader("Model Performance")
        st.write("""
        The model was evaluated using various metrics such as accuracy, precision, recall, and F1-score.
        The most important metric for this application is recall (ability to identify students at risk)
        and precision (avoiding false alarms).
        """)
        
        # Create dummy confusion matrix for visualization
        fig, ax = plt.subplots(figsize=(5, 4))
        cm = np.array([[85, 15], [10, 90]])  # Dummy confusion matrix
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False, ax=ax)
        ax.set_xlabel('Predicted')
        ax.set_ylabel('Actual')
        ax.set_title('Model Confusion Matrix (Example)')
        ax.set_xticklabels(['Dropout', 'Graduate'])
        ax.set_yticklabels(['Dropout', 'Graduate'])
        plt.tight_layout()
        
        st.pyplot(fig)
        
        st.caption("Note: This is a sample visualization. Actual model metrics may vary.")
    
    with tab3:
        st.header("About This Application")
        
        st.markdown("""
        ### Purpose
        
        This application was developed to help educational institutions identify students at risk of dropping out
        so that timely interventions can be made to improve retention and student success rates.
        
        ### How to Use
        
        1. Enter a student's demographic and academic information in the "Make Prediction" tab
        2. Review the prediction results, which include:
           - Probability of dropout
           - Risk level classification
           - Targeted recommendations based on risk level
        
        ### Project Background
        
        This project was developed by Moch Dani Kurniawan Sugiarto as part of:
        - Final project for Edutech company
        - Email: danisugiartolaptop12@gmail.com
        - ID Dicoding: a129ybm285
        
        ### Data Privacy Note
        
        This application does not store any entered student data. All predictions are made locally
        within the app and no information is transmitted or saved.
        """)

# Run the app
if __name__ == "__main__":
    main()
