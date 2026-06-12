# 🎲 GAME DESIGN — Batalha dos Amigos

Documento de referência das mecânicas. Para os números exatos, veja `GAME_DATA.md` / `.csv`.

---

## 🗺️ Tabuleiro

```
            [ BASE FLORIPA ]   (topo, IA)
         ┌──────────┬──────────┐
         │ 🏰 Torre │ 🏰 Torre │   ← torres da IA (bloqueiam)
         │   Esq    │   Dir    │
         │  LANE 0  │  LANE 1  │
         │   ESQ    │   DIR    │
         │ 🏰 Torre │ 🏰 Torre │   ← torres do jogador
         │   Esq    │   Dir    │
         └──────────┴──────────┘
            [ BASE BC ]        (baixo, jogador)
```

- **2 lanes verticais** (Esquerda / Direita), separadas por uma **zona nula** central (reservada para torres centrais futuras).
- Cada jogador tem **2 torres** (uma por lane) + **1 base central**.
- Unidades saem da base, sobem pela lane escolhida, e seguem em direção à base inimiga.

---

## ⚔️ Fluxo de Combate (estilo Fort Condor)

1. Você posiciona unidades **apenas no seu lado**; elas percorrem a lane sozinhas.
2. Unidades **não morrem** ao chegar na estrutura inimiga — ficam **atacando** (cerco).
3. Unidades inimigas **se cruzam** livremente; só entram em combate quando ficam dentro do **alcance (range)** uma da outra.
4. **Prioridade**: unidades sempre preferem lutar contra unidades inimigas a avançar.
5. A **torre bloqueia** a lane: é preciso destruí-la para a unidade seguir até a base.
6. **Torres e bases revidam** (long range): atiram na unidade inimiga mais próxima dentro do alcance.

---

## 🎯 Range (Alcance)

| Range | Alcance | Indicador | Comportamento |
|---|---|---|---|
| ⚔️ Melee | curto | ⚪ branco | luta corpo-a-corpo |
| 🏹 Mid | médio | 🟠 laranja | ataca à média distância |
| 🎯 Long | longo | 🟣 roxo | bombardeia de longe |

Atiradores (mid/long) são perigosos mas frágeis no corpo-a-corpo — proteja-os com tanques na frente.

---

## 🃏 Triângulo de Poder

```
ATK ▶ vence ▶ DEF ▶ vence ▶ BAL ▶ vence ▶ ATK
```
- Vantagem de tipo: **1.5×** dano
- Desvantagem: **0.67×** dano

---

## ⭐ Estrelas e Tributo

| Estrelas | Tributo necessário |
|---|---|
| 1–2 (peões) | nenhum |
| 3–4 (heróis) | nenhum |
| 5–6 (heróis) | sacrificar 1 unidade em campo |

O sacrifício é **imediato** — permite o "deny" (sacrificar uma unidade prestes a morrer para não dar pontos ao inimigo, e ainda invocar um herói forte).

---

## 🧙 Habilidades Especiais

| Herói | Habilidade |
|---|---|
| Arthur | Único herói **long range** |
| Fanta | **Recycler**: +1 ATB ao ser tributado |
| Garopaba | **Morte heroica**: ao morrer, +20% ATK aos aliados por 10s |
| Bala | **Provoker**: atrai os ataques inimigos |
| Vitão | **Healer**: ao entrar, cura o aliado mais ferido (+100 HP) |
| Letti | **Rusher**: ignora unidades e vai direto à torre |

---

## 🎒 Itens

| Item | Custo | Efeito |
|---|---|---|
| 🥩 Churrasco | 2 | cura todas as unidades +80 HP |
| ⚡ Energético | 2 | +30% ATK em campo por 15s |
| 🍺 Rodada | 1 | compra 2 cartas |
| 💨 Turbo Boost | 2 | 2× velocidade por 10s |
| 🔄 Ressurreição | 4 | revive a última unidade morta (50% HP) |
| 🧱 Reforço | 3 | próxima unidade entra com +50% HP |

---

## ⏱️ ATB e Anti-empate

- **ATB** regenera ~0.6/s (máx 10). Cada carta custa ATB para jogar.
- **3 min** → ⚡ Turbo (2× velocidade)
- **4 min** → 🔥 Turbo+ (4× velocidade)
- **5 min** → 💀 Morte Súbita (um hit mata)
- **Deck Out** (deck + mão vazios) = derrota.

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
3. **Buff de deck** permanente (ex: +5% HP geral, −1 custo de peões)

---

## 🏆 Pontuação

| Evento | Pontos |
|---|---|
| Unidade inimiga morta | +50 a +200 (por estrela) |
| Dano em torre/base | +1 por HP |
| Vitória no fight | +500 |
| Bônus velocidade (<1/2/3 min) | +500 / +300 / +100 |
| Cartas restantes na mão | +20 cada |
| Cartas restantes no deck | +10 cada |
| Unidade própria perdida | −30 a −100 |

Score total acumula os 3 fights e entra no ranking local (top 10).

---

## ⭐ Níveis de Carta

| Nível | Tier | Multiplicador | Borda |
|---|---|---|---|
| 1 | Bronze | ×1.00 | fosca |
| 2 | Prata | ×1.10 | metálica |
| 3 | Ouro | ×1.20 | brilhante |
| 4 | Platina | ×1.35 | glow |
| 5 | Esmeralda | ×1.50 | pulsante |
| 6 | Diamante | ×1.75 | arco-íris |

Os níveis persistem entre sessões (localStorage) e sobem via recompensas.
