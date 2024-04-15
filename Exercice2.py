import re

def booleanValue(val) :
    if val == False :
        return 0
    else : 
        return 1
    
def assign_variables(variables, values):
    return {var: val for var, val in zip(variables, values)}

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

def logical_function_boolean_value(logical_function_input, variables):
    for var, val in variables.items():
        logical_function_input = re.sub(r'\bnot_{}\b'.format(re.escape(var)), 'not {}'.format(var), logical_function_input)
        logical_function_input = re.sub(r'\bnot\s+{}'.format(re.escape(var)), 'not {}'.format(var), logical_function_input)
        logical_function_input = re.sub(r'\b{}\b'.format(re.escape(var)), str(val), logical_function_input)
    return booleanValue(eval(logical_function_input))

def boolean_value_of_the_LogicalFunction(logical_function_input,variables, n, q):  
    result = []
    for values in possible_values(n, q):
        result.append(booleanValue(logical_function_boolean_value(logical_function_input,assign_variables(variables, values))))
    return result

def k_table_matrix(logical_function,n, q):
    k_table = boolean_value_of_the_LogicalFunction(logical_function, n, q)
    subdivisions = len(k_table) // len(possible_code_Gray(q))
    k_table = [k_table[i:i+subdivisions] for i in range(0, len(k_table), subdivisions)]
    return k_table

def karnaugh_table():
    
    variables_number = int(input("\nHow many variables is your function ?  → "))

    variables = []
    for i in range(variables_number):
        nom_variable = input(f"Please, enter the variable name for the variable number {i+1}: ").strip()
        variables.append(nom_variable)
    
    logical_function_input = input(f"Please enter your logical function. ('not' or 'not_' : negation, 'and', 'or')\n\t==> f({",".join(variables)}) = ")

    
    if variables_number == 2 :
        n = 1
        q = 1
    else :
        n = int(input("Please, enter the number of variable in the horizontal line of the karnaugh table : → "))
        q = variables_number - n
    
    k_table_array = boolean_value_of_the_LogicalFunction(logical_function_input,variables, n, q)
    k_table_array = [str(e) for e in k_table_array]
    
    letters = ''.join(variables[:n])
    letters1 = ''.join(variables[n :variables_number])
    header = ' | '.join([val for val in possible_code_Gray(n)])
    underline = '=' * (len(header) + 1)
    print(f'{letters}     {header}')
    print(f'{letters1}   || {underline}')
    subdivisions = len(k_table_array) // len(possible_code_Gray(q))
    parts = [k_table_array[i:i+subdivisions] for i in range(0, len(k_table_array), subdivisions)]
    for value, parts in zip(possible_code_Gray(q), parts):
        print(f"{value}   || {'  |  '.join(parts)}")

karnaugh_table()
