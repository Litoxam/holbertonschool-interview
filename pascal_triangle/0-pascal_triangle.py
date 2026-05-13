#!/usr/bin/python3

def pascal_triangle(n):
    """A list of lists of int representing the Pascal's triangle of n"""
    if n <= 0:
        return []

    pascal_list = [[1]]
    for i in range(1, n):
        past_list = pascal_list[-1]
        new_list = [1]

        for j in range(1, i):
            new_list.append(past_list[j-1] + past_list[j])

        new_list.append(1)
        pascal_list.append(new_list)

    return pascal_list

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))

print_triangle(pascal_triangle(5))