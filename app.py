import streamlit as st
from pathlib import Path

# ========================= CONFIG =========================
st.set_page_config(
    page_title="Safaa Zemmar | Portfolio",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ========================= CSS SIMPLE & MODERNE =========================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    .stApp {
        background: #0f172a;
        color: #e2e8f0;
        font-family: 'Inter', sans-serif;
    }

    .hero {
        padding: 5rem 0 4rem 0;
        display: flex;
        align-items: center;
        gap: 4rem;
    }
    .hero-text h1 {
        font-size: 3.8rem;
        font-weight: 700;
        margin: 0 0 0.8rem 0;
        color: white;
    }
    .hero-text p {
        font-size: 1.35rem;
        color: #94a3b8;
        line-height: 1.6;
    }

    .profile-img {
        width: 280px;
        height: 280px;
        border-radius: 20px;
        object-fit: cover;
        border: 6px solid #22d3ee;
        box-shadow: 0 10px 30px rgba(34, 211, 238, 0.2);
    }

    .section-title {
        font-size: 2.2rem;
        font-weight: 600;
        color: white;
        margin: 3rem 0 1.5rem 0;
        border-bottom: 3px solid #22d3ee;
        padding-bottom: 0.5rem;
        display: inline-block;
    }

    .card {
        background: #1e2937;
        padding: 1.8rem;
        border-radius: 16px;
        border: 1px solid #334155;
        transition: all 0.3s;
    }
    .card:hover {
        border-color: #22d3ee;
        transform: translateY(-4px);
    }

    .skill-pill {
        background: #1e2937;
        color: #22d3ee;
        padding: 10px 20px;
        border-radius: 50px;
        margin: 6px 6px;
        font-size: 1rem;
        border: 1px solid #334155;
        display: inline-block;
    }

    .btn {
        background: #22d3ee;
        color: #0f172a;
        padding: 12px 32px;
        border-radius: 50px;
        font-weight: 600;
        text-decoration: none;
        display: inline-block;
        margin: 8px 8px 8px 0;
        transition: all 0.3s;
    }
    .btn:hover {
        background: white;
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

# ========================= DATA =========================
NAME = "SAFAA ZEMMAR"
TAGLINE = "Virtualisation • Cybersécurité • Infrastructure"

PROFILE = """
Étudiante en Bachelor 2 Informatique à Ynov Paris, passionnée par la cybersécurité et la sécurisation des infrastructures. 
Je construis des labs techniques réalistes pour vraiment comprendre les systèmes avant d’utiliser les outils.
Je recherche une alternance B3 en cybersécurité dès septembre 2026.
"""

# ========================= SIDEBAR =========================
with st.sidebar:
    st.markdown(f"### {NAME}")
    st.markdown(f"**{TAGLINE}**")
    st.markdown("---")
    
    page = st.radio(
        "Navigation",
        ["Accueil", "Mon Cyber Lab", "Projets", "Compétences", "Expériences", "Formation", "Objectifs"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("📍 Paris, France")
    st.markdown("📧 safaazemmar@gmail.com")
    st.markdown("🐙 github.com/safaa60")
    
    if st.button("⬇️ Télécharger mon CV PDF", use_container_width=True):
        st.success("CV téléchargé ! (mets ton PDF dans le dossier assets)")

# ========================= PAGES =========================
if page == "Accueil":
    st.markdown('<div class="hero">', unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(f"""
            <div class="hero-text">
                <h1>{NAME}</h1>
                <p style="font-size:1.5rem; color:#22d3ee;">{TAGLINE}</p>
                <p style="margin-top:2rem; font-size:1.15rem;">{PROFILE}</p>
                
                <div style="margin-top:3rem;">
                    <a href="https://github.com/safaa60" target="_blank" class="btn">🐙 GitHub</a>
                    <a href="mailto:safaazemmar@gmail.com" class="btn">✉️ Me contacter</a>
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <img src="https://via.placeholder.com/600x600/1e2937/22d3ee?text=SAFAA" 
                 class="profile-img" alt="Safaa Zemmar">
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "Mon Cyber Lab":
    st.markdown('<h2 class="section-title">🧪 Mon Cyber Lab</h2>', unsafe_allow_html=True)
    st.write("Environnement complet que j’ai construit et configuré moi-même.")
    
    cols = st.columns(3)
    components = [
        ("Machines virtuelles", "Windows 11 • Debian 12 • Ubuntu"),
        ("Firewall pfSense", "NAT • Segmentation • Règles avancées"),
        ("Serveur Apache + Proxy", "Configuration sécurisée"),
        ("Réseau Cisco", "VLAN • Routage • Switching"),
        ("Analyse réseau", "Wireshark • Nmap"),
        ("Environnement isolé", "Tests d’attaque & défense")
    ]
    for i, (title, desc) in enumerate(components):
        with cols[i % 3]:
            st.markdown(f"""
            <div class="card">
                <h3>{title}</h3>
                <p>{desc}</p>
            </div>
            """, unsafe_allow_html=True)

elif page == "Projets":
    st.markdown('<h2 class="section-title">🚀 Projets</h2>', unsafe_allow_html=True)
    projects = [
        ("Cyber Lab Complet", "Infrastructure virtualisée avec pfSense, Apache, Proxy et réseau Cisco"),
        ("Site E-commerce Sécurisé", "PHP/MySQL + protection SQL Injection, XSS et sessions"),
        ("Analyse Réseau Avancée", "Cartographie et diagnostic avec Nmap + Wireshark")
    ]
    for title, desc in projects:
        st.markdown(f"""
        <div class="card" style="margin-bottom:1.5rem;">
            <h3>{title}</h3>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "Compétences":
    st.markdown('<h2 class="section-title">🛠️ Compétences</h2>', unsafe_allow_html=True)
    
    categories = {
        "Infrastructure & Virtualisation": ["VirtualBox", "Linux (Debian/Ubuntu)", "pfSense", "Apache", "Proxy"],
        "Réseau": ["TCP/IP", "VLAN", "Cisco Packet Tracer", "Wireshark", "Nmap"],
        "Cybersécurité": ["Firewall", "SQL Injection", "XSS", "Gestion des sessions", "TLS/HTTPS"],
        "Développement": ["Python", "PHP/MySQL", "Java", "Git"]
    }
    
    for cat, skills in categories.items():
        st.markdown(f"<h3 style='color:#94a3b8; margin-top:2rem;'>{cat}</h3>", unsafe_allow_html=True)
        st.markdown("".join([f'<span class="skill-pill">{s}</span>' for s in skills]), unsafe_allow_html=True)

elif page == "Expériences":
    st.markdown('<h2 class="section-title">💼 Expériences</h2>', unsafe_allow_html=True)
    exps = [
        ("Nov 2025", "Stage IoT & Supervision Sécurisée", "Numeryx", "Architecture IoT sécurisée • MQTT"),
        ("2023", "Stage Girls Can Code", "École 42 & ECE Paris", "Programmation • Linux • Sites web")
    ]
    for date, title, company, desc in exps:
        st.markdown(f"""
        <div class="card" style="margin-bottom:1.5rem;">
            <p style="color:#22d3ee; font-weight:600;">{date}</p>
            <h3>{title}</h3>
            <p style="color:#64748b;">{company}</p>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

elif page == "Formation":
    st.markdown('<h2 class="section-title">🎓 Formation</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <p><strong>Bachelor 2 Informatique</strong> — Ynov Campus Paris Est (2025-2026)<br>
        Spécialisation Cybersécurité</p>
        <p><strong>Baccalauréat Général</strong> — Mention Assez Bien (2023)<br>
        Spécialités NSI + SES</p>
        <p>Certification Pix</p>
    </div>
    """, unsafe_allow_html=True)

elif page == "Objectifs":
    st.markdown('<h2 class="section-title">🎯 Mes Objectifs</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <p style="font-size:1.2rem;">Je recherche une <strong>alternance B3 Cybersécurité</strong> à partir de septembre 2026.</p>
        <ul style="font-size:1.15rem; line-height:2.2;">
            <li>🔹 Analyste SOC / Blue Team</li>
            <li>🔹 Pentest Infrastructure & Virtualisation</li>
            <li>🔹 Sécurité Réseaux & Systèmes</li>
        </ul>
        <p style="margin-top:2rem; color:#94a3b8;">Prête à apporter rigueur, curiosité technique et motivation dans une équipe.</p>
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown('<p style="text-align:center; color:#64748b; padding:2rem 0;">© 2026 Safaa Zemmar — Portfolio simple & moderne</p>', unsafe_allow_html=True)