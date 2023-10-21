INPUT_LETTER = "./Input/Letters/starting_letter.txt"
NAMES_LIST = "./Input/Names/invited_names.txt"
OUTPUT_DIR = "./Output/ReadyToSend/"
NAME_PLACEHOLDER = "[name]"


def read_from_file(file_path):
    with open(file_path, mode="r") as file:
        return file.read()


def get_list_of_names():
    contents = read_from_file(NAMES_LIST)
    lines = contents.split()
    return lines


def get_letter_text():
    return read_from_file(INPUT_LETTER)


def write_to_file(file_path, text):
    with open(file_path, mode="w") as file:
        file.write(text)


def create_letter(name, letter):
    draft_letter = letter.replace(NAME_PLACEHOLDER, name)
    file_path = f"{OUTPUT_DIR}letter_for_{name}.txt"
    write_to_file(file_path, draft_letter)


def run():
    names: list[str] = get_list_of_names()
    letter = get_letter_text()
    for name in names:
        create_letter(name, letter)


if __name__ == "__main__":
    run()
