import pydasm

with open('example.hex', 'r') as file:
	hex_str = file.read()
print '----INPUT----'
print hex_str
print '--END INPUT--'

buffer = str(bytearray.fromhex(hex_str))
start = 0
end = 1
streak = 0
streak_arr = []
print_data = []
while end <= len(buffer):
	i = pydasm.get_instruction(buffer[start:end], pydasm.MODE_32)
	hex_str = ' '.join([format(c, 'x') for c in bytearray(buffer[start:end])])
	if not i:
		print_data.append([hex_str, 'BAD'])
	if i.length != end - start:
		streak += 1
	else:
		print_data.append([hex_str, pydasm.get_instruction_string(i, pydasm.FORMAT_INTEL, 0)])
		#print 'length:', i.length
		start += i.length
		streak_arr.append(streak)
		streak = 0
	end += 1

for row in print_data:
	print("{: <20} {: >30}".format(*row))

#I don't think these are actually relevant to this assignmnet...
#print 'Largest streak:', max(streak_arr)
#print 'Avg streak:', sum(streak_arr)/len(streak_arr)
#print 'Num Streaks:', len(streak_arr)
