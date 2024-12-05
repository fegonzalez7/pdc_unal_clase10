
def ordenarDosNums(b,c):
  if b <= c:
    m2, m3 = b, c
  else:
    m2, m3 = c, b
  return m2, m3

def ordenarTresNums(a,b,c):
  m1 , m2, m3 = a, b, c
  if a <= b and a <= c:
    m1 = a
    m2, m3 = ordenarDosNums(b,c)
  elif b <= a and b <= c:
    m1 = b
    m2, m3 = ordenarDosNums(a,c)
  elif c <= b and c <= a:
    m1 = c
    m2, m3 = ordenarDosNums(b,a)
  return m1, m2, m3

def ordenarCuatroNums(a,b,c,d):
  m1, m2, m3, m4 = a, b, c, d
  if a <= b and a <= c and a<=d: 
    m1 = a
    m2, m3, m4= ordenarTresNums(b,c,d)
  elif b <= a and b <= c and b <= d:
    m1 = b
    m2, m3, m4 = ordenarTresNums(a,c,d)
  elif c <= b and c <= a and c <= d:
    m1 = c
    m2, m3, m4 = ordenarTresNums(b,a,d)
  elif d <= a and d <= b and d <= c:
    m1 = d
    m2, m3, m4 = ordenarTresNums(a,b,c)
  return m1, m2, m3, m4

if __name__ == "__main__":
  a = float(input("num 1: "))
  b = float(input("num 2: "))
  c = float(input("num 3: "))
  d = float(input("num 4: "))
  m1, m2, m3, m4 = ordenarCuatroNums(a,b,c,d)
  print(str(a) + " " + str(b) + " " + str(c) + " " + str(d))
  print(str(m1) + " " + str(m2) + " " + str(m3)+ " " + str(m4))
