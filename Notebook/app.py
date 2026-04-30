import streamlit as st
import pandas as pd
import pickle

# Page Config

st.set_page_config(
page_title="Student Performance Predictor",
page_icon="🎓",
layout="wide"
)

# Load Model + Encoders

model = pickle.load(open("model.pkl", "rb"))
encoders = pickle.load(open("encoders.pkl", "rb"))

# Custom Styling

st.markdown("""

<style>
.main {
    padding-top: 3rem;
}
.block-container {
    padding-top: 4rem;
    padding-bottom: 2rem;
}
.big-title {
    font-size: 42px;
    font-weight: 700;
}
.sub-text {
    color: #9ca3af;
    font-size: 16px;
}
.result-box {
    padding: 20px;
    border-radius: 16px;
    text-align: center;
    font-size: 28px;
    font-weight: bold;
}
</style>

""", unsafe_allow_html=True)

# Header

st.markdown(
'<p class="big-title">🎓 Student Performance Predictor</p>',
unsafe_allow_html=True
)
st.markdown(
'<p class="sub-text">Predict exam score using academic, family and lifestyle inputs.</p>',
unsafe_allow_html=True
)

st.divider()

# Sidebar Inputs

st.sidebar.header("⚙️ Input Controls")

# Numeric Inputs

hours = st.sidebar.slider("Hours Studied", 1, 50, 20)
attendance = st.sidebar.slider("Attendance (%)", 60, 100, 85)
sleep = st.sidebar.slider("Sleep Hours", 4, 10, 7)
previous = st.sidebar.slider("Previous Scores", 40, 100, 70)
tutoring = st.sidebar.slider("Tutoring Sessions", 0, 8, 2)
physical = st.sidebar.slider("Physical Activity", 0, 10, 3)

# Category Inputs

parental = st.sidebar.selectbox("Parental Involvement", ["Low", "Medium", "High"])
resources = st.sidebar.selectbox("Access to Resources", ["Low", "Medium", "High"])
extra = st.sidebar.selectbox("Extracurricular Activities", ["Yes", "No"])
motivation = st.sidebar.selectbox("Motivation Level", ["Low", "Medium", "High"])
internet = st.sidebar.selectbox("Internet Access", ["Yes", "No"])
income = st.sidebar.selectbox("Family Income", ["Low", "Medium", "High"])
teacher = st.sidebar.selectbox("Teacher Quality", ["Low", "Medium", "High"])
school = st.sidebar.selectbox("School Type", ["Public", "Private"])
peer = st.sidebar.selectbox("Peer Influence", ["Negative", "Neutral", "Positive"])
learning = st.sidebar.selectbox("Learning Disabilities", ["Yes", "No"])
education = st.sidebar.selectbox(
"Parental Education Level",
["High School", "College", "Postgraduate"]
)
distance = st.sidebar.selectbox(
"Distance from Home",
["Near", "Moderate", "Far"]
)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])

# Dashboard Cards

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("📚 Study Hours", hours)

with col2:
    st.metric("📅 Attendance", f"{attendance}%")

with col3:
    st.metric("😴 Sleep Hours", sleep)

st.divider()

# Prediction Button

if st.button("🚀 Predict Score", use_container_width=True):


    data = pd.DataFrame([{
        "Hours_Studied": hours,
        "Attendance": attendance,
        "Parental_Involvement": parental,
        "Access_to_Resources": resources,
        "Extracurricular_Activities": extra,
        "Sleep_Hours": sleep,
        "Previous_Scores": previous,
        "Motivation_Level": motivation,
        "Internet_Access": internet,
        "Tutoring_Sessions": tutoring,
        "Family_Income": income,
        "Teacher_Quality": teacher,
        "School_Type": school,
        "Peer_Influence": peer,
        "Physical_Activity": physical,
        "Learning_Disabilities": learning,
        "Parental_Education_Level": education,
        "Distance_from_Home": distance,
        "Gender": gender
    }])

    # Encode categorical values
    for col, encoder in encoders.items():
        if col in data.columns:
            data[col] = encoder.transform(data[col].astype(str))
    
    # Predict
    prediction = model.predict(data)[0]

    st.divider()

# Progress Bar
    score = max(0, min(100, int(prediction)))
    st.progress(score)

# Result Display
    if prediction >= 80:
        st.success(f"🌟 Predicted Exam Score: {prediction:.2f}")
        st.balloons()
    
    elif prediction >= 60:
        st.info(f"✅ Predicted Exam Score: {prediction:.2f}")
    
    else:
        st.warning(f"⚠️ Predicted Exam Score: {prediction:.2f}")

# Footer

st.divider()
st.caption("Built with Python • Pandas • Scikit-learn • Streamlit")
