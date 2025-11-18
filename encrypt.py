import numpy as np
import random
import string

# Create your matrices
matrixA = np.array([[35, 68, 73, 12], [34, 69, 74, 13], [53, 86, 47, 21], [8, 20, 3, 2]])
matrixB = np.array([
    [676860111, 879113573, 513803166, 576438185, 140513967, 526935521, 52593761],
    [192240254, 937178234, 749748463, 295392873, 968958924, 127425078, 507276281],
    [151841683, 632435464, 561198618, 309538414, 688013970, 933745979, 524657879],
    [505308192, 12064706, 862085751, 1620683, 743764195, 461696942, 44135327],
    [593119274, 790992555, 772859195, 916579212, 421622534, 38647847, 636860205],
    [711776285, 974471294, 168378198, 862929645, 443253073, 123764197, 851003458],
    [521318198, 182898976, 434739841, 404514443, 712278703, 35821358, 396728573]
])

# Modified read_file function to return a processed string
def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            processed_string = ""
            for line in lines:
                # Remove non-alphabetic characters and concatenate the remaining letters
                line = ''.join([char for char in line if char.isalpha()])
                processed_string += line
            return processed_string
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    except IOError:
        print(f"Error reading file '{file_path}'.")
    return None

# Function to convert letters to corresponding numbers
def numerizeLetters(letter):
    letter = letter.lower()
    match letter:
        case 'a': return 1
        case 'b': return 2
        case 'c': return 3
        case 'd': return 4
        case 'e': return 5
        case 'f': return 6
        case 'g': return 7
        case 'h': return 8
        case 'i': return 9
        case 'j': return 10
        case 'k': return 11
        case 'l': return 12
        case 'm': return 13
        case 'n': return 14
        case 'o': return 15
        case 'p': return 16
        case 'q': return 17
        case 'r': return 18
        case 's': return 19
        case 't': return 20
        case 'u': return 21
        case 'v': return 22
        case 'w': return 23
        case 'x': return 24
        case 'y': return 25
        case 'z': return 26
        case _: return 0

# Read and process the input file
product = read_file('input.txt')
while len(product) % 7 != 0:
    product += random.choice(string.ascii_letters)

# Convert each character in the string to its corresponding number
lst = [numerizeLetters(char) for char in product]

# Partition the list into chunks of a given size
def partition_list(lst, chunk_size):
    return [lst[i:i + chunk_size] for i in range(0, len(lst), chunk_size)]

# Partition the list into sublists of 7 elements each
list_of_lists = partition_list(lst, 7)

# Convert each sublist into a numpy array (vector)
list_of_vectors = [np.array(vector) for vector in list_of_lists]

# Write the results to the output file
with open('encrypted.txt', 'w') as f:
    for i in range(len(list_of_vectors)):
        result = np.dot(list_of_vectors[i], matrixB)  # Multiply the vector by matrixB
        print(result, file=f)  # Write the result to the file
        Inverse = np.dot(result, np.linalg.inv(matrixB))  # Multiply the result by the inverse of matrixB
        #print(Inverse, file=f)  # Write the inverse result to the file