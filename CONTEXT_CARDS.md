# CONTEXT: Cartas & Conteúdo — Batalha dos Amigos

> **Para o Claude Code:** este é o briefing completo para trabalhar em cartas, heróis, stats e novos conteúdos. Leia este arquivo + `CLAUDE.md` + `GAME_DATA.md` antes de qualquer mudança.

## O que é o projeto
Batalha dos Amigos (`fortbc`) — jogo de cartas turn-based. As cartas-herói são baseadas em 10 amigos reais. Tom: engraçado, adulto, referências a álcool. Ver `CLAUDE.md` para arquitetura.

## Fonte de verdade dos stats
- **`GAME_DATA.csv`** — editar aqui (Excel/Sheets)
- **`BASE_CARDS` em `index.html`** — deve refletir o CSV (hoje sincronizado manualmente)
- Próximo passo planejado: gerar `BASE_CARDS` automaticamente a partir do CSV

## Heróis existentes (10 cartas)
| ID | Nome | Tipo | Estrelas | Tribute | Habilidade |
|---|---|---|---|---|---|
| arthur | Arthur | ATK | ? | ? | long range (legado) |
| fanta | Fanta | BAL | ? | ? | Recycler (legado) |
| garopaba | Garopaba | ATK | ? | ? | Morte heroica (legado) |
| bala | Bala | DEF | ? | ? | Provoker (legado) |
| nathan | Nathan | DEF | ? | ? | — |
| leo | Léo | ATK | ? | ? | — |
| zaga | Zaga | BAL | ? | ? | — |
| vitao | Vitão | BAL | ? | ? | Healer (legado) |
| borba | Borba | DEF | ? | ? | — |
| letti | Letti | ATK | ? | ? | Rusher (legado) |

> Stats exatos: ver `GAME_DATA.md` / `GAME_DATA.csv`.
> Habilidades são do design legado (real-time) e precisam ser redesenhadas para turn-based.

## Novos conteúdos planejados (não implementados)

### Itens — Debuffs (5 cartas)
| Nome | Efeito original (real-time) | Adaptar p/ turn-based |
|---|---|---|
| Ressaca | −40% velocidade 8s | −X ATK no próximo turno |
| Dedinho Mindinho | −30% ATK inimigo mais forte | −30% ATK 1 turno |
| Calúnia | Inimigo ataca aliados 5s | Carta inimiga passa 1 turno sem atacar |
| Joga Areia | −50% range 6s | −X ATK próximo turno |
| Barraco | Todos inimigos −30% velocidade | Todos inimigos −X ATK 1 turno |

### Peões de Vibe (5 cartas novas, ★2, custo 2)
| Vibe | Tipo | Passiva |
|---|---|---|
| 🟡 Festa | ATK | bônus de stat no turno |
| 🔴 Força | ATK | +20% ATK, vai ao herói mais próximo |
| 🔵 Controle | DEF | Cura aliados adjacentes |
| 🟣 Caos | BAL | Debuff aleatório ao morrer |
| 🟢 Sustain | DEF | +5% ATK/HP por turno (empilha até 3x) |

### Arapucas / Armadilhas (5 cartas, ficam face-down)
| Nome | Efeito original (real-time) | Adaptar p/ turn-based |
|---|---|---|
| Buraco na Pista | Para inimigo 3s | Inimigo perde 1 turno |
| Emboscada | 2x dano no 1º inimigo | 2x dano na resolução do turno |
| Rede | −60% velocidade + cura | −ATK + cura aliado |
| Praga | Drena HP | Drena ATK por 2 turnos |
| Bomba de Fumaça | Inimigos ficam melee | Todos inimigos −range (sem efeito turn-based ainda) |

## Sistema de Vibes (aprovado, não implementado)
Cada carta terá campo `vibe`. 5 vibes com mecânicas passivas aprovadas, **nomes a definir**:
- 🟡 Amarelo — Festa/Energia
- 🔴 Vermelho — Força bruta
- 🔵 Azul — Controle/Cura
- 🟣 Roxo — Caos/Debuff
- 🟢 Verde — Sustain

Para implementar: adicionar campo `vibe` em `BASE_CARDS` + CSV.

## Níveis de carta persistentes (roguelike)
| Nível | Multiplicador | Borda |
|---|---|---|
| Bronze | ×1.00 | fosca |
| Prata | ×1.10 | metálica |
| Ouro | ×1.20 | brilhante |
| Platina | ×1.35 | glow |
| Esmeralda | ×1.50 | pulsante |
| Diamante | ×1.75 | arco-íris |

## Convenções importantes
- Ao mudar stats: editar **tanto** `BASE_CARDS` (index.html) **quanto** `GAME_DATA.csv`
- Nomes de arquivo de herói: **minúsculos, sem acento** (`vitao.png`, `leo.png`)
- Imagens ficam em `assets/heroes/` — carregadas via GitHub raw com fallback base64

## Como iniciar uma sessão nesta frente
1. `git pull origin main`
2. Ler este arquivo + `CLAUDE.md` + `GAME_DATA.md`
3. Para habilidades dos heróis: confirmar design turn-based com usuário antes de implementar
4. Para novos cards (itens/peões/arapucas): confirmar adaptação dos efeitos p/ turn-based
5. Ao editar stats: sempre sincronizar `BASE_CARDS` + `GAME_DATA.csv`
