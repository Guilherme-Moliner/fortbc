# 🎲 GAME DESIGN — Batalha dos Amigos (v5 · Turn-Based)

> Documento de referência das mecânicas **atuais**. O jogo é por turnos, estilo **Yu-Gi-Oh! Forbidden Memories**.
> Para os números exatos das cartas, veja `GAME_DATA.md` / `.csv`. Para o design legado (Fort Condor/real-time), veja `gamedesignfort.md`. Para decisões de polish em aberto, veja `POLISH.md`.

---

## 🗺️ Tabuleiro

```
                 [ BASE FLORIPA · 2000 LP ]      (topo, IA)
   🪦 🌍   [ 1 ][ 2 ][ 3 ][ 4 ][ CMD ]           ← campo da IA (5 slots)
            ▽   ▽   ▽   ▽                         ← slots face-down da IA
   ──────────────────  VS  ──────────────────
            △   △   △   △                         ← slots face-down do jogador
   🪦 🌍   [ 1 ][ 2 ][ 3 ][ 4 ][ CMD ]           ← campo do jogador (5 slots)
                 [ BASE BC · 2000 LP ]           (baixo, jogador)
```

Cada lado tem:
- **5 slots de monstro**: 4 normais (1–4) + 1 **Comandante** (CMD).
- **4 slots face-down** (cartas viradas — reservados p/ Arapucas/armadilhas, mecânica a definir).
- **Zona de Campo** 🌍 (efeito global — mecânica a definir).
- **Cemitério** 🪦 (cartas mortas/descartadas).
- **Base** com **2000 LP**. Não há torres separadas — o dano que transborda do campo vai direto à base.

---

## 🔄 Fases do Turno

O turno passa por 5 fases, em ordem, para **ambos os lados simultaneamente**:

| # | Fase | O que acontece |
|---|---|---|
| 1 | **DRAW** | Ambos compram até o limite da mão (5 cartas). Deck vazio + mão vazia = **derrota** (Deck Out). |
| 2 | **STANDBY** | Cartas em campo sobem de **rank** conforme turnos sobrevividos. |
| 3 | **DOWN FASE** | Cada lado baixa **1 carta** num slot. O jogador escolhe; a **IA decide em segredo**. Revelação **simultânea**. |
| 4 | **LAST MINUTE** | Janela de **cartas rápidas** (quick-play). No V1, auto-passa se não houver carta rápida. |
| 5 | **RESOLUÇÃO** | O ATK total de cada campo ataca os slots do adversário. Sobra vai para a base. |

---

## ⚔️ Resolução (o coração do combate)

1. Soma-se o **ATK efetivo** de todas as cartas no campo de cada lado: `sumAtk(field)`.
2. Esse total ataca os slots inimigos **em ordem**: slot 1 → 2 → 3 → 4 → Comandante.
3. Cada slot **absorve** dano até seu HP acabar; o excesso passa para o próximo slot.
4. Cartas que zeram o HP vão para o **cemitério** (e dão pontos ao atacante).
5. Se sobrar dano depois de limpar o campo → **overflow** desconta da **base** inimiga.
6. **Player e IA resolvem ao mesmo tempo** (ambos podem se machucar no mesmo turno).

### ATK efetivo (rank)
```
ATK efetivo = ATK base × multiplicador de rank
```

### Empate de bases
Se as duas bases chegam a 0 no mesmo turno, compara-se o ATK em campo. Maior ATK vence. Se igual, ambas ficam em **1 LP** e o jogo continua.

---

## 📈 Rank de Carta (tempo em campo)

Quanto mais tempo uma carta sobrevive em campo, mais forte fica:

| Turnos em campo | Rank | Multiplicador de ATK |
|---|---|---|
| 0–1 | 🥉 Bronze | ×1.00 |
| 2–3 | 🥈 Prata | ×1.10 |
| 4+ | 🥇 Ouro | ×1.25 |

> Não confundir com os **Níveis de Carta** (Bronze→Diamante do roguelike), que são permanentes e vêm das recompensas. O rank é temporário e vale só dentro do fight.

---

## 🃏 Triângulo de Tipos

```
ATAQUE ⚔  ·  DEFESA 🛡  ·  EQUILÍBRIO ⚖
(ATK)        (DEF)         (BAL)
```

Cada carta tem um tipo, visível no tabuleiro. A regra de vantagem (ATAQUE > DEFESA > EQUILÍBRIO > ATAQUE) **está presente nos dados mas ainda não afeta a resolução** no V1 — é um dos pontos de polish em aberto (`POLISH.md` #3). Renomear `ATK/DEF/BAL` → `ATAQUE/DEFESA/EQUILÍBRIO` também está pendente.

---

## 🎨 Vibes (a implementar)

Sistema paralelo ao triângulo (funcionam como **tipos do Pokémon**: cada carta tem tipo **e** vibe). 5 vibes, com cores e mecânicas passivas já aprovadas; nomes finais a definir pelo usuário (tom engraçado/adulto).

| Cor | Tema | Mecânica passiva |
|---|---|---|
| 🟡 Amarelo | Festa/Energia | (readaptar p/ turn-based) |
| 🔴 Vermelho | Força bruta | Bônus de dano |
| 🔵 Azul | Controle/Cura | Cura aliados |
| 🟣 Roxo | Caos/Debuff | Debuff ao morrer |
| 🟢 Verde | Sustain | Ganha stats progressivamente |

**Sinergia:** 2 cartas da mesma vibe em campo → +10% no stat relevante; 3+ → +20%.

Detalhes e estado em `POLISH.md` #2.

---

## 👑 Comandante (a definir)

O slot CMD só aceita cartas marcadas como `commander`. Hoje nenhuma carta é comandante e o slot não tem bônus especial. A regra (o que torna uma carta Comandante, e que vantagem o slot dá) é um ponto de design em aberto — `POLISH.md` #6.

---

## ⭐ Estrelas e Tributo (a portar)

Cartas têm `star` (1–6) e `tribute` (0–1). No design legado, estrelas altas exigiam sacrificar uma unidade em campo. Essa lógica **ainda não foi portada** para a Down Fase do turn-based — `POLISH.md` #8.

---

## 🔄 Estrutura Roguelike

```
Início (nome + dificuldade)
  → Fight 1 → Recompensa (1 de 3)
  → Fight 2 → Recompensa (1 de 3)
  → Fight 3 → Tela final + Highscores
```

### Recompensas possíveis
1. **Level up** de uma carta (Bronze → ... → Diamante)
2. **Nova carta** adicionada ao deck da run
3. **Buff de deck** permanente (ex: +5% HP geral, +1 carta inicial na mão)

### Dificuldades
| Dificuldade | Nível das cartas da IA | Mult. de ATK |
|---|---|---|
| Iniciante | Bronze | ×0.8 |
| Veterano | Prata | ×1.0 |
| Mestre | Platina | ×1.25 |

---

## 🏆 Pontuação

| Evento | Pontos |
|---|---|
| Carta inimiga destruída na resolução | + ATK da carta |
| Vitória no fight | +500 + (10 × turno) |

> A pontuação foi simplificada na v5 (os bônus de velocidade ligados ao timer saíram com o engine real-time). Score total acumula os 3 fights e entra no ranking local (top 10). Refinamento de pontuação é polish em aberto.

---

## ⭐ Níveis de Carta (persistentes)

| Nível | Tier | Multiplicador | Borda |
|---|---|---|---|
| 1 | Bronze | ×1.00 | fosca |
| 2 | Prata | ×1.10 | metálica |
| 3 | Ouro | ×1.20 | brilhante |
| 4 | Platina | ×1.35 | glow |
| 5 | Esmeralda | ×1.50 | pulsante |
| 6 | Diamante | ×1.75 | arco-íris |

Persistem entre sessões (localStorage) e sobem via recompensas roguelike entre os 3 fights.

---

## 🧩 Constantes do engine (`index.html`)

| Constante | Valor | Significado |
|---|---|---|
| `HAND_LIMIT` | 5 | Tamanho máximo da mão |
| `BASE_HP` | 2000 | LP de cada base |
| `PHASES` | `['draw','standby','main','lastminute','resolution']` | Ordem das fases |

> Funções-chave: `initFight`, `startPhase`, `phaseDraw/Standby/Main/LastMinute/Resolution`, `applyDamageToField`, `sumAtk`, `getEffAtk`, `endFight`. Ver seção "Arquitetura" no `CLAUDE.md`.
