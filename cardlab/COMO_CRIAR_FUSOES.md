# 🔮 Como criar uma FUSÃO

Uma fusão tem **2 partes**: a **carta-resultado** (o que aparece quando funde) e a **receita** (que combinação gera esse resultado). Detalhes da mecânica em `CONTEXT_FUSION.md`.

## Parte 1 — A carta-resultado (na planilha `GAME_DATA.csv`)
É uma linha normal de carta, com duas marcas especiais:
- **`kind` = `fusion`**
- **`copies` = `0`** → assim ela **nunca** entra em deck/loja/recompensa; só surge **via fusão**.

Exemplo:
```
id,name,kind,type,vibe,...,emoji,ability,img
fus_resenha,A Resenha,fusion,ATK,amarelo,...,🎊,Fusão Festa+Festa,baladinha.png
```
- `type` (ATK/DEF/BAL), `vibe`, `hp`, `atk`, `star` etc. funcionam igual às outras cartas.
- `img` = arquivo em `assets/cards/` (mesma regra das cartas; web-safe, sem espaço/acento). Hoje as fusões apontam pra nomes da pasta `Imagens/` → mover e renomear.

## Parte 2 — A receita (na planilha `FUSIONS.csv`)
Schema: **`mode,a,b,result,note`**

- **`mode=recipe`** → `a` e `b` são **requisitos `chave:valor`** (1 por material; ordem não importa):
  - `vibe:<cor>` — `amarelo|vermelho|azul|roxo|verde`
  - `postura:<valor>` — derivada do `type`: **ATK=`briga`, DEF=`muro`, BAL=`labia`**
  - Ex.: `recipe,vibe:amarelo,vibe:vermelho,fus_brigarole,Festa + Força`
  - Ex.: `recipe,postura:muro,postura:muro,fus_tanque,Dois muros`
- **`mode=specific`** → `a` e `b` são **ids de carta** (ex.: `specific,arthur,letti,fus_lenda,...`). **Prioridade máxima** (resolve antes das receitas gerais).
- **Ordem no arquivo = prioridade de match.** Receitas de `postura` ficam **antes** das de `vibe` (senão a vibe casaria sempre primeiro).

## Regras que o jogo aplica (não precisa configurar)
- **Trava de ATK (estilo Forbidden Memories):** o resultado só sai se o ATK dele for **maior que o ATK efetivo dos dois materiais**. Senão o par não funde. → dê ao resultado um ATK alto o suficiente.
- Materiais: 2–5 monstros da mão (teto pelo tier de licença). Itens/arapucas não fundem.

## Passo a passo
1. Crie a **carta-resultado** na `GAME_DATA.csv` (`kind:fusion`, `copies:0`, ATK alto, `img` preenchido).
2. Salve a arte em `assets/cards/` (se tiver).
3. Adicione a **receita** na `FUSIONS.csv` (`recipe` por vibe/postura, ou `specific` por ids).
4. Me diga **"sincroniza"** → eu rodo `python cardlab/sync.py`, que injeta **CARDS_CSV e FUSIONS_CSV** no `index.html`.
5. Commit + push (ou me peça). ✅

> Pendente da mecânica (ver `CONTEXT_FUSION.md`): IA não funde; sem animação dedicada; "famílias" de resultado por par ainda não.
