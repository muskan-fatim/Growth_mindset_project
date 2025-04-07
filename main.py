import streamlit as st
import os
import google.generativeai as genai
from dotenv import load_dotenv

st.set_page_config(page_title="Growth Mindset", layout="wide")

# ----- Custom CSS with Smooth Transitions ----- 
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to bottom right, #DCE35B, #45B649);
        padding: 2rem;
        border-radius: 12px;
        transition: background 0.5s ease-in-out;
    }

    .main:hover {
        background: linear-gradient(to bottom right, #45B649, #DCE35B);
    }

    .section {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
        transition: transform 0.3s ease;
    }

    .section:hover {
        transform: scale(1.05);
    }

    .button {
        background-color: #45B649;
        color: white;
        padding: 12px 25px;
        border-radius: 8px;
        font-size: 16px;
        font-weight: bold;
        border: none;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .button:hover {
        background-color: #DCE35B;
    }

    .content-text {
        font-size: 1.1rem;
        line-height: 1.6;
        color: #333;
    }

    </style>
""", unsafe_allow_html=True)

# ----- Layout ----- 
st.title("🌱 Growth Mindset Project")
st.subheader("Believe in Your Potential — Grow Every Day 💪")

with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
      st.image("https://assets.entrepreneur.com/content/3x2/2000/1600288418-GettyImages-1185654371.jpg")
    with col2:
        st.markdown("""
        ### What is a Growth Mindset?
        A growth mindset is the belief that your abilities and intelligence can be developed through effort, learning, and persistence. This project is a reflection of that mindset — turning an idea into reality while learning new technologies.
        """, unsafe_allow_html=True)

st.markdown("---")

# ----- Project Purpose ----- 
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown("## 💡 Why This Project?")
    st.markdown("""
    - ✅ Learned to integrate **LLMs (Gemini)** into a real app  
    - ✅ Built a **README Generator** to help other developers  
    - ✅ Designed with creativity using **Streamlit UI**  
    - ✅ Overcame bugs, explored, and kept going — true growth mindset!  
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# ----- Timeline ----- 
with st.container():
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.markdown("## 🛠 My Learning Timeline")

    timeline = [
        "✅ Explored Streamlit & LLMs",
        "🧠 Learned about environment variables and API handling",
        "🎨 Designed interactive UI with modern layout",
        "💬 Faced bugs but fixed them with patience",
        "🚀 Created a working tool that helps others!"
    ]

    for step in timeline:
        st.markdown(f"- {step}", unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("## ✨ Ready to generate your own README?")

