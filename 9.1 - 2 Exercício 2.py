#importação da bibliotea pulp
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize

#Criação do modelo
model = LpProblem(name="comitê", sense=LpMinimize)

#Definição das variáveis
a = LpVariable(name="a", cat="Binary")
b = LpVariable(name="b", cat="Binary")
c = LpVariable(name="c", cat="Binary")
d = LpVariable(name="d", cat="Binary")
e = LpVariable(name="e", cat="Binary")
f = LpVariable(name="f", cat="Binary")
g = LpVariable(name="g", cat="Binary")
h = LpVariable(name="h", cat="Binary")
i = LpVariable(name="i", cat="Binary")
j = LpVariable(name="j", cat="Binary")

#Definição da Função objetivo
obj_func = a + b + c + d + e + f + g + h + i + j
model += obj_func

#Definição das restrições
model += (a + b + c + d + e >=1 , "restrição mínimo de mulheres")
model += (f + g + h + i + j >=1 , "restrição mínimo de homens")
model += (a + b + c + j >=1 , "restrição mínimo de estudantes")
model += (e + f >=1 , "restrição mínimo de administradores")
model += (d + g + h + i >=1 , "restrição mínimo de membros da faculdade")

#Executar modelo
status = model.solve()

print("Status da solução:",LpStatus[status])

#Ótimo da função
otimo = model.objective.value()

print("Valor da funçao objetivo:", otimo)

#Exibir valores das variáveis
for var in model.variables():
    print (var.name, var.value())