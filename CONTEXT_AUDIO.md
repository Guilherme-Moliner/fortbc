# CONTEXT: Áudio (OST + SFX) — Batalha dos Amigos

> **Para o Claude Code:** este é o briefing completo para trabalhar na integração de áudio. Leia este arquivo + `CLAUDE.md` antes de qualquer mudança.

## O que é o projeto
Batalha dos Amigos (`fortbc`) — jogo de cartas turn-based single-file (`index.html`). Áudio em `.mp3` (nunca `.ogg` — melhor compat., inclusive iOS Safari).

## Estado atual
- Pasta `assets/audio/` existe mas está **VAZIA** — sem arquivos de áudio ainda
- O código de integração de áudio **não foi implementado** — aguarda os arquivos chegarem
- Botão de mute (🔊) existe no topo do tabuleiro
- Quando os arquivos chegarem, o Claude Code integra

## Mapa de OST (trilha sonora)
Todos os arquivos ficam em `assets/audio/`:

| Arquivo | Quando toca | Estilo sugerido |
|---|---|---|
| `ost_menu.mp3` | Menu principal (loop) | ~100 BPM Pop/Funk |
| `ost_select.mp3` | Seleção de dificuldade/nome | ~75 BPM Ambient |
| `ost_preduel.mp3` | Tela pré-fight (~5s, stinger) | ~85 BPM tensão |
| `ost_battle1.mp3` | Fight 1 (loop) | ~130 BPM Rock/Electronic |
| `ost_battle2.mp3` | Fight 2 (loop) | ~145 BPM mais intenso |
| `ost_battle3.mp3` | Fight 3 final (loop) | ~155 BPM épico |
| `ost_sudden.mp3` | Morte Súbita (se implementado) | ~170 BPM Industrial |
| `ost_reward.mp3` | Tela de recompensa | ~90 BPM Lo-fi/Jazz |
| `ost_win.mp3` | Vitória final da run | ~120 BPM Triunfal |
| `ost_lose.mp3` | Derrota / Game Over | ~65 BPM Piano |
| `ost_scores.mp3` | Ranking/Highscores | ~80 BPM Ambient |

> Modo Turbo (se implementado): variação pitch+speed +15% da trilha atual — dinâmico, sem arquivo extra.

## Mapa de SFX (efeitos sonoros)
Ficam em `assets/audio/sfx/`:

### UI
`ui_card_draw` · `ui_card_select` · `ui_cancel` · `ui_atb_full` · `ui_error` · `ui_click`

### Combate
`hit_melee` · `hit_mid` · `hit_long` · `unit_die` · `struct_hit` · `struct_destroy` · `base_hit` · `tower_retaliate`

### Invocação de heróis (um por herói)
`hero_arthur` · `hero_fanta` · `hero_garopaba` · `hero_bala` · `hero_nathan` · `hero_leo` · `hero_zaga` · `hero_vitao` · `hero_borba` · `hero_letti`

### Especiais (habilidades)
`special_recycler` · `special_deathbuff` · `special_provoker` · `special_healer` · `special_rusher`

### Arapucas & Itens
`trap_place` · `trap_trigger` · `item_heal` · `item_debuff` · `item_buff`

### Estado do jogo
`fight_win` · `fight_lose` · `reward` · `mode_turbo` · `mode_sudden`

## O que implementar quando os arquivos chegarem
1. Sistema de gerenciamento de OST: `playOST(filename)`, `stopOST()`, com loop automático
2. Troca de trilha nas transições de tela (`showScreen` chama o OST certo)
3. Volume master + mute (já tem botão na UI, falta a lógica)
4. SFX: `playSFX(filename)` — fogo e esquece, sem interferir na OST
5. Modo Turbo OST: `setOSTSpeed(1.15)` via Web Audio API
6. Preload dos arquivos críticos junto com o preload de imagens (`preloadImages`)

## Convenções
- Formato: sempre `.mp3` — nunca `.ogg`
- Fallback gracioso: se arquivo não existir, o jogo não quebra (catch silencioso)
- Não embutir áudio em base64 — arquivos são grandes demais

## Como iniciar uma sessão nesta frente
1. `git pull origin main`
2. Verificar se os arquivos de áudio chegaram em `assets/audio/`
3. Ler este arquivo + `CLAUDE.md`
4. Implementar o sistema de áudio básico (OST loop + SFX) e integrar nas transições de tela
5. Testar no Chrome e Safari (iOS é o mais crítico para compat. de áudio)
