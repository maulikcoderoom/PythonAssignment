def parse_encoded_string(encoded_string):
    parts = encoded_string.split('0')

    parts = [part for part in parts if part]
    if len(parts)==3:
        first_name = parts[0]
        last_name = parts[1]
        id = parts[2]
        return {"first_name": first_name, "last_name": last_name, "id": id}
    else:
        return "Invalid string"
    

encoded_string = "Robert000Smith000123"
parsed_data = parse_encoded_string(encoded_string)
print(parsed_data)