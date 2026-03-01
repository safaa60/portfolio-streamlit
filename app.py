import streamlit as st

# ========================= CONFIG =========================
st.set_page_config(
    page_title="Safaa Zemmar | Cyber Portfolio",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========================= ULTRA PREMIUM CSS (pour cette page Accueil) =========================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    :root {
        --bg: #0a0f1c;
        --accent: #00f5ff;
        --accent2: #ff2e63;
        --glow: #00f5ff;
    }

    .stApp {
        background: linear-gradient(180deg, #0a0f1c 0%, #0f172a 100%);
        color: #e0f2fe;
    }

    /* HERO - Version ultra premium */
    .hero {
        padding: 6rem 0 5rem 0;
        text-align: center;
        position: relative;
        overflow: hidden;
        background: radial-gradient(circle at center, rgba(0,245,255,0.08) 0%, transparent 70%);
    }
    .hero::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(0,245,255,0.12) 0%, transparent 60%);
        animation: pulse 15s infinite ease-in-out;
    }
    @keyframes pulse {
        0%, 100% { opacity: 0.6; }
        50% { opacity: 1; }
    }

    .name {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 5.2rem;
        font-weight: 700;
        letter-spacing: -2px;
        background: linear-gradient(90deg, #ffffff, var(--accent));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 
            0 0 20px var(--glow),
            0 0 40px var(--glow),
            0 0 80px var(--accent2);
        margin: 0;
    }
    .tagline {
        font-size: 1.65rem;
        color: var(--accent);
        letter-spacing: 4px;
        margin: 1rem 0 2.5rem 0;
        font-weight: 500;
    }

    /* Boutons Hero */
    .hero-btn {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        background: rgba(15,23,42,0.9);
        color: white;
        padding: 14px 32px;
        border-radius: 50px;
        font-weight: 600;
        text-decoration: none;
        border: 1px solid rgba(0,245,255,0.4);
        transition: all 0.3s;
        margin: 0 12px;
    }
    .hero-btn:hover {
        background: var(--accent);
        color: #0a0f1c;
        transform: translateY(-4px);
        box-shadow: 0 0 30px rgba(0,245,255,0.6);
        border-color: var(--accent);
    }

    /* Section Bienvenue */
    .welcome-section {
        background: rgba(15,23,42,0.85);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(0,245,255,0.25);
        border-radius: 24px;
        padding: 3rem;
        margin: -4rem auto 4rem;
        max-width: 1100px;
        position: relative;
        box-shadow: 0 20px 60px rgba(0,0,0,0.4);
    }
    .welcome-title {
        font-size: 2.8rem;
        font-weight: 700;
        color: var(--accent);
        text-shadow: 0 0 30px var(--glow);
        margin-bottom: 1.5rem;
    }

    /* Photo flottante */
    .profile-photo {
        width: 320px;
        height: 320px;
        border-radius: 24px;
        border: 6px solid var(--accent);
        box-shadow: 
            0 0 40px rgba(0,245,255,0.5),
            0 0 80px rgba(255,46,99,0.3);
        object-fit: cover;
        transition: transform 0.4s;
    }
    .profile-photo:hover {
        transform: scale(1.05) rotate(2deg);
    }

    /* Badges */
    .badge {
        display: inline-block;
        background: rgba(0,245,255,0.1);
        color: var(--accent);
        padding: 6px 18px;
        border-radius: 30px;
        font-size: 0.9rem;
        font-weight: 600;
        border: 1px solid rgba(0,245,255,0.3);
        margin: 8px 6px 8px 0;
    }
</style>
""", unsafe_allow_html=True)

# ========================= DATA =========================
NAME = "SAFAA ZEMMAR"
TAGLINE = "CYBERSECURITY • VIRTUALISATION • INFRASTRUCTURE"

PROFILE_TEXT = """
Étudiante en Bachelor 2 Informatique à Ynov Paris, passionnée par la cybersécurité opérationnelle 
et la sécurisation des infrastructures. Je construis des environnements techniques réalistes 
pour comprendre les mécanismes avant d’utiliser les outils. 

Mon objectif : devenir une analyste SOC ou pentester technique spécialisée en virtualisation sécurisée.
"""

# ========================= HERO + ACCUEIL (version beaucoup plus belle) =========================
st.markdown(f"""
<div class="hero">
    <h1 class="name">{NAME}</h1>
    <p class="tagline">{TAGLINE}</p>
    
    <div style="margin: 2rem 0 3rem 0;">
        <a href="https://github.com/safaa60" target="_blank" class="hero-btn">
            🐙 GitHub
        </a>
        <a href="mailto:safaazemmar@gmail.com" class="hero-btn">
            ✉️ Contact
        </a>
        <a href="#" class="hero-btn" onclick="window.location.reload()">📄 CV PDF</a>
    </div>
</div>
""", unsafe_allow_html=True)

# ====================== SECTION BIENVENUE (le cœur de la page) ======================
col_left, col_right = st.columns([1.65, 1])

with col_left:
    st.markdown(f"""
    <div class="welcome-section">
        <span style="font-size:3.5rem;">👋</span>
        <h2 class="welcome-title">Bienvenue sur mon portfolio</h2>
        <p style="font-size:1.22rem; line-height:1.85; color:#cbd5e1;">
            {PROFILE_TEXT}
        </p>
        
        <div style="margin-top:2rem;">
            <span class="badge">Alternance B3 Cybersécurité recherchée</span>
            <span class="badge">Ynov Paris 2025-2026</span>
            <span class="badge">Cyber Lab 100% fait main</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col_right:
    # Remplace l'URL par ta vraie photo (idéalement 800x800 px)
    st.markdown("""
    <div style="text-align:center; margin-top:2rem;">
        <img src="https://via.placeholder.com/600x600/1e2937/00f5ff?text=SAFAA" 
             class="profile-photo" alt="Safaa Zemmar">
    </div>
    """, unsafe_allow_html=True)

# Bouton Download CV en bas de la section (très visible)
st.markdown("""
<div style="text-align:center; margin:3rem 0 2rem 0;">
    <a href="#" style="background:#00f5ff; color:#0a0f1c; padding:16px 48px; border-radius:50px; 
    font-weight:700; font-size:1.1rem; text-decoration:none; box-shadow:0 0 40px #00f5ff;">
        ⬇️ Télécharger mon CV complet
    </a>
</div>
""", unsafe_allow_html=True)

st.caption("© 2026 Safaa Zemmar — Portfolio Cyber • Design premium neon")