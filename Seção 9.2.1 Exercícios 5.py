#importação da bibliotea pulp
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize

#Criação do modelo
model = LpProblem(name="exemplo", sense=LpMaximize)

#Definição das variáveis
x1 = LpVariable(name="x1", lowBound=0, cat="Binary")
x2 = LpVariable(name="x2", lowBound=0, cat="Binary")
x3 = LpVariable(name="x3", lowBound=0, cat="Binary")
x4 = LpVariable(name="x4", lowBound=0, cat="Binary")
x5 = LpVariable(name="x5", lowBound=0, cat="Binary")

#Definição da Função objetivo
obj_func = (18 * x1 + 14 * x2 + 8 * x3 + 4 * x4)
model += obj_func

#Definição das restrições
model += (15 * x1 + 12 * x2 + 7 * x3 + 4 * x4 + x5 <= 37, "restrição 1")

#Executar modelo
status = model.solve()

print("Status: ",LpStatus[status])

#Ótimo da função
otimo = model.objective.value()

print("Valor da Função objetivo: ",otimo)

#Exibir valores das variáveis
for var in model.variables():
    print (var.name, var.value())

# Status:  Optimal
# Valor da Função objetivo:  40.0
# x1 1.0
# x2 1.0
# x3 1.0
# x4 0.0
# x5 0.0