# -*- coding: utf-8 -*-

class Mealy(object):
    """Mealy Machine : Finite Automata with Output """

    def __init__(self, states, input_alphabet, output_alphabet, transitions, initial_state):
        """
        6 tuple (Q, ∑, O, δ, X, q0) where −
        states is a finite set of states.
        alphabet is a finite set of symbols called the input alphabet.
        output_alphabet is a finite set of symbols called the output alphabet.
        transitions is the resultant data dictionary of input and output transition functions
        initial_state is the initial state from where any input is processed (q0 ∈ Q).
        """
        self.states = states
        self.input_alphabet = input_alphabet
        self.output_alphabet = output_alphabet
        self.transitions = transitions
        self.initial_state = initial_state

    def get_output_from_string(self, string):
        """Return Mealy Machine's output when a given string is given as input"""

        #temp_list = list(string)
        temp_list = string
        current_state = self.initial_state
        output = ''
        for x in temp_list:
            output+= self.transitions[current_state][x][1]
            current_state = self.transitions[current_state][x][0]

        return output


states = ['q0', 'q25', 'q50', 'q75', 'q100', 'q125', 'q150', 'q175']
input_alphabet = ['0', '1']
output_alphabet = ['0', '1']
transitions =  {
                'q0' : {'25' : ('q25', '0'), 
                        '50' : ('q50', '0'),
                        '100' : ('q100', '1')},
                'q25' : {'25' : ('q50', '0'), 
                        '50' : ('q75', '0'),
                        '100' : ('q125', '1')},
                'q50' : {'25' : ('q75', '0'), 
                        '50' : ('q100', '1'),
                        '100' : ('q150', '1')},
                'q75' : {'25' : ('q100', '1'), 
                        '50' : ('q125', '1'),
                        '100' : ('q175', '1')},
                'q100' : {'25' : ('q25', '0'), 
                        '50' : ('q50', '0'),
                        '100' : ('q100', '1')},
                'q125' : {'25' : ('q50', '0'), 
                        '50' : ('q75', '0'),
                        '100' : ('q125', '1')},
                'q150' : {'25' : ('q75', '0'), 
                        '50' : ('q100', '1'),
                        '100' : ('q150', '1')},
                'q175' : {'25' : ('q100', '1'), 
                        '50' : ('q125', '1'),
                        '100' : ('q175', '1')},
                }
initial_state = 'q0'

mealy = Mealy(states, input_alphabet, output_alphabet, transitions, initial_state)

print(mealy.get_output_from_string(['50','25','50','100','25','50','25']))
