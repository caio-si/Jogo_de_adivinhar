import random as rd
num = int(input('Informe um numero\t'))
qlqr =  rd.randint(1,10)
tentantiva = 1
if qlqr != num:
  while qlqr != num:
    print('Numero errado')
    num = int(input('Informe um numero\t'))
    tentantiva = tentantiva + 1
print(f'Numero certo, o numero sorteado foi {qlqr}')
print()
print(f'O Numero de tentativas foi {tentantiva}')