class CreditTest:
    
    endSimulation = False
    desiredValue = 0
    installmentQuantity = 0
    
    def __init__(self):
        self.desiredValue = float(input("Valor desejado: "))
        self.installmentQuantity = int(input("Quantidade de vezes que deseja pagar: "))
        self.simulate()
        self.valuesGetter()
    
    def simulate(self):
        tax = 1 + self.installmentQuantity * 0.25
        finalValue = self.desiredValue * tax
        diffValue = finalValue - self.desiredValue
        installmentValue = finalValue / self.installmentQuantity
        
        print("Requerido: ", self.desiredValue)
        print("Total final: ", finalValue)
        print("A pagar a mais: ", diffValue)
        print("Total por parcela: ", installmentValue)
        print("Taxa: ", tax)
        print("Taxa final do contrato: ", tax * self.installmentQuantity)

    def setValues(self): 
        type = float(input("Deseja mudar: 1 - Valor | 2 - Quantidade de parcelas | 3 - Continuar processo"))
        if type == 1:
            self.desiredValue = float(input("Novo valor desejado: "))
            self.simulate()
        elif type == 2:
            self.installmentQuantity = int(input("Quantidade que deseja pagar: "))
            self.simulate()
        elif type == 3:
            self.endSimulation = True
            print("Comeremos seu rabo")
        else:
            print("Digitou um valor errado paizão")

    def valuesGetter(self): 
        while(not self.endSimulation): 
            self.setValues()
            

CreditTest()