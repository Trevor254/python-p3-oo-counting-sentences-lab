# #!/usr/bin/env python3

# class MyString:
#   def __init__(self, value=''):
#         if not isinstance(value, str):
#             raise ValueError("Value must be a string")
#         self.value = value

#   def is_sentence(self):
#         """Check if the string ends with a period."""
#         return self.value.endswith('.')

#   def is_question(self):
#         """Check if the string ends with a question mark."""
#         return self.value.endswith('?')

#   def is_exclamation(self):
#         """Check if the string ends with an exclamation mark."""
#         return self.value.endswith('!')

#   def count_sentences(self):
#         """
#         Count the number of sentences in the string.
#         Sentences are assumed to end with '.', '!', or '?'.
#         """
#         # Split the string by sentence-ending punctuation and filter out empty strings
#         sentences = [s for s in self.value.replace('!', '.').replace('?', '.').split('.') if s.strip()]
#         return len(sentences)

class MyString:
    def __init__(self, value=''):
        self._value = ''  # Use a private attribute to store the value
        self.value = value  # Call the setter to validate the initial value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value

    def is_sentence(self):
        """Check if the string ends with a period."""
        return self.value.endswith('.')

    def is_question(self):
        """Check if the string ends with a question mark."""
        return self.value.endswith('?')

    def is_exclamation(self):
        """Check if the string ends with an exclamation mark."""
        return self.value.endswith('!')

    def count_sentences(self):
        """
        Count the number of sentences in the string.
        Sentences are assumed to end with '.', '!', or '?'.
        """
        sentences = [s for s in self.value.replace('!', '.').replace('?', '.').split('.') if s.strip()]
        return len(sentences)

# Example Usage
string = MyString()
string.value = 123  # Prints: "The value must be a string."
string.value = "This is a string!"
print(string.is_sentence())     # False
print(string.count_sentences()) # 1
