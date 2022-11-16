def read_line():
    line = input("Enter password: ")
    if line == "quit":
        return None
    return line

def get_digits(line):
    return sum(character.isdigit() for character in line)

def is_valid(line):
    return len(line) >= 8 and get_digits(line) >= 3

def print_stats(name, arr):
    if len(arr) > 0:
        print("{} passwords:".format(name))
        print(" ".join(arr))
        print("Average length:", round(sum([len(password) for password in arr]) / len(arr), 1))
        print("Average # of digits:", round(sum([get_digits(password) for password in arr]) / len(arr), 1))




quit = False
valids = []
invalids = []
while not quit:
    line = read_line()
    if line is None:
        quit = True
    else:
        if is_valid(line):
            valids.append(line)
            print("Password is valid")
        else:
            invalids.append(line)
            print("Password is invalid")
print_stats("Valid", valids)
print_stats("Invalid", invalids)
