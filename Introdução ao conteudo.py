''''#nome
n=input('Qual seu nome ?')
print('Olá,'+n+'. Satisfação aspira.')
idade_input=input('Qual a sua idade?')
idade_numerica=''.join(filter(str.isdigit,idade_input))
idade=int(idade_numerica)
if idade >= 18:
    print("Já pode ser preso babaca")
elif idade >= 15 and idade < 18:
    print('Jovenzinho')
else:
    print("Deu sorte")

#soma
v=int(input("Digite um número:"))
z=int(input("Digite outro número:"))
somar=v+z
print(f'A soma de {v} + {z} equivale a {somar}')

#Calculo IMC
peso=float(input("Digite o seu peso:"))
altura=

#Tabuada
n=float(input("Digite um número de de 1 a 10:"))
if 1 <= n <= 10:
    print(f'A tabuada do {n}')
    for i in range (1,11):
        r=n*i
        print(f'{n} * {i} = {r}')
else:
    print('Leia a porra do enunciado fdp')

#Adivinhe o número
ncerto=8
while(tentativa:=int(input('Chute um número:')))!=ncerto:
    print('Errou babaca')
print('Bem loco')

#Lista
lista=[1,2,3]
lista.append(6)
print(lista[0])

#Dicionario
contatos={'Amaro': '123456', 'Maria': '369741'}
contatos.update({'Amaro': '7410', 'Maria': '0111'})
print(contatos)'''