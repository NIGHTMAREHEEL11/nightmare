# Nightmare - Streamlit Press Kit

Landing page, press kit e catálogo musical em Streamlit para a marca artística **Nightmare**, com navegação superior fixa e visual dark/premium.

## Estrutura

```text
.
├── app.py
├── requirements.txt
├── assets/
│   ├── nightmare_logo_transparent.png
│   ├── nightmare_logo_new.png
│   └── nightmare_logo.jpeg
├── data/
│   ├── songs.json
│   ├── videos.json
│   └── albums.json
└── README.md
```

## Como rodar

```bash
pip install -r requirements.txt
streamlit run app.py

```

Depois acesse:

```text
http://localhost:8501
```

## Onde editar

- Logo principal transparente: `assets/nightmare_logo_transparent.png`.
- Fallbacks: `assets/nightmare_logo_new.png` e `assets/nightmare_logo.jpeg`.
- Músicas: `data/songs.json`.
- Clipes: `data/videos.json`.
- Álbuns/projetos: `data/albums.json`.
- Links de Spotify, YouTube, Instagram, TikTok, SoundCloud, e-mail e WhatsApp: constante `CONTACT_LINKS` no topo de `app.py`.
- Serviços: lista `SERVICES` em `app.py`.

## Vídeos

Deixe `youtube_url` vazio enquanto não houver link real. O site exibirá um placeholder artístico:

```json
"youtube_url": ""
```

Quando houver um link oficial, adicione a URL do YouTube no JSON e o app renderizará o embed com `st.video()`.

## Observações

Os dados são fictícios e editáveis. Substitua nomes, links, descrições e informações de contato pelos dados oficiais da marca Nightmare.

A navegação principal fica no topo do site e não depende da sidebar do Streamlit.
