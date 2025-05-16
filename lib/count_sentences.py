#!/usr/bin/env python3
import re  # <- this goes at the top of the file

class MyString:
    def __init__(self, value=''):
        if isinstance(value, str):
            self._value = value
        else:
            raise ValueError("The value must be a string.") # <-- fixed
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            raise ValueError("value must be a string")
    
    def is_sentence(self):
        return self.value.endswith('.')
    
    def is_question(self):
        return self.value.endswith('?')
    
    def is_exclamation(self):
        return self.value.endswith('!')
    
    def count_sentences(self):
        parts = re.split(r'[.!?]', self.value)
        sentences = [s.strip() for s in parts if s.strip()]
        return len(sentences)
