import sys

if len(sys.argv) != 4:
   print("Usage: calc.py <a> <op> <b>")
   sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])
op = sys.argv[2]

if op == "+":
   print(a+b)
elif op == "-":
     print(a - b);
elif op == "*":
     print(a*b)
elif op == "/" :
  if b == 0:
     print("Error: division by zero")
  else :
     print(a/b)
elif op == "//" :
  if b == 0:
     print("Error: division by zero")
  else :
     print(a // b);
elif op == "%":
  if b == 0:
     print("Error: division by zero")
  else :
     print(a % b)
elif op == "**":
     print(a ** b)
