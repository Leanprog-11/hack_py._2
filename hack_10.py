"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = []
    contador = 1
    
    for diccionario in s:
        nuevo_diccionario = {}
        
        for clave, valor in diccionario.items():
            nuevo_diccionario[str(contador)] = str(contador + 1)
            contador += 2
        
        result.append(nuevo_diccionario)
    return result
