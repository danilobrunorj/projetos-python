print('Bem vindo ao quiz do Show de perguntas 2025')
comeco = input('Vamos começar? (S/N) ').lower()

if comeco != "s":
    quit()

acertos = 0
print("Começando o quiz... \n")

print("1- Quem é o atual presidente do Brasil? \n\n (A) Bolsonaro \n (B) Paulo Guedes \n (C) Haddad \n (D) Lula \n" )
resposta1 = input("Resposta: ").lower()
if resposta1 == "d":
    print("Certa resposta!\n")
    acertos += 1
else:
    print("Incorreto!\n")

print("2- Qual time ganhou a libertadores de 2022? \n\n (A) Olimpia \n (B) Flamengo \n (C) Palmeiras \n (D) Boca Júniors \n" )
resposta2 = input("Resposta: ").lower()
if resposta2 == "b":
    print("Certa resposta!\n")
    acertos += 1
else:
    print("Incorreto!\n")

print("3- Qual desses elementos é uma fruta? \n\n (A) Abóbora \n (B) Abacate \n (C) Palmito \n (D) Couve \n" )
resposta3 = input("Resposta: ").lower()
if resposta3 == "b":
    print("Certa resposta!\n")
    acertos += 1
else:
    print("Incorreto!\n")

print("4- Qual desses elementos não é uma fruta? \n\n (A) Ovo \n (B) Banana \n (C) Pêssego \n (D) Maçã \n" )
resposta4 = input("Resposta: ").lower()
if resposta4 == "a":
    print("Certa resposta!\n")
    acertos += 1
else:
    print("Incorreto!\n")

print("5- Qual estação vem depois do outono? \n\n (A) Primavera \n (B) Inverno \n (C) Minguante \n (D) Verão \n" )
resposta5 = input("Resposta: ").lower()
if resposta5 == "b":
    print("Certa resposta!\n")
    acertos += 1
else:
    print("Incorreto!\n")

print("6- Em qual time carioca jogou Garrincha? \n\n (A) Fluminense \n (B) Vasco \n (C) Botafogo \n (D) Flamengo \n" )
resposta6 = input("Resposta: ").lower()
if resposta6 == "c":
    print("Certa resposta!\n")
    acertos += 1
else:
    print("Incorreto!\n")

print(f"Quiz acabou... Você acertou: {acertos}/6")
