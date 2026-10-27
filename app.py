import base64
import json
from html import escape
from pathlib import Path
from textwrap import dedent

import streamlit as st


BASE_DIR = Path(__file__).parent
ASSETS_DIR = BASE_DIR / "assets"
DATA_DIR = BASE_DIR / "data"

LOGO_PATH = ASSETS_DIR / "Logo NIGHTMARE.png"
FALLBACK_LOGOS = [ASSETS_DIR / "nightmare_logo_new.png", ASSETS_DIR / "nightmare_logo.jpeg"]

CONTACT_LINKS = {
    "spotify": "https://open.spotify.com/artist/2cNROZ2xUZblfGjrCXcGlf?si=awUqrWP1QxWizTnxut1mHQ&utm_source=copy-link",
    "youtube": "https://www.youtube.com/channel/UCrzAXVA1LbLpjVwYh3Uynuw",
    "instagram": "https://www.instagram.com/menordavaoriginal",
    "tiktok": "https://www.tiktok.com/@menordava.original",
    "soundcloud": "https://soundcloud.com/mc-menor-da-va",
    "whatsapp": "https://wa.me/5511973533287",
    "pinterest": "https://br.pinterest.com/menordavaoriginal/",
    "x": "https://x.com/MCMenordaVA11",
    "email": "mailto:label.nightmare@gmail.com",
    "telegram": "https://t.me/MCMenordaVA",

}

PRESS_KIT = {
    "artist_name": "Nightmare",
    "base": "Brasil | Atendimento remoto",
    "styles": "Rap, Trap, Boom Bap, Dark Trap, Experimental, Instrumental",
    "contact": "contato@nightmaremusic.com",
}

SERVICES = [
    {
        "name": "Beat exclusivo",
        "description": "Instrumental original criado para a identidade do artista, com assinatura própria.",
        "deliverables": "WAV, MP3, trackouts, contrato de uso exclusivo",
        "deadline": "5 a 10 dias",
    },
    {
        "name": "Beat lease",
        "description": "Licenciamento rápido para single, demo, conteúdo ou pré-lançamento.",
        "deliverables": "WAV, MP3, termos de licença",
        "deadline": "24 a 48 horas",
    },
    {
        "name": "Produção completa",
        "description": "Direção do conceito, beat, arranjo, textura e estrutura da faixa.",
        "deliverables": "Beat, guia vocal, arranjo, sessão organizada",
        "deadline": "10 a 20 dias",
    },
    {
        "name": "Mixagem",
        "description": "Voz firme, grave controlado e espaço para a música bater com clareza.",
        "deliverables": "Mix final, instrumental mix, acapella, revisão",
        "deadline": "3 a 7 dias",
    },
    {
        "name": "Masterização",
        "description": "Finalização para streaming, show, teaser e distribuição digital.",
        "deliverables": "Master WAV, MP3, versão clean se necessário",
        "deadline": "2 a 4 dias",
    },
    {
        "name": "Pacote para single",
        "description": "Produção, mix, master e direção de lançamento para uma faixa.",
        "deliverables": "Faixa final, briefing visual, direção de release",
        "deadline": "15 a 25 dias",
    },
]

PAGES = {
"Home": "Home",
"Projetos": "Álbuns / Projetos",
"Clipes": "Clipes",
"Contato": "Contato"  
}

STYLE_OPTIONS = ["Todos"]


st.set_page_config(
    page_title="NIGHTMARE",
    page_icon="N",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def resolve_logo_path() -> Path | None:
    if LOGO_PATH.exists():
        return LOGO_PATH
    for path in FALLBACK_LOGOS:
        if path.exists():
            return path
    return None


def load_json(path: str | Path) -> list[dict]:
    file_path = DATA_DIR / path if isinstance(path, str) else path
    try:
        with file_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        st.warning(f"Não foi possível ler {file_path.name}. Confira o JSON.")
        return []
    return data if isinstance(data, list) else []


def image_to_base64(path: str | Path | None) -> str:
    if not path:
        return ""
    image_path = Path(path)
    if not image_path.exists():
        return ""
    return base64.b64encode(image_path.read_bytes()).decode("utf-8")


def image_data_uri(path: str | Path | None) -> str:
    if not path:
        return ""
    image_path = Path(path)
    encoded = image_to_base64(image_path)
    if not encoded:
        return ""
    mime = "image/png" if image_path.suffix.lower() == ".png" else "image/jpeg"
    return f"data:{mime};base64,{encoded}"


def logo_img(class_name: str = "brand-logo") -> str:
    src = image_data_uri(resolve_logo_path())
    if not src:
        return '<div class="logo-fallback">NIGHTMARE</div>'
    return f'<img class="{class_name}" src="{src}" alt="Nightmare logo">'



def get_catalog_data() -> tuple[list[dict], list[dict], list[dict]]:
    return load_json("songs.json"), load_json("videos.json"), load_json("albums.json")


def html(markup: str) -> None:
    compact = " ".join(line.strip() for line in dedent(markup).strip().splitlines())
    st.markdown(compact, unsafe_allow_html=True)


def inject_css() -> None:
    logo_uri = image_data_uri(resolve_logo_path())
    watermark = f"url('{logo_uri}')" if logo_uri else "none"
    css = dedent(
        """
    
        
        <style>
        .album-card {
    position: relative;
}

.album-click-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 50;
    display: block;
    cursor: pointer;
    border-radius: inherit;
    text-decoration: none !important;
}
        @import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Inter:wght@400;500;700;800;900&family=Rajdhani:wght@500;600;700&display=swap');

        :root {
            --bg: #000000;
            --bg2: #030303;
            --card: #08090B;
            --card2: #0C0D10;
            --line: rgba(255,255,255,0.07);
            --active: rgba(105, 0, 18, 0.45);
            --red: #650012;
            --red-hover: #7A0018;
            --glow: rgba(90, 0, 18, 0.18);
            --text: #F0F0F0;
            --muted: #9B9B9B;
            --weak: #646464;
        }

        #MainMenu, footer, header, [data-testid="stSidebar"], [data-testid="collapsedControl"] {
            display: none !important;
            visibility: hidden !important;
        }

        html, body, [class*="css"] {
            font-family: 'Inter', sans-serif;
        }

        .stApp {
            color: var(--text);
            background:
                radial-gradient(circle at 74% 18%, rgba(90, 0, 18, 0.12), transparent 34rem),
                radial-gradient(circle at 14% 88%, rgba(55, 0, 10, 0.14), transparent 28rem),
                linear-gradient(145deg, #000000 0%, #030303 48%, #000000 100%);
        }

        .stApp::before {
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            background-image: __WATERMARK__;
            background-repeat: no-repeat;
            background-position: right 3vw bottom 4vh;
            background-size: min(45vw, 830px);
            opacity: 0.042;
            filter: grayscale(1) contrast(1.12);
            z-index: 0;
        }

        .stApp::after {
            content: "";
            position: fixed;
            inset: 0;
            pointer-events: none;
            background: linear-gradient(90deg, rgba(0,0,0,0.98), rgba(0,0,0,0.66), rgba(0,0,0,0.92));
            z-index: 0;
        }

        [data-testid="stAppViewContainer"], [data-testid="stToolbar"], .block-container {
            position: relative;
            z-index: 1;
        }

        .block-container {
            max-width: none;
            padding: 0 2.2rem 2.8rem;
        }

        h1, h2, h3 {
            font-family: 'Bebas Neue', sans-serif;
            color: var(--text);
            text-transform: uppercase;
            letter-spacing: 0.035em;
            font-weight: 400;
        }

        h1 {
            font-size: clamp(5.8rem, 12vw, 11rem);
            line-height: 0.78;
            margin: 0.1rem 0 0.85rem;
        }

        h2 {
            font-size: clamp(2.7rem, 5.4vw, 5.4rem);
            line-height: 0.9;
            margin-bottom: 0.45rem;
        }

        h3 {
            font-size: clamp(1.45rem, 2.1vw, 2rem);
            line-height: 1;
            margin: 0 0 0.55rem;
        }

        p {
            color: var(--muted);
            font-size: 0.98rem;
            line-height: 1.65;
        }

        hr {
            border-color: var(--line);
        }

        ::-webkit-scrollbar { width: 10px; }
        ::-webkit-scrollbar-track { background: #000; }
        ::-webkit-scrollbar-thumb {
            background: linear-gradient(180deg, #262626, #650012);
            border-radius: 999px;
        }

        .site-topbar {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            height: 72px;
            z-index: 999;
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 2rem;
            background: rgba(0, 0, 0, 0.82);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--line);
            box-shadow: 0 18px 42px rgba(0,0,0,0.38);
        }

        .topbar-brand {
    width: 100%;
    display: flex;
    justify-content: center;
    align-items: center;
}

        .topbar-logo {
    width: 150px;
    height: auto;
}
        }

        .topbar-title {
            font-family: 'Bebas Neue', sans-serif;
            color: #fff;
            font-size: 1.75rem;
            letter-spacing: 0.08em;
            line-height: 1;
        }

        .topbar-subtitle {
            margin-top: 0.08rem;
            color: var(--weak);
            font-family: 'Rajdhani', sans-serif;
            font-size: 0.68rem;
            text-transform: uppercase;
            letter-spacing: 0.12em;
        }

        .nav-shell {
            height: 72px;
        }

        .nav-shell [data-testid="stRadio"] {
            position: fixed;
            top: 13px;
            right: 1.6rem;
            z-index: 1000;
            width: min(760px, calc(100vw - 320px));
        }

        .nav-shell [data-testid="stRadio"] > label {
            display: none;
        }

        .nav-shell [role="radiogroup"] {
            display: flex;
            justify-content: flex-end;
            gap: 0.18rem;
            background: transparent;
        }

        .nav-shell [role="radiogroup"] label {
            padding: 0.46rem 0.68rem;
            border-radius: 7px;
            border: 1px solid transparent;
            background: transparent;
            transition: color 160ms ease, background 160ms ease, border-color 160ms ease;
        }

        .nav-shell [role="radiogroup"] label > div:first-child {
            display: none;
        }

        .nav-shell [role="radiogroup"] label p {
            color: var(--muted);
            font-family: 'Rajdhani', sans-serif;
            font-size: 0.86rem;
            font-weight: 800;
            letter-spacing: 0.07em;
            text-transform: uppercase;
            margin: 0;
        }

        .nav-shell [role="radiogroup"] label:hover {
            background: rgba(255,255,255,0.035);
        }

        .nav-shell [role="radiogroup"] label:hover p {
            color: #fff;
        }

        .nav-shell [role="radiogroup"] label:has(input:checked) {
            border-color: transparent;
            background: linear-gradient(180deg, transparent 0 80%, var(--red) 80% 100%);
        }

        .nav-shell [role="radiogroup"] label:has(input:checked) p {
            color: #fff;
        }

        .page-shell {
    width: 100%;
    padding-top: 20px;
}

        .content-wrap {
            width: min(100%, 1320px);
            margin: 0 auto;
        }

        .section-block {
            padding: clamp(2.4rem, 5vw, 4.6rem) 0;
        }

        .kicker,
        .eyebrow {
            color: #B3152E;
            font-family: 'Rajdhani', sans-serif;
            font-size: 0.76rem;
            font-weight: 800;
            letter-spacing: 0.24em;
            text-transform: uppercase;
        }

        .lead {
            color: #E5E5E5;
            max-width: 850px;
            font-size: clamp(1.02rem, 1.45vw, 1.2rem);
            line-height: 1.62;
        }

   .hero-shell {
    min-height: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 2rem;
    text-align: center;
}    
    .hero-shell {
    min-height: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    gap: 2rem;
    text-align: center;
}

.hero-copy {

.hero-copy {
    position: relative;
    width: 100%;
    padding-left: 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    margin-left: auto;
    margin-right: auto;
}

.hero-copy h1 {
    width: 100% !important;
    text-align: center !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
    padding-left: 0 !important;
    transform: none !important;
}

.hero-copy::before {
            content: "";
            position: absolute;
            top: 0.35rem;
            bottom: 0.35rem;
            left: 0;
            width: 3px;
            border-radius: 999px;
            background: linear-gradient(180deg, transparent, #650012 16%, #650012 82%, transparent);
        }

        .hero-text {
            max-width: 690px;
            color: var(--muted);
            font-size: 1.03rem;
        }

 .hero-actions {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-wrap: wrap;
    gap: 0.74rem;
    margin: 1.55rem auto 1.25rem;
}
        }

    
}

        .night-btn {
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 0.78rem 1.12rem;
            text-decoration: none !important;
        }

        .night-btn.primary,
        .stLinkButton > a,
        .stButton > button {
            background: linear-gradient(135deg, #650012, #42000B) !important;
            border-color: rgba(105, 0, 18, 0.65) !important;
        }

        .night-btn:hover,
        .stLinkButton > a:hover,
        .stButton > button:hover {
            transform: translateY(-2px);
            background: #111216 !important;
            border-color: rgba(122,0,24,0.72) !important;
            color: #fff !important;
        }

        .night-btn.primary:hover,
        .stLinkButton > a:hover,
        .stButton > button:hover {
            background: linear-gradient(135deg, #7A0018, #4E000D) !important;
        }

        .hero-logo-wrap {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 60px;
    position: relative;
    transform: translateY(-40px);
    z-index: 2;
}

        .hero-logo-wrap::before {
            content: "";
            position: absolute;
            width: min(78%, 520px);
            aspect-ratio: 1;
            border-radius: 50%;
            background: radial-gradient(circle, rgba(90,0,18,0.12), transparent 66%);
            filter: blur(4px);
        }

        .brand-logo {
            position: relative;
width: min(100%, 850px);
max-height: 420px;
            object-fit: contain;
            display: block;
            filter: drop-shadow(0 42px 40px rgba(0,0,0,0.72));
            opacity: 0.94;
        }

        .logo-fallback {
            font-family: 'Bebas Neue', sans-serif;
            color: #fff;
            font-size: 5rem;
        }

        .identity-note {
            position: absolute;
            right: 0;
            bottom: 1rem;
            max-width: 420px;
            border: 1px solid var(--line);
            border-radius: 9px;
            padding: 1rem;
            background: rgba(8, 9, 11, 0.72);
            backdrop-filter: blur(12px);
        }

        .stat-grid {
            display: grid;
            grid-template-columns: repeat(4, minmax(0, 1fr));
            gap: 0.62rem;
            max-width: 640px;
        }

        .stat-card {
            background: rgba(8,9,11,0.7);
            border: 1px solid var(--line);
            border-radius: 8px;
            padding: 0.75rem 0.82rem;
            min-height: 4.55rem;
        }

        .stat-card strong {
            display: block;
            color: #fff;
            font-family: 'Bebas Neue', sans-serif;
            font-size: 1.75rem;
            line-height: 0.9;
            letter-spacing: 0.035em;
        }

        .stat-card span {
            display: block;
            margin-top: 0.38rem;
            color: var(--weak);
            font-family: 'Rajdhani', sans-serif;
            font-size: 0.72rem;
            font-weight: 800;
            letter-spacing: 0.12em;
            text-transform: uppercase;
        }

        .card {
            background: linear-gradient(180deg, rgba(12,13,16,0.96), rgba(5,5,6,0.97));
            border: 1px solid var(--line);
            border-radius: 9px;
            padding: 1.18rem;
            min-height: 100%;
            box-shadow: 0 22px 48px rgba(0,0,0,0.42);
            transition: transform 180ms ease, border-color 180ms ease, box-shadow 180ms ease;
        }

        .card:hover {
            transform: translateY(-2px);
            border-color: rgba(255,255,255,0.12);
            box-shadow: 0 28px 60px rgba(0,0,0,0.52);
        }

        .tag-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.38rem;
            margin-bottom: 0.8rem;
        }

        .tag {
            display: inline-flex;
            align-items: center;
            border: 1px solid rgba(255,255,255,0.09);
            color: #D7D7D7;
            background: rgba(255,255,255,0.035);
            border-radius: 999px;
            padding: 0.22rem 0.56rem;
            font-family: 'Rajdhani', sans-serif;
            font-size: 0.72rem;
            font-weight: 800;
            letter-spacing: 0.09em;
            text-transform: uppercase;
        }

        .tag.accent {
            color: #fff;
            border-color: rgba(105,0,18,0.45);
            background: rgba(105,0,18,0.13);
        }

        .manifesto,
        .cta-box {
            border: 1px solid var(--line);
            border-left: 3px solid #650012;
            border-radius: 9px;
            padding: clamp(1.25rem, 2.4vw, 2rem);
            margin: 1.35rem 0 1.2rem;
            background: linear-gradient(135deg, rgba(12,13,16,0.94), rgba(4,4,5,0.98));
            box-shadow: 0 26px 62px rgba(0,0,0,0.5);
        }

        .manifesto strong {
            display: block;
            color: #fff;
            font-family: 'Bebas Neue', sans-serif;
            font-size: clamp(1.75rem, 3vw, 3rem);
            line-height: 1.05;
            letter-spacing: 0.035em;
            text-transform: uppercase;
        }

        .media-card {
            position: relative;
            min-height: 19rem;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            overflow: hidden;
        }

        .media-card::before {
            content: "";
            position: absolute;
            inset: 0;
            opacity: 0.1;
            background-image: linear-gradient(90deg, transparent 0 9px, rgba(255,255,255,0.08) 9px 10px, transparent 10px 20px);
            pointer-events: none;
        }

        .media-content,
        .player-strip {
            position: relative;
            z-index: 1;
        }

        .media-content {
            display: grid;
            grid-template-columns: 88px minmax(0, 1fr);
            gap: 1rem;
        }

        .cover-mark {
            width: 88px;
            aspect-ratio: 1 / 1;
            border-radius: 8px;
            border: 1px solid var(--line);
            background:
                radial-gradient(circle at 65% 30%, rgba(105, 0, 18, 0.28), transparent 34%),
                linear-gradient(135deg, #101116, #050506),
                repeating-linear-gradient(45deg, #121216 0 7px, #060607 7px 14px);
            box-shadow: inset 0 0 34px rgba(0,0,0,0.65);
        }

        .player-strip {
            margin-top: 1rem;
            display: grid;
            grid-template-columns: auto minmax(0, 1fr) auto;
            align-items: center;
            gap: 0.78rem;
        }

        .play-dot {
            width: 2.6rem;
            height: 2.6rem;
            display: inline-flex;
            align-items: center;
            justify-content: center;
            border-radius: 50%;
            color: #fff !important;
            text-decoration: none !important;
            background: linear-gradient(135deg, #650012, #360008);
            border: 1px solid rgba(255,255,255,0.11);
            box-shadow: 0 0 18px rgba(90,0,18,0.16);
        }

        .progress-shell {
            height: 0.42rem;
            border-radius: 999px;
            overflow: hidden;
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.05);
        }

        .progress-bar {
            height: 100%;
            border-radius: inherit;
            background: linear-gradient(90deg, #343434 0 70%, #650012);
        }

        .mini-links {
            display: flex;
            flex-wrap: wrap;
            justify-content: flex-end;
            gap: 0.38rem;
        }

        .mini-link,
        .social-btn {
            color: #D7D7D7 !important;
            border: 1px solid var(--line);
            background: rgba(255,255,255,0.03);
            text-decoration: none !important;
            font-family: 'Rajdhani', sans-serif;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.07em;
            transition: border-color 160ms ease, background 160ms ease, color 160ms ease;
        }

        .mini-link {
            border-radius: 999px;
            padding: 0.28rem 0.56rem;
            font-size: 0.73rem;
        }

        .mini-link:hover,
        .social-btn:hover {
            color: #fff !important;
            border-color: rgba(105,0,18,0.55);
            background: rgba(105,0,18,0.12);
        }

       .video-frame {
    width: 100%;
    aspect-ratio: 16 / 9;
    overflow: hidden;
    border-radius: 10px;
    background: #000;
}

.video-frame iframe {
    width: 100%;
    height: 100%;
    border: 0;
    display: block;
}
        .album-card {
            background: linear-gradient(180deg, #0C0D10, #050505);
            border: 1px solid var(--line);
            border-radius: 9px;
            padding: 1rem;
            min-height: 30rem;
            box-shadow: 0 26px 58px rgba(0,0,0,0.5);
        }

        .album-art {
            aspect-ratio: 1 / 1;
            border-radius: 8px;
            margin-bottom: 1rem;
            border: 1px solid rgba(255,255,255,0.08);
            background:
                radial-gradient(circle at 70% 22%, rgba(105, 0, 18, 0.28), transparent 28%),
                linear-gradient(135deg, #17181C, #050505 58%),
                repeating-linear-gradient(45deg, rgba(255,255,255,0.035) 0 8px, transparent 8px 16px);
            box-shadow: inset 0 0 70px rgba(0,0,0,0.72);
        }

        .social-grid {
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 0.78rem;
            margin: 1rem 0 1.4rem;
        }

        .social-btn {
            min-height: 3.1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            border-radius: 8px;
        }
.social-btn.whatsapp {
    background: linear-gradient(180deg, #650012 0%, #3a000b 100%);
    border: 1px solid #7a0018;
    color: #ffffff;
    box-shadow:
        0 0 12px rgba(255, 0, 0, 0.22),
        inset 0 1px 0 rgba(255, 255, 255, 0.08);
}

.social-btn.whatsapp:hover {
    background: linear-gradient(180deg, #7a0018 0%, #4a000e 100%);
    border-color: #a00020;
}
        }

        .stSelectbox [data-baseweb="select"] > div {
            background-color: #08090B;
            border-color: var(--line);
        }

        @media (max-width: 1050px) {
            .site-topbar {
                height: auto;
                min-height: 72px;
                padding: 0.65rem 1rem;
                align-items: flex-start;
            }

            .topbar-brand {
                min-width: 180px;
            }

            .nav-shell {
                height: 118px;
            }

            .nav-shell [data-testid="stRadio"] {
                top: 68px;
                left: 1rem;
                right: 1rem;
                width: auto;
            }

            .nav-shell [role="radiogroup"] {
                justify-content: flex-start;
                overflow-x: auto;
                padding-bottom: 0.25rem;
            }

            .page-shell {
    padding-top: 40px;
}

            .hero-shell,
            .press-grid {
                grid-template-columns: 1fr;
            }

            .hero-logo-wrap {
            min-height: 180px;
            }

            .stat-grid,
            .social-grid {
                grid-template-columns: repeat(2, minmax(0, 1fr));
            }

            .player-strip {
                grid-template-columns: auto minmax(0, 1fr);
            }

            .mini-links {
                grid-column: 1 / -1;
                justify-content: flex-start;
            }
        }

        @media (max-width: 720px) {
            .block-container {
                padding: 0 1rem 2rem;
            }

            .hero-actions {
                flex-direction: column;
            }

            .night-btn {
                width: 100%;
            }

            .media-content {
                grid-template-columns: 72px minmax(0, 1fr);
            }

            .cover-mark {
                width: 72px;
            }

            .stApp::before {
                background-position: center 22vh;
                background-size: 92vw;
                opacity: 0.038;
            }
        }.hero-actions {
    display: flex !important;
    justify-content: center !important;
    align-items: center !important;
    gap: 12px !important;
    margin: 30px auto !important;
    width: 100% !important;
}

.hero-actions > a {
    min-height: 3rem !important;
    padding: 0.85rem 1.25rem !important;
    border-radius: 7px !important;
    border: 1px solid rgba(255, 255, 255, 0.14) !important;
    background: #08090b !important;
    color: #f0f0f0 !important;
    text-decoration: none !important;

    font-family: Arial, Helvetica, sans-serif !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    letter-spacing: 0.02em !important;
    line-height: 1 !important;
    text-transform: uppercase !important;

    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;

    text-rendering: optimizeLegibility !important;
    -webkit-font-smoothing: antialiased !important;
    -moz-osx-font-smoothing: grayscale !important;
    text-shadow: none !important;
    filter: none !important;
    transform: none !important;
}
}

.hero-actions > a:first-child {
    background: linear-gradient(180deg, #d61a1a 0%, #9c0000 100%) !important;
    border: 1px solid #ff3b3b !important;
    color: #ffffff !important;

    box-shadow:
        0 0 12px rgba(255,0,0,.45),
        0 0 24px rgba(255,0,0,.30),
        inset 0 1px 0 rgba(255,255,255,.18) !important;
}

.hero-actions > a:first-child:hover {
    background: linear-gradient(180deg, #ff2d2d 0%, #b50000 100%) !important;

    box-shadow:
        0 0 18px rgba(255,0,0,.65),
        0 0 38px rgba(255,0,0,.45),
        inset 0 1px 0 rgba(255,255,255,.25) !important;

    transform: translateY(-2px);
}
        </style>
        """
    ).replace("__WATERMARK__", watermark)
    st.markdown(css, unsafe_allow_html=True)


def stat_card(value: str, label: str) -> str:
    return f'<'


def tag_html(value: str, accent: bool = False) -> str:
    class_name = "tag accent" if accent else "tag"
    return f'<span class="{class_name}">{escape(str(value))}</span>'


def action_link(label: str, url: str, primary: bool = False) -> str:
    class_name = "night-btn primary" if primary else "night-btn"
    return f'<a class="{class_name}" href="{escape(url or "#", quote=True)}" target="_blank" rel="noopener">{escape(label)}</a>'


def mini_link(label: str, url: str) -> str:
    if not url:
        return ""
    return f'<a class="mini-link" href="{escape(url, quote=True)}" target="_blank" rel="noopener">{escape(label)}</a>'


def social_link(label: str, url: str) -> str:
    extra_class = " whatsapp" if label.lower() == "whatsapp" else ""
    return f'<a class="social-btn{extra_class}" href="{escape(url or "#", quote=True)}" target="_blank">{label}</a>'


def render_topbar() -> str:
    html(
        f"""
        <div class="site-topbar">
            <div class="topbar-brand">
                {logo_img("topbar-logo")}
                
            </div>
        </div>
        <div class="nav-shell">
        """
    )
    selected = st.radio("Navegação", list(PAGES.keys()), horizontal=True, key="main_navigation", label_visibility="collapsed")
    html("</div>")
    return PAGES[selected]


def render_basic_card(title: str, body: str, tag: str | None = None) -> None:
    tags = f'<div class="tag-row">{tag_html(tag, True)}</div>' if tag else ""
    html(
        f"""
        <div class="card">
            {tags}
            <h3>{escape(title)}</h3>
            <p>{escape(body)}</p>
        </div>
        """
    )


def render_home(songs: list[dict], videos: list[dict], albums: list[dict]) -> None:
    singles = len([song for song in songs if song.get("category") == "Single"])
    html(
        f"""
        <main class="page-shell">
     <section class="content-wrap hero-shell">

    <div class="hero-copy">

        <div class="eyebrow"></div>

        <h1>NIGHTMARE</h1>

        <p class="lead"></p>

        <p class="hero-text"></p>



    </div>

    <div class="hero-logo-wrap">
        {logo_img()}
    </div>

</section>
        </main>
        """
    )
    
    
        
     


def render_about() -> None:
    html(
        """
        <main class="page-shell">
            <section class="content-wrap section-block">
                <div class="kicker">Sobre</div>
                <h2>Quem é Nightmare</h2>
                <p class="lead">Nightmare é uma marca artística e musical voltada para beats, direção de identidade sonora e construção de lançamentos com presença.</p>
                <p>O projeto une peso, atmosfera urbana, textura escura e visão comercial para artistas que precisam soar fortes antes mesmo do primeiro refrão. Do conceito ao master, a direção é criar uma faixa com narrativa, energia e estética própria.</p>
                <div class="manifesto"><strong>Nightmare não entrega apenas beat. Entrega atmosfera, peso e assinatura sonora.</strong></div>
            </section>
       </main>
    """
)
    
  


def render_song_player(song: dict, index: int) -> None:
    links = song.get("links", {})
    listen_url = next((url for url in links.values() if url), "")
    progress = 28 + ((index * 19) % 46)
    tags = "".join(
        [
            tag_html(song.get("style", "Sound"), True),
            tag_html(song.get("year", "")),
            tag_html(song.get("category", "")),
        ]
    )
    links_html = "".join(
        [
            mini_link("Spotify", links.get("spotify", "")),
            mini_link("SoundCloud", links.get("soundcloud", "")),
            mini_link("YouTube", links.get("youtube", "")),
        ]
    ) or '<span class="mini-link">Link pendente</span>'
    html(
        f"""
        <div class="card media-card">
            <div class="media-content">
                <div class="cover-mark"></div>
                <div>
                    <div class="tag-row">{tags}</div>
                    <h3>{escape(song.get("name", "Faixa sem nome"))}</h3>
                    <p>{escape(song.get("description", ""))}</p>
                </div>
            </div>
            <div class="player-strip">
                <a class="play-dot" href="{escape(listen_url or "#", quote=True)}" target="_blank" rel="noopener">▶</a>
                <div class="progress-shell"><div class="progress-bar" style="width:{progress}%"></div></div>
                <div class="mini-links">{links_html}</div>
            </div>
        </div>
        """
    )
    audio_url = song.get("audio_url") or song.get("audio_file")
    if audio_url:
        st.audio(audio_url)


def render_songs(songs: list[dict]) -> None:
    html('<main class="page-shell"><section class="content-wrap section-block"><div class="kicker">Catálogo musical</div><h2>Músicas / Songs</h2></section></main>')
    selected_style = st.selectbox("Filtrar por estilo", STYLE_OPTIONS)
    filtered = songs if selected_style == "Todos" else [song for song in songs if song.get("style") == selected_style]
    for category, title in [("Single", "Singles"), ("Produção", "Produções")]:
        section_items = [song for song in filtered if song.get("category") == category]
        html(f'<div class="content-wrap"><h3>{escape(title)}</h3></div>')
        if not section_items:
            st.caption("Nenhum item encontrado neste filtro.")
            continue
        cols = st.columns(2, gap="medium")
        for index, song in enumerate(section_items):
            with cols[index % 2]:
                render_song_player(song, index)


def render_videos(videos: list[dict]) -> None:
    html(
        """
        <main class="page-shell">
            <section class="content-wrap section-block">
                <h2>Clipes / Music Videos</h2>
            </section>
        </main>
        """
    )

    for video in videos:
        html(
            f"""
            <div class="content-wrap">
                <div class="card">
                    <div class="tag-row">
                        {tag_html(video.get("year", ""))}
                    </div>

                    <h3>{escape(video.get("name", "Clipe sem nome"))}</h3>

                    <p>
                        <strong>Direção/produção:</strong>
                        {escape(video.get("director", "A definir"))}
                    </p>

                    <p>{escape(video.get("description", ""))}</p>
                </div>
            </div>
            """
        )

        youtube_url = video.get("youtube_url", "").strip()

        if youtube_url:
            if "youtu.be/" in youtube_url:
                video_id = youtube_url.split("youtu.be/")[-1].split("?")[0]
            elif "v=" in youtube_url:
                video_id = youtube_url.split("v=")[-1].split("&")[0]
            else:
                video_id = ""

            html(
                f"""
                <div class="content-wrap">
                    <div class="video-frame">
                        <iframe
                            src="https://www.youtube.com/embed/{video_id}"
                            title="YouTube video player"
                            frameborder="0"
                            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                            allowfullscreen>
                        </iframe>
                    </div>
                </div>
                """
            )
            
        else:
            html(
                """
                <div class="content-wrap">
                    <div class="video-frame">
                        Embed pendente — adicione o link em data/videos.json
                    </div>
                </div>
                """
            )




def render_albums(albums: list[dict]) -> None:
    if not albums:
        st.caption("Nenhum projeto cadastrado ainda.")
        return

    cols = st.columns(3, gap="medium")

    for index, album in enumerate(albums):
        cover_name = str(album.get("cover", "")).strip()
        cover_path = ASSETS_DIR / cover_name if cover_name else None
        cover_src = (
            image_data_uri(cover_path)
            if cover_path and cover_path.exists()
            else ""
        )

        tracks = ", ".join(album.get("main_tracks", []))
        status = str(album.get("status", "unreleased")).title()

        links = album.get("links", {})
        spotify_url = links.get("spotify", "")

        is_clickable = (
    album.get("name", "").strip().upper() in ["PODER PARALELO", "NIGHTMARE", "RESTRITO", "CAMPEÃO", "BENTLEY", "MAQUIAVÉLICO", "ENVOLVENTE", "MEMÓRIAS", "PROGRESSÃO", "NOSSO SENTIMENTO", "LADO FEROZ", "2 LADOS DA MOEDA", "AGRADEÇO À DEUS"]
)
        click_overlay = ""

        if is_clickable and spotify_url:
            click_overlay = (
                f'<a class="album-click-overlay" '
                f'href="{escape(spotify_url, quote=True)}" '
                f'target="_blank" '
                f'rel="noopener noreferrer" '
                f'aria-label="Ouvir {escape(album.get("name", ""))} nas plataformas"></a>'
            )

        cover_style = (
            f' style="background-image:url(\'{cover_src}\');'
            f'background-size:cover;'
            f'background-position:center;"'
            if cover_src
            else ""
        )

        tracks_html = (
            f'<p><strong>Faixas principais:</strong> {escape(tracks)}</p>'
            if tracks
            else ""
        )

        with cols[index % 3]:
            html(
                f"""
                <div class="album-card">
                    {click_overlay}

                    <div class="album-art"{cover_style}></div>

                    <div class="tag-row">
                        {tag_html(status, True)}
                        {tag_html(album.get("year"))}
                    </div>

                    <h3>{escape(album.get("name", "Projeto sem nome"))}</h3>

                    <p>{escape(album.get("concept", ""))}</p>

                    {tracks_html}
                </div>
                """
            )


def render_services() -> None:
    html(
        """
        <main class="page-shell">
            <section class="content-wrap section-block">
                <div class="kicker">Produção musical</div>
                <h2>Serviços</h2>
                <p class="lead">Serviços para artistas, marcas e projetos que precisam sair do rascunho e chegar no lançamento com peso, identidade e acabamento profissional.</p>
            </section>
        </main>
        """
    )
    cols = st.columns(2, gap="medium")
    for index, service in enumerate(SERVICES):
        with cols[index % 2]:
            html(
                f"""
                <div class="card">
                    <h3>{escape(service["name"])}</h3>
                    <p>{escape(service["description"])}</p>
                    <p><strong>Entregáveis:</strong> {escape(service["deliverables"])}</p>
                    <p><strong>Prazo:</strong> {escape(service["deadline"])}</p>
                    <div class="hero-actions">{action_link("Solicitar orçamento", CONTACT_LINKS["whatsapp"], True)}</div>
                </div>
                """
            )
    html(
        f"""
        <div class="content-wrap">
            <div class="cta-box">
                <div class="kicker">Ready for release</div>
                <h2>Quer transformar uma ideia em música finalizada?</h2>
                <p>Do primeiro loop ao master final, o foco é construir uma faixa com identidade, presença e impacto.</p>
                <div class="hero-actions">{action_link("Falar com Nightmare", CONTACT_LINKS["whatsapp"], True)}</div>
            </div>
        </div>
        """
    )


def render_contact() -> None:
    socials = "".join(
        [
            social_link("Instagram", CONTACT_LINKS["instagram"]),
            social_link("YouTube", CONTACT_LINKS["youtube"]),
            social_link("Spotify", CONTACT_LINKS["spotify"]),
            social_link("TikTok", CONTACT_LINKS["tiktok"]),
            social_link("SoundCloud", CONTACT_LINKS["soundcloud"]),
            social_link("WhatsApp", CONTACT_LINKS["whatsapp"]),
            social_link("Telegram", CONTACT_LINKS["telegram"]),
            social_link("Pinterest", CONTACT_LINKS["pinterest"]),
            social_link("X (Twitter)", CONTACT_LINKS["x"]),
            social_link("E-mail", CONTACT_LINKS["email"]),
        

        ]
    )

    html(
        f"""
        <main class="page-shell">
            <section class="content-wrap section-block">

               

               
                <h3 style="margin-top: 1.7rem;">REDES OFICIAIS</h3>

                <div class="social-grid">
                    {socials}
                </div>

               

            </section>
        </main>
        """
    )


def render_footer() -> None:
    st.divider()
    st.caption("Nightmare ©")


def main() -> None:
    inject_css()
    songs, videos, albums = get_catalog_data()
    page = render_topbar()

    if page == "Home":
        render_home(songs, videos, albums)
    elif page == "Sobre":
        render_about()
    elif page == "Songs":
        render_songs(songs)
    elif page == "Clipes":
        render_videos(videos)
    elif page == "Álbuns / Projetos":
        render_albums(albums)
    elif page == "Produção musical / Serviços":
        render_services()
    elif page == "Contato":
        render_contact()

    render_footer()


if __name__ == "__main__":
    main()
