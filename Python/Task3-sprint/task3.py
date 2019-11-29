def dict_squares(n):
  d=dict()
  for x in range(1,n):
    d[x]=x**2
  return d

print(dict_squares(8))
