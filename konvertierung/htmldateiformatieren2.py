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
    new_html_table = 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sudoku Tabelle</title>
    <style>
		body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .sudoku-table {
            border-collapse: collapse;
        }
        .sudoku-table td {
            width: 40px;
            height: 40px;
            text-align: center;
            font-size: 20px;
            border: 2px solid black;
        }
        .sudoku-table .thick-top {
            border-top-width: 4px;
        }
        .sudoku-table .thick-left {
    
            border-left-width: 4px;
        }		
        .sudoku-table .thick-bottom{
            border-bottom-width: 4px;
        }
		.sudoku-table .thick-right {
            border-right-width: 4px;
        }
    </style>
</head>
<body>
    <table class="sudoku-table">
    # Füge die Sudoku-Blöcke zum neuen HTML hinzu und füge die Klassen hinzu
    for block in sudoku_blocks:
        new_html_table += '    <tr>\n'
        for cell_content in block:
            classes = ""
            if "thick-top" in new_html_table:
                classes += " thick-top"
            if "thick-bottom" in new_html_table:
                classes += " thick-bottom"
            if "thick-left" in new_html_table:
                classes += " thick-left"
            if "thick-right" in new_html_table:
                classes += " thick-right"
            new_html_table += f'        <td class="{classes}">{cell_content}</td>\n'
        new_html_table += '    </tr>\n'
    
    # Schließe das HTML-Tags
    new_html_table += '</table>\n</body>\n</html>'
    
    return new_html_table

# Lese den HTML-Inhalt aus der Datei 'matrix_sudoku1.txt.html'
with open('matrix_sudoku1.txt.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Wende die Funktion auf die gelesene HTML-Tabelle an
sudoku_html_table = convert_to_sudoku_table(html_content)

# Schreibe das Ergebnis in eine neue Datei 'sudoku_output.html'
with open('sudoku_output.html', 'w', encoding='utf-8') as output_file:
    output_file.write(sudoku_html_table)

print("Die Sudoku-Tabelle wurde erfolgreich ins gewünschte Format konvertiert und in 'sudoku_output.html' gespeichert.")