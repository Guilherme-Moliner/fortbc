# CLAUDE.md — Contexto do Projeto fortbc

> Este arquivo é lido automaticamente pelo Claude Code ao iniciar. Mantém o contexto do projeto entre sessões. Atualize-o quando decisões importantes mudarem.

## 🎯 O que é

**Batalha dos Amigos** (repo: `fortbc`) é um jogo de cartas de batalha em lanes, single-file HTML, inspirado no minigame **Fort Condor** de Final Fantasy VII Remake/Rebirth. As cartas-herói são feitas a partir de fotos de 10 amigos reais, com habilidades humorísticas personalizadas.

- **Plataforma:** navegador (single-file `index.html`, sem build, sem servidor)
- **Persistência atual:** `localStorage` (scores e níveis de carta)
- **Hospedagem de assets:** GitHub raw (`raw.githubusercontent.com/Guilherme-Moliner/fortbc/main/assets/`) com fallback base64 embutido
- **Repo:** https://github.com/Guilherme-Moliner/fortbc

## 🗂️ Estrutura esperada do repositório

```
fortbc/
├── index.html          # o jogo completo (single-file, ~300KB com base64 fallback)
├── CLAUDE.md           # este arquivo
├── README.md           # visão geral + como rodar
├── ASSETS.md           # guia de nomes/specs de imagens e áudio
├── GAME_DESIGN.md      # mecânicas e regras detalhadas
├── GAME_DATA.md        # tabela de stats (leitura)
├── GAME_DATA.csv       # tabela de stats (edição)
└── assets/
    ├── heroes/         # arthur.png, fanta.png, garopaba.png, bala.png,
    │                   # nathan.png, leo.png, zaga.png, vitao.png,
    │                   # borba.png, letti.png  (nomes minúsculos, sem acento)
    └── audio/
        └── bgmusic.mp3 # trilha em loop (opcional; jogo roda sem ela)
```

## 🎮 Mecânicas-chave (estado atual)

- **Tabuleiro:** retangular, 2 lanes verticais (Esq/Dir) + zona nula central. Cada lado tem 2 torres (uma por lane, 400 HP) + 1 base central (1000 HP). Base BC = jogador (baixo), Base Floripa = IA (topo).
- **Combate estilo Fort Condor:** unidades não morrem ao chegar na estrutura (ficam em cerco atacando); se cruzam livremente; lutam por proximidade conforme o **range**. Torre **bloqueia** a lane (precisa destruí-la para chegar à base). Torres e bases **revidam** em long range (60 de dano).
- **Range:** melee (~46px) / mid (~120px) / long (~220px). Arthur é o único herói long range. Genérico (peão) é atirador mid. Resto melee.
- **Triângulo:** ATK > DEF > BAL > ATK (1.5x vantagem / 0.67x desvantagem).
- **Tributo:** estrelas 1-4 sem tributo; estrelas 5-6 precisam sacrificar 1 unidade (imediato, permite "deny").
- **ATB:** regenera 0.6/s (máx 10). 5 cartas na mão, compra automática.
- **Anti-empate:** 3min Turbo (2x), 4min Turbo+ (4x), 5min Morte Súbita (1 hit mata). Deck out = derrota.
- **Roguelike:** 3 fights, recompensa entre eles (1 de 3: level up de carta / nova carta / buff de deck).
- **Níveis de carta:** Bronze→Prata→Ouro→Platina→Esmeralda→Diamante (×1.0 a ×1.75), persistidos em localStorage, sobem via recompensa.
- **Pontuação:** kills, dano em estrutura, vitória, bônus velocidade, cartas restantes (+), unidades perdidas (-). Top 10 highscore local.
- **Dificuldades:** Iniciante / Veterano / Mestre (afetam nível e intervalo de jogada da IA).

## 🧙 Heróis e habilidades

| Herói | Tipo | Range | Habilidade |
|---|---|---|---|
| Arthur | ATK | long | único herói long range |
| Fanta | BAL | mid | Recycler: +1 ATB ao ser tributado |
| Garopaba | ATK | melee | Morte heroica: +20% ATK aliados 10s ao morrer |
| Bala | DEF | melee | Provoker: atrai ataques |
| Nathan | DEF | melee | — |
| Léo | ATK | melee | — |
| Zaga | BAL | mid | — |
| Vitão | BAL | mid | Healer: cura aliado ferido ao entrar |
| Borba | DEF | melee | — |
| Letti | ATK | melee | Rusher: ignora unidades, vai direto à torre |

## 🏗️ Arquitetura do código (index.html)

- **`BASE_CARDS`** — array com todos os stats das cartas (fonte da verdade no código; deve espelhar `GAME_DATA.csv`).
- **`HERO_IMAGES_B64`** — fallback base64 dos 10 heróis embutido.
- **`preloadImages()`** — tenta GitHub raw, cai pro base64 se falhar (timeout 2.5s por imagem).
- **`G`** — estado do fight atual (unidades, estruturas, ATB, etc).
- **`APP`** — estado da run (nome, dificuldade, fight atual, deck, score total).
- **`gameLoop()`** — loop principal (movimento, range, combate, cerco, retaliação de estruturas).
- **Telas:** loading → start → game → reward → end (controladas por `showScreen()`).

## ✅ Checklist de tarefas pendentes

- [ ] Garantir `index.html` na raiz do repo
- [ ] Criar `assets/heroes/` e mover os 10 PNGs (nomes exatos minúsculos)
- [ ] Criar `assets/audio/` (e adicionar `bgmusic.mp3` quando houver)
- [ ] `git add`, commit e push de tudo
- [ ] Ativar GitHub Pages (Settings → Pages → branch main) para jogar online
- [ ] Testar um link `raw` de imagem no navegador para validar o caminho

## 🛣️ Roadmap futuro

- [ ] Gerar `BASE_CARDS` automaticamente a partir do `GAME_DATA.csv` (hoje é manual)
- [ ] Imagens de peões/itens (hoje são emoji); o código só busca `heroes/` — precisa estender para `pawns/` e `items/`
- [ ] Trilha sonora + SFX (deploy, hit, vitória)
- [ ] Persistência de score via **n8n** (webhook) além do localStorage
- [ ] Torres centrais adicionais na zona nula (twist)
- [ ] Lanes curvas (polish visual)
- [ ] Mecânicas para alterar o caminho das unidades

## ⚠️ Convenções importantes

- Nomes de arquivos de herói: **minúsculos, sem acento** (`vitao.png`, `leo.png`).
- Não quebrar o fallback base64: o jogo deve sempre rodar mesmo offline ou sem os assets no GitHub.
- Ao mudar stats: editar **tanto** `BASE_CARDS` (no index.html) **quanto** `GAME_DATA.csv` para manterem-se sincronizados.
