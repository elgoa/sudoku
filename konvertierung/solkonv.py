#!/usr/bin/env python3
import os
import pandas as pd

def generiere_dateiname(dateipfad):
    zaehler = 1
    neuer_dateiname = dateipfad

    while os.path.exists(neuer_dateiname):
        zaehler += 1
        basisname, erweiterung = os.path.splitext(dateipfad)
        neuer_dateiname = f"{basisname}{zaehler}{erweiterung}"

    return neuer_dateiname

def datei_lesen(dateipfad):
    with open(dateipfad, 'r') as datei:
        zeilen = datei.readlines()
    matrix = []
    for zeile in zeilen:
        werte = zeile.strip().split()
        matrix.append(werte)
    return matrix

def generiere_html_tabelle(matrix, zaehler):
    df = pd.DataFrame(matrix)
    html_table = df.to_html(index=False, header=False, border=0, classes='sudoku-table')
    html_content = f"<html><head><style>.sudoku-table {{margin: 0 auto;}}</style></head><body>{html_table}"
    html_content += f'<p class="numbers">Nummer: {zaehler}</p>\n</body></html>'
    return html_content

if __name__ == "__main__":
    dateipfade = [
        "sudokusolution1.txt", "sudokusolution2.txt", "sudokusolution3.txt", "sudokusolution4.txt", "sudokusolution5.txt",
        "sudokusolution6.txt", "sudokusolution7.txt", "sudokusolution8.txt", "sudokusolution9.txt", "sudokusolution10.txt",
        "sudokusolution11.txt", "sudokusolution12.txt", "sudokusolution13.txt", "sudokusolution14.txt", "sudokusolution15.txt",
        "sudokusolution16.txt", "sudokusolution17.txt", "sudokusolution18.txt", "sudokusolution19.txt", "sudokusolution20.txt",
        "sudokusolution21.txt", "sudokusolution22.txt", "sudokusolution23.txt", "sudokusolution24.txt", "sudokusolution25.txt",
        "sudokusolution26.txt", "sudokusolution27.txt", "sudokusolution28.txt", "sudokusolution29.txt", "sudokusolution30.txt",
        "sudokusolution31.txt", "sudokusolution32.txt", "sudokusolution33.txt", "sudokusolution34.txt", "sudokusolution35.txt",
        "sudokusolution36.txt", "sudokusolution37.txt", "sudokusolution38.txt", "sudokusolution39.txt", "sudokusolution40.txt",
        "sudokusolution41.txt", "sudokusolution42.txt", "sudokusolution43.txt", "sudokusolution44.txt", "sudokusolution45.txt",
        "sudokusolution46.txt", "sudokusolution47.txt", "sudokusolution48.txt", "sudokusolution49.txt", "sudokusolution50.txt",
        "sudokusolution51.txt", "sudokusolution52.txt", "sudokusolution53.txt", "sudokusolution54.txt", "sudokusolution55.txt",
        "sudokusolution56.txt", "sudokusolution57.txt", "sudokusolution58.txt", "sudokusolution59.txt", "sudokusolution60.txt",
        "sudokusolution61.txt", "sudokusolution62.txt", "sudokusolution63.txt", "sudokusolution64.txt", "sudokusolution65.txt",
        "sudokusolution66.txt", "sudokusolution67.txt", "sudokusolution68.txt", "sudokusolution69.txt", "sudokusolution70.txt",
        "sudokusolution71.txt", "sudokusolution72.txt", "sudokusolution73.txt", "sudokusolution74.txt", "sudokusolution75.txt",
        "sudokusolution76.txt", "sudokusolution77.txt", "sudokusolution78.txt", "sudokusolution79.txt", "sudokusolution80.txt",
        "sudokusolution81.txt", "sudokusolution82.txt", "sudokusolution83.txt", "sudokusolution84.txt", "sudokusolution85.txt",
        "sudokusolution86.txt", "sudokusolution87.txt", "sudokusolution88.txt", "sudokusolution89.txt", "sudokusolution90.txt",
        "sudokusolution91.txt", "sudokusolution92.txt", "sudokusolution93.txt", "sudokusolution94.txt", "sudokusolution95.txt",
        "sudokusolution96.txt", "sudokusolution97.txt", "sudokusolution98.txt", "sudokusolution99.txt", "sudokusolution100.txt"
    ]

    zaehler = 1
    html_content = ""
    for dateipfad in dateipfade:
        matrix = datei_lesen(dateipfad)
        if matrix is not None:
            html_content += generiere_html_tabelle(matrix, zaehler)
            zaehler += 1

            # Wenn 8 Sudokus generiert wurden, speichere das HTML-Dokument
            if zaehler % 6 == 1:
                html_dateiname = generiere_dateiname(f'matrix_{dateipfad}.html')
                with open(html_dateiname, 'w') as html_datei:
                    html_datei.write(html_content)
                print(f"HTML-Dokument mit Sudokus von {zaehler-6} bis {zaehler-1} erstellt.\nIn '{html_dateiname}' gespeichert.")
                html_content = ""  # Setze den HTML-Content für die nächsten 8 Sudokus zurück

    # Speichere das letzte HTML-Dokument, falls weniger als 8 Sudokus vorhanden sind
    if zaehler % 6 != 1:
        html_dateiname = generiere_dateiname(f'matrix_{dateipfad}.html')
        with open(html_dateiname, 'w') as html_datei:
            html_datei.write(html_content)
        print(f"HTML-Dokument mit Sudokus von {zaehler-zaehler%8} bis {zaehler-1} erstellt.\nIn '{html_dateiname}' gespeichert.")