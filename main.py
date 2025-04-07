import streamlit as st
from streamlit_lottie import st_lottie
import requests
import os

st.set_page_config(page_title="Growth Mindset", layout="wide")

# ----- Load Lottie Animation -----
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_growth = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_qp1q7mct.json")

# ----- Custom CSS -----
st.markdown("""
    <style>
    .main {
        background: linear-gradient(to bottom right, #DCE35B, #45B649);
        padding: 2rem;
        border-radius: 12px;
    }
    .section {
        background-color: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# ----- Layout -----
st.title("🌱 Growth Mindset Project")
st.subheader("Believe in Your Potential — Grow Every Day 💪")

with st.container():
    col1, col2 = st.columns([1, 2])
    with col1:
        st_lottie(lottie_growth, height=250, speed=1.2)
    with col2:
        st.markdown("""
        ### What is a Growth Mindset?
        A growth mindset is the belief that your abilities and intelligence can be developed through effort, learning, and persistence. This project is a reflection of that mindset — turning an idea into reality while learning new technologies.
        """)

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
        st.markdown(f"- {step}")

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("## ✨ Ready to generate your own README?")
if st.button("🚀 Launch README Generator"):
    os.system("streamlit run README.py")
