# pseudo code taken from CLRS book

SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")  # formatting to use subscript
    # works only with Python 3
    # can be safely commented out for Python 2

def matrix_multiplication_order(matrix_size_list):
    # matrix_size_list=[p0,p1,p2,...,pn]
    # size of 'i'th matrix: p(i-1) x p(i)
    n = len(matrix_size_list)-1
    if n < 1 :
        return 'Invalid Input'
    costs = []  # list to store resulting costs
    paren = []  # list to store resulting parenthesis positions
    for i in range(n+1):
        temp = []
        temp2= []
        for j in range(n+1):
            temp.append(float('inf'))
            temp2.append(-1)
        costs.append(temp)
        paren.append(temp2)
    mmo_helper(matrix_size_list, 1, n, costs, paren)
    print_result(paren, 1, n)


def mmo_helper(matrix_size_list, i, j, costs, paren):
    if costs[i][j] < float('inf'):
        return costs[i][j]
    else:
        if i == j:
            costs[i][j] = 0
        else:
            for k in range(i, j):
                sub_cost = matrix_size_list[i-1] * matrix_size_list[k] * matrix_size_list[j]
                cost = sub_cost + mmo_helper(matrix_size_list, i, k, costs, paren) + mmo_helper(matrix_size_list, k+1, j, costs, paren)
                if cost < costs[i][j]:
                    costs[i][j] = cost
                    paren[i][j] = k
        return costs[i][j]

def print_result(paren, i, j):
    if i == j:
        print('A', str(i).translate(SUB), sep='', end='')
    else:
        k = paren[i][j]
        print("(", sep='', end='')
        print_result(paren, i, k)
        print_result(paren, k+1, j)
        print(")", sep='', end='')
