#importação da bibliotea pulp
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize
import pandas as pd

#Definição dos parâmetros
#qtde. de clientes
#Número de períodos no horizonte de planejamento
T = 4

#número de itens finais
n = 3

#estoque inicial do item i
lo = 0

#número de itens i
i = 3

#Números o item i necessário para produzir um item j
R = 3

#tempo de preparação de máquina para processar o item i
sp = [40,40,40]

#custo unitário de estoque do item i
h = [150, 100, 70]

#Conjunto de sucessores imediatos do item i
s = [350, 100, 90]

#Capacidade de produção em horas de uma máquina ou instalação no período t
C = [280, 320, 280, 400]

#tempo para produzir uma unidade do item i
b = [20, 10, 20]

#demanda independente do item i no período t
D = [[1, 10, 3, 10],
     [2, 4, 0, 5],
     [2, 4, 0, 5]]
     
#Criação do modelo
model = LpProblem(name="3.6.1", sense=LpMinimize)

#Definição das variáveis
x = LpVariable.dicts("x",(range(i), range(T)), cat='Continuous')
l = LpVariable.dicts("l",(range(i), range(T)), cat='Continuous')
y = LpVariable.dicts("y",(range(i), range(T)), cat='Binary')

#Definição da Função objetivo - DL14
obj_func = lpSum(s[i] * y[i][t] + h[i] * l[i][t] for i in range(n) for t in range(T))
model += obj_func

#Definição das restrições

#DL15
for n in range(j):
    model += (l[i][t] == lpSum(x[m][n] for m in range(i)) == 1)
    
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