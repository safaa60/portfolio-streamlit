import streamlit as st

st.set_page_config(
    page_title="Safaa Zemmar | Portfolio",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== CSS SIMPLE & ÉLÉGANT ======================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    .stApp { 
        background: #0a1428; 
        color: #e0f2fe; 
        font-family: 'Inter', sans-serif; 
    }
    
    .accueil {
        text-align: center;
        padding: 7rem 0 5rem 0;
    }
    .name {
        font-size: 5.2rem;
        font-weight: 700;
        color: white;
        margin: 0;
        letter-spacing: -2px;
    }
    .tagline {
        font-size: 1.7rem;
        color: #22d3ee;
        margin: 1.2rem 0 3rem 0;
    }
    .bio {
        max-width: 720px;
        margin: 0 auto;
        font-size: 1.25rem;
        line-height: 1.8;
        color: #cbd5e1;
    }
    
    .btn {
        display: inline-block;
        background: transparent;
        color: white;
        border: 2px solid #22d3ee;
        padding: 14px 36px;
        border-radius: 50px;
        font-weight: 600;
        margin: 0 12px;
        text-decoration: none;
        transition: all 0.3s;
    }
    .btn:hover {
        background: #22d3ee;
        color: #0a1428;
    }
    
    .section-title {
        font-size: 2.3rem;
        font-weight: 600;
        color: white;
        margin: 3rem 0 1.5rem 0;
        border-bottom: 3px solid #22d3ee;
        padding-bottom: 8px;
        display: inline-block;
    }
    
    .card {
        background: #1e2937;
        padding: 1.8rem;
        border-radius: 16px;
        border: 1px solid #334155;
        margin-bottom: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# ====================== SIDEBAR ======================
with st.sidebar:
    st.markdown("### SAFAA ZEMMAR")
    st.markdown("**Virtualisation • Cybersécurité • Infrastructure**")
    st.markdown("---")
    
    page = st.radio(
        "Navigation",
        ["Accueil", "Compétences", "Mon Cyber Lab", "Projets", "Expériences", "Formation", "Objectifs"],
        label_visibility="collapsed"
    )
    
    st.markdown("---")
    st.markdown("📍 Paris, France")
    st.markdown("📱 07 54 58 73 77")
    st.markdown("✉️ safaazemmar@gmail.com")
    st.markdown("🐙 [GitHub](https://github.com/safaa60)")

    if st.button("⬇️ Télécharger mon CV PDF", use_container_width=True):
        st.success("CV téléchargé !")

# ====================== ACCUEIL (très simple et propre) ======================
if page == "Accueil":
    st.markdown('<div class="accueil">', unsafe_allow_html=True)
    st.markdown('<h1 class="name">SAFAA ZEMMAR</h1>', unsafe_allow_html=True)
    st.markdown('<p class="tagline">Virtualisation • Cybersécurité • Infrastructure</p>', unsafe_allow_html=True)
    
    st.markdown("""
    <p class="bio">
        Étudiante en Bachelor 2 Informatique à Ynov Paris, passionnée par la cybersécurité 
        et la sécurisation des infrastructures. 
        Je construis des labs techniques réalistes pour vraiment comprendre les systèmes.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="margin-top: 3.5rem;">
        <a href="https://github.com/safaa60" target="_blank" class="btn">🐙 GitHub</a>
        <a href="mailto:safaazemmar@gmail.com" class="btn">✉️ Me contacter</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ====================== AUTRES PAGES ======================
elif page == "Compétences":
    st.markdown('<h2 class="section-title">🛠️ Compétences</h2>', unsafe_allow_html=True)
    st.markdown("#### Virtualisation & Infrastructure")
    st.markdown("• VirtualBox • VM Linux/Windows • Segmentation réseau • NAT et réseaux internes")
    st.markdown("#### Administration Linux")
    st.markdown("• Debian • Ubuntu • Apache/Proxy • Gestion utilisateurs • Services système")
    st.markdown("#### Réseau & Analyse")
    st.markdown("• TCP/IP • Cisco (VLAN, routage, switching) • DNS • SSH • Wireshark • Nmap")
    st.markdown("#### Sécurité")
    st.markdown("• pfSense • Firewall • HTTPS/TLS • SQLi / XSS • Tests en environnement isolé")

elif page == "Mon Cyber Lab":
    st.markdown('<h2 class="section-title">🧪 Mon Cyber Lab</h2>', unsafe_allow_html=True)
    st.write("Environnement complet que j’ai construit et configuré moi-même.")
    st.markdown("• Machines virtuelles Linux + Windows  \n• Réseau interne virtualisé avec pfSense  \n• Analyse du trafic avec Wireshark")

elif page == "Projets":
    st.markdown('<h2 class="section-title">🚀 Projets</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        • Site E-commerce sécurisé (PHP / SQL)<br>
        • Application Java Swing<br>
        • Scripts Python d’automatisation<br>
        • Sites web HTML/CSS
    </div>
    """, unsafe_allow_html=True)

elif page == "Expériences":
    st.markdown('<h2 class="section-title">💼 Expériences</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        Novembre 2025 (2 mois) — Stage IoT & Supervision Sécurisée chez Numeryx
    </div>
    <div class="card">
        2023 — Stage Girls Can Code (École 42 & ECE Paris)
    </div>
    """, unsafe_allow_html=True)

elif page == "Formation":
    st.markdown('<h2 class="section-title">🎓 Formation</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        • Bachelor 2 Informatique — Ynov Campus Paris Est (2025-2026)<br>
        • Baccalauréat Général NSI + SES (2024)<br>
        • Certification Pix
    </div>
    """, unsafe_allow_html=True)

elif page == "Objectifs":
    st.markdown('<h2 class="section-title">🎯 Objectifs</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        Je recherche une alternance B3 en cybersécurité dès septembre 2026,<br>
        <strong>si possible orientée virtualisation et infrastructure sécurisée.</strong>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.markdown('<p style="text-align:center; color:#64748b; padding:2rem;">© 2026 Safaa Zemmar</p>', unsafe_allow_html=True)