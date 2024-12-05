def comprueba_rimas(verso1: str, verso2: str) -> bool:
    if verso1.endswith(verso2[-2][-1]):
        return True
    else:
        return False


comprueba_rimas("caca", "vaca")