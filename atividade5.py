lado1=input("digite o lado do triangulo:")
lado2=input("digite o outro lado do triangulo:")
lado3=input("digite o outro lado do triangulo:")
if lado1==lado2 and lado2==lado3:
  print("o triangulo é equilatero")
elif lado1==lado2 or lado1==lado3 or lado2==lado3:
  print("o triangulo é isosceles")
else:
  print("o triangulo é escaleno")
