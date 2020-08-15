# lê valores, separa, coloca cada um em uma var
valores = input()
v = valores.split()
x,y = float(v[0]),float(v[1])
print(f'x={x}, y={y}')

# define localização dos quadrantes
if x > 0 and y > 0:
  print('Q1')
elif x < 0 and y > 0:
  print('Q2')
elif x < 0 and y < 0:
  print('Q3')
elif x > 0 and y < 0:
  print('Q4')
elif x == 0 and y == 0:
  print('Origem')
elif x == 0 and (y != 0):
  print('Eixo Y')
elif y == 0 and (x != 0):
  print('Eixo X')