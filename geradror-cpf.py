#-------------------------------------------------GERADOR DE DIGITO VERIFICADOR -------------------------------------------------
a = (float(input("Digite o primeiro numero ")))
b = (float(input("Digite o segundo numero ")))
c = (float(input("Digite o terceiro numero ")))
d = (float(input("Digite o quarto numero ")))
e = (float(input("Digite o quinto numero ")))
f = (float(input("Digite o sexto numero ")))
g = (float(input("Digite o setimo numero ")))
h = (float(input("Digite o oitavo numero ")))
i = (float(input("Digite o nono numero ")))
k_averificar = (float(input("Digite o primeiro digito verificador ")))
j_averificar = (float(input("Digite o segundo digito verificador ")))

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

#primeiro digito verificador 
j_verificador=(int((float((a*10)+(b*9)+(c*8)+(d*7)+(e*6)+(f*5)+(g*4)+(h*3)+(i*2))%11)))
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

#verificar se o digito verificador condiz com o inserido 
verificador = []

#primeiro digito verificador 
if k == j_averificar :
  print("Primeiro digito verificador ok")
  verificador.append(1)
else : 
  print("Primeiro digito verificador esta errado")

#segundo digito verificador 
if j == k_averificar :
  print("Segundo digito verificador ok")
  verificador.append(1)
else : 
  print("Segundo digito verificador esta errado")

if k_averificar and j_averificar == k and j: 
   print("o digito verificador esta correto")
else :
 print("o digito verificador esta errado")

#Verificador estado de origem 


#print("O estado de origem é Rio Grande do Sul")
#print("O estado de origem é Distrito Federal, Goiás, Mato Grosso do Sul ou Tocantins")
#print("O estado de origem é Pará, Amazonas, Acre, Amapá, Rondônia ou Roraima")
#print("O estado de origem é Ceará, Maranhão ou Piau")
#print("O estado de origem é Pernambuco, Rio Grande do Norte, Paraíba ou Alagoas")
#print("O estado de origem é Bahia ou Sergipe")
#print("O estado de origem é Minas Gerais")
#print("O estado de origem é Rio de Janeiro e Espírito Santo")
#print("O estado de origem é São Paulo")
#print("O estado de origem é Paraná e Santa Catarina")

print("O digito verificador é "+str(j) + str(k))
print("O CPF com os digitos verificadores é " + str(a) + str(b) + str(c)+ "." + str(d) + str(e) + str(f)+ "." + str(g) + str(h)  + str(i) +"-" + str(j) + str(k))

#-------------------------------------------------GERADOR DE CPF-------------------------------------------------
import random 

a = (random.randrange(0, 9))
b = (random.randrange(0, 9))
c = (random.randrange(0, 9))
d = (random.randrange(0, 9))
e = (random.randrange(0, 9))
f = (random.randrange(0, 9))
g = (random.randrange(0, 9))
h = (random.randrange(0, 9))
i = (random.randrange(0, 9))
j = (random.randrange(0, 9))
k = (random.randrange(0, 9))

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

print("O digito verificador é "+str(j) + str(k))
print("O CPF com os digitos verificadores é " + str(a) + str(b) + str(c)+ "." + str(d) + str(e) + str(f)+ "." + str(g) + str(h)  + str(i) +"-" + str(j) + str(k))


#---------------------------------------------GERAR CPF EM MASSA E SALVAR EM UMA PLANILHA---------------------------------------------
import xlrd 
import random 


a = (random.randrange(0, 9))
b = (random.randrange(0, 9))
c = (random.randrange(0, 9))
d = (random.randrange(0, 9))
e = (random.randrange(0, 9))
f = (random.randrange(0, 9))
g = (random.randrange(0, 9))
h = (random.randrange(0, 9))
i = (random.randrange(0, 9))
j = (random.randrange(0, 9))
k = (random.randrange(0, 9))

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

cpf=[]
cpf.append(str(a) + str(b) + str(c)+ "." + str(d) + str(e) + str(f)+ "." + str(g) + str(h)  + str(i) +"-" + str(j) + str(k))

#----------Caso utilize excel--------------------------------
#wb=xlrd.open_workbook_xls('C:\\Users\\Usuario\\Desktop\\cpf.xlsx')
#wb=xlrd.open_workbook_xls('cpf.xlsx')
#plan=wb.sheet_by_name('Planilha1')

f=open("cpf.txt","w")
f.write('%a.bf \n' %(cpf) )
f.close()
# (UTILIZAR PARA GERAR O CPF em massa ) for i in range(1, 100):
#    print(i)