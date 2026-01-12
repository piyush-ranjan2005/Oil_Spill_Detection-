import streamlit as st
import tensorflow as tf
import numpy as np
import cv2
import base64
import time
from PIL import Image
from io import BytesIO
from huggingface_hub import hf_hub_download

# 1. Page Configuration
st.set_page_config(page_title="Marine Surveillance AI", page_icon="⚓", layout="wide")

# 2. Refined Professional CSS (Subdued Transitions & Clean Layout)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

    html, body, [data-testid="stAppViewContainer"] {
        background: #050c1a;
        color: #e2e8f0;
        font-family: 'Inter', sans-serif;
    }

    /* Subdued Professional Heading */
    h1 {
        font-family: 'Inter', sans-serif;
        font-weight: 700 !important;
        letter-spacing: -0.02em;
        color: #f8fafc;
    }

    /* Professional Card - Reduced Transitions */
    .img-card {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        overflow: hidden;
        margin-bottom: 12px;
        transition: transform 0.2s ease-in-out, border 0.2s ease; /* Faster, subtle transition */
    }
    
    .img-card:hover { 
        border: 1px solid #2ecbff; 
        transform: translateY(-3px); /* Minimal lift */
    }
    
    .toolbar { 
        background: rgba(15, 23, 42, 0.8); 
        padding: 8px 12px; 
        display: flex; 
        justify-content: flex-end; 
        gap: 15px; 
    }
    
    .icon-link { color: #2ecbff !important; font-size: 18px; text-decoration: none !important; cursor: pointer; }
    .icon-link:hover { color: #ffffff !important; }
    
    .img-content { display: block; width: 100%; aspect-ratio: 1/1; object-fit: cover; }

    .legend-text { 
        font-size: 0.75rem; 
        font-weight: 500; 
        color: #64748b; 
        margin-bottom: 20px; 
        text-align: center; 
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    /* Minimalist Dashboard Tiles */
    .metric-container { display: flex; gap: 12px; margin-top: 25px; }
    .metric-tile { 
        flex: 1; 
        background: rgba(30, 41, 59, 0.5); 
        padding: 18px; 
        border-radius: 8px; 
        border-left: 3px solid #334155;
        text-align: center;
    }

    .advisor-box {
        background: rgba(30, 41, 59, 0.3);
        border: 1px solid rgba(46, 203, 255, 0.2);
        padding: 20px;
        border-radius: 8px;
        margin-top: 20px;
    }

    .footer {
        width: 100%; padding: 30px 0; margin-top: 50px;
        border-top: 1px solid rgba(255, 255, 255, 0.05);
        text-align: center; color: #475569; font-size: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# 3. Logic & Processing
def img_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def render_card(img_obj, filename="sar_data.png"):
    if img_obj is None:
        return f'<div class="img-card"><div style="height:320px; display:flex; align-items:center; justify-content:center; color:#334155; font-size:0.9rem;">SIGNAL STANDBY...</div></div>'
    b64 = img_to_base64(img_obj)
    data_url = f"data:image/png;base64,{b64}"
    return f'<div class="img-card"><div class="toolbar"><a href="{data_url}" target="_blank" class="icon-link">⛶</a><a href="{data_url}" download="{filename}" class="icon-link">⬇</a></div><img src="{data_url}" class="img-content"></div>'

@st.cache_resource(show_spinner=False)
def load_oil_model():
    path = hf_hub_download(repo_id="pro-developer/unet-oil-spill-segmentation", filename="unet_oil_spill_finetuned.keras")
    return tf.keras.models.load_model(path, compile=False)

# 4. App Core
if "results" not in st.session_state: st.session_state.results = None
if "last_file" not in st.session_state: st.session_state.last_file = None

st.markdown("<h1 style='text-align:center;'>AI-ENABLED <span style='color:#2ecbff'>MARINE OIL SURVEILLANCE</span></h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#64748b; font-size:1rem; margin-top:-10px; margin-bottom:40px;'>Orbital SAR Neural Analysis & Operational Response Protocol</p>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("### 🛰️ SAR Input")
    uploaded_file = st.file_uploader("Upload", type=["jpg", "png"], label_visibility="collapsed")
    
    if uploaded_file:
        if st.session_state.last_file != uploaded_file.name:
            st.session_state.results = None
            st.session_state.last_file = uploaded_file.name
            
        input_img = Image.open(uploaded_file).convert("L").resize((320, 320))
        st.markdown(render_card(input_img, "sar_uplink.png"), unsafe_allow_html=True)
        st.markdown("<div class='legend-text'>Radar Backscatter Signal</div>", unsafe_allow_html=True)
        
        if st.button("EXECUTE NEURAL DIAGNOSTIC", use_container_width=True):
            start = time.time()
            model = load_oil_model()
            
            proc = (cv2.resize(np.array(input_img), (256, 256)) / 255.0)[np.newaxis, ..., np.newaxis]
            raw_pred = model.predict(proc, verbose=0)[0].squeeze()
            mask = (raw_pred > 0.5).astype(np.uint8)
            
            # Area Calc (Ref: 100km2 scene)
            km_area = (mask.sum() / mask.size) * 100 
            conf = np.mean(raw_pred[mask == 1]) * 100 if np.any(mask) else (1 - np.mean(raw_pred)) * 100
            heat = cv2.cvtColor(cv2.applyColorMap((raw_pred * 255).astype(np.uint8), cv2.COLORMAP_JET), cv2.COLOR_BGR2RGB)
            
            # Updated Severity Logic
            if km_area > 20: status, color, advice = "High", "#f87171", "Immediate Emergency Deployment: Multi-agency response required."
            elif km_area > 5: status, color, advice = "Medium", "#fbbf24", "Operational Alert: Deploy containment and cleanup vessels."
            elif km_area > 0: status, color, advice = "Low", "#34d399", "Precautionary Monitoring: Verify with aerial recon."
            else: status, color, advice = "No Oil Spill", "#2ecbff", "System Nominal: Signal indicates clear water conditions."

            st.session_state.results = {
                "mask": Image.fromarray(mask * 255).resize((320, 320)),
                "heat": Image.fromarray(heat).resize((320, 320)),
                "area": km_area, "status": status, "color": color, 
                "conf": conf, "latency": time.time() - start, "advice": advice
            }

with col2:
    st.markdown("### 🔳 Binary Extraction")
    mask_img = st.session_state.results["mask"] if st.session_state.results else None
    st.markdown(render_card(mask_img, "spill_mask.png"), unsafe_allow_html=True)
    st.markdown("<div class='legend-text'>WHITE = OIL DETECTED</div>", unsafe_allow_html=True)

with col3:
    st.markdown("### 🌡️ Probability Gradient")
    heat_img = st.session_state.results["heat"] if st.session_state.results else None
    st.markdown(render_card(heat_img, "probability_map.png"), unsafe_allow_html=True)
    st.markdown("<div class='legend-text'>RED = OIL SPILL | BLUE = WATER</div>", unsafe_allow_html=True)

# 5. Dashboard Summary
if st.session_state.results:
    r = st.session_state.results
    st.markdown(f"""
        <div class="metric-container">
            <div class="metric-tile" style="border-left-color: {r['color']}">
                <div style="font-size: 0.7rem; color: #64748b; font-weight:600;">SEVERITY</div>
                <div style="font-size: 1.3rem; font-weight: 700; color: {r['color']}">{r['status']}</div>
            </div>
            <div class="metric-tile">
                <div style="font-size: 0.7rem; color: #64748b; font-weight:600;">TOTAL AREA</div>
                <div style="font-size: 1.3rem; font-weight: 700;">{r['area']:.2f} km²</div>
            </div>
            <div class="metric-tile">
                <div style="font-size: 0.7rem; color: #64748b; font-weight:600;">AI CONFIDENCE</div>
                <div style="font-size: 1.3rem; font-weight: 700; color: #2ecbff;">{r['conf']:.1f}%</div>
            </div>
            <div class="metric-tile">
                <div style="font-size: 0.7rem; color: #64748b; font-weight:600;">LATENCY</div>
                <div style="font-size: 1.3rem; font-weight: 700;">{r['latency']:.3f}s</div>
            </div>
        </div>
        <div class="advisor-box">
            <h5 style="margin-top:0; color:#2ecbff; font-weight:600;">MARINE DEPT. GUIDANCE</h5>
            <p style="margin-bottom:0; font-size:0.95rem; color:#cbd5e1;">{r['advice']}</p>
        </div>
    """, unsafe_allow_html=True)

# 6. Final Footer
st.markdown("""
    <div class="footer">
        <b>MARINE OIL SPILL INTELLIGENCE PLATFORM v2.6</b><br>
        U-Net Neural Network Optimized for C-Band Synthetic Aperture Radar<br>
        Department of Maritime Surveillance & Response © 2026
    </div>
""", unsafe_allow_html=True)