# Funktion, um die Tabelle ins gewünschte Format zu bringen und die Klassen hinzuzufügen
def convert_to_sudoku_table(html_table):
    # Teile den HTML-Code in Zeilen auf
    rows = html_table.strip().split('\n')
    
    # Entferne das äußere Tabellentag und führe eine Zeilentrennung durch
    rows = rows[1:-1]
    
    # Iteriere über die Zeilen und Spalten, um das neue Format zu erstellen
    sudoku_table = []
    for row in rows:
        cells = row.split('</td>')
        for i in range(len(cells) - 1):
            cell_content = cells[i].split('>')[-1].strip()  # Extrahiere den Zelleninhalt
            sudoku_table.append(cell_content)  # Füge den Zelleninhalt zur neuen Tabelle hinzu
    
    # Teile die Tabelle in 9x9 Blöcke für Sudoku
    sudoku_blocks = [sudoku_table[i:i + 9] for i in range(0, len(sudoku_table), 9)]
    
    # Erzeuge das neue HTML-Format für die Sudoku-Tabelle mit den erforderlichen Klassen
    new_html_table = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>Sudoku Tabelle</title>\n<style>\nbody {\n    display: flex;\n    justify-content: center;\n    align-items: center;\n    height: 100vh;\n    margin: 0;\n}\n.sudoku-table {\n    border-collapse: collapse;\n}\n.sudoku-table td {\n    width: 40px;\n    height: 40px;\n    text-align: center;\n    font-size: 20px;\n    border: 2px solid black;\n}\n.thick-top, .thick-bottom, .thick-left, .thick-right {\n    border-width: 4px;\n}\n</style>\n</head>\n<body>\n<table class="sudoku-table">\n'
    
    # Füge die Sudoku-Blöcke zum neuen HTML hinzu und füge die Klassen hinzu
    for i, block in enumerate(sudoku_blocks):
        new_html_table += '    <tr>\n'
        for j, cell_content in enumerate(block):
            classes = ""
            if i in (0, 3, 6):
                classes += ' thick-top'
            if j in (0, 3, 6):
                classes += ' thick-left'
            if i == 8:
                classes += ' thick-bottom'
            if j == 8:
                classes += ' thick-right'
            new_html_table += f'        <td class="{classes}">{cell_content}</td>\n'
        new_html_table += '    </tr>\n'
    
    # Schließe das HTML-Tags
    new_html_table += '</table>\n</body>\n</html>'
    
    return new_html_table

for i in range(1, 101):
    # Lese den HTML-Inhalt aus der Datei 'sudoku{i}.html'
    with open(f'matrix_sudoku1.txt.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Wende die Funktion auf die gelesene HTML-Tabelle an
    sudoku_html_table = convert_to_sudoku_table(html_content)

    # Füge die Sudoku-Tabelle in das gesamte HTML-Dokument ein
    new_html_content = f'<p>Beliebiger Text vor der Tabelle</p>\n{sudoku_html_table}\n<p>Beliebiger Text nach der Tabelle</p>'

    # Schreibe das gesamte HTML-Dokument in eine neue Datei
    with open(f'sudoku_output1.html', 'w', encoding='utf-8') as output_file:
        output_file.write(new_html_content)

    print(f"Die Sudoku-Tabelle aus 'sudoku{i}.html' wurde erfolgreich ins gewünschte Format konvertiert und in 'udoku{i}.txts.html' gespeichert.")
