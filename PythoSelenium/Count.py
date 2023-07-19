def count_occurrences(string, char):
    count = 0
    for c in string:
        if c == char:
            count += 1
    return count

# Example usage
input_string = input("Enter a string: ")
input_char = input("Enter a character to count: ")

occurrences = count_occurrences(input_string, input_char)
print("Number of occurrences:", occurrences)

def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")  # Print the element followed by a space
        print()  # Move to the next line after printing each row

# Example matrix
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print_matrix(matrix)