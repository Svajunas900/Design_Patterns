"""Decorator pattern is used to extend existing codes functionality"""
def make_blink(function):
    def inner():
        res = function()
        result = "<blink>" + res + "</blink>"
        return result
    return inner

@make_blink
def hello_world():
    return "Hello world"

print(hello_world())