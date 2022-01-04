import sys

raw_string = sys.stdin.readline().strip()
pkt = bin(int(raw_string,16))
pkt_bitstring = str(pkt)[2:]

init_val = int(raw_string[0], 16)
if init_val >= 8:
  pass
elif init_val >= 4:
  pkt_bitstring = '0' + pkt_bitstring
elif init_val >= 2:
  pkt_bitstring = '00' + pkt_bitstring
elif init_val >= 1:
  pkt_bitstring = '000' + pkt_bitstring

def parse_literal(data):
  idx = 0
  value_str = ''
  while data[idx*5] == '1':
    value_str += data[idx*5+1:idx*5+5]
    idx += 1
  value_str += data[idx*5+1:idx*5+5]
  return idx*5+5, int(value_str, 2)

tot_version_sum = 0
def decode_pkt(bits, values, cur_bits, cur_pkts, max_bits=None, max_pkts=None):
  global tot_version_sum
  if max_bits is not None and cur_bits >= max_bits:
    return cur_bits, cur_pkts, values
  if max_pkts is not None and cur_pkts >= max_pkts:
    return cur_bits, cur_pkts, values
  if len(bits) < 6:
    print("<<<END>>>")
    return cur_bits, cur_pkts, values
  version, type_id = int(bits[:3], 2), int(bits[3:6], 2)
  tot_version_sum += version
  print(f"Pkt header[{bits[:6]}] v{version}: {type_id}")
  data = bits[6:]
  if type_id == 4:
    if len(data) < 5:
      return cur_bits, cur_pkts, values
    num_bits, value = parse_literal(data)
    print(f"  val: {value} | num bits parsed: {num_bits} | remaining: {data[num_bits:]} | bits({cur_bits},{max_bits}) pkts({cur_pkts},{max_pkts})")
    return decode_pkt(data[num_bits:], values + [value], cur_bits+6+num_bits, cur_pkts+1, max_bits=max_bits, max_pkts=max_pkts)
  else:
    if len(data) < 1:
      return cur_bits, cur_pkts, values
    L_bit = data[0]
    print(f"  L: {L_bit}")
    if L_bit == '0':
      if len(data) < 16:
        return cur_bits, cur_pkts, values
      bit_length = int(data[1:16], 2)
      tot_bits, tot_pkts, pkt_values = decode_pkt(data[16:], [], 0, 0, max_bits=bit_length)
      num_bits = 16+tot_bits
      print(f"  opr bits: {num_bits}")
      return decode_pkt(data[num_bits:], values + pkt_values, cur_bits+6+num_bits, cur_pkts+1, max_bits=max_bits, max_pkts=max_pkts)
    else:
      if len(data) < 12:
        return cur_bits, cur_pkts, values
      pkt_length = int(data[1:12], 2)
      tot_bits, tot_pkts, pkt_values = decode_pkt(data[12:], [], 0, 0, max_pkts=pkt_length)
      num_bits = 12+tot_bits
      print(f"  opr bits: {num_bits}")
      return decode_pkt(data[num_bits:], values + pkt_values, cur_bits+6+num_bits, cur_pkts+1, max_bits=max_bits, max_pkts=max_pkts)

parsed_bits, parsed_pkts, parsed_values = decode_pkt(pkt_bitstring, [], 0, 0)
print(tot_version_sum)
