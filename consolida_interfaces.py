import os

INB = os.getenv("INB")
os.chdir(INB)
files200=[]
files600=[]

for i in os.listdir(INB):
    if i.startswith('Registro200'):
        files200.append(i)
    elif i.startswith('Registro600'):
        files600.append(i)

def crea200(l1: list) ->None:
    for line in l1:
        age=line[55:58]
        year=line[33:37]
        with open(f'200_{year}_{age}.txt', "a") as salida:
            salida.writelines(line) 

def crea600(l1:list) ->None:
    for line in l1:
        age=line[29:32]
        year=line[45:49]
        with open(f'600_{year}_{age}.txt', "a") as salida:
            salida.writelines(line) 

def procesa200(l1:list) ->None:
    for i in l1:
        with open(i, 'r') as f:
            inter=f.readlines()
        crea200(inter)

def procesa600(l1:list) ->None:
    for i in l1:
        with open(i, 'r') as f:
            inter=f.readlines()
        crea600(inter)

if __name__ == "__main__":
    procesa200(files200)
    procesa600(files600)
