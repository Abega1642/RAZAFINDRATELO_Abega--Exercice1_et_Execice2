import string

#You can change this logical function in order to test it with other logical functions
def logical_function(*variables):
    return (variables[0] and variables[1]) or (variables[0] and variables[2]) or (not variables[1] and (not variables[2])) or variables[3]

def booleanValue(val) :
    if val == False :
        return 0
    else : 
        return 1

def negation_form(expression) :
    expression = expression.split("*")
    expression = [f"(not {e})" if len(e) == 1 else e[len(e) - 2] for e in expression]
    return " + ".join(expression)

def code_gray(a):
    a = a + tuple(reversed(a))
    half_length_of_a = len(a) // 2
    a = tuple(['0' + element for element in a[:half_length_of_a]]) + a[half_length_of_a:]
    a = a[:half_length_of_a] + tuple(['1' + element for element in a[half_length_of_a:]])
    return a

def possible_code_Gray(n):
    single = ('0', '1')
    if n == 1:
        return single
    else:
        result = code_gray(single)
        for i in range(3,n+1) :
            result = code_gray(result)
    return result

def transform_into_tuple(n):
    result = list(possible_code_Gray(n))
    for i in range(0, len(result)):
        result[i] = tuple(int(e) for e in tuple(result[i]))
    return result
def possible_values(n, q) :
    first = transform_into_tuple(q)
    result = []
    for i in range(0, len(first)):
        second = transform_into_tuple(n)
        
        for j in range (0, len(second)):
            second[j] += first[i]
        result.append(second)
    return [element for sous_tableau in result for element in sous_tableau]

def boolean_value_of_the_LogicalFunction(logical_function, n, q):  
    result = []
    for values in possible_values(n, q):
        result.append(booleanValue(logical_function(*values)))
    return result

def k_table_matrix(n, q):
    k_table = boolean_value_of_the_LogicalFunction(logical_function, n, q)
    subdivisions = len(k_table) // len(possible_code_Gray(q))
    k_table = [k_table[i:i+subdivisions] for i in range(0, len(k_table), subdivisions)]
    return k_table

def karnaugh_table(n,q):
    k_table_array = boolean_value_of_the_LogicalFunction(logical_function, n, q)
    k_table_array = [str(e) for e in k_table_array]
    letters = string.ascii_lowercase[:n]
    letters1 = string.ascii_lowercase[n :n + q]
    header = ' | '.join([val for val in possible_code_Gray(n)])
    underline = '=' * (len(header) + 2)
    print(f'{letters}     {header}')
    print(f'{letters1}   || {underline}')
    subdivisions = len(k_table_array) // len(possible_code_Gray(q))
    parts = [k_table_array[i:i+subdivisions] for i in range(0, len(k_table_array), subdivisions)]
    for value, parts in zip(possible_code_Gray(q), parts):
        print(f"{value}   || {'  | '.join(parts)}")
