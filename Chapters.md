# Chapters — Batalha dos Amigos (`fortbc`)

> Índice das **frentes de trabalho** ("capítulos") do projeto. Cada capítulo vira (ou já é) uma conversa separada no Claude. Use o **título sugerido** pra renomear a conversa correspondente e manter a referência organizada.
>
> Convenção: cada capítulo tem um doc de contexto `CONTEXT_*.md` que o Claude lê no início da sessão (junto do `CLAUDE.md`). Ao abrir uma conversa, mande o Claude dar `git pull` e ler `CLAUDE.md` + o `CONTEXT_*` do capítulo.

| Status | Significado |
|---|---|
| ✅ | V1 implementado e testado |
| 🟡 | Em andamento / parcial |
| 🔜 | Planejado, ainda não começou |
| 🔁 | Revisão de algo já existente |

---

## 🔊 Capítulo: Áudio (OST + SFX) — ✅ V1
**Título sugerido da conversa:** `fortbc · Áudio (OST + SFX)`
**Doc:** [`CONTEXT_AUDIO.md`](CONTEXT_AUDIO.md)

Trilha sonora por tela (crossfade) + efeitos sonoros. Já implementado: gerenciador de OST com troca automática em `onScreenEnter`, SFX fire-and-forget com pool, unlock de áudio no iOS (1º clique da title), preload com fallback gracioso, volumes separados Música × Efeitos (2 sliders em ⚙). OST em `.mp3`, SFX em `.wav`.

**Falta:** ligar SFX dos eventos que ainda não existem (invocação por herói, especiais, arapucas, vibes); `ost_preduel`/`ost_sudden` aguardam telas/modos; Modo Turbo (pitch +15% via Web Audio).

---

## 🃏 Capítulo: Expansão de Base / Cartas — 🔜
**Título sugerido da conversa:** `fortbc · Cartas & Base de Dados`
**Doc:** [`CONTEXT_CARDS.md`](CONTEXT_CARDS.md) · fonte de stats: [`GAME_DATA.csv`](GAME_DATA.csv) / [`GAME_DATA.md`](GAME_DATA.md)

Expandir o conjunto de cartas pra deixar o jogo mais rico e **balanceado**. Criar diversas cartas novas (heróis, peões de vibe, itens/debuffs, arapucas) e refletir em `BASE_CARDS` (index.html) **e** no CSV. Inclui o pipeline de gerar `BASE_CARDS` a partir do CSV (hoje manual).

**Relacionado:** o jogo hoje está **difícil demais** pra avançar — o balanceamento entra aqui e/ou em Game Mechanics.

---

## 📖 Capítulo: Visual Novel — 🔜
**Título sugerido da conversa:** `fortbc · Visual Novel`
**Doc:** `CONTEXT_VISUALNOVEL.md` *(a criar no início do capítulo)*

Sistema de narração: um personagem como **imagem PNG** + uma **caixa de texto** que surge na tela e conta as informações necessárias (tutoriais, contexto, dicas de balanceamento). Usar como camada de apresentação/onboarding e pra explicar mecânicas ao jogador.

**A definir:** quem é o personagem, gatilhos (quando aparece), estilo da caixa, se é dispensável/avançável, integração com `showScreen`.

---

## ⚙ Capítulo: Game Mechanics — 🔜
**Título sugerido da conversa:** `fortbc · Game Mechanics`
**Doc:** [`CONTEXT_GAMEPLAY.md`](CONTEXT_GAMEPLAY.md) · design: [`GAME_DESIGN.md`](GAME_DESIGN.md)

Adicionar/ajustar mecânicas do engine turn-based. Candidatos já no backlog do `CLAUDE.md`: triângulo de tipos na resolução (ATK→DEF→BAL), sinergia de Vibes, arapucas (face-down ativadas por inimigos), especiais dos heróis, "zerar campo antes de bater na base", mecânica de comeback. **Inclui ajustar a dificuldade** (está alta demais).

> ⚠️ A descrição original deste capítulo veio cortada ("quero adicio..."). **Completar o escopo no início da conversa.**

---

## 🎨 Capítulo: UI & Telas — 🔁
**Título sugerido da conversa:** `fortbc · UI & Telas`
**Docs:** [`CONTEXT_MENUS.md`](CONTEXT_MENUS.md) · [`CONTEXT_VISUAL.md`](CONTEXT_VISUAL.md) · [`POLISH.md`](POLISH.md)

A UI já está boa pra entender o básico, mas precisa ficar **mais lógica e ajustada**. Revisão de fluxo de telas, hierarquia, clareza dos menus e do tabuleiro, consistência visual.

---

## Mapa rápido capítulo → doc de contexto
| Capítulo | Doc principal |
|---|---|
| Áudio | `CONTEXT_AUDIO.md` |
| Cartas & Base | `CONTEXT_CARDS.md` (+ `GAME_DATA.csv`) |
| Visual Novel | `CONTEXT_VISUALNOVEL.md` (a criar) |
| Game Mechanics | `CONTEXT_GAMEPLAY.md` (+ `GAME_DESIGN.md`) |
| UI & Telas | `CONTEXT_MENUS.md` / `CONTEXT_VISUAL.md` |

> **Sempre:** ao fechar uma sessão de capítulo, atualizar o `CONTEXT_*` daquele capítulo, o `CLAUDE.md` (arquitetura/backlog) e o status aqui no `Chapters.md`.
