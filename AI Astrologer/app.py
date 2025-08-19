import streamlit as st
from chart_generation import generate_chart_summary
from llm_inference import LLMEngine
from random_facts import random_fact

st.title("AI Astrologer ✨")

st.write("Enter your birth details to discover your astrological chart.")

# User input

name = st.text_input("Your Name")
dob = st.text_input("Date of Birth (DD/MM/YYYY). Ensure proper format.")
tob = st.text_input("Time of Birth (HH\:MM), 24-hour format)")+":00"
place = st.text_input("Place of Birth (City, Country)")


# Chart Generation
if st.button("Generate Horoscope"):
    if dob and tob and place:
        with st.spinner(f"✨ Calculating your chart... {random_fact()}"):
            try:
                chart_summary = generate_chart_summary(dob, tob, place)
                st.session_state["chart_summary"] = chart_summary
                st.write("### Chart Summary")
                st.success(chart_summary)
            except Exception as e:
                st.error(f"Error generating chart: {e}")
    else:
        st.error("⚠️ Please fill all required fields.")

# loading LLM
if "llm" not in st.session_state:
    st.session_state["llm"] = LLMEngine()  # ollama model

# one free question
question = st.text_input("Ask a question (e.g., 'What about my career?')")

if st.button("Ask AI Astrologer") and "chart_summary" in st.session_state:
    with st.spinner(f"🔮 Consulting the stars... {random_fact()}"):
        response = st.session_state["llm"].ask(st.session_state["chart_summary"], question)
        st.write("### AI Astrologer Says:")
        st.info(response)




# ________________________________________________________________________________________________________
# name = input("Your Name: ")
# dob = input("Date of Birth (DD/MM/YYYY): ")
# tob = input("Time of Birth (HH:MM:SS): ")
# place = input("Place of Birth (City, Country): ")  # Placeholder, lat/lon lookup can be added

# chart_summary = generate_chart_summary(str(dob), str(tob), place)
# # print(chart_summary)

# # print("Loading AI model...")

# llm = LLMEngine()
# question = input("Ask a question (e.g., 'What about my career?'): ")

# print("Generating horoscope...")
# response = llm.ask(chart_summary, question)

# print(response)
# ________________________________________________________________________________________________________