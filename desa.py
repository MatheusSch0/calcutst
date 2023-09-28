a = ('ola amg seja bem vindo ao nosso restaurante')
print(a)
w = 'agua'
r = 'refrigerante'
v = 'vinho'
print('Temos:', w, r, v)

#########################################

c = input('qual bebida gostaria? ')

if c == w:
  print('okay uma agua', 'e para comer?')

elif c == r:
  print('okay refrigerane', 'e para comer?')

elif c == v:
  print('boa escolha um vinho,', 'e para comer?')

##########################################

m = 'macarronada'
p = 'pizza'
cc = 'camarão'

print ('Pra comer temos:', m, p, 'e', cc)

x = input('qual voce gostaria?')

if x == m:
  print(m,'com',c)

elif x == p:
  print('bom pedido', p, 'e', c)
  
elif c == cc:
  print('boa escolha', cc, "e de bebida", c)

print('sua escolha foi:',x,'com',c)
