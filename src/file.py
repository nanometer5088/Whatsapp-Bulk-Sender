import openpyxl

def read_excel_file(filename):
    # Load the workbook
    wb = openpyxl.load_workbook(filename)

    # Select the active worksheet
    ws = wb.active

    # Create empty lists to store the data
    names = []
    phones = []
    sexes = []
    messages = []

    # Iterate through each row (excluding the first row)
    for row in ws.iter_rows(min_row=2, values_only=True):
        # Extract the data from the columns
        name = row[0]
        phone = row[1]
        sex = row[2]
        message = row[3]

        # Append the data to the relevant list
        names.append(name)
        phones.append("+" + str(phone))
        sexes.append(sex)
        messages.append(str(message))

    # Return the sorted lists
    return names, phones, sexes, messages

def saudacao():
    import datetime
    hour = int(f"{datetime.datetime.now()}".split()[1].split(":")[0])
    if hour >= 18 or hour < 6:
        return "Boa noite"
    elif hour >= 6 and hour < 12:
        return "Bom dia"
    elif hour >= 12 and hour < 18:
        return "Boa tarde"