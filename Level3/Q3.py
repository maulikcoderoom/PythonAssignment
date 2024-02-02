def JtoI(file_name):
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            corrected_content = content.replace('J', 'I')
            print(corrected_content)
    except FileNotFoundError:
        print("File not found.")
