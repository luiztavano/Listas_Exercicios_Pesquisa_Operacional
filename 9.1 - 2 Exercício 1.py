##Não consegui terminar esse exercício##

#importação da bibliotea pulp
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable, LpMinimize

#Criação do modelo
model = LpProblem(name="rotas de entrega", sense=LpMinimize)

#Definição das variáveis
x1 = LpVariable(name="x1", cat="Binary")
x2 = LpVariable(name="x2", cat="Binary")
x3 = LpVariable(name="x3", cat="Binary")
x4 = LpVariable(name="x4", cat="Binary")
x5 = LpVariable(name="x5", cat="Binary")
x6 = LpVariable(name="x6", cat="Binary")

rota1 = 10 + 32 + 14 + 15
rota2 = 9 + 15 + 18
rota3 = 10 + 32 + 20
rota4 = 12 + 14 + 18
rota5 = 10 + 17 + 21
rota6 = 10 + 8 + 18


#Definição da Função objetivo
obj_func = rota1 * x1 + rota2 * x2 + rota3 * x3 + rota4 * x4 + rota5 * x5 + rota6 * x6
model += obj_func

# #Definição das restrições
# model += (5 * x1 + 8 * x2 + 3 * x3 + 2 * x4 + 7 * x5 <= 112, "restrição de peso")
# model += (1 * x1 + 8 * x2 + 6 * x3 + 5 * x4 + 4 * x5 <= 109, "restrição de volume")


#Executar modelo
status = model.solve()

print("Status da solução:",LpStatus[status])

#Ótimo da função
otimo = model.objective.value()

print("Valor da funçao objetivo:", otimo)

#Exibir valores das variáveis
for var in model.variables():
    print (var.name, var.value())