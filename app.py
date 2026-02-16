import streamlit as st
import pdfplumber
from chatbot import analyze_resume
import time

st.set_page_config(
    page_title="AIRA - AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

    .stApp {
        background-color: #000000;
        background-image: 
            radial-gradient(at 0% 0%, rgba(76, 29, 149, 0.3) 0px, transparent 50%),
            radial-gradient(at 100% 0%, rgba(219, 39, 119, 0.3) 0px, transparent 50%);
        font-family: 'Outfit', sans-serif;
    }
    
    body {
        color: #ffffff !important;
        font-size: 18px !important;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Outfit', sans-serif;
        color: #ffffff !important;
        font-weight: 800 !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.6); 
    }
    
    p, div, span, label {
        color: #e0e7ff !important; 
    }

    li {
        color: #e0e7ff !important;
        font-size: 1.1rem !important;
        margin-bottom: 0.8rem;
    }

    .hero-container {
        text-align: center;
        padding: 4rem 2rem;
        background: rgba(17, 24, 39, 0.8);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        margin-bottom: 3rem;
        box-shadow: 0 0 30px rgba(124, 58, 237, 0.2);
    }
    
    .hero-title {
        font-size: 5rem;
        font-weight: 900;
        color: #38bdf8 !important; 
        margin-bottom: 1rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8); 
        letter-spacing: 2px;
    }
    
    .hero-subtitle {
        font-size: 1.4rem;
        color: #cbd5e1 !important;
        margin-top: 1rem;
    }

    .stFileUploader {
        background-color: #111827;
        border: 2px dashed #6366f1;
        border-radius: 15px;
        padding: 2rem;
    }
    
    .metric-card {
        background: #1f2937;
        border-radius: 15px;
        padding: 2rem;
        text-align: center;
        border: 1px solid #374151;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.5);
    }
    
    .metric-label {
        color: #9ca3af !important;
        font-size: 0.9rem;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        font-size: 3rem;
        font-weight: 800;
        color: #22d3ee !important; 
        text-shadow: 0 0 15px rgba(34, 211, 238, 0.4);
    }

    .analysis-container {
        background-color: #111827;
        border: 1px solid #374151;
        border-radius: 20px;
        padding: 3rem;
        margin-top: 2rem;
        box-shadow: 0 0 40px rgba(0,0,0,0.5);
    }
    
    .analysis-header {
        font-size: 2rem;
        color: #a78bfa !important; 
        border-bottom: 2px solid #4ade80; 
        padding-bottom: 1rem;
        margin-bottom: 2rem;
    }
    
    .stMarkdown h2 {
        color: #4ade80 !important; 
        border-left: 5px solid #4ade80;
        padding-left: 15px;
        margin-top: 30px !important;
    }
    
    .stMarkdown h3 {
        color: #f472b6 !important; 
        margin-top: 20px !important;
    }
    
    .stMarkdown p {
        color: #e5e7eb !important; 
        line-height: 1.8;
        font-size: 1.1rem;
    }

    .stButton button {
        background: #4f46e5;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        height: 50px;
        width: 100%;
        border: none;
        transition: 0.3s;
    }
    
    .stButton button:hover {
        background: #4338ca;
        box-shadow: 0 0 15px rgba(79, 70, 229, 0.6);
    }
</style>
""", unsafe_allow_html=True)

def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

API_KEY = "AIzaSyDYsO6ftZBwOYBTl6INWmlLx2Cyr7ls45s"

with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135679.png", width=80)
    st.title("AIRA Settings")
    st.info("Ensure your resume is in PDF format for the best analysis results.")
    st.markdown("---")
    st.write("### Features")
    st.markdown("✅ **Instant Analysis**")
    st.markdown("✅ **Sector Identification**")
    st.markdown("✅ **Scoring System**")
    st.markdown("✅ **Detailed Feedback**")
    
    st.markdown("---")
    st.caption("Powered by Google Gemini 2.5 Flash")

st.markdown("""
<div class="hero-container">
    <div class="hero-title">AIRA</div>
    <div class="hero-subtitle">Advanced AI Resume Analyzer. Upload your CV to get instant, actionable feedback and improve your job prospects.</div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    uploaded_file = st.file_uploader("Drop your resume here (PDF)", type=["pdf"])

if uploaded_file is not None:
    resume_text = extract_text(uploaded_file)
    
    if not resume_text or len(resume_text.strip()) < 100:
        st.error("⚠️ Could not extract text. Please ensure the PDF is text-readable and not an image.")
    else:
        st.success("✅ Resume uploaded successfully!")
        
        if st.button("🚀 Analyze Resume Now"):
            with st.spinner("🤖 Analyzing your profile..."):
                try:
                    time.sleep(1) 
                    result = analyze_resume(API_KEY, resume_text)
                    st.session_state['analysis_result'] = result
                except Exception as e:
                    st.error(f"An error occurred during analysis: {e}")
        
        if 'analysis_result' in st.session_state:
            result = st.session_state['analysis_result']
            
            if "INVALID RESUME" in result:
                st.error("🚫 The uploaded document does not appear to be a valid resume.")
            else:
                rating = "N/A"
                sector = "General"
                analysis_text = result
                
                lines = result.split('\n')
                for line in lines:
                    if "RATING:" in line:
                        rating = line.replace("RATING:", "").strip()
                    if "SECTOR:" in line:
                        sector = line.replace("SECTOR:", "").strip()
                
                if "ANALYSIS:" in result:
                    analysis_text = result.split("ANALYSIS:", 1)[1].strip()

                st.markdown("### Analysis Results")
                
                metric_col1, metric_col2 = st.columns(2)
                
                with metric_col1:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">Resume Score</div>
                        <div class="metric-value">{rating}</div>
                    </div>
                    """, unsafe_allow_html=True)
                
                with metric_col2:
                    st.markdown(f"""
                    <div class="metric-card">
                        <div class="metric-label">Identified Sector</div>
                        <div class="metric-value" style="font-size: 2rem;">{sector}</div>
                    </div>
                    """, unsafe_allow_html=True)

                st.markdown("""
                <div class="analysis-container">
                    <div class="analysis-header">Detailed Insights</div>
                </div>
                """, unsafe_allow_html=True)
                
                st.markdown(analysis_text)

else:
    st.markdown("""
    <div style="text-align: center; color: #64748b; margin-top: 2rem;">
        <p>Upload a resume to begin...</p>
    </div>
    """, unsafe_allow_html=True)
