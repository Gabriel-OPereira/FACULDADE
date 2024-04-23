from classe import *
import os
os.system('cls')

cc = ContaCorrente('gabriel', 2000)
cp = ContaPoupanca('gabriel123', 4000)

valor = float(input('digite um valor para saque: '))
deposito = float(input('digite um valor para deposito: '))
cc.sacar(valor)
cc.depositar(deposito)
cc.exibirDados()


while True:
    try:
        cc.alterarSenha('gabriel')
        break
    except:
        print('tente novamente ')
        
    
