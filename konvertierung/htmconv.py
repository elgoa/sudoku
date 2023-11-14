from bs4 import BeautifulSoup

html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            display: grid;
            grid-template-columns: repeat(1, 1fr);
            grid-template-rows: repeat(3, 1fr); /* 4 rows instead of 2 */
            gap: 10px;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 20px;
        }}

        .sudokusection {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 5px;
            height: 25vh;
        }}

        .sudoku-table {{
            border-collapse: collapse;
            margin: 10px;
        }}

        .sudoku-table td {{
            width: 11%;
            height: 11%;
            text-align: center;
            border: 2px solid black;
        }}

        .sudokudiv {{
            width: 100%;
            height: 100%;
        }}

        .sudoku-table .thick-top {{
            border-top-width: 4px;
        }}

        .sudoku-table .thick-left {{
            border-left-width: 4px;
        }}

        .sudoku-table .thick-bottom {{
            border-bottom-width: 4px;
        }}

        .sudoku-table .thick-right {{
            border-right-width: 4px;
        }}
    </style>
    <title>Your Sudoku Page</title>
</head>
<body>
    <!-- Your HTML content goes here -->
</body>
</html>
"""

# Funktion zur Extraktion der Zahlen aus einer HTML-Tabelle
def extract_numbers_from_html(html_file):
    with open(html_file, 'r') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')
    tables = soup.find_all('table')  # Finde alle Tabellen im HTML-Dokument

    numbers = []
    for table in tables:
        rows = table.find_all('tr')  # Finde alle Zeilen in der aktuellen Tabelle
        for row in rows:
            cells = row.find_all('td')  # Finde alle Zellen in der aktuellen Zeile
            for cell in cells:
                number = cell.text.strip()
                numbers.append(number)

    return numbers
def generate_numbered_tables(input_html, output_html):
    numbers = extract_numbers_from_html(input_html)

    # Öffne die Ausgabedatei im Schreibmodus
    with open(output_html, 'w') as output_file:
        # Schreibe den HTML-Header und die Style-Regeln
        output_file.write(html_content)
        # Iteriere über 9 Tabellen
        for table_num in range(1, 7):
            # Schreibe die Tabelle mit den entsprechenden Klassen und Zahlen
            if table_num % 2 == 1:
                output_file.write(f'<div class="sudokusection">\n')
            output_file.write(f'<div class="sudokudiv">\n')
            output_file.write(f'<table class="sudoku-table">\n')
            for i in range(9):
                output_file.write('    <tr>\n')
                for j in range(9):
                    classes = ''
                    if i in (0, 3, 6):
                        classes += ' thick-top'
                    if j in (0, 3, 6):
                        classes += ' thick-left'
                    if i == 8:
                        classes += ' thick-bottom'
                    if j == 8:
                        classes += ' thick-right'
                    number = numbers.pop(0) if numbers else ''
                    output_file.write(f'        <td class="{classes}">{number}</td>\n')
                output_file.write('    </tr>\n')
            output_file.write('</table>\n')
            output_file.write(f'</div>')
            if table_num % 2 == 0:
                output_file.write(f'</div>')

        # Schreibe den HTML-Footer
        output_file.write('</body>\n</html>')

for i in range (6, 101, 6):
    input_html = f'matrix_sudokusolution{i}.txt.html'
    output_html = f'sudokusolution_output{i}.html'
    generate_numbered_tables(input_html, output_html)