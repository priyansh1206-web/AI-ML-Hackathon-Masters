import streamlit as st
import ollama
import time
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="AI Course Assistant", page_icon="🎓", layout="wide")

# -------- LOAD LOTTIE ANIMATION --------
def load_lottie(url):
    r = requests.get(url)
    return r.json()

ai_animation = load_lottie(
    "https://assets2.lottiefiles.com/packages/lf20_x62chJ.json"
)

# -------- MODERN CSS --------
st.markdown("""
<style>

@keyframes gradient {
0% {background-position:0% 50%}
50% {background-position:100% 50%}
100% {background-position:0% 50%}
}

body {
background: linear-gradient(-45deg,#020617,#0f172a,#1e293b,#020617);
background-size:400% 400%;
animation: gradient 12s ease infinite;
color:white;
}

.hero-title {
font-size:65px;
font-weight:900;
text-align:center;
background: linear-gradient(90deg,#22c55e,#3b82f6,#a855f7);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
}

.subtitle {
text-align:center;
font-size:20px;
color:#94a3b8;
margin-bottom:30px;
}

.card {
background: rgba(255,255,255,0.05);
backdrop-filter: blur(12px);
padding:25px;
border-radius:20px;
box-shadow:0 10px 30px rgba(0,0,0,0.6);
transition:0.3s;
}

.card:hover {
transform:translateY(-8px);
box-shadow:0 25px 50px rgba(0,0,0,0.8);
}

.metric {
background:#0f172a;
padding:10px;
border-radius:10px;
text-align:center;
font-weight:600;
}

</style>
""", unsafe_allow_html=True)

# -------- HERO SECTION --------
col1, col2 = st.columns([1.2,1])

with col1:
    st.markdown('<div class="hero-title">🎓 AI Course Assistant</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="subtitle">Explore programs, eligibility and careers instantly with AI</div>',
        unsafe_allow_html=True
    )

with col2:
    st_lottie(ai_animation, height=220)

# -------- FEATURE SECTION --------
st.write("")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
    <h3>⚡ Instant Answers</h3>
    <p>Get program information in seconds.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
    <h3>📚 Course Insights</h3>
    <p>Discover subjects, duration and learning outcomes.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
    <h3>🚀 Career Guidance</h3>
    <p>Learn about future career opportunities.</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# -------- SIDEBAR --------
with st.sidebar:
    st.header("💡 Example Questions")

    examples = [
        "What is the eligibility criteria?",
        "What subjects are taught?",
        "What is the program duration?",
        "What career opportunities will I get?"
    ]

    for e in examples:
        if st.button(e):
            st.session_state.example = e

    st.divider()

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# -------- CHAT MEMORY --------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------- SHOW CHAT --------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -------- INPUT --------
prompt = st.chat_input("💬 Ask your question...")

if "example" in st.session_state:
    prompt = st.session_state.example
    del st.session_state.example

# -------- AI RESPONSE --------
if prompt:

    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        start = time.time()

        with st.spinner("🤖 AI is thinking..."):

            response = ollama.chat(
                model="llama3",
                messages=[
                    {"role":"system","content":"You are a helpful course assistant."},
                    {"role":"user","content":prompt}
                ]
            )

        answer = response["message"]["content"]
        end = time.time()

        st.markdown(answer)

        a, b = st.columns(2)

        with a:
            st.markdown(
                f'<div class="metric">⏱ {round(end-start,2)} sec</div>',
                unsafe_allow_html=TrueS
            )

        with b:
            st.markdown(
                f'<div class="metric">📝 {len(answer.split())} words</div>',
                unsafe_allow_html=True
            )

    st.session_state.messages.append({"role":"assistant","content":answer})