class GenericMachine():
    alphabet = set()
    trans_func = dict()
    start_state = str()
    final_states = set()

    def __init__(self, _alphabet, _trans_func, _start_state, _final_states):
        self.alphabet = _alphabet
        self.trans_func = _trans_func
        self.start_state = _start_state
        self.final_states = _final_states
    
    def __validate_string(self, _string):
        for char in _string:
            if char not in self.alphabet:
                return False
        return True

    def process_string(self, string):
        state = self.start_state
        for char in string:
            try:
                state = self.trans_func[state][char]
            except:
                return False

        return (state in self.final_states)
