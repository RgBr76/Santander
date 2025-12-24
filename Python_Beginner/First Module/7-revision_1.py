
registered = ["ana@email.com", "beatriz@email.com", "caio@email.com", "duda@email.com"]
buyers = ["caio@email.com", "duda@email.com", "elias@email.com"]

# print(type(registered))
registered = set(registered)
buyers = set(buyers)

# print(type(registered))

# Difference 
dif = registered - buyers

# Loop to send the personalized message
print(dif)

for email in dif:
    print(f'Enviar cupom para {email}')

# Specific to ana@email.com

if "ana@email.com" in dif:
    print('Enviar cupom para ana@email.com')