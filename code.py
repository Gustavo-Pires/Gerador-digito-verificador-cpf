
a = (float(input("Digite o primeiro numero ")))
b = (float(input("Digite o segundo numero ")))
c = (float(input("Digite o terceiro numero ")))
d = (float(input("Digite o quarto numero ")))
e = (float(input("Digite o quinto numero ")))
f = (float(input("Digite o sexto numero ")))
g = (float(input("Digite o setimo numero ")))
h = (float(input("Digite o oitavo numero ")))
i = (float(input("Digite o nono numero ")))

#primeiro digito verificador 
j_verificador=(((float(int(a*10)+(b*9)+(c*8)+(d*7)+(e*6)+(f*5)+(g*4)+(h*3)+(i*2))%11)))
if j_verificador <= 1:
    j=0
    j_float= float(j)
elif j_verificador >=2 :
    j=(11 - j_verificador)
    j_float= float(j)

#segundo digito verificador 
k_verificador=(float(int(((a*11)+(b*10)+(c*9)+(d*8)+(e*7)+(f*6)+(g*5)+(h*4)+(i*3)+(j*2))%11)))
if k_verificador <= 1:
    k=0
    k_float= float(k)
elif k_verificador >=2 :
    k=(11-k_verificador)
    k_float= float(k)

a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)
g = int(g)
h = int(h)
i = int(i)
j = int(j)
k = int(k)

print("O digito verificador é " + str(j) + str(k))
print("O CPF com os digitos verificadores é " + str(a) + str(b) + str(c)+ "." + str(d) + str(e) + str(f)+ "." + str(g) + str(h)  + str(i) +"-" + str(j) + str(k))
