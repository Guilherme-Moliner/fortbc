# CONTEXT: Menus & Telas — Batalha dos Amigos

> **Para o Claude Code:** este é o briefing completo para trabalhar nos menus e telas do jogo. Leia este arquivo + `CLAUDE.md` antes de qualquer mudança.

## O que é o projeto
Batalha dos Amigos (`fortbc`) — jogo de cartas turn-based single-file (`index.html`), estilo Yu-Gi-Oh! Forbidden Memories. Cartas-herói são amigos reais. Tom: engraçado, adulto, referências a álcool/boteco. Ver `CLAUDE.md` para arquitetura completa.

## Telas existentes hoje (via `showScreen()`)
| ID | Nome | Estado |
|---|---|---|
| `loading` | Tela de loading / preload de imagens | Funcional |
| `start` | Menu inicial (nome + dificuldade) | Funcional, visual genérico |
| `game` | Tabuleiro de jogo | Funcional |
| `reward` | Tela de recompensa entre fights | Funcional |
| `end` | Tela final / Highscores | Funcional |

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
- [ ] Redesenhar tela `start` (visual + tom)
- [ ] Mensagens de UI com tom certo (vitória, derrota, fases)
- [ ] Tela de highscores melhorada
- [ ] Animações de transição entre telas
- [ ] Tela "como jogar" / regras inline (opcional)
- [ ] Configurações de volume acessíveis

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
