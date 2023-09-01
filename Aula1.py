# calculo da media 

n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
nome = str(input("Informe seu nome: "))
m = (n1 + n2)/2
if (m>= 60):
    print("Aluno:", nome, "Aprovado! \nSua média foi de", m, "Nota1:", n1, "Nota2:", n2)
else:
    print("Aluno:", nome, "Reprovado! \nSua média foi de", m, "Nota1:", n1, "Nota2:", n2)
    