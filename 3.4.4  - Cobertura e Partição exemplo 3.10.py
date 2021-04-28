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
x7 = LpVariable(name="x7", lowBound=0, cat="Binary")
x8 = LpVariable(name="x8", lowBound=0, cat="Binary")
x9 = LpVariable(name="x9", lowBound=0, cat="Binary")
x10 = LpVariable(name="x10", lowBound=0, cat="Binary")
x11 = LpVariable(name="x11", lowBound=0, cat="Binary")
x12 = LpVariable(name="x12", lowBound=0, cat="Binary")
x13 = LpVariable(name="x13", lowBound=0, cat="Binary")
x14 = LpVariable(name="x14", lowBound=0, cat="Binary")
x15 = LpVariable(name="x15", lowBound=0, cat="Binary")
x16 = LpVariable(name="x16", lowBound=0, cat="Binary")
x17 = LpVariable(name="x17", lowBound=0, cat="Binary")
x18 = LpVariable(name="x18", lowBound=0, cat="Binary")
x19 = LpVariable(name="x19", lowBound=0, cat="Binary")
x20 = LpVariable(name="x20", lowBound=0, cat="Binary")
x21 = LpVariable(name="x21", lowBound=0, cat="Binary")
x22 = LpVariable(name="x22", lowBound=0, cat="Binary")
x23 = LpVariable(name="x23", lowBound=0, cat="Binary")
x24 = LpVariable(name="x24", lowBound=0, cat="Binary")

#Definição da Função objetivo
obj_func = (20 * x1 + 16 * x2 + 17 * x3 + 18 * x4 + 20 * x5 + 13 * x6 + 14 * x7 + 15 * x8 +
            20 * x9 + 21 * x10 + 31 * x11 + 15 * x12 + 11 * x13 + 43 * x14 + 54 * x15 + 45 * x16 +
            34 * x17 + 23 * x18 + 34 * x19 + 12 * x20 + 34 * x21 + 11 * x22 + 43 * x23 + 12 * x24)

model += obj_func

#Definição das restrições
model += (x1 + x2 + x3 + x4 + x9 +  x11 +x13 + x15 + x17 + x18 + x21 + x22 == 1, "restrição 1")
model += (x5 + x6 + x7 + x8 + x10 + x12 +x14 + x16 + x19 + x20 + x23 + x24 == 1, "restrição 2")
model += (x1 + x2 + x5 + x6 + x9 +  x10 +x11 + x12 + x17 + x19 + x21 + x23 == 1, "restrição 3")
model += (x3 + x4 + x7 + x8 + x13 + x14 +x15 + x16 + x18 + x20 + x22 + x24 == 1, "restrição 4")
model += (x1 + x3 + x5 + x7 + x9 +  x10 +x13 + x14 + x17 + x18 + x19 + x20 == 1, "restrição 5")
model += (x2 + x4 + x6 + x8 + x11 + x12 +x15 + x16 + x21 + x22 + x23 + x24 == 1, "restrição 6")

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
# Valor da Função objetivo:  24.0
# x1 0.0
# x10 0.0
# x11 0.0
# x12 0.0
# x13 1.0
# x14 0.0
# x15 0.0
# x16 0.0
# x17 0.0
# x18 0.0
# x19 0.0
# x2 0.0
# x20 0.0
# x21 0.0
# x22 0.0
# x23 0.0
# x24 0.0
# x3 0.0
# x4 0.0
# x5 0.0
# x6 1.0
# x7 0.0
# x8 0.0
# x9 0.0