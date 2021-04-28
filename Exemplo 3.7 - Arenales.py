#importação da biblioteca pulp
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize
#Criação do modelo
model = LpProblem(name="Exemplo 3.7", sense=LpMaximize)

#Definição das variáveis
x1 = LpVariable(name="x1",lowBound=0, cat="Binary")
x2 = LpVariable(name="x2",lowBound=0, cat="Binary")
x3 = LpVariable(name="x3",lowBound=0, cat="Binary")
x4 = LpVariable(name="x4",lowBound=0, cat="Binary")
x5 = LpVariable(name="x5",lowBound=0, cat="Binary")
x6 = LpVariable(name="x6",lowBound=0, cat="Binary")
x7 = LpVariable(name="x7",lowBound=0, cat="Binary")
x8 = LpVariable(name="x8",lowBound=0, cat="Binary")
#Definição da Função objetivo
obj_func = (41 * x1 + 33 * x2 + 14 * x3 + 25 * x4 + 
            32 * x5 + 32 * x6 + 9 * x7 + 19 * x8)
model += obj_func

#Definição das restrições
model += (47 * x1 + 40 * x2 + 17 * x3 + 27 * x4 + 
          34 * x5 + 23 * x6 + 5 * x7 + 44 * x8 <= 100)


# model += (x1 >= 0)
# model += (x2 >> 0)
# model += (x3 >> 0)

#Executar modelo
status = model.solve()

print("Status da solução:",LpStatus[status])

#Ótimo da função
otimo = model.objective.value()

print("FO:", otimo)

#Exibir valores das variáveis
for var in model.variables():
    print (var.name, var.value())
