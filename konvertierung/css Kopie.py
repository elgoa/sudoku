from bs4 import BeautifulSoup

# Schleife durch die Dateien von 'sudoku_output1.html' bis 'sudoku_output100.html'
for i in range(1, 101):
    # Lese den HTML-Inhalt aus der Datei 'sudoku_output{i}.html'
    with open(f'sudoku_output{i}.html', 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Parsen des HTML-Dokuments
    soup = BeautifulSoup(html_content, 'html.parser')

    # Finde das <style>-Element und lösche die vorhandenen CSS-Regeln
    style_tag = soup.find('style')
    if style_tag:
        style_tag.decompose()

    # Ersetze die CSS-Regeln durch neue Regeln
    new_css_rules = '''
   body {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh; /* 100% der Viewport-Höhe */
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

.sudoku-table .thick-bottom {
    border-bottom-width: 4px;
}

.sudoku-table .thick-right {
    border-right-width: 4px;
}

.numbers {
    text-align: center;
}
    '''

    # Füge das neue <style>-Element mit den neuen CSS-Regeln hinzu
    new_style_tag = soup.new_tag('style')
    new_style_tag.string = new_css_rules
    soup.head.append(new_style_tag)

    # Schreibe die aktualisierten Daten zurück in die Datei
    with open(f'sudoku_output{i}.html', 'w', encoding='utf-8') as file:
        file.write(str(soup))

    print(f"Die CSS-Regeln in 'sudoku_output{i}.html' wurden erfolgreich aktualisiert.")