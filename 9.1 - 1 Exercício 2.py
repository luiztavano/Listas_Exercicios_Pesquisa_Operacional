#importação da bibliotea pulp
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

#Criação do modelo
model = LpProblem(name="small-problem", sense=LpMaximize)

#Definição das variáveis
x1 = LpVariable(name="x1", lowBound=0, cat="Integer")
x2 = LpVariable(name="x2", lowBound=0, cat="Integer")
x3 = LpVariable(name="x3", lowBound=0, cat="Integer")
x4 = LpVariable(name="x4", lowBound=0, cat="Integer")
x5 = LpVariable(name="x5", lowBound=0, cat="Integer")

#Definição da Função objetivo
obj_func = 4 * x1 + 7 * x2 + 6 * x3 + 5 * x4 + 4 * x5
model += obj_func

#Definição das restrições
model += (5 * x1 + 8 * x2 + 3 * x3 + 2 * x4 + 7 * x5 <= 112, "restrição de peso")
model += (1 * x1 + 8 * x2 + 6 * x3 + 5 * x4 + 4 * x5 <= 109, "restrição de volume")


#Executar modelo
status = model.solve()

print("Status da solução:",LpStatus[status])

#Ótimo da função
otimo = model.objective.value()

print("Valor da funçao objetivo:", otimo)

#Exibir valores das variáveis
for var in model.variables():
    print (var.name, var.value())
