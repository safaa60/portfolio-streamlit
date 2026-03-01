import streamlit as st
from pathlib import Path

# ========================= CONFIG =========================
st.set_page_config(
    page_title="Safaa Zemmar | Cyber Portfolio",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={"Get Help": None, "Report a bug": None, "About": "Portfolio Cyber 2026"}
)

# ========================= ULTRA PREMIUM CYBER CSS =========================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    :root {
        --bg: #0a0f1c;
        --card: rgba(15, 23, 42, 0.92);
        --accent: #00f5ff;
        --accent2: #ff2e63;
        --glow: #00f5ff;
        --text: #e0f2fe;
    }

    .stApp {
        background: linear-gradient(180deg, #0a0f1c 0%, #0f172a 100%);
        color: var(--text);
        font-family: 'Inter', sans-serif;
    }

    /* HERO - Version ultime */
    .hero {
        padding: 7rem 0 5rem 0;
        text-align: center;
        position: relative;
        overflow: hidden;
        background: radial-gradient(circle at 50% 30%, rgba(0,245,255,0.12) 0%, transparent 70%);
    }
    .hero::before {
        content: '';
        position: absolute;
        top: -100%;
        left: -100%;
        width: 300%;
        height: 300%;
        background: radial-gradient(circle, rgba(255,46,99,0.08) 0%, transparent 60%);
        animation: pulse-glow 20s infinite ease-in-out;
    }
    @keyframes pulse-glow { 0%,100% {opacity:0.7;} 50% {opacity:1;} }

    .name {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 5.8rem;
        font-weight: 700;
        letter-spacing: -3px;
        background: linear-gradient(90deg, #fff, var(--accent), var(--accent2));
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-shadow: 0 0 40px var(--glow), 0 0 80px var(--accent2);
        margin: 0 0 0.5rem 0;
    }
    .tagline {
        font-size: 1.85rem;
        color: var(--accent);
        letter-spacing: 6px;
        font-weight: 500;
        margin-bottom: 2.5rem;
    }

    .hero-btn {
        display: inline-flex;
        align-items: center;
        gap: 12px;
        background: rgba(15,23,42,0.95);
        color: white;
        padding: 16px 36px;
        border-radius: 50px;
        font-weight: 700;
        font-size: 1.1rem;
        text-decoration: none;
        border: 2px solid var(--accent);
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        box-shadow: 0 0 20px rgba(0,245,255,0.3);
    }
    .hero-btn:hover {
        background: var(--accent);
        color: #0a0f1c;
        transform: translateY(-6px) scale(1.05);
        box-shadow: 0 0 50px rgba(0,245,255,0.7);
    }

    /* Glass Card */
    .glass {
        background: var(--card);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(0,245,255,0.25);
        border-radius: 24px;
        padding: 2.2rem;
        transition: all 0.4s;
    }
    .glass:hover {
        transform: translateY(-12px);
        box-shadow: 0 25px 60px rgba(0,245,255,0.2);
        border-color: var(--accent);
    }

    /* Section Header */
    .section-header {
        font-size: 2.6rem;
        font-weight: 700;
        color: white;
        margin: 3rem 0 1.8rem 0;
        position: relative;
    }
    .section-header::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 0;
        width: 80px;
        height: 4px;
        background: linear-gradient(90deg, var(--accent), var(--accent2));
        border-radius: 4px;
    }

    /* Skill Pills */
    .skill-pill {
        display: inline-block;
        background: rgba(0,245,255,0.1);
        color: var(--accent);
        padding: 12px 24px;
        border-radius: 50px;
        margin: 8px 6px;
        font-weight: 600;
        border: 1px solid rgba(0,245,255,0.35);
        transition: all 0.3s;
    }
    .skill-pill:hover {
        background: var(--accent);
        color: #0a0f1c;
        transform: scale(1.08);
    }

    /* Project Card */
    .proj-card {
        background: rgba(15,23,42,0.8);
        border: 1px solid rgba(0,245,255,0.2);
        border-radius: 20px;
        padding: 1.8rem;
        height: 100%;
    }

    /* Timeline */
    .timeline-item {
        position: relative;
        padding-left: 2.5rem;
        margin-bottom: 2rem;
    }
    .timeline-item::before {
        content: '';
        position: absolute;
        left: 8px;
        top: 6px;
        width: 14px;
        height: 14px;
        background: var(--accent);
        border-radius: 50%;
        box-shadow: 0 0 0 4px rgba(0,245,255,0.3);
    }
</style>
""", unsafe_allow_html=True)

# ========================= DATA =========================
NAME = "SAFAA ZEMMAR"
TAGLINE = "CYBERSECURITY • VIRTUALISATION • INFRASTRUCTURE"

PROFILE = """
Étudiante en Bachelor 2 Informatique à Ynov Paris, passionnée par la cybersécurité opérationnelle 
et la sécurisation des infrastructures. Je construis des environnements techniques réalistes 
pour comprendre les mécanismes avant d’utiliser les outils. 

Mon objectif : devenir une analyste SOC ou pentester technique spécialisée en virtualisation sécurisée.
"""

LAB_COMPONENTS = [
    ("🖥️", "Machines Virtuelles", "Windows 11 • Debian 12 • Ubuntu Server"),
    ("🔥", "pfSense Firewall", "NAT • Règles avancées • Segmentation"),
    ("🌐", "Serveur Web & Proxy", "Apache • Reverse Proxy sécurisé"),
    ("📡", "Réseau Cisco", "VLAN • Routage • Switching"),
    ("🔍", "Analyse Trafic", "Wireshark • Nmap • TCPDump"),
    ("🛡️", "Environnement Isolé", "Tests d’attaque & défense")
]

PROJECTS = [
    {
        "title": "Cyber Lab Complet",
        "desc": "Infrastructure virtualisée complète avec pfSense, Apache, Proxy et réseau Cisco.",
        "tags": ["Virtualisation", "Firewall", "Réseau"]
    },
    {
        "title": "Application E-commerce Sécurisée",
        "desc": "PHP/MySQL avec protection contre SQLi, XSS et gestion des sessions.",
        "tags": ["Web Security", "PHP", "Auth"]
    },
    {
        "title": "Analyse Réseau Avancée",
        "desc": "Cartographie complète avec Nmap + Wireshark + scripts Python.",
        "tags": ["Nmap", "Wireshark", "Python"]
    }
]

EXPERIENCES = [
    ("Nov 2025", "Stage IoT & Supervision Sécurisée", "Numeryx", "Architecture IoT sécurisée • Brokers MQTT"),
    ("2023", "Stage Girls Can Code", "École 42 & ECE Paris", "Programmation • Linux • Sites web"),
]

SKILLS = {
    "Infrastructure": ["VirtualBox", "VMware", "Linux", "pfSense", "Apache", "Proxy"],
    "Réseau": ["TCP/IP", "VLAN", "Cisco Packet Tracer", "Wireshark", "Nmap"],
    "Cybersécurité": ["Firewall", "SQL Injection", "XSS", "Session Management", "TLS/HTTPS", "CTF"],
    "Développement": ["Python", "PHP/MySQL", "Java Swing", "HTML/CSS/JS", "Git"]
}

# ========================= LAYOUT =========================
# HERO
st.markdown(f"""
<div class="hero">
    <h1 class="name">{NAME}</h1>
    <p class="tagline">{TAGLINE}</p>
    <div style="margin-top: 2.5rem;">
        <a href="https://github.com/safaa60" target="_blank" class="hero-btn">🐙 GitHub</a>
        <a href="mailto:safaazemmar@gmail.com" class="hero-btn">✉️ Me contacter</a>
        <a href="#" onclick="window.scrollTo({{top: document.body.scrollHeight, behavior: 'smooth'}})" class="hero-btn">⬇️ Télécharger CV</a>
    </div>
</div>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.markdown("### 🛡️ Safaa Zemmar")
    page = st.radio(
        "Navigation",
        ["Accueil", "Cyber Lab", "Projets", "Compétences", "Parcours", "Vision"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.caption("🎯 Alternance B3 Cybersécurité recherchée • Septembre 2026")
    if st.button("⬇️ Télécharger mon CV PDF", use_container_width=True):
        st.success("CV téléchargé ! (place ton PDF dans assets/CV_Safaa_Zemmar.pdf)")

# ====================== PAGES ======================
if page == "Accueil":
    col1, col2 = st.columns([1.7, 1])
    with col1:
        st.markdown(f"""
        <div class="glass" style="margin-top: -4rem;">
            <span style="font-size:4rem;">👋</span>
            <h2 style="font-size:3rem; color:var(--accent); margin:1rem 0;">Bienvenue sur mon portfolio</h2>
            <p style="font-size:1.25rem; line-height:1.9;">{PROFILE}</p>
            <div style="margin-top:2rem;">
                <span style="background:rgba(0,245,255,0.15); color:var(--accent); padding:8px 22px; border-radius:30px; margin-right:10px;">Ynov Paris</span>
                <span style="background:rgba(255,46,99,0.15); color:#ff2e63; padding:8px 22px; border-radius:30px;">Cyber Lab 100% fait main</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div style="text-align:center; margin-top:1.5rem;">
            <img src="https://via.placeholder.com/520x520/1e2937/00f5ff?text=SAFAA+ZEMMAR" 
                 style="width:100%; max-width:420px; border-radius:28px; border:8px solid #00f5ff; box-shadow:0 0 60px rgba(0,245,255,0.5);" alt="Safaa">
        </div>
        """, unsafe_allow_html=True)

elif page == "Cyber Lab":
    st.markdown('<h2 class="section-header">🧪 Mon Cyber Lab Personnel</h2>', unsafe_allow_html=True)
    st.write("Un environnement réel que j’ai entièrement conçu et configuré pour expérimenter la cybersécurité.")
    cols = st.columns(3)
    for idx, (icon, title, desc) in enumerate(LAB_COMPONENTS):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class="glass" style="text-align:center; height:100%;">
                <div style="font-size:4rem; margin-bottom:1rem;">{icon}</div>
                <h3 style="color:var(--accent); margin:0.8rem 0 0.4rem 0;">{title}</h3>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

elif page == "Projets":
    st.markdown('<h2 class="section-header">🚀 Mes Projets</h2>', unsafe_allow_html=True)
    for proj in PROJECTS:
        st.markdown(f"""
        <div class="glass proj-card" style="margin-bottom:1.8rem;">
            <h3 style="color:var(--accent);">{proj["title"]}</h3>
            <p style="font-size:1.15rem;">{proj["desc"]}</p>
            <div style="margin-top:1.2rem;">
                {''.join([f'<span style="background:rgba(0,245,255,0.1); color:var(--accent); padding:6px 16px; border-radius:30px; margin-right:8px; font-size:0.9rem;">{t}</span>' for t in proj["tags"]])}
            </div>
        </div>
        """, unsafe_allow_html=True)

elif page == "Compétences":
    st.markdown('<h2 class="section-header">🛠️ Compétences</h2>', unsafe_allow_html=True)
    for cat, items in SKILLS.items():
        st.markdown(f"""
        <div class="glass" style="margin-bottom:2rem;">
            <h3 style="color:var(--accent); margin-bottom:1.2rem;">{cat}</h3>
            {''.join([f'<span class="skill-pill">{item}</span>' for item in items])}
        </div>
        """, unsafe_allow_html=True)

elif page == "Parcours":
    st.markdown('<h2 class="section-header">📖 Mon Parcours</h2>', unsafe_allow_html=True)
    for date, title, where, desc in EXPERIENCES:
        st.markdown(f"""
        <div class="timeline-item glass">
            <div style="color:var(--accent); font-weight:700;">{date}</div>
            <h3>{title}</h3>
            <p style="color:#94a3b8;">{where}</p>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("**Formation** : Bachelor 2 Informatique – Ynov Campus Paris Est (2025-2026)")

elif page == "Vision":
    st.markdown('<h2 class="section-header">🎯 Vision & Objectifs</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="glass">
        <p style="font-size:1.3rem; line-height:2;">Je recherche une alternance B3 en cybersécurité pour septembre 2026 dans :</p>
        <ul style="font-size:1.2rem; line-height:2.2;">
            <li>🔹 Analyste SOC / Blue Team</li>
            <li>🔹 Pentest Infrastructure & Virtualisation</li>
            <li>🔹 Sécurité des réseaux et systèmes</li>
        </ul>
        <div style="margin-top:2.5rem; padding:2rem; background:rgba(0,245,255,0.08); border-left:6px solid var(--accent); border-radius:16px;">
            <strong>Prête à rejoindre une équipe où la technique rencontre la sécurité réelle.</strong>
        </div>
    </div>
    """, unsafe_allow_html=True)

# FOOTER
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#64748b; padding:3rem 0 2rem;">
    © 2026 Safaa Zemmar — Portfolio Cyber • Design neon premium • Fait avec passion et Streamlit
</div>
""", unsafe_allow_html=True)