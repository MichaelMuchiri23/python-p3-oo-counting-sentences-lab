#!/usr/bin/env python3

class MyString:
    def __init__(self, value = ""):
        self.value = value

    def get_value(self):
        return self._value

    def set_value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    value = property(get_value, set_value)        
            
    def is_sentence(self):
        if self.value[-1] == ".":
            return True
        else:
            return False

    def is_question(self):
        if self.value[-1] == "?":
            return True
        else:
            return False  

    def is_exclamation(self):
        if self.value[-1] == "!":
            return True
        else:
            return False

    def count_sentences(self):
        new_value = self.value
        for item in ["!", "?"]:
            new_value = new_value.replace(item, ".")

        new_value = [item for item in new_value.split(".") if item] 
        return len(new_value)
        

#Case examples
simple_string = MyString("one. two. three?")
empty_string = MyString()
complex_string = MyString("This, well, is a sentence. This is too!! And so is this, I think? Woo...")
superb_string = MyString("Yoohoo.Anyone there?  Gojo is the bisected one!!!")


print(simple_string.count_sentences())
print(empty_string.count_sentences())
print(complex_string.count_sentences())
print(superb_string.count_sentences())