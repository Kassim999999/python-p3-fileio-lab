def write_file(file_name, file_content):
    
    full_file_name = f"{str(file_name)}.txt"

    with open(full_file_name, 'w', encoding='utf-8') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    
    full_file_name = f"{str(file_name)}.txt"

    with open(full_file_name, 'a', encoding='utf-8') as file:
        file.write(append_content)

def read_file(file_name):
    

    full_file_name = f"{str(file_name)}.txt"

    with open(full_file_name, 'r', encoding='utf-8') as file:
        return file.read()
