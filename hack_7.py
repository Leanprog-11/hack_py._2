"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    resultados = []
    for letra in s:
        if letra == "a":
            resultados.append("1")
        elif letra == "b":
            resultados.append(2)
        elif letra == "c":
            resultados.append("3")
        elif letra == "d":
            resultados.append(4)
        elif letra == "e":
            resultados.append("5")
        elif letra == 0:
            resultados.append(0)
        else:
            resultados.append(None)  # Manejar casos no esperados o letras adicionales
    
    return resultados