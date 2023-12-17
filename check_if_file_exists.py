from csv import DictWriter


# Here we are checking if the file exists and if it dose not exist we create it
def check_if_file_exists(file_name, encoding, fieldnames):
    try:
        with open(file_name, "r", encoding=encoding, newline="") as file:
            pass
    except FileNotFoundError:
        with open(file_name, "w", encoding=encoding, newline="") as file:
            writer = DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
