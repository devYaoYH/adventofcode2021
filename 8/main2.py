import sys

ans = 0
uniques = set([2,3,4,7])
for line in sys.stdin:
  digit_map = {}
  samples, out = line.strip().split('|')
  query = list(map(lambda x: ''.join(sorted(x)),out.split()))
  segments = list(map(lambda x: ''.join(sorted(x)),samples.split()))
  segments_len = list(map(len,segments))
  len_5 = []
  len_6 = []
  for l, seg in zip(segments_len, segments):
    if l == 2: # 1
      digit_map[1] = seg
    elif l == 3: # 7
      digit_map[7] = seg
    elif l == 4: # 4
      digit_map[4] = seg
    elif l == 7: # 8
      digit_map[8] = seg
    elif l == 5:
      len_5.append(seg)
    elif l == 6:
      len_6.append(seg)
  set1 = set(digit_map[1])
  set4 = set(digit_map[4])
  setL = set4 - set1
  # Unmask (5)
  for seg in len_5:
    segSet = set(seg)
    if len(segSet & set1) == 2:
      digit_map[3] = seg
    elif len(segSet & setL) == 2:
      digit_map[5] = seg
    else:
      digit_map[2] = seg
  # Unmask (6)
  for seg in len_6:
    segSet = set(seg)
    if len(segSet & set4) == 4:
      digit_map[9] = seg
    elif len(segSet & setL) == 2:
      digit_map[6] = seg
    else:
      digit_map[0] = seg
  # Decode
  rev_map = {s: d for d, s in digit_map.items()}
  output = ''
  for o in query:
    output += str(rev_map[o])
  ans += int(output)
print(ans)
