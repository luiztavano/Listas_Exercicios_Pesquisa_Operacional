#importação da biblioteca pulp
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable
#Criação do modelo
model = LpProblem(name="Gapco localizações", sense=LpMaximize)

#Definição das variáveis
x1 = LpVariable(name="x1",lowBound=0, cat="Integer")
x2 = LpVariable(name="x2",lowBound=0, cat="Integer")
x3 = LpVariable(name="x3",lowBound=0, cat="Integer")
y = LpVariable(name="y", lowBound=0, upBound = 1, cat="Binary")
M = 1000    

#Definição da Função objetivo
obj_func = 25 * x1 + 30 * x2 + 22 * x3
model += obj_func

#Definição das restrições
model += (3* x1 + 4* x2 + 5* x3 <= 100 + M * y)
model += (4* x1 + 3* x2 + 6* x3 <= 100 + M * y)
model += (3* x1 + 4* x2 + 5* x3 <= 90 + M * (1-y))
model += (4* x1 + 3* x2 + 6* x3 <= 120 + M * (1-y))

#Executar modelo
status = model.solve()

print("Status da solução:",LpStatus[status])

#Ótimo da função
otimo = model.objective.value()

print("FO:", otimo)

#Exibir valores das variáveis
for var in model.variables():
    print (var.name, var.value())