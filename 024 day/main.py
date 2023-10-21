TEST_TXT = "../../../Desktop/test.txt"  # "/Users/sergeybozhko/Desktop/test.txt"
# TEST_TXT = "test.txt"

def read_file():
    with open(TEST_TXT) as f:
        lines = f.read()
        print(lines)


def write_to_file():
    with open(TEST_TXT, mode="w") as file:
        file.write("fds\nasdasd")


def append_to_file():
    with open(TEST_TXT, mode="a") as file:
        file.write("\nafsasfg\nasdasd")


write_to_file()
read_file()
append_to_file()
print()
read_file()
