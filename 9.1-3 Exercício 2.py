#importação da biblioteca pulp
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize

#Criação do modelo
model = LpProblem(name="Custo das Máquinas", sense=LpMinimize)

#Definição das variáveis
x1 = LpVariable(name="x1", cat="Integer")
x2 = LpVariable(name="x2", cat="Integer")
x3 = LpVariable(name="x3", cat="Integer")
y1 = LpVariable(name="y1", cat="Binary")
y2 = LpVariable(name="y2", cat="Binary")
y3 = LpVariable(name="y3", cat="Binary")

#Definição da Função objetivo
obj_func = 2 * x1 + 10 * x2 + 5 * x3 + 300 * y1 + 100 * y2 + 200 * y3
model += obj_func

#Definição das restrições
model += (x1 + x2 + x3 >= 2000)
model += (x1 - 600 * y1 <= 0)
model += (x2 - 800 * y2 <= 0)
model += (x3 - 1200 * y3 <= 0)
model += (x1 >=500)
model += (x2 >=500)
model += (x3 >=500)

#Executar modelo
status = model.solve()

print("Status da solução:",LpStatus[status])

#Ótimo da função
otimo = model.objective.value()

print("FO:", otimo)

#Exibir valores das variáveis
for var in model.variables():
    print (var.name, var.value())