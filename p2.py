import pydasm

with open('example.hex', 'r') as file:
	hex_str = file.read()

print hex_str

buffer = str(bytearray.fromhex(hex_str))
start = 0
end = 1
streak = 0
streak_arr = []
while end < len(buffer):
	i = pydasm.get_instruction(buffer[start:end], pydasm.MODE_32)
	print 'hex:', ' '.join([format(c, 'x') for c in bytearray(buffer[start:end])])
	if i.length != end - start:
		print 'OFF TRACK'
		streak += 1
	else:
		print 'instr:', pydasm.get_instruction_string(i, pydasm.FORMAT_INTEL, 0)
		print 'length:', i.length
		start += i.length
		streak_arr.append(streak)
		streak = 0
	if not i:
		print 'BAD'
	print '----'
	end += 1

print 'Largest streak:', max(streak_arr)
print 'Avg streak:', sum(streak_arr)/len(streak_arr)
print 'Num Streaks:', len(streak_arr)
