#!/usr/bin/env python3
# Sincroniza a base de cartas: GAME_DATA.csv  ->  CARDS_CSV embutido no index.html
#
# O que faz:
#  1. Lê os arquivos de arte em assets/cards/.
#  2. Para toda carta cujo "<id>.png" existe na pasta, preenche a coluna `img`
#     (não mexe em imagens já preenchidas, ex.: as fusões com .jpeg).
#  3. Reescreve a GAME_DATA.csv (fonte de edição).
#  4. Copia o conteúdo pra dentro do bloco `const CARDS_CSV = ` ... `;` do index.html
#     (o que o jogo realmente lê).
#  5. Imprime um resumo + avisa sobre img que aponta pra arquivo inexistente.
#
# Uso:  python cardlab/sync.py            (rode da raiz do projeto)

import csv, os, re, sys, io

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS_DIR = os.path.join(ROOT, "assets", "cards")
CSV_PATH  = os.path.join(ROOT, "GAME_DATA.csv")
HTML_PATH = os.path.join(ROOT, "index.html")

def main():
    files = set(os.listdir(CARDS_DIR)) if os.path.isdir(CARDS_DIR) else set()

    with open(CSV_PATH, "r", encoding="utf-8", newline="") as f:
        rows = list(csv.reader(f))
    header, data = rows[0], [r for r in rows[1:] if r and any(c.strip() for c in r)]
    idx = {name: i for i, name in enumerate(header)}
    i_id, i_img = idx["id"], idx["img"]

    wired, missing = [], []
    for r in data:
        while len(r) < len(header):
            r.append("")
        cid = r[i_id].strip()
        png = cid + ".png"
        if png in files:
            if r[i_img] != png:
                r[i_img] = png
                wired.append(cid)
        elif r[i_img].strip():               # tem img mas arquivo não existe
            if r[i_img] not in files:
                missing.append((cid, r[i_img]))

    # 3. reescreve a GAME_DATA.csv
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(header)
    for r in data:
        w.writerow(r)
    csv_text = buf.getvalue().rstrip("\n")
    with open(CSV_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(csv_text + "\n")

    # 4. injeta no index.html
    with open(HTML_PATH, "r", encoding="utf-8", newline="") as f:
        html = f.read()
    nl = "\r\n" if "\r\n" in html else "\n"
    body = csv_text.replace("\n", nl)
    pat = re.compile(r"(const CARDS_CSV = `\r?\n)(.*?)(\r?\n`;)", re.DOTALL)
    if not pat.search(html):
        print("ERRO: bloco CARDS_CSV não encontrado no index.html"); sys.exit(1)
    html2 = pat.sub(lambda m: m.group(1) + body + m.group(3), html, count=1)
    with open(HTML_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(html2)

    # 5. resumo
    files_no_card = sorted(fn for fn in files if fn.endswith(".png")
                           and fn[:-4] not in {r[i_id].strip() for r in data})
    print(f"OK · {len(data)} cartas sincronizadas (GAME_DATA.csv -> index.html)")
    print(f"img preenchido em {len(wired)} carta(s): {', '.join(wired) if wired else '(nenhuma nova)'}")
    if missing:
        print("AVISO · img aponta p/ arquivo inexistente em assets/cards/:")
        for cid, fn in missing:
            print(f"   - {cid}: {fn}")
    if files_no_card:
        print(f"AVISO · arte sem carta na base: {', '.join(files_no_card)}")

if __name__ == "__main__":
    main()
