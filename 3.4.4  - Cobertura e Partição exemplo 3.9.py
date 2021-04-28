#importação da bibliotea pulp
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize

#Criação do modelo
model = LpProblem(name="exemplo", sense=LpMinimize)

#Definição das variáveis
x1 = LpVariable(name="x1", lowBound=0, cat="Binary")
x2 = LpVariable(name="x2", lowBound=0, cat="Binary")
x3 = LpVariable(name="x3", lowBound=0, cat="Binary")
x4 = LpVariable(name="x4", lowBound=0, cat="Binary")
x5 = LpVariable(name="x5", lowBound=0, cat="Binary")
x6 = LpVariable(name="x6", lowBound=0, cat="Binary")

#Definição da Função objetivo
obj_func = 20 * x1 + 76 * x2 + 16 * x3 + 23 * x4 + 23 * x5 + 18 * x6
model += obj_func

#Definição das restrições
model += (x1 + x2 + x5 >= 1, "restrição 1")
model += (x1 + x3 >= 1, "restrição 2")
model += (x2 + x4 >= 1, "restrição 3")
model += (x3 + x6 >= 1, "restrição 4")
model += (x2 + x3 + x6 >= 1, "restrição 5")


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
# Valor da Função objetivo:  59.0
# x1 1.0
# x2 0.0
# x3 1.0
# x4 1.0
# x5 0.0
# x6 0.0