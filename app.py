import streamlit as st

st.set_page_config(
    page_title="Safaa Zemmar | Portfolio",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== CSS SIMPLE & MODERNE ======================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    .stApp { background: #0a1428; color: #e0f2fe; font-family: 'Inter', sans-serif; }
    
    .hero { padding: 6rem 0 4rem 0; text-align: center; }
    .name { font-size: 4.8rem; font-weight: 700; margin: 0; color: white; letter-spacing: -2px; }
    .tagline { font-size: 1.65rem; color: #22d3ee; margin: 1rem 0 2rem 0; font-weight: 500; }
    
    .profile-text { 
        max-width: 780px; 
        margin: 0 auto; 
        font-size: 1.22rem; 
        line-height: 1.75; 
        color: #cbd5e1;
    }
    
    .btn {
        display: inline-block;
        background: transparent;
        color: white;
        border: 2px solid #22d3ee;
        padding: 14px 32px;
        border-radius: 50px;
        font-weight: 600;
        margin: 0 12px;
        text-decoration: none;
        transition: all 0.3s;
    }
    .btn:hover {
        background: #22d3ee;
        color: #0a1428;
        transform: translateY(-3px);
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
    st.markdown("🌐 [Portfolio](https://portfoliosafaaazemmar.streamlit.app)")

    if st.button("⬇️ Télécharger mon CV PDF", use_container_width=True):
        st.success("CV téléchargé ! (place ton PDF dans le dossier assets)")

# ====================== ACCUEIL (comme ton screenshot) ======================
if page == "Accueil":
    st.markdown("""
    <div class="hero">
        <h1 class="name">SAFAA ZEMMAR</h1>
        <p class="tagline">Virtualisation • Cybersécurité • Infrastructure</p>
        
        <p class="profile-text">
            Étudiante en Bachelor 2 Informatique à Ynov Paris, passionnée par la cybersécurité 
            et la sécurisation des infrastructures. Je construis des labs techniques réalistes 
            pour vraiment comprendre les systèmes avant d’utiliser les outils. 
            Je recherche une alternance B3 en cybersécurité dès septembre 2026.
        </p>
        
        <div style="margin-top: 3rem;">
            <a href="https://github.com/safaa60" target="_blank" class="btn">🐙 GitHub</a>
            <a href="mailto:safaazemmar@gmail.com" class="btn">✉️ Me contacter</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ====================== AUTRES SECTIONS ======================
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
    st.markdown("""
    • Déploiement de plusieurs machines virtuelles (Linux + Windows)  
    • Réseau interne virtualisé (NAT + réseau isolé)  
    • Installation et configuration de pfSense  
    • Analyse du trafic réseau avec Wireshark
    """)

elif page == "Projets":
    st.markdown('<h2 class="section-title">🚀 Projets</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <strong>Site E-commerce</strong> — PHP / SQL avec protection contre SQL Injection et XSS<br>
        <strong>Application Java</strong> — Interface Swing<br>
        <strong>Scripts Python</strong> — Automatisation<br>
        <strong>Sites web</strong> — HTML/CSS
    </div>
    """, unsafe_allow_html=True)

elif page == "Expériences":
    st.markdown('<h2 class="section-title">💼 Expériences</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        <strong>Novembre 2025 (2 mois)</strong><br>
        Stage IoT & Supervision Sécurisée — Numeryx<br>
        Architecture IoT basée sur MQTT, Mosquitto, Node-RED, Grafana, Thingspeak
    </div>
    <div class="card">
        <strong>2023</strong><br>
        Stage Girls Can Code — École 42 & ECE Paris<br>
        Algorithmique, résolution de problèmes, travail en équipe, découverte Linux
    </div>
    """, unsafe_allow_html=True)

elif page == "Formation":
    st.markdown('<h2 class="section-title">🎓 Formation</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        • Bachelor 2 Informatique — Ynov Campus Paris Est (2025-2026)<br>
        • Baccalauréat Général (spécialités NSI + SES) — 2024<br>
        • Certification Pix
    </div>
    """, unsafe_allow_html=True)

elif page == "Objectifs":
    st.markdown('<h2 class="section-title">🎯 Objectifs</h2>', unsafe_allow_html=True)
    st.markdown("""
    <div class="card">
        Je recherche une <strong>alternance B3 Cybersécurité</strong> dès septembre 2026 dans les domaines :<br><br>
        • Analyste SOC / Blue Team<br>
        • Pentest Infrastructure & Virtualisation<br>
        • Sécurité des systèmes et réseaux
    </div>
    """, unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown('<p style="text-align:center; color:#64748b; padding:2rem;">© 2026 Safaa Zemmar — Portfolio simple & moderne</p>', unsafe_allow_html=True)