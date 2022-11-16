def open_file(filename):
  '''Opens the given file, returning its file object if found, otherwise None'''
  try:
    file_object = open(filename, 'r')
    return file_object
  except FileNotFoundError:
    return None

def read_file(my_file):
    result = {}
    for line in my_file:
        data = line.split(';')
        result[data[0]] = [round(float(num), 2) for num in data[1:]]
    return result

def print_sales(data, totals=True):
    for key, value in sorted(data.items()):
        total = 0
        print("{:<15}".format(key), end='')
        for num in value:
            print("{:>12.2f}".format(num), end='')
            total += num
        if totals:
            print("{:>12.2f}".format(total))
        else:
            print()

def print_totals(data):
    result = None
    for _, value in data.items():
        if result is None:
            result = value
        else:
            result = [sum(x) for x in zip(value, result)]
    print_sales({'Total:': result}, False)

def main():
    file_name = input("Enter file name: ")
    file_object = open_file(file_name)
    # Your continue the program from here
    totals = input("Show totals per store (y/n)? ")
    show_totals = totals == 'y'
    sales_data = read_file(file_object)
    print_sales(sales_data)
    if show_totals:
        print_totals(sales_data)

# Main program starts here.  Do NOT change the starter code.
if __name__ == "__main__":
    main()
