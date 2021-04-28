#importação da bibliotea pulp
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize

#Criação do modelo
model = LpProblem(name="Problema_desginação", sense=LpMinimize)

#Definição das variáveis
x11 = LpVariable(name="x11", lowBound = 0, cat="Binary")
x12 = LpVariable(name="x12", lowBound = 0, cat="Binary")
x13 = LpVariable(name="x13", lowBound = 0, cat="Binary")
x14 = LpVariable(name="x14", lowBound = 0, cat="Binary")
x15 = LpVariable(name="x15", lowBound = 0, cat="Binary")
x16 = LpVariable(name="x16", lowBound = 0, cat="Binary")
x17 = LpVariable(name="x17", lowBound = 0, cat="Binary")
x18 = LpVariable(name="x18", lowBound = 0, cat="Binary")

x21 = LpVariable(name="x21", lowBound = 0, cat="Binary")
x22 = LpVariable(name="x22", lowBound = 0, cat="Binary")
x23 = LpVariable(name="x23", lowBound = 0, cat="Binary")
x24 = LpVariable(name="x24", lowBound = 0, cat="Binary")
x25 = LpVariable(name="x25", lowBound = 0, cat="Binary")
x26 = LpVariable(name="x26", lowBound = 0, cat="Binary")
x27 = LpVariable(name="x27", lowBound = 0, cat="Binary")
x28 = LpVariable(name="x28", lowBound = 0, cat="Binary")

x31 = LpVariable(name="x31", lowBound = 0, cat="Binary")
x32 = LpVariable(name="x32", lowBound = 0, cat="Binary")
x33 = LpVariable(name="x33", lowBound = 0, cat="Binary")
x34 = LpVariable(name="x34", lowBound = 0, cat="Binary")
x35 = LpVariable(name="x35", lowBound = 0, cat="Binary")
x36 = LpVariable(name="x36", lowBound = 0, cat="Binary")
x37 = LpVariable(name="x37", lowBound = 0, cat="Binary")
x38 = LpVariable(name="x38", lowBound = 0, cat="Binary")

#Definição da Função objetivo

obj_func = (  15 * x11 + 61 * x12 +  3 * x13 + 94 * x14 + 86 * x15 + 68 * x16 + 69 * x17 + 51 * x18
            + 21 * x21 + 28 * x22 + 76 * x23 + 48 * x24 + 54 * x25 + 85 * x26 + 39 * x27 + 72 * x28
            + 21 * x31 + 21 * x32 + 46 * x33 + 43 * x34 + 21 * x35 +  3 * x36 + 84 * x37 + 44 * x38)

model += obj_func

#Definição das restrições
model += (31 * x11 + 69 * x12 + 14 * x13 + 87 * x14 + 51 * x15 + 65 * x16 + 35 * x17 + 54 * x18 <= 100)
model += (23 * x21 + 20 * x22 + 71 * x23 + 86 * x24 + 91 * x25 + 57 * x26 + 30 * x27 + 74 * x28 <= 100)
model += (20 * x31 + 55 * x32 + 39 * x33 + 60 * x34 + 83 * x35 + 67 * x36 + 35 * x37 + 32 * x38 <= 100)

model += (x11 + x21 + x31 == 1)
model += (x12 + x22 + x32 == 1)
model += (x13 + x23 + x33 == 1)
model += (x14 + x24 + x34 == 1)
model += (x15 + x25 + x35 == 1)
model += (x16 + x26 + x36 == 1)
model += (x17 + x27 + x37 == 1)
model += (x18 + x28 + x38 == 1)

#Executar modelo
status = model.solve()

print("Status da solução:",LpStatus[status])

#Ótimo da função
otimo = model.objective.value()

print("Valor da funçao objetivo:", otimo)


#Exibir valores das variáveis
for var in model.variables():
    if var.value() > 0:
        print (var.name, var.value())

# Status da solução: Optimal
# Valor da funçao objetivo: 379.0
# x13 1.0
# x15 1.0
# x17 1.0
# x21 1.0
# x22 1.0
# x26 1.0
# x34 1.0
# x38 1.0

