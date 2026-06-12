# ⚔️ Batalha dos Amigos · fortbc

Um jogo de cartas de batalha em lanes, inspirado no minigame **Fort Condor** de Final Fantasy VII Remake/Rebirth, com cartas-herói feitas a partir de fotos de amigos reais. Single-file HTML, sem build, sem servidor.

---

## 🎮 Como rodar

**Opção 1 — Direto do arquivo:** abra `index.html` no navegador (Chrome, Firefox, Edge). Funciona offline; se não achar as imagens no GitHub, usa as embutidas em base64.

**Opção 2 — GitHub Pages:** ative Pages no repositório (Settings → Pages → branch `main`) e acesse `https://guilherme-moliner.github.io/fortbc/`.

---

## 🗂️ Estrutura do repositório

```
fortbc/
├── index.html          ← o jogo (single-file)
├── README.md           ← este arquivo
├── ASSETS.md           ← guia de imagens e áudio
├── GAME_DESIGN.md      ← mecânicas e regras
├── GAME_DATA.md        ← tabela de stats (leitura)
├── GAME_DATA.csv       ← tabela de stats (edição)
└── assets/
    ├── heroes/         ← arthur.png, fanta.png, ... (10 heróis)
    └── audio/          ← bgmusic.mp3
```

O jogo tenta carregar imagens de `assets/heroes/<id>.png` via `raw.githubusercontent.com`. Se falhar (offline, arquivo ausente), usa o fallback base64 embutido — **nunca quebra**.

---

## 🕹️ Controles

| Ação | Como |
|---|---|
| Selecionar carta | Clique na carta da mão |
| Jogar na lane | Botões "Lane Esq / Lane Dir" |
| Focar no campo | Seta **↑** |
| Focar na mão | Seta **↓** |
| Mutar música | Botão 🔊 no topo |

---

## 🎯 Objetivo

Cada lado tem **2 torres** (uma por lane) + **1 base central**. Para vencer, destrua a **base inimiga** — mas primeiro derrube a **torre** que bloqueia cada lane. Vença os **3 fights** seguidos, escolhendo recompensas entre eles (estilo roguelike).

Veja `GAME_DESIGN.md` para as regras completas e `GAME_DATA.md` para os stats.

---

## 🛠️ Editar stats

1. Abra `GAME_DATA.csv` (Excel/Google Sheets)
2. Ajuste os números
3. Reflita as mudanças na constante `BASE_CARDS` dentro do `index.html`

> Próximo passo planejado: gerar o `BASE_CARDS` automaticamente a partir do CSV.

---

## 🗺️ Roadmap

- [x] Lanes, torres intermediárias e bases
- [x] Sistema de range (melee / mid / long)
- [x] Roguelike de 3 fights + recompensas
- [x] Níveis de carta (Bronze → Diamante)
- [x] Highscores locais
- [x] Loading + preload de imagens via GitHub
- [ ] Trilha sonora final (`assets/audio/bgmusic.mp3`)
- [ ] Persistência de score via n8n
- [ ] Torres centrais adicionais (twist)
- [ ] Lanes curvas (polish visual)
