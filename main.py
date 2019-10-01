#!/usr/bin/env python3

from GenericMachine import GenericMachine as Machine

def main():
    print("1a")
    alphabet = set(['0', '1'])
    trans_func = {'q0' : {'0' : 'q0', '1' : 'q1'},
                  'q1' : {'0' : 'q2'},
                  'q2' : {'0' : 'q3'},
                  'q3' : {'0' : 'q3', '1' : 'q1'}}
    start_state = 'q0'
    final_states = set(['q0', 'q3'])
    
    machine = Machine(alphabet, trans_func, start_state, final_states)

    strings = ['', '100', '0100', '01000']
    
    for string in strings:
        result = machine.process_string(string)
        # if result != None:
        print ('%s = %s' % (string, result))
     
    print("1b")
    alphabet = set(['a', 'b'])
    trans_func = {'q0' : {'b' : 'q3', 'a' : 'q1'},
                  'q1' : {'b' : 'q1', 'a' : 'q2'},
                  'q2' : {'a' : 'q1', 'b' : 'q3'},
                  'q3' : {'a' : 'q1', 'b' : 'q3'}}
    start_state = 'q0'
    final_states = set(['q3'])
    
    machine = Machine(alphabet, trans_func, start_state, final_states)

    strings = ['aab', 'ababaab']
    
    for string in strings:
        result = machine.process_string(string)
        # if result != None:
        print ('%s = %s' % (string, result))

    print("2a")
    alphabet = set(['a', 'b', 'c'])
    trans_func = {'q0' : {'a' : 'q1'},
                  'q1' : {'b' : 'q1', 'c' : 'q1'}}
    start_state = 'q0'
    final_states = set(['q0', 'q1'])
    
    machine = Machine(alphabet, trans_func, start_state, final_states)

    strings = ['ab', 'ababaab']
    
    for string in strings:
        result = machine.process_string(string)
        # if result != None:
        print ('%s = %s' % (string, result))

    print("2b")
    alphabet = set(['a', 'b', 'c'])
    trans_func = {'q0' : {'a' : 'q1', 'b': 'q4', 'c': 'q4'},
                  'q1' : {'a' : 'q2'},
                  'q2' : {'a' : 'q3'},
                  'q3' : {'b' : 'q3', 'c' : 'q3'},
                  'q4' : {'a' : 'q5', 'b': 'q4', 'c': 'q4'},
                  'q5' : {'a' : 'q6'},
                  'q6' : {'a' : 'q7'},
                  'q7python' : {}}
    start_state = 'q0'
    final_states = set(['q3', 'q7'])
    
    machine = Machine(alphabet, trans_func, start_state, final_states)

    strings = ['a']
    
    for string in strings:
        result = machine.process_string(string)
        # if result != None:
        print ('%s = %s' % (string, result))

    print("2c")
    alphabet = set(['a', 'b'])
    trans_func = {'q0' : {'a' : 'q1', 'b': 'q3'},
                  'q1' : {'a' : 'q4', 'b' : 'q2'},
                  'q2' : {'b' : 'q2'},
                  'q3' : {},
                  'q4' : {'a' : 'q4', 'b': 'q3'}}
    start_state = 'q0'
    final_states = set(['q1', 'q2', 'q3'])
    
    machine = Machine(alphabet, trans_func, start_state, final_states)

    strings = ['aaaab']
    
    for string in strings:
        result = machine.process_string(string)
        # if result != None:
        print ('%s = %s' % (string, result))

    print("2d")
    alphabet = set(['a', 'b'])
    trans_func = {'q0' : {'a' : 'q1'},
                  'q1' : {'a' : 'q1', 'b' : 'q3', 'c' : 'q2'},
                  'q2' : {'c' : 'q2'},
                  'q3' : {'a' : 'q2', 'b' : 'q3'}}
    start_state = 'q0'
    final_states = set(['q1', 'q2'])
    
    machine = Machine(alphabet, trans_func, start_state, final_states)

    strings = ['']
    
    for string in strings:
        result = machine.process_string(string)
        # if result != None:
        print ('%s = %s' % (string, result))


if __name__ == "__main__":
    print("Questions 1 and 2:")
    main()

    print("Question 3:")
    import find_indeces_pattern_on_text

    import MealyMachine
