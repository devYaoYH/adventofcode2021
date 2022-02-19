import sys

def filterO2(idx, diag):
  n_diag = [[], []]
  for l in diag:
    n_diag[int(l[idx])].append(l)
  if (len(n_diag[0]) > len(n_diag[1])):
    o2, co2 = n_diag
  else:
    co2, o2 = n_diag
  if (len(o2) == 1):
    return int(''.join(o2[0]), 2)
  else:
    return filterO2(idx+1, o2)

def filterCo2(idx, diag):
  n_diag = [[], []]
  for l in diag:
    n_diag[int(l[idx])].append(l)
  if (len(n_diag[0]) > len(n_diag[1])):
    o2, co2 = n_diag
  else:
    co2, o2 = n_diag
  if (len(co2) == 1):
    return int(''.join(co2[0]), 2)
  else:
    return filterCo2(idx+1, co2)

def filterDiag(diag):
  n_diag = [[], []]
  for l in diag:
    n_diag[int(l[0])].append(l)
  if (len(n_diag[0]) > len(n_diag[1])):
    o2, co2 = n_diag
  else:
    co2, o2 = n_diag
  if (len(o2) == 1 and len(co2) == 1):
    return int(''.join(o2[0]), 2)*int(''.join(co2[0]), 2)
  elif (len(o2) == 1):
    return int(''.join(o2[0]), 2)*filterCo2(1, co2)
  elif (len(co2) == 1):
    return filterO2(1, o2)*int(''.join(co2[0]), 2)
  else:
    return filterO2(1, o2)*filterCo2(1, co2)

diag = []
for line in sys.stdin:
  diag.append(list(line.strip()))

print(filterDiag(diag))
