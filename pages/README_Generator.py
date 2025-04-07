import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Page configuration
st.set_page_config(page_title="README Generator", layout="wide")

# Load environment variables and configure Gemini
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel(model_name="gemini-1.5-flash")

# Title and description
st.title("📄 AI README.md Generator")
st.caption("💡 Built with a Growth Mindset: Every README is a step towards becoming better!")
st.markdown("Generate a professional `README.md` file for your project using AI!")

# Option for user input
input_type = st.radio("Choose Input Type:", ["GitHub Repository Link", "Manual Project Details"])

# Input fields
if input_type == "GitHub Repository Link":
    repo_link = st.text_input("🔗 Enter your GitHub Repository Link:")
    submit = st.button("Generate README")
    
    if submit and repo_link:
        prompt = f"Generate a detailed README.md file based on this GitHub repository: {repo_link}"
        with st.spinner("Generating README..."):
            response = model.generate_content(prompt)
        readme = response.text if hasattr(response, "text") else ""
        st.subheader("📄 Generated README.md")
        st.code(readme, language="markdown")

elif input_type == "Manual Project Details":
    project_name = st.text_input("📌 Project Name:")
    description = st.text_area("📝 Project Description:")
    tech_stack = st.text_input("💻 Tech Stack (comma-separated):")
    features = st.text_area("✨ Key Features:")
    installation = st.text_area("⚙️ Installation Steps:")
    usage = st.text_area("🚀 Usage Instructions:")
    license = st.text_input("📄 License Type (e.g., MIT, Apache):")

    submit_manual = st.button("Generate README")

    if submit_manual and project_name:
        prompt = f"""
        Write a professional README.md for a project with the following details:

        Project Name: {project_name}
        Description: {description}
        Tech Stack: {tech_stack}
        Features: {features}
        Installation Steps: {installation}
        Usage Instructions: {usage}
        License: {license}
        """
        with st.spinner("Generating README..."):
            response = model.generate_content(prompt)
        readme = response.text if hasattr(response, "text") else ""
        st.subheader("📄 Generated README.md")
        st.code(readme, language="markdown")

# Add a button to go back to the main page
if st.button("← Back to Home"):
    st.switch_page("main.py") 