# CLAUDE.md — Contexto do Projeto fortbc

> Este arquivo é lido automaticamente pelo Claude Code ao iniciar. Mantém o contexto do projeto entre sessões. Atualize-o quando decisões importantes mudarem.
> **Sempre atualize este arquivo ao final de cada sessão de trabalho.**

## 🎯 O que é

**Batalha dos Amigos** (repo: `fortbc`) é um jogo de cartas de batalha em lanes, single-file HTML, inspirado no minigame **Fort Condor** de Final Fantasy VII Remake/Rebirth. As cartas-herói são feitas a partir de fotos de 10 amigos reais, com habilidades humorísticas personalizadas. Tom: engraçado, adulto, referências a álcool e cultura de amigos.

- **Plataforma:** navegador (single-file `index.html`, sem build, sem servidor)
- **Persistência atual:** `localStorage` (scores e níveis de carta)
- **Hospedagem de assets:** GitHub raw (`raw.githubusercontent.com/Guilherme-Moliner/fortbc/main/assets/`) com fallback base64 embutido
- **Repo:** https://github.com/Guilherme-Moliner/fortbc
- **Jogo online:** https://guilherme-moliner.github.io/fortbc/

## 🗂️ Estrutura do repositório

```
fortbc/
├── index.html          # o jogo completo (single-file, ~300KB com base64 fallback)
├── CLAUDE.md           # este arquivo
├── README.md
├── ASSETS.md
├── GAME_DESIGN.md
├── GAME_DATA.md
├── GAME_DATA.csv       # fonte de verdade dos stats (edição manual, refletir em BASE_CARDS)
├── SETUP.md
└── assets/
    ├── heroes/         # arthur.png fanta.png garopaba.png bala.png
    │                   # nathan.png leo.png zaga.png vitao.png borba.png letti.png
    └── audio/          # MP3 (não OGG — melhor compat. cross-browser, inclusive iOS Safari)
```

## 🎮 Mecânicas-chave

- **Tabuleiro:** 2 lanes verticais (Esq/Dir). Cada lado: 2 torres (400 HP, uma por lane) + 1 base central (1000 HP). Base BC = jogador (baixo), Base Floripa = IA (topo).
- **Torre dano:** `TOWER_ATK = 30` (cortado pela metade em 2025-06-12; era 60).
- **Projéteis de ataque:** animação de bolinha viajando do atacante ao alvo — vermelho (ATAQUE), azul (DEFESA), verde (EQUILÍBRIO), amarelo (estruturas). Torres e bases também têm projétil ao revidar.
- **Triângulo de tipos** (nomes novos em código pendente):
  - `ATK` → **ATAQUE** ⚔ (vermelho)
  - `DEF` → **DEFESA** 🛡 (azul)
  - `BAL` → **EQUILÍBRIO** ⚖ (verde)
  - Vantagem 1.5x / desvantagem 0.67x. ATAQUE > DEFESA > EQUILÍBRIO > ATAQUE.
- **Range:** melee (~46px) / mid (~120px) / long (~220px).
- **Tributo:** estrelas 1-4 sem tributo; estrelas 5-6 sacrificam 1 unidade.
- **ATB:** regenera 0.6/s (máx 10). 5 cartas na mão, compra automática.
- **Anti-empate:** 3min Turbo (2x), 4min Turbo+ (4x), 5min Morte Súbita (1 hit mata). Deck out = derrota.
- **Roguelike:** 3 fights, recompensa entre eles (level up / nova carta / buff de deck).
- **Níveis:** Bronze→Prata→Ouro→Platina→Esmeralda→Diamante (×1.0 a ×1.75), em localStorage.
- **Dificuldades:** Iniciante / Veterano / Mestre.

## 🎨 Sistema de VIBES (a implementar)

Vibes coexistem com o triângulo ATAQUE/DEFESA/EQUILÍBRIO — funcionam como tipos do Pokémon: cada carta tem tipo (triângulo) **e** vibe. Os nomes das vibes serão trocados pelo usuário para algo engraçado/adulto; as mecânicas e cores abaixo estão aprovadas.

| # | Cor | Tema | Mecânica passiva |
|---|---|---|---|
| 1 | 🟡 Amarelo | Festa/Energia | Regenera ATB extra em campo |
| 2 | 🔴 Vermelho | Força bruta | Bonus dano, vai ao herói mais próximo |
| 3 | 🔵 Azul | Controle/Cura | Cura aliados adjacentes |
| 4 | 🟣 Roxo | Caos/Debuff | Debuff aleatório ao morrer |
| 5 | 🟢 Verde | Sustain | Ganha stats progressivamente |

**Sinergia:** 2 cartas da mesma Vibe em campo → +10% stat relevante. 3+ → +20%.
**Items de Vibe:** efeito bônus se o player tiver ≥1 carta da Vibe em campo.
**Arapucas de Vibe:** bônus se ativadas por carta inimiga da mesma Vibe.

## 🧙 Heróis e habilidades

| Herói | Tipo | Range | Vibe | Habilidade |
|---|---|---|---|---|
| Arthur | ATAQUE | long | (a definir) | único herói long range |
| Fanta | EQUILÍBRIO | mid | (a definir) | Recycler: +1 ATB ao ser tributado |
| Garopaba | ATAQUE | melee | (a definir) | Morte heroica: +20% ATK aliados 10s ao morrer |
| Bala | DEFESA | melee | (a definir) | Provoker: atrai ataques |
| Nathan | DEFESA | melee | (a definir) | — |
| Léo | ATAQUE | melee | (a definir) | — |
| Zaga | EQUILÍBRIO | mid | (a definir) | — |
| Vitão | EQUILÍBRIO | mid | (a definir) | Healer: cura aliado ferido ao entrar |
| Borba | DEFESA | melee | (a definir) | — |
| Letti | ATAQUE | melee | (a definir) | Rusher: ignora unidades, vai direto à torre |

## 🃏 Novos cards planejados (a implementar)

### Itens — Debuffs
| Nome | Vibe | Custo | Efeito |
|---|---|---|---|
| Ressaca | 🟡 | 2 | Inimigo perde 40% velocidade por 8s |
| Dedinho Mindinho | 🟣 | 2 | Inimigo mais forte perde 30% ATK por 10s |
| Calúnia | 🟣 | 3 | Inimigo ataca aliados por 5s (confusão) |
| Joga Areia | 🔴 | 1 | Inimigo mais próximo perde 50% de range por 6s |
| Barraco | 🟣 | 4 | Todos inimigos em campo ficam lentos (−30%) por 4s |

### Peões de Vibe (1 por vibe, ★2, custo 2)
| Nome | Vibe | Tipo | Passiva |
|---|---|---|---|
| (nome a definir) 🎉 | 🟡 | ATAQUE | +0.2 ATB/s extra enquanto em campo |
| (nome a definir) ⚔️ | 🔴 | ATAQUE | +20% ATK, vai ao herói inimigo mais próximo |
| (nome a definir) 🌊 | 🔵 | DEFESA | Cura 15 HP/s aos aliados adjacentes. Mid range. |
| (nome a definir) 💀 | 🟣 | EQUILÍBRIO | Ao morrer: debuff aleatório no inimigo que o matou |
| (nome a definir) 🌿 | 🟢 | DEFESA | +5% ATK/HP a cada 10s em campo (empilha até 3x) |

### Arapucas (Armadilhas — novo tipo de carta)
| Nome | Vibe | Custo | Efeito ao ativar |
|---|---|---|---|
| Buraco na Pista | 🟡 | 2 | Para inimigo por 3s (bônus HYPE: 5s) |
| Emboscada | 🔴 | 3 | 2x dano no 1º inimigo (bônus: atinge todos da lane) |
| Rede | 🔵 | 2 | −60% velocidade 8s + cura aliado mais próximo |
| Praga | 🟢 | 3 | Drena 20 HP/s por 6s, transfere para aliado |
| Bomba de Fumaça | 🟣 | 3 | Todos inimigos da lane ficam melee por 5s |

## 🔊 Mapa de SFX (`assets/audio/sfx/`)

### UI
`ui_card_draw` · `ui_card_select` · `ui_cancel` · `ui_atb_full` · `ui_error` · `ui_click`

### Combate
`hit_melee` · `hit_mid` · `hit_long` · `unit_die` · `struct_hit` · `struct_destroy` · `base_hit` · `tower_retaliate`

### Invocação de heróis
`hero_arthur` · `hero_fanta` · `hero_garopaba` · `hero_bala` · `hero_nathan` · `hero_leo` · `hero_zaga` · `hero_vitao` · `hero_borba` · `hero_letti`

### Especiais
`special_recycler` · `special_deathbuff` · `special_provoker` · `special_healer` · `special_rusher`

### Arapucas & Itens
`trap_place` · `trap_trigger` · `item_heal` · `item_debuff` · `item_buff`

### Estado do jogo
`fight_win` · `fight_lose` · `reward` · `mode_turbo` · `mode_sudden`

## 🎵 Mapa de OST (`assets/audio/`)

| Arquivo | Quando toca | Estilo |
|---|---|---|
| `ost_menu.mp3` | Menu principal (loop) | ~100 BPM Pop/Funk |
| `ost_select.mp3` | Seleção de dificuldade/nome | ~75 BPM Ambient |
| `ost_preduel.mp3` | Tela pré-fight (~5s, stinger) | ~85 BPM tensão |
| `ost_battle1.mp3` | Fight 1 (loop) | ~130 BPM Rock/Electronic |
| `ost_battle2.mp3` | Fight 2 (loop) | ~145 BPM mais intenso |
| `ost_battle3.mp3` | Fight 3 final (loop) | ~155 BPM épico |
| `ost_sudden.mp3` | Morte Súbita (últimos 60s) | ~170 BPM Industrial |
| `ost_reward.mp3` | Tela de recompensa | ~90 BPM Lo-fi/Jazz |
| `ost_win.mp3` | Vitória final da run | ~120 BPM Triunfal |
| `ost_lose.mp3` | Derrota / Game Over | ~65 BPM Piano |
| `ost_scores.mp3` | Ranking/Highscores | ~80 BPM Ambient |

> Modo Turbo: variação pitch+speed +15% da trilha atual (dinâmico, sem arquivo novo).

## 🏗️ Arquitetura do código (index.html)

- **`BASE_CARDS`** — array com todos os stats das cartas. Fonte da verdade; espelhar no `GAME_DATA.csv`.
- **`TOWER_ATK`** — dano de retaliação das torres/bases. Valor atual: `30`.
- **`HERO_IMAGES_B64`** — fallback base64 dos 10 heróis embutido.
- **`preloadImages()`** — tenta GitHub raw, cai pro base64 se falhar (timeout 2.5s por imagem).
- **`G`** — estado do fight atual (unidades, estruturas, ATB, etc).
- **`APP`** — estado da run (nome, dificuldade, fight atual, deck, score total).
- **`gameLoop()`** — loop principal (movimento, range, combate, cerco, retaliação).
- **`drawCombatLine(a,b)`** — dispara projétil animado do atacante ao alvo (Web Animations API).
- **Telas:** loading → start → game → reward → end (`showScreen()`).

## ✅ Próximas tarefas (backlog priorizado)

- [ ] Renomear ATK/DEF/BAL → ATAQUE/DEFESA/EQUILÍBRIO em toda a UI e lógica
- [ ] Definir nomes finais das 5 Vibes (usuário vai escolher nomes engraçados/adultos)
- [ ] Adicionar campo `vibe` em `BASE_CARDS` para todos os heróis existentes
- [ ] Implementar sinergia passiva de Vibes (2+ cartas em campo)
- [ ] Adicionar novos itens de debuff ao `BASE_CARDS` e CSV
- [ ] Criar 5 peões de Vibe
- [ ] Implementar Arapucas (novo tipo de carta com placement na lane)
- [ ] Integrar SFX e OST quando os arquivos chegarem
- [ ] Gerar `BASE_CARDS` automaticamente a partir do CSV (hoje é manual)
- [ ] Imagens de peões/itens (hoje são emoji)
- [ ] Persistência de score via n8n (webhook)

## ⚠️ Convenções importantes

- **Áudio:** usar `.mp3` (não `.ogg`) — melhor compatibilidade, inclusive iOS Safari.
- Nomes de arquivos de herói: **minúsculos, sem acento** (`vitao.png`, `leo.png`).
- Não quebrar o fallback base64: o jogo deve rodar offline.
- Ao mudar stats: editar **tanto** `BASE_CARDS` (index.html) **quanto** `GAME_DATA.csv`.
- Todo push atualiza automaticamente o GitHub Pages.

## 🔄 Fluxo de trabalho multi-máquina

O usuário trabalha em mais de um computador. Fluxo ao trocar de máquina:
1. Na máquina atual: fazer commit + push de tudo antes de sair.
2. Na nova máquina: `git pull` (ou `git clone` se for a primeira vez).
3. Abrir o Claude Code apontando para a pasta — este CLAUDE.md carrega o contexto automaticamente.

**Sempre atualizar este arquivo ao final de cada sessão** com decisões, mudanças de mecânica e backlog atualizado.
