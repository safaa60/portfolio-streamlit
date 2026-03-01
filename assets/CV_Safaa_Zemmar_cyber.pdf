import streamlit as st
from pathlib import Path

# ====================== CONFIG ======================
st.set_page_config(
    page_title="Safaa Zemmar | Cyber Portfolio",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

CV_PATH = Path("CV_Safaa_Zemmar_cyber.pdf")  # mets ton PDF ici (même dossier que app.py)

# ====================== CSS CYBER MODERNE ======================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root{
  --bg0:#070b18;
  --bg1:#0a1428;
  --card: rgba(17, 25, 40, .72);
  --stroke: rgba(148, 163, 184, .18);
  --text:#e2e8f0;
  --muted:#94a3b8;
  --cyan:#22d3ee;
  --green:#34d399;
  --violet:#a78bfa;
  --pink:#fb7185;
}

html, body, [class*="css"]{
  font-family: 'Inter', sans-serif;
}

.stApp{
  background: radial-gradient(1200px 700px at 20% 10%, rgba(34,211,238,.22), transparent 55%),
              radial-gradient(900px 600px at 90% 20%, rgba(167,139,250,.18), transparent 55%),
              radial-gradient(900px 700px at 40% 90%, rgba(52,211,153,.12), transparent 60%),
              linear-gradient(180deg, var(--bg0), var(--bg1));
  color: var(--text);
}

/* subtle animated grid */
.stApp:before{
  content:"";
  position: fixed;
  inset: 0;
  background-image:
    linear-gradient(rgba(34,211,238,.06) 1px, transparent 1px),
    linear-gradient(90deg, rgba(34,211,238,.06) 1px, transparent 1px);
  background-size: 64px 64px;
  mask-image: radial-gradient(500px 300px at 25% 15%, black, transparent 70%);
  pointer-events:none;
  animation: gridmove 18s linear infinite;
}
@keyframes gridmove { from{transform:translateY(0)} to{transform:translateY(64px)} }

/* Sidebar */
section[data-testid="stSidebar"]{
  background: rgba(2,6,23,.72);
  border-right: 1px solid rgba(148,163,184,.12);
  backdrop-filter: blur(14px);
}

/* Headings */
h1,h2,h3,h4{ color: white; letter-spacing: -0.02em; }

/* cyber glow helpers */
.glow{
  text-shadow: 0 0 16px rgba(34,211,238,.45);
}
.badge{
  display:inline-flex;
  align-items:center;
  gap:.5rem;
  padding:.35rem .7rem;
  border-radius: 999px;
  background: rgba(34,211,238,.10);
  border: 1px solid rgba(34,211,238,.22);
  color: #c7f9ff;
  font-size: .9rem;
  font-weight: 600;
}

.hero{
  padding: 5.2rem 0 2.6rem 0;
  text-align:center;
}
.hero-name{
  font-size: clamp(3rem, 5vw, 5.2rem);
  font-weight: 800;
  margin: 0;
}
.hero-tag{
  margin-top: 1rem;
  font-size: 1.25rem;
  color: var(--cyan);
  font-weight: 700;
}
.hero-bio{
  max-width: 860px;
  margin: 1.5rem auto 0 auto;
  color: #cbd5e1;
  font-size: 1.08rem;
  line-height: 1.9;
}

/* Buttons */
.btnrow{ margin-top: 2.2rem; display:flex; justify-content:center; gap: 1rem; flex-wrap: wrap;}
a.cybtn{
  display:inline-flex;
  align-items:center;
  gap:.6rem;
  padding: .9rem 1.25rem;
  border-radius: 999px;
  text-decoration:none;
  font-weight: 700;
  border: 1px solid rgba(34,211,238,.35);
  background: rgba(34,211,238,.08);
  color: white;
  transition: transform .15s ease, box-shadow .2s ease, background .2s ease;
  box-shadow: 0 0 0 rgba(34,211,238,0);
}
a.cybtn:hover{
  transform: translateY(-1px);
  background: rgba(34,211,238,.14);
  box-shadow: 0 0 28px rgba(34,211,238,.22);
}
a.cybtn.secondary{
  border: 1px solid rgba(167,139,250,.35);
  background: rgba(167,139,250,.08);
}
a.cybtn.secondary:hover{
  background: rgba(167,139,250,.14);
  box-shadow: 0 0 28px rgba(167,139,250,.22);
}

/* Cards */
.card{
  background: var(--card);
  border: 1px solid var(--stroke);
  border-radius: 20px;
  padding: 1.25rem 1.25rem;
  backdrop-filter: blur(14px);
  box-shadow: 0 12px 40px rgba(0,0,0,.35);
}
.card:hover{
  border-color: rgba(34,211,238,.35);
}

.kpi{
  display:flex; gap:1rem; flex-wrap:wrap; margin-top: 1rem;
}
.kpi .pill{
  padding:.55rem .85rem;
  border-radius: 14px;
  border: 1px solid rgba(148,163,184,.16);
  background: rgba(15,23,42,.45);
  color: #dbeafe;
  font-weight: 650;
  font-size: .95rem;
}

/* Section title */
.section-title{
  display:inline-flex;
  align-items:center;
  gap:.6rem;
  margin: 1.4rem 0 1rem 0;
  padding-bottom: .55rem;
  border-bottom: 2px solid rgba(34,211,238,.35);
  font-size: 1.65rem;
  font-weight: 800;
}

/* Timeline */
.timeline{
  position: relative;
  padding-left: 1.2rem;
}
.timeline:before{
  content:"";
  position:absolute;
  left:.35rem;
  top:.2rem;
  bottom:.2rem;
  width: 2px;
  background: rgba(34,211,238,.25);
}
.tl-item{
  position:relative;
  margin: 0 0 1rem 0;
  padding: 0 0 0 1.2rem;
}
.tl-item:before{
  content:"";
  position:absolute;
  left:.15rem;
  top:.25rem;
  width:10px; height:10px;
  border-radius:99px;
  background: rgba(34,211,238,.9);
  box-shadow: 0 0 18px rgba(34,211,238,.45);
}

/* Small text */
.muted{ color: var(--muted); }

/* Streamlit widgets tweaks */
div[data-testid="stRadio"] label, .stMarkdown, .stText, .stWrite{ color: var(--text); }
.stButton>button{
  border-radius: 14px !important;
  border: 1px solid rgba(34,211,238,.35) !important;
  background: rgba(34,211,238,.10) !important;
  color: white !important;
  font-weight: 750 !important;
}
.stButton>button:hover{
  background: rgba(34,211,238,.16) !important;
  box-shadow: 0 0 22px rgba(34,211,238,.18) !important;
}

/* Footer */
.footer{
  text-align:center;
  color: rgba(148,163,184,.75);
  padding: 2rem 0 1rem 0;
}
</style>
""", unsafe_allow_html=True)

# ====================== SIDEBAR ======================
with st.sidebar:
    st.markdown("## 🛡️ SAFAA ZEMMAR")
    st.markdown("<span class='badge'>Virtualisation</span> <span class='badge'>Cybersécurité</span> <span class='badge'>Infra</span>",
                unsafe_allow_html=True)
    st.markdown("---")

    page = st.radio(
        "Navigation",
        ["Accueil", "Compétences", "Cyber Lab", "Projets", "Expériences", "Formation", "Objectifs", "Contact"],
        label_visibility="collapsed"
    )

    st.markdown("---")
    st.markdown("📍 Paris, France")
    st.markdown("📱 07 54 58 73 77")
    st.markdown("✉️ safaazemmar@gmail.com")
    st.markdown("🐙 GitHub : github.com/safaa60")

    st.markdown("---")
    if CV_PATH.exists():
        with open(CV_PATH, "rb") as f:
            st.download_button(
                "⬇️ Télécharger mon CV (PDF)",
                data=f,
                file_name=CV_PATH.name,
                mime="application/pdf",
                use_container_width=True
            )
    else:
        st.warning("Ajoute ton CV PDF dans le dossier du projet (ex: CV_Safaa_Zemmar_cyber.pdf).")

# ====================== PAGES ======================
if page == "Accueil":
    st.markdown("<div class='hero'>", unsafe_allow_html=True)
    st.markdown("<h1 class='hero-name glow'>SAFAA ZEMMAR</h1>", unsafe_allow_html=True)
    st.markdown("<div class='hero-tag'>Virtualisation • Cybersécurité • Infrastructure</div>", unsafe_allow_html=True)
    st.markdown("""
    <div class="hero-bio">
      Étudiante en Bachelor Informatique à <b>Ynov Paris</b>, passionnée par la cybersécurité et la sécurisation
      des infrastructures. Je construis des <b>labs techniques réalistes</b> pour comprendre en profondeur
      les systèmes, le réseau, et les attaques/défenses.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="btnrow">
      <a class="cybtn" href="https://github.com/safaa60" target="_blank">🐙 GitHub</a>
      <a class="cybtn secondary" href="mailto:safaazemmar@gmail.com">✉️ Me contacter</a>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3, gap="large")
    with c1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🔐 Focus")
        st.markdown("- Hardening & segmentation réseau\n- Firewalling (pfSense)\n- Analyse trafic & détection")
        st.markdown("</div>", unsafe_allow_html=True)
    with c2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🧪 Méthode")
        st.markdown("- Construire → tester → casser → sécuriser\n- Labs isolés (NAT / réseau interne)\n- Notes & docs pour reproduire")
        st.markdown("</div>", unsafe_allow_html=True)
    with c3:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🎯 Objectif")
        st.markdown("Alternance B3 Cybersécurité dès **septembre 2026**, idéalement orientée **virtualisation & infra sécurisée**.")
        st.markdown("</div>", unsafe_allow_html=True)

elif page == "Compétences":
    st.markdown("<div class='section-title'>🛠️ Compétences</div>", unsafe_allow_html=True)

    left, right = st.columns([1,1], gap="large")
    with left:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🧱 Virtualisation & Infrastructure")
        st.markdown("""
- VirtualBox • VM Linux/Windows  
- Segmentation réseau • NAT / réseaux internes  
- Déploiement d’environnements multi-VM  
        """)
        st.markdown("<div class='kpi'>"
                    "<div class='pill'>VMs multi-réseaux</div>"
                    "<div class='pill'>Routage / NAT</div>"
                    "<div class='pill'>Isolement</div>"
                    "</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🐧 Admin Linux")
        st.markdown("""
- Debian • Ubuntu  
- Apache / Proxy  
- Gestion utilisateurs • services système  
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🌐 Réseau & Analyse")
        st.markdown("""
- TCP/IP • DNS • SSH  
- Cisco : VLAN, routage, switching  
- Wireshark • Nmap  
        """)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### 🛡️ Sécurité")
        st.markdown("""
- pfSense • firewalling  
- HTTPS/TLS  
- SQLi / XSS (tests en environnement isolé)  
        """)
        st.markdown("</div>", unsafe_allow_html=True)

elif page == "Cyber Lab":
    st.markdown("<div class='section-title'>🧪 Mon Cyber Lab</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Architecture (vue rapide)")
    st.markdown("""
- Plusieurs VMs **Linux + Windows**  
- Réseau interne virtualisé (**NAT / réseau isolé**)  
- **pfSense** en frontière (règles, NAT, segmentation)  
- Analyse trafic avec **Wireshark** / scans **Nmap**  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

    a, b = st.columns([1,1], gap="large")
    with a:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Scénarios que je reproduis")
        st.markdown("""
- Accès admin : durcissement, services, droits  
- Réseau : VLAN/logique, filtrage, règles firewall  
- Sécurité web : HTTPS/TLS, tests basiques d’attaque  
        """)
        st.markdown("</div>", unsafe_allow_html=True)
    with b:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Ce que je mesure")
        st.markdown("""
- Surface d’attaque (ports/services)  
- Flux réseau (avant/après filtrage)  
- Trafic anormal (captures, patterns simples)  
        """)
        st.markdown("</div>", unsafe_allow_html=True)

elif page == "Projets":
    st.markdown("<div class='section-title'>🚀 Projets</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### Sélection")
    st.markdown("""
- **Architecture IoT (MQTT/MQTTS)** : sécurisation Mosquitto, Node-RED, dashboards (Grafana), intégration IoT  
- **Lab cybersécurité** : pfSense, réseau isolé, analyse trafic  
- **Site e-commerce** (PHP/SQL) : principes de sécurité (validation, erreurs, etc.)  
- **Scripts Python** : automatisation / tooling  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Expériences":
    st.markdown("<div class='section-title'>💼 Expériences</div>", unsafe_allow_html=True)

    st.markdown("<div class='card timeline'>", unsafe_allow_html=True)
    st.markdown("""
<div class="tl-item">
  <h4>Novembre 2025 — Stage IoT & Supervision Sécurisée (Numeryx) <span class="muted">• 2 mois</span></h4>
  <div class="muted">MQTT/MQTTS • Mosquitto • Node-RED • ThingSpeak • Grafana</div>
</div>
<div class="tl-item">
  <h4>2023 — Stage Girls Can Code <span class="muted">• École 42 & ECE Paris</span></h4>
  <div class="muted">Découverte dev / algo / projets</div>
</div>
    """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Formation":
    st.markdown("<div class='section-title'>🎓 Formation</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("""
- **Bachelor Informatique** — Ynov Campus Paris Est (**2024–2026**)  
- **Baccalauréat Général** — spécialités **NSI + SES** (2024)  
- **Certification Pix**  
- Langues : Français (natif), Arabe (bilingue), Anglais, Espagnol  
    """)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Objectifs":
    st.markdown("<div class='section-title'>🎯 Objectifs</div>", unsafe_allow_html=True)

    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("""
Je recherche une **alternance B3 en cybersécurité** dès **septembre 2026**, si possible orientée :

- **Virtualisation**
- **Infrastructure sécurisée**
- **Réseau / firewalling**
    """)
    st.markdown("</div>", unsafe_allow_html=True)

elif page == "Contact":
    st.markdown("<div class='section-title'>📨 Contact</div>", unsafe_allow_html=True)

    left, right = st.columns([1,1], gap="large")
    with left:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Me joindre")
        st.markdown("""
- ✉️ **safaazemmar@gmail.com**  
- 🐙 GitHub : **github.com/safaa60**  
- 📍 Paris, France  
        """)
        st.markdown("</div>", unsafe_allow_html=True)

    with right:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("### Message rapide (démo)")
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Nom")
            email = st.text_input("Email")
            msg = st.text_area("Message", height=140)
            sent = st.form_submit_button("Envoyer")
        if sent:
            st.success("Message envoyé (démo). Pour un vrai envoi, on peut connecter un service mail/API.")
        st.markdown("</div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>© 2026 Safaa Zemmar • Cyber Portfolio</div>", unsafe_allow_html=True)