#importação da bibliotea pulp
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize
import pandas as pd

#Definição dos parâmetros
#qtde. de clientes
j = 20

#qtde. de locais
i = 5

#demanda dos clientes j
q = [716, 181, 182, 567, 125, 330, 153, 234, 117, 510,
     928, 541, 148, 291, 360, 434, 148, 560, 321, 583]

#custo de atender uma demanda q a partir de uma falicidade instalada no local i
c = pd.read_excel("C:/Users/DBI5/Documents/Pesquisa Operacional/base.xlsx")

#custo fixo de instalação de uma falicidade no local i
f = [50201, 44208, 58800, 51130, 4940]

#capacidade da facilidade instalada no local i
Q = [1324, 1975, 1506, 1938, 2010]


#Criação do modelo
model = LpProblem(name="3.5.2", sense=LpMinimize)

#Definição das variáveis
x = LpVariable.dicts("x",(range(i), range(j)), cat='Binary')
y = LpVariable.dicts("y",(range(i)), cat='Binary')


#Definição da Função objetivo - LF9
obj_func = (lpSum(f[m] * y[m] for m in range(i)) + lpSum(c.iloc[m][n] * x[m][n] for m in range(i) for n in range(j)))
model += obj_func

#Definição das restrições

#LF10
for n in range(j):
    model += (lpSum(x[m][n] for m in range(i)) == 1)
    
#LF8
for m in range(i):
    model += (lpSum(q[n] * x[m][n] for n in range(j)) <= Q[m] * y[m])
    
    
#Executar modelo
status = model.solve()

print("Status: ",LpStatus[status])

#Ótimo da função
otimo = model.objective.value()

print("Valor da Função objetivo: ",otimo)

for var in model.variables():
    if var.value() > 0:
         print (var.name, var.value())