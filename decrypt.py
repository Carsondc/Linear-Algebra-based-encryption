import numpy as np
import math
matrixB = np.array([
    [676860111, 879113573, 513803166, 576438185, 140513967, 526935521, 52593761],
    [192240254, 937178234, 749748463, 295392873, 968958924, 127425078, 507276281],
    [151841683, 632435464, 561198618, 309538414, 688013970, 933745979, 524657879],
    [505308192, 12064706, 862085751, 1620683, 743764195, 461696942, 44135327],
    [593119274, 790992555, 772859195, 916579212, 421622534, 38647847, 636860205],
    [711776285, 974471294, 168378198, 862929645, 443253073, 123764197, 851003458],
    [521318198, 182898976, 434739841, 404514443, 712278703, 35821358, 396728573]
])
import re

def read_matrices_from_file(filename):
    matrices = []
    with open(filename, 'r') as file:
        content = file.read()
    
    # Use regex to find all matrix-like substrings
    matrix_strings = re.findall(r'\[(.*?)\]', content, re.DOTALL)
    
    for matrix_string in matrix_strings:
        # Strip whitespace and convert the matrix string into a list of integers
        matrix_string = matrix_string.replace('\n', ' ').strip()
        if matrix_string:
            row = list(map(int, matrix_string.split()))
            # Determine the size of the matrix, assuming 1 row matrices for simplicity
            matrix = np.array(row).reshape(1, -1)
            matrices.append(matrix)
    
    return matrices

# Usage    

def denumerizeNumbers(number):
    # Check if the input is an integer
    if not isinstance(number, int):
        raise ValueError("Input must be an integer")

    # Use match to handle the number to letter mapping
    match number:
        case 1: return 'a'
        case 2: return 'b'
        case 3: return 'c'
        case 4: return 'd'
        case 5: return 'e'
        case 6: return 'f'
        case 7: return 'g'
        case 8: return 'h'
        case 9: return 'i'
        case 10: return 'j'
        case 11: return 'k'
        case 12: return 'l'
        case 13: return 'm'
        case 14: return 'n'
        case 15: return 'o'
        case 16: return 'p'
        case 17: return 'q'
        case 18: return 'r'
        case 19: return 's'
        case 20: return 't'
        case 21: return 'u'
        case 22: return 'v'
        case 23: return 'w'
        case 24: return 'x'
        case 25: return 'y'
        case 26: return 'z'
        case _: raise ValueError("Number out of range, must be between 1 and 26")
        
filename = 'encrypted.txt'
matrices = read_matrices_from_file(filename)
first_list = []
for matrix in matrices:
    Inverse = np.dot(matrix, np.linalg.inv(matrixB))
    for number in Inverse:
        first_list.append((number))
        second_list = []
for lst in first_list:
    second_list.append(lst.tolist())
third_list = []
for lst in second_list:
    for num in lst:
        third_list.append(denumerizeNumbers(round(num)))
str = ""
for letter in third_list:
    str += letter
with open("decrypted.txt", 'w') as f:
    print(str,file=f)
    
    
    
    
Inverse = np.dot(third_list, np.linalg.inv(matrixB))  # Multiply the result by the inverse of matrixB
print(Inverse, file=f)  # Write the inverse result to the file
            