"""
Project for Week 3 of "Python Data Analysis".
Read and write CSV files using a dictionary of dictionaries.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

import csv

def read_csv_fieldnames(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Ouput:
      A list of strings corresponding to the field names in
      the given CSV file.
    """
    table = []
    with open(filename, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=separator, quotechar=quote)
        for row in csv_reader:
            table.append(row)

    return table[0]


def read_csv_as_list_dict(filename, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a list of dictionaries where each item in the list
      corresponds to a row in the CSV file.  The dictionaries in the
      list map the field names to the field values for that row.
    """
    table = []
    with open(filename, "r", newline = '') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter = separator, quotechar = quote)
        for row in csv_reader:
            table.append(row)
    return table


def read_csv_as_nested_dict(filename, keyfield, separator, quote):
    """
    Inputs:
      filename  - name of CSV file
      keyfield  - field to use as key for rows
      separator - character that separates fields
      quote     - character used to optionally quote fields
    Output:
      Returns a dictionary of dictionaries where the outer dictionary
      maps the value in the key_field to the corresponding row in the
      CSV file.  The inner dictionaries map the field names to the
      field values for that row.
    """
    with open(filename, "r") as csv_file:
        table = {}
        csv_reader = csv.DictReader(csv_file, delimiter = separator, quotechar = quote)
        for row in csv_reader:
            table[row[keyfield]] = row
    return table


def write_csv_from_list_dict(filename, table, fieldnames, separator, quote):
    """
    Inputs:
      filename   - name of CSV file
      table      - list of dictionaries containing the table to write
      fieldnames - list of strings corresponding to the field names in order
      separator  - character that separates fields
      quote      - character used to optionally quote fields
    Output:
      Writes the table to a CSV file with the name filename, using the
      given fieldnames.  The CSV file should use the given separator and
      quote characters.  All non-numeric fields will be quoted.
    """
    table1 = []
    for row in table:
        table2 = []
        for fieldname in fieldnames:
            table2.append(row[fieldname])
        table1.append(table2)

    filename = open(filename, 'w', newline='')
    #
    csv_w = csv.writer(filename, delimiter=separator, quotechar=quote, quoting=csv.QUOTE_NONNUMERIC)
    csv_w.writerow(fieldnames)
    for dt2 in table1:
        csv_w.writerow(dt2)
    filename.close()
        
#print(read_csv_fieldnames("table3.csv", ",", "'"))
#print(read_csv_as_list_dict("table4.csv", ",", '"'))
#print(read_csv_as_nested_dict('table1.csv', 'Field1', ',', '"'))
#print(read_csv_as_nested_dict('table1.csv', 'Field1', ',', '"'))
write_csv_from_list_dict('output1.csv', [{'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14}, {'a': 20, 'b': 21, 'c': 22, 'd': 23, 'e': 24}, {'a': 30, 'b': 31, 'c': 32, 'd': 33, 'e': 34}, {'a': 40, 'b': 41, 'c': 42, 'd': 43, 'e': 44}], ['a', 'b', 'c', 'd', 'e'], ',', '"') 