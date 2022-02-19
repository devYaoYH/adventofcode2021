import sys

seq = list(sys.stdin.readline().strip())
sys.stdin.readline()

seq_pairs = [f'{seq[i-1]}{seq[i]}' for i in range(1,len(seq))]
seq_count = {}
for pair in seq_pairs:
  try:
    seq_count[pair] += 1
  except KeyError:
    seq_count[pair] = 1

substitution = {}
for line in sys.stdin:
  key, ins = line.strip().split(' -> ')
  substitution[key] = ins

for turn in range(40):
  new_seq_count = {}
  for key, count in seq_count.items():
    if key in substitution:
      try:
        new_seq_count[f'{key[0]}{substitution[key]}'] += count
      except KeyError:
        new_seq_count[f'{key[0]}{substitution[key]}'] = count
      try:
        new_seq_count[f'{substitution[key]}{key[1]}'] += count
      except KeyError:
        new_seq_count[f'{substitution[key]}{key[1]}'] = count
    else:
      try:
        new_seq_count[key] += count
      except KeyError:
        new_seq_count[key] = count
  seq_count = new_seq_count

ele_freq = {}
for key, count in seq_count.items():
  try:
    ele_freq[key[0]] += count
  except KeyError:
    ele_freq[key[0]] = count
  try:
    ele_freq[key[1]] += count
  except KeyError:
    ele_freq[key[1]] = count
ele_freq[seq[0]] += 1
ele_freq[seq[-1]] += 1

for key in ele_freq:
  ele_freq[key] //= 2

print(ele_freq)

li = sorted(ele_freq.values())
print(li[-1] - li[0])
