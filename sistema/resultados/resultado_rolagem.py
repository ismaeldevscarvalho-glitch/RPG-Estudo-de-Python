class ResultadoRolagem:

    def __init__(self, expressao, rolagens):

        self.expressao = expressao
        self.rolagens = rolagens
        self.total = sum(rolagens)

    def mostrar(self):

        print("=" * 40)
        print("ROLAGEM DE DADOS")
        print("=" * 40)

        print(f"Expressão : {self.expressao}")
        print(f"Rolagens  : {self.rolagens}")
        print(f"Total     : {self.total}")

        
        print("=" * 40)
