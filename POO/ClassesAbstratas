from abc import ABC, abstractmethod

class ContaBancaria(ABC):

    def __init__(self, senha):
        self.senha = senha

    
    def alterarSenha(self, novaSenha):
        senha_atual = input('insira outra senha: ')
        if senha_atual == self.senha:           
            self.senha = novaSenha
            print('senha alterada')
        else:
            raise Exception("senhas não conferem")
        return self.senha

    @abstractmethod
    def sacar(self):
        pass
    
    @abstractmethod
    def depositar(self):
        pass

    @abstractmethod
    def consultarExtrato():
        pass

    def exibirDados(self):
        print(f'senha atual: {self.senha}')
        print(f'saldo atual: {self.saldo}')

class ContaCorrente(ContaBancaria):
    
    def __init__(self, senha, saldo):
        super().__init__(senha)
        self.saldo = saldo

    def setSaldo(self, saldo):
        self.saldo = saldo
    
    def getSaldo(self):
        return self.saldo
    
    def setValor(self, valor):
        self.valor = valor
        
    def getValor(self):
        return self.valor
    
    def sacar(self, valor:float):
        self.saldo = self.saldo - valor
    
    def depositar(self, valor):
        self.saldo = self.saldo + valor
    
    def consultarExtrato(self):
        return self.valor
    

    

class ContaPoupanca(ContaBancaria):
    
    def __init__(self, senha, saldo):
        super().__init__(senha)
        self.saldo = saldo

    def setSaldo(self, saldo):
        self.saldo = saldo
    
    def getSaldo(self):
        return self.saldo
    
    def setValor(self, valor):
        self.valor = valor
        
    def getValor(self):
        return self.valor
    
    def sacar(self, valor:float):
        self.saldo = self.saldo - valor - 0.50
    
    def depositar(self, valor):
        self.saldo = self.saldo + valor
    
    def consultarExtrato(self):
        return self.valor
    
