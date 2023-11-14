from bs4 import BeautifulSoup

def add_table_numbers(input_html, output_html, index):
    with open(input_html, 'r') as file:
        content = file.read()

    soup = BeautifulSoup(content, 'html.parser')

    tables = soup.find_all('table')
    for table_index, table in enumerate(tables, start=index):
        # Überprüfe, ob die Nummer bereits existiert
        if not table.find('p', string=f'Nr {table_index}'.strip()):
            # Erstelle ein neues <p> Element mit der Tabellennummer
            table_number_element = soup.new_tag('p')
            table_number_element.string = f'Nr {table_index}'

            # Erstelle ein neues <div> Element mit der Klasse 'sudokucontainer'
            div_element = soup.new_tag('div', class_='sudokucontainer')

            # Füge das <p> Element unter das <div> Element ein
            div_element.append(table_number_element)

            # Füge die Tabelle unter das <div> Element ein
            table.wrap(div_element)

    with open(output_html, 'w') as output_file:
        output_file.write(str(soup))

# Beispielaufruf für verschiedene Dateien
index = 1
for i in range(8, 101, 8):
    input_html = f'sudokusolution_output{i}.html'
    output_html = f'sudokusolution_output{i}.html'
    add_table_numbers(input_html, output_html, index)
    index += 8  # Inkrementiere den Index für die näch