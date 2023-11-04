# Funktion, um die Tabelle ins gewünschte Format zu bringen
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
    
    # Erzeuge das neue HTML-Format für die Sudoku-Tabelle
    new_html_table = '<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<title>Sudoku Tabelle</title>\n<style>\nbody {\n    display: flex;\n    justify-content: center;\n    align-items: center;\n    height: 100vh;\n    margin: 0;\n}\n.sudoku-table {\n    border-collapse: collapse;\n}\n.sudoku-table td {\n    width: 40px;\n    height: 40px;\n    text-align: center;\n    font-size: 20px;\n    border: 2px solid black;\n}\n.thick-top, .thick-bottom, .thick-left, .thick-right {\n    border-width: 4px;\n}\n</style>\n</head>\n<body>\n<table class="sudoku-table">\n'
    
    # Füge die Sudoku-Blöcke zum neuen HTML hinzu
    for block in sudoku_blocks:
        new_html_table += '    <tr>\n'
        for cell_content in block:
            new_html_table += f'        <td>{cell_content}</td>\n'
        new_html_table += '    </tr>\n'
    
    # Schließe das HTML-Tags
    new_html_table += '</table>\n</body>\n</html>'
    
    return new_html_table

# Lese den HTML-Inhalt aus der Datei 'sudoku1.html'
with open('sudoku1.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Wende die Funktion auf die gelesene HTML-Tabelle an
sudoku_html_table = convert_to_sudoku_table(html_content)

# Schreibe das Ergebnis in eine neue Datei 'sudoku_output.html'
with open('sudoku_output.html', 'w', encoding='utf-8') as output_file:
    output_file.write(sudoku_html_table)

print("Die Sudoku-Tabelle wurde erfolgreich ins gewünschte Format konvertiert und in 'sudoku_output.html' gespeichert.")