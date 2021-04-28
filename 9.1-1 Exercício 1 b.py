#importação da bibliotea pulp
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

#Criação do modelo
model = LpProblem(name="Avaliação de Projetos", sense=LpMaximize)

#Definição das variáveis
x1 = LpVariable(name="x1", lowBound=0, upBound = 1, cat="Binary")
x2 = LpVariable(name="x2", lowBound=0, upBound = 1, cat="Binary")
x3 = LpVariable(name="x3", lowBound=0, upBound = 1, cat="Binary")
x4 = LpVariable(name="x4", lowBound=0, upBound = 1, cat="Binary")
x5 = LpVariable(name="x5", lowBound=0, upBound = 1, cat="Binary")

#Definição da Função objetivo
obj_func = 20 * x1 + 40 * x2 + 20 * x3 + 15 * x4 + 30 * x5
model += obj_func

#Definição das restrições
model += (5 * x1 + 4 * x2 + 3 * x3 + 7 * x4 + 8 * x5 <= 25)
model += (    x1 + 7 * x2 + 9 * x3 + 5 * x4 + 6 * x5 <= 25)
model += (8 * x1 + 10 * x2 + 2 * x3 +   x4 + 10 * x5 <= 25)
model += (8 * x1 + 10 * x2 + 2 * x3 +   x4 + 10 * x5 <= 25)
model += (x2 + x3<=1)

#Executar modelo
status = model.solve()

#Ótimo da função
otimo = model.objective.value()
print("FO = ", otimo)

#Exibir valores das variáveis
for var in model.variables():
    print (var.name, var.value())