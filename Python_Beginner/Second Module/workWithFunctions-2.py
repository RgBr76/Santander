#Trabalhando com variáveis locais e globais

global_variable = 20

def local_var():
    local_variable = 10
    return print(local_variable)

def global_var():
    return print(global_variable)

global_var()
local_var()
print(global_variable)
# print(local_variable)