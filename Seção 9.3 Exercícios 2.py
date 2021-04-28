#importação da bibliotea pulp
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize

#Criação do modelo
model = LpProblem(name="exemplo", sense=LpMinimize)

#Definição das variáveis

x12 = LpVariable(name="Basin x Wald", lowBound=0, cat="Integer")
x13 = LpVariable(name="Basin x Bon", lowBound=0, cat="Integer")
x14=  LpVariable(name="Basin x Mena", lowBound=0, cat="Integer")
x15 = LpVariable(name="Basin x Kiln", lowBound=0, cat="Integer")

x21 = LpVariable(name="Wald x Basin", lowBound=0, cat="Integer")
x23 = LpVariable(name="Wald x Bon", lowBound=0, cat="Integer")
x24=  LpVariable(name="Wald x Mena", lowBound=0, cat="Integer")
x25 = LpVariable(name="Wald x Kiln", lowBound=0, cat="Integer")

x31 = LpVariable(name="Bon x Basin", lowBound=0, cat="Integer")
x32 = LpVariable(name="Bon x Wald", lowBound=0, cat="Integer")
x34=  LpVariable(name="Bon x Mena", lowBound=0, cat="Integer")
x35 = LpVariable(name="Bon x Kiln", lowBound=0, cat="Integer")

x41 = LpVariable(name="Mena x Basin", lowBound=0, cat="Integer")
x42 = LpVariable(name="Mena x Wald", lowBound=0, cat="Integer")
x43 = LpVariable(name="Mena x Bon", lowBound=0, cat="Integer")
x45 = LpVariable(name="Mena x Kiln", lowBound=0, cat="Integer")

x51 = LpVariable(name="Kiln x Basin", lowBound=0, cat="Integer")
x52 = LpVariable(name="Kiln x Wald", lowBound=0, cat="Integer")
x53 = LpVariable(name="Kiln x Bon", lowBound=0, cat="Integer")
x54=  LpVariable(name="Kiln x Mena", lowBound=0, cat="Integer")

#Definição da Função objetivo
obj_func = (  120 * x12 + 220 * x13 + 150 * x14 + 210 * x15
            + 120 * x21 +  80 * x23 + 110 * x24 + 130 * x25
            + 220 * x31 +  80 * x32 + 160 * x34 + 185 * x35
            + 150 * x41 + 110 * x42 + 160 * x43 + 190 * x45
            + 210 * x51 + 130 * x52 + 185 * x53 + 190 * x54)

model += obj_func

#Definição das restrições
model += (x12 + x13 + x14 + x15 == 1, "restrição 1")
model += (x21 + x23 + x24 + x25 == 1, "restrição 2")
model += (x31 + x32 + x34 + x35 == 1, "restrição 3")
model += (x41 + x42 + x43 + x45 == 1, "restrição 4")
model += (x51 + x52 + x53 + x54 == 1, "restrição 5")

model += (x21 + x31 + x41 + x51 == 1, "restrição 6")
model += (x12 + x32 + x42 + x52 == 1, "restrição 7")
model += (x13 + x23 + x43 + x53 == 1, "restrição 8")
model += (x14 + x24 + x34 + x54 == 1, "restrição 9")
model += (x15 + x25 + x35 + x45 == 1, "restrição 10")

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
# Valor da Função objetivo:  695.0
# Basin_x_Mena 1.0
# Mena_x_Basin 1.0
# Bon_x_Kiln 1.0
# Kiln_x_Wald 1.0
# Wald_x_Bon 1.0



