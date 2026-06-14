# CONTEXT: Menus & Telas — Batalha dos Amigos

> **Para o Claude Code:** este é o briefing completo para trabalhar nos menus e telas do jogo. Leia este arquivo + `CLAUDE.md` antes de qualquer mudança.

## O que é o projeto
Batalha dos Amigos (`fortbc`) — jogo de cartas turn-based single-file (`index.html`), estilo Yu-Gi-Oh! Forbidden Memories. Cartas-herói são amigos reais. Tom: engraçado, adulto, referências a álcool/boteco. Ver `CLAUDE.md` para arquitetura completa.

## Telas existentes hoje (via `showScreen()`)
> **Atualizado 2026-06-13** — a tela `start` foi substituída pelo sistema de Menu completo (capítulo Menu).

| ID | Nome | Estado |
|---|---|---|
| `loading` | Loading / preload de imagens | Funcional |
| `title` | Title Screen (logo + "Pressione Start" piscando) | ✅ novo |
| `nameload` | Entrada de nome / Continuar save | ✅ novo (input simples) |
| `menu` | Menu Principal (5 opções, cursor `VMenu`) | ✅ novo |
| `campaign` | Campanha — stage-select **esqueleto** (sem narrativa) | ✅ estrutura |
| `runsetup` | Roguelite — seleção de dificuldade | ✅ novo |
| `freeduel` | Duelo Livre — oponente + dificuldade | ✅ novo |
| `library` | Biblioteca — grid de `BASE_CARDS` + card viewer | ✅ novo |
| `password` | Password — código → deck pré-montado | ✅ novo |
| `deckselect` | Escolha de vibe inicial (pós conta) → coleção | ✅ novo |
| `shop` | Loja — boosters/gacha com pity | ✅ novo |
| `score` | Ranking das runs roguelite | ✅ novo |
| `game` | Tabuleiro de jogo | Funcional |
| `reward` | Recompensa entre fights | Funcional |
| `end` | Tela final / Highscores | Funcional |

### Persistência (camadas)
- **Camada 1 (feita):** `Save` em `localStorage` (`fortbc_save`) — perfil `{name, created, lastPlayed, campaign, runs}`.
- **Camada 2 (stub):** `Save.cloudSync()` pronto p/ POST a Google Sheets via Apps Script.
- **Camada 3 (futuro):** Google OAuth.

## Problemas visuais atuais
- Visual genérico, sem identidade (cores escuras padrão, sem personalidade "boteco")
- Tom dos textos de UI é neutro — não reflete o estilo adulto/zoeiro do jogo
- Nome dos lados hoje: "BC" (player) vs "FLORIPA" (IA)
- Tela de start: sem personalidade, só campos funcionais
- Não há tela de configurações (volume, etc.)
- Não há tela de "como jogar" / tutorial inline

## Identidade visual desejada (a definir com usuário)
- Paleta: ainda não definida — discutir no chat (POLISH.md #1)
- Tom: engraçado, adulto, com gírias/referências internas
- Referências visuais: boteco? neon? zoeira? — a definir

## Backlog desta frente
- [x] Estrutura de telas do Menu (title/nameload/menu/campaign/runsetup/freeduel/library/password) — 2026-06-13
- [x] Abstração de Save (camada 1 localStorage + stub cloud) — 2026-06-13
- [x] Biblioteca navegável + card viewer — 2026-06-13
- [x] Fade entre telas (~0.3s) — 2026-06-13
- [x] Texto maior nas telas de menu — 2026-06-13
- [x] Fundo animado de cartas dos heróis — 2026-06-13
- [x] Deck inicial por vibe (vira coleção/histórico do player) — 2026-06-13
- [x] Botão Score (ranking roguelite) — 2026-06-13
- [x] Biblioteca com discovery (verso nas não descobertas) — 2026-06-13
- [x] Duelo Livre com lista de oponentes (preset + slot trancado de campanha) — 2026-06-13
- [x] HUD inferior (nome, capítulo, dinheiro, licença, ⚙ settings/volume, login) — 2026-06-13
- [x] Loja com gacha + pity (Duel Links-style) — 2026-06-13
- [x] Licença de duelista (evolui por duelos; libera fusões — mecânica futura) — 2026-06-13
- [ ] Trocar nomes provisórios das VIBES por algo engraçado/adulto (usuário)
- [ ] KB de adversários (preencher OPPONENTS + desbloqueio via campanha) — usuário
- [ ] Implementar a mecânica de fusão (dupla→quíntupla) gateada pela licença
- [ ] Ganho de cartas no jogo (reward/roguelite) alimentar a coleção (discovery)
- [ ] Ligar o deck jogável à coleção (hoje o deck de fight usa todo o BASE_CARDS)
- [ ] Redesenhar visual quando a identidade (POLISH.md #1) for definida — hoje placeholder dourado/escuro
- [ ] Mensagens de UI com tom boteco/adulto (vitória, derrota, fases)
- [ ] Conteúdo narrativo da Campanha (sprite+texto digitando) — só depois
- [ ] Wire da camada 2 (Apps Script/Sheets) em `Save.cloudSync()`

## Dependências
- Identidade visual (POLISH.md #1) precisa ser decidida no chat antes do redesign completo
- OST: `ost_menu.mp3` toca no menu principal (ainda não existe o arquivo)
- `showScreen(id)` é a função que troca telas — não criar novo sistema de roteamento

## Arquitetura relevante
- Telas são `<div id="screen-X">` com `display:none` por padrão
- `showScreen('id')` esconde todas e mostra a escolhida
- Estado da run fica em `APP` (nome, dificuldade, fightNum, totalScore)
- localStorage: scores e níveis de carta

## Como iniciar uma sessão nesta frente
1. `git pull origin main` na pasta do projeto
2. Ler este arquivo + `CLAUDE.md`
3. Abrir `index.html` no navegador para ver o estado atual
4. Confirmar com o usuário qual tela/item atacar primeiro
