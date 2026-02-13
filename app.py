import streamlit as st

st.set_page_config(
    page_title="Safaa Zemmar — Portfolio Cyber",
    page_icon="🛡️",
    layout="wide"
)

# ---------------- STYLE PREMIUM ----------------
st.markdown("""
<style>
.block-container {max-width: 1200px;}

.bg {
    position: fixed;
    inset: 0;
    z-index: -1;
    background:
      radial-gradient(900px 600px at 15% 10%, rgba(99,102,241,.22), transparent 60%),
      radial-gradient(700px 500px at 85% 15%, rgba(16,185,129,.18), transparent 60%),
      radial-gradient(900px 650px at 55% 88%, rgba(236,72,153,.14), transparent 55%),
      linear-gradient(180deg, #050611 0%, #050611 100%);
    animation: hue 10s ease-in-out infinite alternate;
}

@keyframes hue {
    from { filter: hue-rotate(0deg); }
    to { filter: hue-rotate(25deg); }
}

.hero {
    border: 1px solid rgba(255,255,255,.10);
    background: rgba(255,255,255,.05);
    backdrop-filter: blur(12px);
    border-radius: 22px;
    padding: 26px;
    box-shadow: 0 25px 60px rgba(0,0,0,.45);
    position: relative;
    overflow: hidden;
}

.hero:before {
    content: "";
    position: absolute;
    inset: -2px;
    background: linear-gradient(90deg, rgba(99,102,241,.60), rgba(16,185,129,.40), rgbargba(236,72,153,.35));
    opacity: 0.35;
    filter: blur(30px);
    animation: glow 4s ease-in-out infinite alternate;
}

@keyframes glow {
    from { transform: translateX(-10px); }
    to { transform: translateX(10px); }
}

.title {
    font-size: 2.5rem;
    font-weight: 900;
    color: rgba(255,255,255,.95);
    letter-spacing: -0.03em;
}

.subtitle {
    color: rgba(255,255,255,.65);
    font-size: 1.05rem;
}

.text {
    color: rgba(255,255,255,.80);
    line-height: 1.6;
}

.card {
    border: 1px solid rgba(255,255,255,.10);
    background: rgba(255,255,255,.04);
    backdrop-filter: blur(12px);
    border-radius: 18px;
    padding: 18px;
    box-shadow: 0 18px 35px rgba(0,0,0,.30);
    transition: all 0.25s ease;
}

.card:hover {
    transform: translateY(-6px);
    border: 1px solid rgba(255,255,255,.20);
    background: rgba(255,255,255,.06);
}

.section-title {
    font-size: 1.15rem;
    font-weight: 900;
    margin-top: 30px;
    color: rgba(255,255,255,.92);
}

.chip {
    display:inline-block;
    padding:.35rem .7rem;
    border-radius:999px;
    background: rgba(255,255,255,.08);
    border: 1px solid rgba(255,255,255,.14);
    color: rgba(255,255,255,.88);
    font-size: .85rem;
    margin: .2rem .25rem 0 0;
}
</style>

<div class="bg"></div>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ----------------
page = st.sidebar.radio(
    "Navigation",
    [
        "Présentation",
        "Cyber Lab",
        "Sécurité Applicative",
        "Compétences",
        "Vision & Objectifs"
    ]
)

# ---------------- HERO ----------------
st.markdown("""
<div class="hero">
<div class="title">🛡️ Safaa Zemmar</div>
<div class="subtitle">Portfolio Cybersécurité</div>
<div class="text">
Étudiante en informatique orientée cybersécurité, avec un background en développement et un intérêt 
particulier pour les systèmes, réseaux et architectures techniques.
</div>
</div>
""", unsafe_allow_html=True)

# ---------------- PAGE 1 ----------------
if page == "Présentation":

    st.markdown('<div class="section-title">Profil</div>', unsafe_allow_html=True)

    st.markdown("""
<div class="card">
<div class="text">
Mon approche de la cybersécurité repose sur la compréhension des mécanismes techniques avant 
l’utilisation des outils.

Je développe mes compétences à travers :

• La construction de labs virtualisés  
• L’expérimentation réseau et systèmes  
• L’analyse des comportements applicatifs  
• L’intégration des problématiques de sécurité dans mes projets de développement  
</div>
</div>
""", unsafe_allow_html=True)

# ---------------- PAGE 2 ----------------
elif page == "Cyber Lab":

    st.markdown('<div class="section-title">🧪 Cyber Lab</div>', unsafe_allow_html=True)

    st.markdown("""
<div class="card">
<div class="text">

<b>Objectif</b><br>
Créer un environnement technique réaliste permettant d’expérimenter des architectures réseau 
et des mécanismes de sécurité.

<b>Composants</b>

• Machines virtuelles Windows / Linux  
• Firewall pfSense  
• Serveur Apache  
• Serveur Proxy  
• LDAP (lab)  

<b>Axes de travail</b>

• Compréhension des flux réseau  
• Logique de segmentation  
• Interaction entre services et systèmes  
• Diagnostic et résolution de problèmes techniques  

</div>
</div>
""", unsafe_allow_html=True)

# ---------------- PAGE 3 ----------------
elif page == "Sécurité Applicative":

    st.markdown('<div class="section-title">🌐 Sécurité Applicative</div>', unsafe_allow_html=True)

    st.markdown("""
<div class="card">
<div class="text">

Mes projets de développement constituent un support d’analyse des problématiques de sécurité :

• Gestion des utilisateurs et authentification  
• Validation des entrées utilisateur  
• Gestion des sessions  
• Réflexion sur les vulnérabilités web (SQL Injection, XSS)  

Approche : intégrer progressivement la sécurité dans la conception applicative.
</div>
</div>
""", unsafe_allow_html=True)

# ---------------- PAGE 4 ----------------
elif page == "Compétences":

    st.markdown('<div class="section-title">🛠️ Compétences</div>', unsafe_allow_html=True)

    skills = [
        "Linux", "TCP/IP", "pfSense", "Wireshark",
        "SQL Injection", "XSS", "Sessions",
        "Python", "PHP/SQL", "Java", "Cisco"
    ]

    st.markdown('<div class="card">', unsafe_allow_html=True)
    for skill in skills:
        st.markdown(f'<span class="chip">{skill}</span>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------- PAGE 5 ----------------
elif page == "Vision & Objectifs":

    st.markdown('<div class="section-title">🎯 Vision & Objectifs</div>', unsafe_allow_html=True)

    st.markdown("""
<div class="card">
<div class="text">
Je souhaite évoluer vers des environnements liés à :

• La cybersécurité opérationnelle  
• Les architectures réseau & systèmes  
• La sécurité des applications  
• Les infrastructures techniques  

Objectif : développer une expertise technique solide et une capacité d’analyse approfondie.
</div>
</div>
""", unsafe_allow_html=True)

st.caption("© Safaa Zemmar — Portfolio Cyber")
