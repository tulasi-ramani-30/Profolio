import google.generativeai as genai
import streamlit as st

st.title("ProFolio")
st.write("Generate a clean, professional resume using AI")


genai.configure(api_key="...................")

model = genai.GenerativeModel("gemini-2.5-flash")

name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
linkedin = st.text_input("LinkedIn / Portfolio URL")

Job_description = st.text_area("Job Description")
skills = st.text_area("Skills (comma separated)")
experience = st.text_area("Work Experience")
education = st.text_area("Education")
projects = st.text_area("Projects (optional)")

if st.button("Generate Resume"):
    if not name or not email or not education or not experience:
        st.warning("Please fill required fields")
    else:
        prompt = f"""
        Create a professional resume with the following details:

        Name: {name}
        Email: {email}
        Phone: {phone}
        LinkedIn: {linkedin}
        Work Experience:{experience}
        Education:{education}
        Projects:{projects}
        Skills:{skills}
    
        Understanding of job descriptions
Resume optimization concepts
Keyword matching, make some columns , outlines , and highlight the required skill
Logical filtering of information
use minimum words but resume should look impressive
start with the name itself,
write in this formality:
name / email: / ph no: / linked in: 
Introduction
skills
projects
qualification
build resume in impressive way
donot mention any extra lines in starting

"""

        with st.spinner("Generating professional resume..."):
            response = model.generate_content(prompt)

        st.success("Resume Generated Successfully")

        st.subheader("📑 Generated Resume")
        st.write("Resume Output", response.text)