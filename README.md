# Growth Mindset: AI-Powered README.md Generator

## Description

This project leverages the power of Google Gemini AI to automatically generate professional `README.md` files for software projects.  Users can choose to input their project details either manually or by providing a link to their GitHub repository. The application then uses the Gemini AI model to craft a comprehensive and well-formatted `README.md` file, saving developers valuable time and effort.

## Tech Stack

* Python
* Streamlit
* Google Gemini AI

## Features

* **GitHub Repository Integration:**  Generate a `README.md` directly from a GitHub repository link. The AI analyzes the repository's contents (code, structure, etc.) to create a relevant and accurate `README`.
* **Manual Input:** Allows users to manually input project details, including project name, description, tech stack, features, installation instructions, usage instructions, and license information.
* **AI-Powered Generation:**  Uses the Google Gemini AI model to generate high-quality, professional-grade `README.md` files.
* **User-Friendly Interface:** A simple and intuitive Streamlit interface provides an easy-to-use experience.
* **Code Display:** The generated `README.md` is displayed in a formatted code block, ready for copying and pasting.


## Installation Steps

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   ```
2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Set up your Google Gemini API Key:**
   - Obtain a Gemini API key from Google.
   - Create a `.env` file in the project's root directory and add your API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```
5. **Run the application:**
   ```bash
   streamlit run app.py
   ```


## Usage Instructions

1.  Run the application as described in the Installation Steps.
2.  Choose either "GitHub Repository Link" or "Manual Project Details" as your input type.
3.  If selecting "GitHub Repository Link", enter a valid GitHub repository URL.
4.  If selecting "Manual Project Details," fill in all the required fields.
5.  Click the "Generate README" button.
6.  The generated `README.md` will be displayed in the application. Copy and paste the content into your project's `README.md` file.

