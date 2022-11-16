def open_file(file_name): # Do not change this line
    '''Opens the given filename and returns its file object, or None if not found'''
    try:
        f = open(file_name, "r")
        return f
    except:
        return None
    
def read_matrix(file_object): # Do not change this line
    '''Creates an n-by-n integer matrix by reading data from file_object. 
    The matrix is a list of lists.'''
    return [[int(num) for num in line.split()] for line in file_object]

def row_sum_same(matrix): # Do not change this line
    '''Returns the sum of the elements in each row of the matrix if the sum is the same, else 0'''
    row_sum = 0
    for row in matrix:
        if row_sum == 0:
            row_sum = sum(row)
        else:
            if sum(row) != row_sum:
                return 0
    return row_sum

def col_sum_same(matrix): # Do not change this line
    '''Returns the sum of the elements in each column of the matrix if the sum is the same, else 0'''
    col_sum = 0
    for i in range(len(matrix)):
        if col_sum == 0:
            col_sum = sum([row[i] for row in matrix])
        else:
            if sum([row[i] for row in matrix]) != col_sum:
                return 0
    return col_sum

def print_matrix(matrix):
    for line in matrix:
        print('\t'.join([str(num) for num in line]))

def main(): # Do not change this line
    file_name = input("File name: ")
    my_file = open_file(file_name)
    if my_file is None:
        print("File not found")
        return
    matrix = read_matrix(my_file)

    print_matrix(matrix)

    row_sum = row_sum_same(matrix)
    col_sum = col_sum_same(matrix)
    if col_sum == 0 or row_sum != col_sum:
        print("Not same sums")
        return
    print("Same sums")

# Main program starts here. Do not change it.
if __name__ == "__main__":
    main()
