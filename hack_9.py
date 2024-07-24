"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = {}
    for clave, valor in s.items():
        if clave.startswith("foo"): 
         valor_sin_k = valor.replace('k', '')
         result[clave.capitalize()] = valor_sin_k.capitalize()
    return result
