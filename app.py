import streamlit as st
from pathlib import Path

# ========================= CONFIG =========================
st.set_page_config(
    page_title="Safaa Zemmar | Cyber Portfolio",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========================= PREMIUM CYBER CSS =========================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700&display=swap');

    :root {
        --bg: #0a0f1c;
        --card: rgba(15, 23, 42, 0.85);
        --accent: #00f5ff;
        --accent2: #ff2e63;
        --text: #e0f2fe;
        --light: #94a3b8;
    }

    .stApp {
        background: linear-gradient(180deg, #0a0f1c 0%, #0f172a 100%);
        color: var(--text);
        font-family: 'Inter', sans-serif;
    }

    .hero {
        text-align: center;
        padding: 4rem 0 3rem 0;
        background: linear-gradient(90deg, rgba(0,245,255,0.08), transparent);
        border-bottom: 2px solid var(--accent);
    }
    .name {
        font-family: 'Space Grotesk', sans-serif;
        font-size: 4.2rem;
        font-weight: 700;
        background: linear-gradient(90deg, #00f5ff, #ff2e63);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin: 0;
        text-shadow: 0 0 30px rgba(0,245,255,0.5);
    }
    .tagline {
        font-size: 1.5rem;
        color: var(--accent);
        margin: 0.5rem 0 1.5rem 0;
        letter-spacing: 2px;
    }

    .glass-card {
        background: var(--card);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(0,245,255,0.2);
        border-radius: 16px;
        padding: 1.8rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .glass-card:hover {
        transform: translateY(-8px);
        box-shadow: 0 20px 40px rgba(0,245,255,0.15);
        border-color: var(--accent);
    }

    .neon-text {
        color: var(--accent);
        text-shadow: 0 0 15px var(--accent);
    }

    .skill-pill {
        display: inline-block;
        background: rgba(0,245,255,0.1);
        color: var(--accent);
        padding: 0.55rem 1.2rem;
        border-radius: 50px;
        margin: 0.35rem;
        font-weight: 500;
        border: 1px solid rgba(0,245,255,0.3);
        transition: all 0.2s;
    }
    .skill-pill:hover {
        background: var(--accent);
        color: #0a0f1c;
        transform: scale(1.05);
    }

    .lab-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
        gap: 1.2rem;
    }
    .lab-item {
        text-align: center;
        padding: 1.5rem 1rem;
        background: rgba(15,23,42,0.7);
        border-radius: 14px;
        border: 1px solid rgba(0,245,255,0.15);
    }
    .lab-icon {
        font-size: 3rem;
        margin-bottom: 1rem;
    }

    .section-header {
        font-size: 2rem;
        font-weight: 700;
        margin: 2.5rem 0 1.5rem 0;
        color: white;
        position: relative;
    }
    .section-header::after {
        content: '';
        position: absolute;
        bottom: -8px;
        left: 0;
        width: 60px;
        height: 3px;
        background: var(--accent);
        border-radius: 3px;
    }
</style>
""", unsafe_allow_html=True)

# ========================= DATA =========================
NAME = "SAFAA ZEMMAR"
TAGLINE = "CYBERSECURITY • VIRTUALISATION • INFRASTRUCTURE"

PROFILE = """
Étudiante en Bachelor 2 Informatique à Ynov Paris, passionnée par la cybersécurité opérationnelle et la sécurisation des infrastructures. 
Je construis des environnements techniques réalistes pour comprendre les mécanismes avant d’utiliser les outils. 
Mon objectif : devenir une analyste SOC ou pentester technique spécialisée en virtualisation sécurisée.
"""

LAB_COMPONENTS = [
    {"icon": "🖥️", "title": "Machines Virtuelles", "desc": "Windows 10/11 + Debian 12 + Ubuntu Server"},
    {"icon": "🔥", "title": "pfSense Firewall", "desc": "Règles de filtrage, NAT, segmentation réseau"},
    {"icon": "🌐", "title": "Serveur Apache + Proxy", "desc": "Reverse proxy + configuration sécurisée"},
    {"icon": "📡", "title": "Réseau Cisco", "desc": "VLAN • Routage • Switching • Packet Tracer"},
    {"icon": "🔍", "title": "Analyse Réseau", "desc": "Wireshark • Nmap • TCPDump"},
    {"icon": "🛡️", "title": "Environnement Isolé", "desc": "Tests d’attaques & défense en lab contrôlé"}
]

SKILLS = {
    "Infrastructure & Virtualisation": ["VirtualBox", "VMware", "Linux (Debian/Ubuntu)", "Windows Server", "pfSense", "Apache", "Proxy"],
    "Réseau & Analyse": ["TCP/IP", "VLAN", "Cisco", "Wireshark", "Nmap", "DNS/SSH"],
    "Cybersécurité": ["Firewall Rules", "SQL Injection", "XSS", "Session Management", "TLS/HTTPS", "CTF"],
    "Développement": ["Python", "PHP & MySQL", "Java Swing", "HTML/CSS/JS", "Git"]
}

VISION = """
Je veux évoluer vers des postes où la technique rencontre la sécurité :  
• Analyste SOC / Blue Team  
• Administratrice systèmes & réseaux sécurisés  
• Pentester infrastructure & virtualisation  
Mon moteur : comprendre profondément les systèmes pour mieux les protéger.
"""

# ========================= LAYOUT =========================
# HERO
st.markdown(f"""
<div class="hero">
    <h1 class="name">{NAME}</h1>
    <p class="tagline">{TAGLINE}</p>
    <div style="margin-top:2rem;">
        <a href="https://github.com/safaa60" target="_blank" style="color:var(--accent); margin:0 1.5rem; text-decoration:none;">🐙 GitHub</a>
        <a href="mailto:safaazemmar@gmail.com" style="color:var(--accent); margin:0 1.5rem; text-decoration:none;">✉️ Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)

# SIDEBAR
with st.sidebar:
    st.markdown("### 🛡️ Navigation")
    page = st.radio(
        label="",
        options=["Accueil", "Mon Cyber Lab", "Sécurité Applicative", "Compétences", "Vision & Objectifs"],
        label_visibility="collapsed"
    )
    st.markdown("---")
    st.caption("Étudiante en alternance recherchée • B3 Cybersécurité")
    if st.button("⬇️ Télécharger mon CV PDF", use_container_width=True):
        st.success("CV téléchargé ! (ajoute ton vrai PDF dans assets pour que ça marche)")

# MAIN CONTENT
if page == "Accueil":
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"""
        <div class="glass-card" style="margin-top:2rem;">
            <h2 class="neon-text">👋 Bienvenue sur mon portfolio</h2>
            <p style="font-size:1.15rem; line-height:1.7;">{PROFILE}</p>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.image("https://via.placeholder.com/380x420/0a0f1c/00f5ff?text=SAFAA+ZEMMAR", use_container_width=True)  # Remplace par ta vraie photo

elif page == "Mon Cyber Lab":
    st.markdown('<h2 class="section-header">🧪 Mon Cyber Lab Personnel</h2>', unsafe_allow_html=True)
    st.markdown("Un environnement complet que j’ai construit moi-même pour expérimenter en conditions réelles.")
    
    st.markdown('<div class="lab-grid">', unsafe_allow_html=True)
    for item in LAB_COMPONENTS:
        st.markdown(f"""
            <div class="lab-item glass-card">
                <div class="lab-icon">{item["icon"]}</div>
                <h3 style="margin:0.5rem 0 0.3rem 0;">{item["title"]}</h3>
                <p style="color:var(--light); font-size:0.95rem;">{item["desc"]}</p>
            </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Sécurité Applicative":
    st.markdown('<h2 class="section-header">🌐 Sécurité Applicative</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="glass-card">
        <p>J’intègre la sécurité dès la conception de mes projets de développement :</p>
        <ul style="font-size:1.1rem; line-height:2;">
            <li>Authentification & gestion des sessions</li>
            <li>Validation stricte des entrées utilisateur</li>
            <li>Protection contre SQL Injection & XSS</li>
            <li>Réflexion sur l’architecture sécurisée</li>
        </ul>
        <p><strong>Chaque ligne de code est une opportunité d’apprendre la cybersécurité.</strong></p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Compétences":
    st.markdown('<h2 class="section-header">🛠️ Mes Compétences</h2>', unsafe_allow_html=True)
    for category, items in SKILLS.items():
        st.markdown(f"""
        <div class="glass-card" style="margin-bottom:1.8rem;">
            <h3 style="color:var(--accent); margin-bottom:1rem;">{category}</h3>
            <div>
                {''.join([f'<span class="skill-pill">{skill}</span>' for skill in items])}
            </div>
        </div>
        """, unsafe_allow_html=True)

elif page == "Vision & Objectifs":
    st.markdown('<h2 class="section-header">🎯 Ma Vision</h2>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="glass-card">
        <p style="font-size:1.2rem; line-height:1.8;">{VISION}</p>
        <div style="margin-top:2rem; padding:1.5rem; background:rgba(0,245,255,0.05); border-radius:12px; border-left:5px solid var(--accent);">
            <strong>Je cherche une alternance B3 Cybersécurité dès septembre 2026</strong><br>
            SOC • Pentest • Infrastructure sécurisée • Virtualisation
        </div>
    </div>
    """, unsafe_allow_html=True)

# FOOTER
st.markdown("---")
st.markdown("""
<div style="text-align:center; color:#64748b; padding:2rem 0;">
    © 2026 Safaa Zemmar — Portfolio Cybersécurité • Fait avec passion et du café ☕
</div>
""", unsafe_allow_html=True)