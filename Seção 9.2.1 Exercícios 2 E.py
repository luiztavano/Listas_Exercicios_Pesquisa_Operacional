#importação da bibliotea pulp
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize

#Criação do modelo
model = LpProblem(name="exemplo", sense=LpMaximize)

#Definição das variáveis
x1 = LpVariable(name="x1", lowBound=0, cat="Integer")
x2 = LpVariable(name="x2", lowBound=0, cat="Integer")

#Definição da Função objetivo
obj_func = 5 * x1 + 7 * x2
model += obj_func

#Definição das restrições
model += (2 * x1 + 1 * x2 <= 13, "restrição 1")
model += (5 * x1 + 9 * x2 <= 41, "restrição 2")

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
# Valor da Função objetivo:  37.0
# x1 6.0
# x2 1.0
