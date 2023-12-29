class Esquina:
    def __init__(self,valores) -> None:
        self.__valores = valores

class Rubik:
    def __init__(self,modo) -> None:
        self.__mode=modo
        if modo == "spefzz":
            self.__esquinas = ["aer","bnq","cjm","dfi","glu","kpv","otw","hsx"]
            self.__aristas = ["aq","bm","ci","de","hr","fl","jp","nt","ku","ov","sw","gx"]
 