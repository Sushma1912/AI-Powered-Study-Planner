import streamlit as st
from ai_engine import generate_study_plan
st.markdown("""
<style>
.block {
    background-color: white;
    color: black;
    padding: 15px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)
st.markdown("""
# 📚 AI Study Planner (Gemini Powered)
### 🚀 Your personalized learning roadmap generator
""")
topic = st.text_input("Enter Topic")
days = st.number_input("Days", min_value=1, max_value=30, value=5)
level = st.selectbox("Level", ["Beginner", "Intermediate", "Advanced"])

if st.button("Generate Plan"):
    if topic:
        with st.spinner("Generating your AI study plan..."):
            result = generate_study_plan(topic, days, level)
            st.markdown(result)
    else:
        st.warning("Please enter a topic")
