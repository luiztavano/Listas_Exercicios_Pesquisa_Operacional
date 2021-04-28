#importação da bibliotea pulp
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

#Criação do modelo
model = LpProblem(name="exemplo", sense=LpMaximize)

#Definição das variáveis
x1 = LpVariable(name="x1", lowBound=0, cat="Integer")
x2 = LpVariable(name="x2", lowBound=0, cat="Integer")


#Definição da Função objetivo
obj_func = 1 * x1 + 1 * x2
model += obj_func

#Definição das restrições
model += (2 * x1 + 5 * x2 <= 16, "restrição 1")
model += (6 * x1 + 5 * x2 <= 27, "restrição 2")

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
# Valor da Função objetivo:  4.0
# x1 2.0
# x2 2.0