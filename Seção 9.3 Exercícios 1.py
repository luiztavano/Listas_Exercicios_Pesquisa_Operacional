#importação da bibliotea pulp
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize

#Criação do modelo
model = LpProblem(name="Chamadas_telefonicas", sense=LpMinimize)

#Definição das variáveis
x12 = LpVariable(name="x12", lowBound = 0, cat="Binary")
x14 = LpVariable(name="x14", lowBound = 0, cat="Binary")
x15 = LpVariable(name="x15", lowBound = 0, cat="Binary")

x21 = LpVariable(name="x21", lowBound = 0, cat="Binary")
x23 = LpVariable(name="x23", lowBound = 0, cat="Binary")
x25 = LpVariable(name="x25", lowBound = 0, cat="Binary")

x32 = LpVariable(name="x32", lowBound = 0, cat="Binary")
x33 = LpVariable(name="x33", lowBound = 0, cat="Binary")
x34 = LpVariable(name="x34", lowBound = 0, cat="Binary")
x36 = LpVariable(name="x36", lowBound = 0, cat="Binary")

x43 = LpVariable(name="x43", lowBound = 0, cat="Binary")
x44 = LpVariable(name="x44", lowBound = 0, cat="Binary")
x45 = LpVariable(name="x45", lowBound = 0, cat="Binary")

x51 = LpVariable(name="x51", lowBound = 0, cat="Binary")
x52 = LpVariable(name="x52", lowBound = 0, cat="Binary")
x53 = LpVariable(name="x53", lowBound = 0, cat="Binary")

x61 = LpVariable(name="x61", lowBound = 0, cat="Binary")
x62 = LpVariable(name="x62", lowBound = 0, cat="Binary")
x63 = LpVariable(name="x63", lowBound = 0, cat="Binary")
x64 = LpVariable(name="x64", lowBound = 0, cat="Binary")
x66 = LpVariable(name="x66", lowBound = 0, cat="Binary")

x71 = LpVariable(name="x71", lowBound = 0, cat="Binary")
x72 = LpVariable(name="x72", lowBound = 0, cat="Binary")
x75 = LpVariable(name="x75", lowBound = 0, cat="Binary")
x76 = LpVariable(name="x76", lowBound = 0, cat="Binary")

x81 = LpVariable(name="x81", lowBound = 0, cat="Binary")
x83 = LpVariable(name="x83", lowBound = 0, cat="Binary")
x84 = LpVariable(name="x84", lowBound = 0, cat="Binary")

x95 = LpVariable(name="x95", lowBound = 0, cat="Binary")
x96 = LpVariable(name="x96", lowBound = 0, cat="Binary")

x101 = LpVariable(name="x101", lowBound = 0, cat="Binary")
x102 = LpVariable(name="x102", lowBound = 0, cat="Binary")
x104 = LpVariable(name="x104", lowBound = 0, cat="Binary")
x105 = LpVariable(name="x105", lowBound = 0, cat="Binary")
x106 = LpVariable(name="x106", lowBound = 0, cat="Binary")


#Definição da Função objetivo

obj_func = 20*(x12 + x14 + x15 + x21 + x23 + x25
               + x32 + x33 + x34 + x36 + x43 + x44 + x45
               + x51 + x52 + x53 + x61 + x62 + x63 + x64 + x66
               + x71 + x72 + x75 + x76 + x81 + x83 + x84
               + x95 + x96 + x101 + x102 + x104 + x105 + x106)

model += obj_func

#Definição das restrições
model += (x12 + x14 + x15 >= 1)
model += (x21 + x23 + x25 >= 1)
model += (x32 + x33 + x34 + x36 >= 1)
model += (x43 + x44 + x45 >= 1)
model += (x51 + x52 + x53 >= 1)
model += (x61 + x62 + x63 + x64 + x66 >= 1)
model += (x71 + x72 + x75 + x76 >= 1)
model += (x81 + x83 + x84 >= 1)
model += (x95 + x96 >= 1)
model += (x101 + x102 + x104 + x105 + x106 >= 1)

# model += (x21 + x51 + x61 + x71 + x81 + x101 == 1)
# model += (x12 + x32 + x52 + x62 + x72 + x102 == 1)
# model += (x23 + x33 + x43 + x53 + x63 + x83 == 1)
# model += (x14 + x34 + x44 + x64 + x84 + x104 == 1)
# model += (x15 + x25 + x45 + x75 + x95 + x105 == 1)
# model += (x36 + x66 + x76 + x96 + x106 == 1)

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
# Valor da funçao objetivo: 200.0
# x106 1.0
# x15 1.0
# x25 1.0
# x36 1.0
# x45 1.0
# x51 1.0
# x66 1.0
# x76 1.0
# x84 1.0
# x96 1.0

