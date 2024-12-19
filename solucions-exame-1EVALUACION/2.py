def tarxeta(palabra: str, caracter: str) -> str:
    """
    Crea unha tarxeta cunha palabra.
    
    Args:
        palabra (str): Palabra a incluír na tarxeta.
        caracter (str): Caracter co que se creará a tarxeta.
        
    Returns:
        str: Tarxeta creada.
        
    >>> tarxeta("Ola", "*")
    '*******\\n* OLA *\\n*******\\n'
    >>> tarxeta("Adeus", "-")
    '---------\\n- ADEUS -\\n---------\\n'
    >>> tarxeta("PalabraLonga", "#")
    '################\\n# PALABRALONGA #\\n################\\n'
    """ 
    primeira_ultima = caracter * (len(palabra) + 4) + "\n"
    intermedia = caracter + " " + palabra.upper() + " " + caracter + "\n"
    return primeira_ultima + intermedia + primeira_ultima

def crea_tarxetas(cadea: str, caracter: str) -> str:
    """
    Crea unha tarxeta por cada palabra dunha cadea.
    
    Args:
        cadea (str): Cadea de texto.
        
    Returns:
        None
        
    >>> crea_tarxetas("Xoán María Ana Pedro Maricarmen", '*')
    '********\\n* XOÁN *\\n********\\n*********\\n* MARÍA *\\n*********\\n*******\\n* ANA *\\n*******\\n*********\\n* PEDRO *\\n*********\\n**************\\n* MARICARMEN *\\n**************\\n'
    """
    palabras = cadea.split()
    resultado = ""
    for palabra in palabras:
        resultado += tarxeta(palabra, caracter)
    return resultado

print(crea_tarxetas("Xoán María Ana Pedro Maricarmen", '*'))

def cancelar_asistencia(asistentes: str, nome: str) -> str:
    """
    Cancela a asistencia dunha persoa.
    
    Args:
        asistentes (str): Lista de asistentes.
        nome (str): Nome da persoa a cancelar.
        
    Returns:
        str: Lista de asistentes actualizada.
        
    >>> cancelar_asistencia("Xoán María Ana Pedro Maricarmen", "Pedro")
    'Xoán María Ana Maricarmen'
    >>> cancelar_asistencia("Xoán María Ana Pedro Maricarmen", "María")
    'Xoán Ana Pedro Maricarmen'
    """
    lista = asistentes.split()
    lista.remove(nome)
    return " ".join(lista)