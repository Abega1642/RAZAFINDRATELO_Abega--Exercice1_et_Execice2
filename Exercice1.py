import itertools
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

def first_canonic_form_function(values, result) :
    letters = string.ascii_lowercase[:len(values)]
    expression = []
    for value, letter in zip(values, letters):
        if value == 0:
            expression.append(f"(not {letter})")
        else:
            expression.append(letter)
    expression_str = '*'.join(expression)
    result.append(expression_str)

def second_canonic_form_function(values, result):
    letters = string.ascii_lowercase[:len(values)]
    expression = []
    for value, letter in zip(values, letters):
        if value == 0:
            expression.append(f"(not {letter})")
        else:
            expression.append(letter)
    expression_str = '*'.join(expression)
    expression_str = negation_form(expression_str)
    expression_str = f'[{expression_str}]'
    result.append(expression_str)

def possible_values(variables_numbers):
    return list(itertools.product([1, 0], repeat=variables_numbers))

def table_of_truth(logical_function, variables_numbers) :
    print('\n\t==== TABLE OF TRUTH --- TABLE DE VERITE ==== \n')
    line_one = "  |  ".join([f"{chr(i)}" for i in range(97, 97 + variables_numbers)] + ["Logical function"])  
    print(line_one)
    print("-" * len(line_one))
    
    first_canonic_form = []
    second_canonic_form = []
    
    for values in possible_values(variables_numbers):
        lines = "  |  ".join(str(value) for value in values)
        boolean_value_of_the_function = booleanValue(logical_function(*values))
        if boolean_value_of_the_function == 1:
            first_canonic_form_function(values, first_canonic_form)   
        else :
            second_canonic_form_function(values, second_canonic_form)
        print(f"{lines}  |       {boolean_value_of_the_function}")
    
    first_canonic_form = " + ".join(first_canonic_form)
    second_canonic_form = " * ".join(second_canonic_form)
    
    print(f'\n==> The first canonic form of the logical function f is  : {first_canonic_form}')
    print(f'\n==> The second canonic form of the logical function f is  : {second_canonic_form}\n')
