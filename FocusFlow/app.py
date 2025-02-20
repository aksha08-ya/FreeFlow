import streamlit as st
import google.generativeai as genai
import time

genai.configure(api_key="AIzaSyBdlQksMSSxo-zYv3-viYcs2xalhNBbvhA")  # Replace with your Gemini API key

st.title("Study Planner using AI")

age = st.number_input("Enter learner's age", min_value=6, max_value=80, step=1)
subject = st.text_area("Enter the subject")
topic = st.text_area("Enter the topic of your Subject")

complexity_levels = ["Beginner", "Intermediate", "Advanced"]
complexity = st.selectbox("Select the complexity", complexity_levels)

duration = ["1 week", "15 days", "10 days", "20 days", "1 month"]
plan_duration = st.selectbox("Choose your duration", duration)

if st.button("Generate schedule"):
    prompt = f"""
    You are an expert tutor. Create a detailed study schedule for a {age}-year-old 
    student to study {subject} on the topic '{topic}' at a {complexity} level. 
    The schedule should be designed for {plan_duration}. 
    Provide daily study plans and key topics covered.
    """

    # Generate response using Gemini API
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    lesson_plan = response.text if hasattr(response, 'text') else "Error generating response."

    st.subheader("Generated Study Schedule")
    st.write(lesson_plan)