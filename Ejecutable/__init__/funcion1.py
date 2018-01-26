from __init__.setting import *

text = ""
def setText(texto=TEXTO_PRETERMINADO):
    if (texto != TEXTO_PRETERMINADO) == True:
        print(f"Se ha guardado el nuevo texto ---> |{texto}|")
        return texto
    else:
        text = list(TEXTO_PRETERMINADO)
        return text[0]
