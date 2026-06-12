# 📊 GAME DATA — Batalha dos Amigos (fortbc)

> Base de referência de todos os stats. Edite o `GAME_DATA.csv` para ajustar números, e estes valores devem ser refletidos no `index.html` (constante `BASE_CARDS`).

## 🎯 Sistema de Range

| Range | Alcance | Comportamento |
|---|---|---|
| ⚔️ **Melee** | ~46px | Para e luta corpo-a-corpo |
| 🏹 **Mid** | ~120px | Ataca à média distância, sem encostar |
| 🎯 **Long** | ~220px | Bombardeia de longe, fica recuado |

Unidades long range são perigosas mas vulneráveis: se um melee inimigo as alcança, elas não levam vantagem defensiva. Proteja seus atiradores.

---

## 🃏 Triângulo de Poder

```
ATK ▶ vence ▶ DEF ▶ vence ▶ BAL ▶ vence ▶ ATK
```
Vantagem de tipo = **1.5× dano**. Desvantagem = **0.67× dano**.

---

## 👑 Heróis

| Nome | Tipo | Range | ⭐ | Custo | HP | ATK | Veloc. | Tributo | Habilidade |
|---|---|---|---|---|---|---|---|---|---|
| Arthur | ATK | 🎯 Long | 3 | 3 | 220 | 110 | Rápido | 0x | Long range — único herói que atira de longe |
| Fanta | BAL | 🏹 Mid | 3 | 3 | 200 | 70 | Médio | 0x | Recycler: +1 ATB ao ser tributado |
| Nathan | DEF | ⚔️ Melee | 3 | 3 | 320 | 45 | Lento | 0x | — |
| Garopaba | ATK | ⚔️ Melee | 4 | 4 | 250 | 130 | Médio | 0x | Morte heroica: +20% ATK aliados por 10s |
| Bala | DEF | ⚔️ Melee | 4 | 4 | 420 | 50 | Lento | 0x | Provoker: atrai ataques inimigos |
| Léo | ATK | ⚔️ Melee | 4 | 4 | 260 | 130 | Médio | 0x | — |
| Zaga | BAL | 🏹 Mid | 4 | 4 | 320 | 95 | Médio | 0x | — |
| Vitão | BAL | 🏹 Mid | 5 | 5 | 350 | 80 | Médio | 1x | Healer: cura aliado ferido ao entrar (+100) |
| Borba | DEF | ⚔️ Melee | 5 | 5 | 600 | 70 | Lento | 1x | — |
| Letti | ATK | ⚔️ Melee | 6 | 6 | 280 | 160 | Muito rápido | 1x | Rusher: ignora unidades, vai direto à torre |

> Destaque: **Arthur** é o único herói long range — é o diferencial dele, mantendo os stats originais.

## ♟️ Peões

| Nome | Tipo | Range | ⭐ | Custo | HP | ATK | Veloc. | Tributo | Habilidade |
|---|---|---|---|---|---|---|---|---|---|
| Zé Mané | ATK | ⚔️ Melee | 1 | 1 | 100 | 60 | Rápido | 0x | — |
| Muralha | DEF | ⚔️ Melee | 1 | 1 | 200 | 30 | Lento | 0x | — |
| Genérico | BAL | 🏹 Mid | 2 | 2 | 150 | 50 | Médio | 0x | Atirador |
| Fortão | DEF | ⚔️ Melee | 2 | 2 | 280 | 40 | Lento | 0x | — |

## 🎒 Itens

| Carta | Custo | Cópias | Efeito |
|---|---|---|---|
| Churrasco | 2 | 3 | Cura todas as unidades +80 HP |
| Energético | 2 | 3 | +30% ATK em campo por 15s |
| Rodada | 1 | 3 | Compra 2 cartas |
| Turbo Boost | 2 | 3 | 2x velocidade por 10s |
| Ressurreição | 4 | 3 | Revive última unidade morta (50% HP) |
| Reforço | 3 | 3 | Próxima unidade +50% HP |

---

## 🏛️ Estruturas (Torres & Bases)

| Estrutura | HP | Range | ATK | Função |
|---|---|---|---|---|
| Torre | 400 | 🎯 Long | = dano de unidade básica (60) | Bloqueia a lane; precisa ser destruída para passar |
| Base | 1000 | 🎯 Long | = dano de unidade básica (60) | Objetivo final; destruí-la vence o fight |

- Cada lado tem **2 torres** (uma por lane) + **1 base**.
- As torres **bloqueiam** a lane: a unidade precisa destruir a torre para seguir até a base.
- Torres e bases **revidam** (long range, 60 de dano = unidade básica).

---

## 🏆 Pontuação

| Evento | Pontos |
|---|---|
| Unidade inimiga morta | +50 a +200 (por estrela) |
| Dano em torre/base inimiga | +1 por HP |
| Vitória no fight | +500 |
| Bônus de velocidade (<1/2/3 min) | +500 / +300 / +100 |
| Cartas restantes na mão | +20 cada |
| Cartas restantes no deck | +10 cada |
| Unidade própria perdida | −30 a −100 |

---

## ⭐ Níveis de Carta

| Nível | Tier | Multiplicador |
|---|---|---|
| 1 | Bronze | ×1.00 |
| 2 | Prata | ×1.10 |
| 3 | Ouro | ×1.20 |
| 4 | Platina | ×1.35 |
| 5 | Esmeralda | ×1.50 |
| 6 | Diamante | ×1.75 |

Sobem via recompensas roguelike entre os 3 fights.
