# 🎨 ASSETS — Guia de Imagens e Áudio

Como subir arquivos para o repositório `fortbc` e quais nomes o jogo espera.

---

## 📐 Imagens dos Heróis

O jogo carrega cada herói de:
```
assets/heroes/<id>.png
```
via `https://raw.githubusercontent.com/Guilherme-Moliner/fortbc/main/assets/heroes/<id>.png`

### Nomes EXATOS dos arquivos (id → arquivo)

| Herói | Arquivo (obrigatório) |
|---|---|
| Arthur | `assets/heroes/arthur.png` |
| Fanta | `assets/heroes/fanta.png` |
| Garopaba | `assets/heroes/garopaba.png` |
| Bala | `assets/heroes/bala.png` |
| Nathan | `assets/heroes/nathan.png` |
| Léo | `assets/heroes/leo.png` |
| Zaga | `assets/heroes/zaga.png` |
| Vitão | `assets/heroes/vitao.png` |
| Borba | `assets/heroes/borba.png` |
| Letti | `assets/heroes/letti.png` |

> ⚠️ Os nomes precisam ser **idênticos** (minúsculo, sem acento). `vitao` e `leo` sem acento.

### Especificações recomendadas

| Item | Valor |
|---|---|
| Formato | PNG |
| Proporção | retrato (~2:3), igual a uma carta |
| Resolução mínima | 184 × 262 px |
| Resolução ideal | 368 × 524 px (2×, telas retina) |
| Fundo | pode ser ilustrado (como as cartas atuais) |
| Tamanho do arquivo | < 500 KB cada (otimize com tinypng.com) |

O jogo redimensiona automaticamente; só mantenha a proporção retrato para não distorcer.

---

## ♟️ Imagens de Peões e Itens (pendência)

Hoje peões e itens usam **emoji** como placeholder. Para trocar por arte:

| Tipo | id | Placeholder atual | Sugestão de arte |
|---|---|---|---|
| Peão ATK | `peon_atk` | 👊 | lutador genérico |
| Peão DEF | `peon_def` | 🧱 | escudo / muro |
| Peão BAL (atirador) | `peon_bal` | 🎯 | arqueiro/atirador |
| Peão DEF 2 | `peon_def2` | 💪 | brutamontes |
| Churrasco | `churrasco` | 🥩 | item churrasco |
| Energético | `energetico` | ⚡ | lata energético |
| Rodada | `rodada` | 🍺 | cerveja |
| Turbo Boost | `turboboost` | 💨 | rajada |
| Ressurreição | `ressurreicao` | 🔄 | fênix |
| Reforço | `reforco` | 🧱 | tijolos |

Quando tiver as artes, suba em `assets/pawns/<id>.png` e `assets/items/<id>.png` — e me avise para eu plugar no código (hoje o código só busca `heroes/`).

---

## 🎵 Trilha Sonora

O jogo procura:
```
assets/audio/bgmusic.mp3
```

| Item | Valor |
|---|---|
| Formato | MP3 |
| Duração | 1–3 min (toca em loop) |
| Tamanho | < 3 MB |
| Volume | o jogo já reduz para 35% |
| Licença | use música livre de direitos (ex: Pixabay, Incompetech) |

Se o arquivo não existir, o jogo roda **sem música** (sem erro). O botão 🔊 no topo controla mute.

> SFX (hit, deploy, vitória) podem ser adicionados depois em `assets/audio/sfx/`.

---

## 📤 Como subir no GitHub

**Pelo site (mais fácil):**
1. No repo, entre na pasta `assets/heroes/` (crie se não existir: "Add file" → "Create new file" → digite `assets/heroes/.gitkeep`)
2. "Add file" → "Upload files" → arraste os PNGs
3. Commit

**Por linha de comando:**
```bash
git clone https://github.com/Guilherme-Moliner/fortbc.git
cd fortbc
mkdir -p assets/heroes assets/audio
# copie os arquivos para as pastas
git add assets/
git commit -m "add hero images and audio"
git push
```

---

## ✅ Checklist de upload

- [ ] `index.html` na raiz
- [ ] 10 PNGs em `assets/heroes/` com nomes exatos
- [ ] `assets/audio/bgmusic.mp3` (opcional)
- [ ] Testar abrindo o GitHub Pages ou o `raw` de uma imagem no navegador
