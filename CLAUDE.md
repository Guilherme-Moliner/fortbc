# CLAUDE.md — Contexto do Projeto fortbc

> Este arquivo é lido automaticamente pelo Claude Code ao iniciar. Mantém o contexto do projeto entre sessões. Atualize-o quando decisões importantes mudarem.
> **Sempre atualize este arquivo ao final de cada sessão de trabalho.**

## 🎯 O que é

**Batalha dos Amigos** (repo: `fortbc`) é um jogo de cartas de batalha **por turnos** (estilo Yu-Gi-Oh! Forbidden Memories), single-file HTML. As cartas-herói são feitas a partir de fotos de 10 amigos reais, com habilidades humorísticas personalizadas. Tom: engraçado, adulto, referências a álcool e cultura de amigos.

> **v5 (2026-06-12):** Jogo completamente reescrito de real-time lanes → turn-based. Engine antigo (lanes/ATB) removido. Ver seção "Arquitetura" abaixo.

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
├── POLISH.md           # backlog de polish v5.1 + briefing p/ discussão no chat
├── README.md
├── ASSETS.md
├── GAME_DESIGN.md      # ⚠️ LEGADO (descreve engine v4 real-time)
├── GAME_DATA.md
├── GAME_DATA.csv       # fonte de verdade dos stats (edição manual, refletir em BASE_CARDS)
├── SETUP.md
└── assets/
    ├── heroes/         # arthur.png fanta.png garopaba.png bala.png
    │                   # nathan.png leo.png zaga.png vitao.png borba.png letti.png
    └── audio/          # MP3 (não OGG — melhor compat. cross-browser, inclusive iOS Safari)
```

## 🎮 Mecânicas-chave (v5 — Turn-Based)

### Tabuleiro
- **Jogador (BC):** 5 slots de monstro (4 normais + 1 Comandante) + 4 slots face-down + zona de campo + cemitério
- **IA (Floripa):** espelho do jogador
- **Base:** 2000 LP cada lado. Não há torres separadas — dano direto à base.

### Fases por turno (estilo YGO Forbidden Memories)
1. **DRAW** — ambos compram até o limite da mão (5 cartas). Deck out = derrota.
2. **STANDBY** — cartas em campo sobem de rank por turns survived.
3. **DOWN FASE** — cada lado baixa 1 carta simultaneamente (player escolhe, IA decide em segredo).
4. **LAST MINUTE** — fase de cartas rápidas (V1: auto-passa se não há quick-play).
5. **RESOLUÇÃO** — ATK total do campo ataca os slots do adversário em ordem (slot 1→2→3→4→CMD). Overflow vai para a base do adversário.

### Combate
- `sumAtk(field)` = soma de `getEffAtk(card)` para cada slot ocupado.
- `getEffAtk` = `atk × rankMult` onde rankMult = Bronze×1.0 / Prata×1.10 / Ouro×1.25.
- `applyDamageToField(totalAtk, field, grave)` — desconta HP slot a slot, envia mortos ao cemitério, retorna overflow.
- Se overflow > 0 → aplica na base inimiga.
- Simultâneo: player e IA resolvem ao mesmo tempo.
- Empate de bases (ambas chegam a 0): compare ATK em campo. Se igual, ambas ficam em 1 LP.

### Rank de cartas (turnsOnField)
- 0 turnos → 🥉 Bronze (×1.0)
- 2 turnos → 🥈 Prata (×1.10)
- 4 turnos → 🥇 Ouro (×1.25)

### Triângulo de tipos (mantido no código, sem efeito ativo no V1)
- `ATK` ⚔ / `DEF` 🛡 / `BAL` ⚖ — visível nas cartas, mecânica de vantagem a implementar.

### Constantes chave
- `HAND_LIMIT = 5` (mão máxima)
- `BASE_HP = 2000` (LP de cada base)
- `PHASES = ['draw','standby','main','lastminute','resolution']`

### Roguelike (mantido)
- 3 fights, recompensa entre eles (level up / nova carta / buff de deck).
- Níveis: Bronze→Prata→Ouro→Platina→Esmeralda→Diamante (×1.0 a ×1.75), em localStorage.
- Dificuldades: Iniciante / Veterano / Mestre.

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

### Constantes e dados
- **`BASE_CARDS`** — array com todos os stats das cartas. Fonte da verdade; espelhar no `GAME_DATA.csv`.
- **`HERO_IMAGES_B64`** — fallback base64 dos 10 heróis embutido. **NÃO MODIFICAR.**
- **`preloadImages()`** — tenta GitHub raw, cai pro base64 se falhar (timeout 2.5s por imagem).
- **`HAND_LIMIT=5`, `BASE_HP=2000`, `PHASES=[...]`** — constantes do engine turn-based.
- **`AI_DECKS`** — configs de dificuldade (lvOverride, atkMult).

### Estado do jogo
- **`G`** — estado do fight atual:
  - `playerField[5]`, `aiField[5]` — slots 0-3 + slot 4 (Comandante)
  - `playerHidden[4]`, `aiHidden[4]` — slots face-down
  - `playerBase{hp,maxHp}`, `aiBase{hp,maxHp}` — LP das bases
  - `playerHand[]`, `aiHand[]`, `playerDeck[]`, `aiDeck[]`, `playerGrave[]`, `aiGrave[]`
  - `turn`, `phase`, `score`, `gameOver`
- **`APP`** — estado da run (nome, dificuldade, fightNum, totalScore, deck, extraHandSize).

### Engine turn-based (linhas ~930+, substituem o engine real-time antigo)
- **`initFight()`** → configura G, distribui mãos iniciais, chama `startPhase('draw')`
- **`startPhase(phase)`** → dispatcher de fases
- **`phaseDraw()`** → compra cartas
- **`phaseStandby()`** → rank-up de cartas em campo
- **`phaseMain()`** → player escolhe carta + slot; IA decide em segredo via `aiDecideMain()`
- **`confirmMain()`** → revela ambas as escolhas, chama `phaseLastMinute`
- **`phaseResolution()`** → `applyDamageToField()` para ambos os lados, verifica vitória
- **`endFight(winner)`** → atualiza APP, vai para recompensa ou fim

### UI
- **`updateFieldUI()`** → re-renderiza todos os slots (`renderFC()` por carta)
- **`updateBaseUI()`** → atualiza barras de LP e topbar
- **`renderHand()`** → re-renderiza a mão do player (clicável via `selectHandCard(idx)`)
- **`updatePhaseBanner/Badge()`** → atualiza indicador de fase
- **Telas:** loading → start → game → reward → end (`showScreen()`).

### Nota: código antigo ainda presente no arquivo
O engine real-time (lanes, ATB, gameLoop, etc.) ainda existe nas linhas 514-825 mas é **inerte**: as novas funções com mesmo nome declaradas depois sobrescrevem-no. Não chamar nem modificar essas funções antigas.

## ✅ Próximas tarefas (backlog priorizado)

> **Fase de POLISH (v5.1):** o gameplay V1 turn-based foi testado e funciona mecanicamente. O backlog de polish está detalhado em **`POLISH.md`**, separando o que precisa de decisão criativa do usuário (🗣️ CHAT) do que é implementação direta (🔧). Consultar antes de iniciar polish.

### Concluído
- [x] Testar o fluxo completo do jogo turn-based — OK (2026-06-12)

### Urgente — Gameplay V1 (turn-based recém-implementado)
- [ ] Limpar o código antigo (engine real-time linhas 514-825) — opcional, não bloqueia nada
- [ ] Implementar triângulo de tipos na resolução (ATK bate DEF bate BAL bate ATK, multiplicador 1.5x/0.67x)
- [ ] Implementar mecânica de "campo deve ser zerado antes de atacar a base" (opcional para V1)
- [ ] Mecânica de comeback ligada à torre/defesa (a definir)

### Conteúdo
- [ ] Renomear ATK/DEF/BAL → ATAQUE/DEFESA/EQUILÍBRIO em toda a UI e lógica
- [ ] Definir nomes finais das 5 Vibes (usuário vai escolher nomes engraçados/adultos)
- [ ] Adicionar campo `vibe` em `BASE_CARDS` para todos os heróis existentes
- [ ] Implementar sinergia passiva de Vibes (2+ cartas em campo)
- [ ] Adicionar novos itens de debuff ao `BASE_CARDS` e CSV
- [ ] Criar 5 peões de Vibe
- [ ] Implementar Arapucas (face-down, ativadas por inimigos)
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
