import pydasm

with open('example.hex', 'r') as file:
	hex_str = file.read()

print hex_str

buffer = str(bytearray.fromhex(hex_str))
start = 0
end = 1
while end < len(buffer):
	i = pydasm.get_instruction(buffer[start:end], pydasm.MODE_32)
	print 'instr:', pydasm.get_instruction_string(i, pydasm.FORMAT_INTEL, 0)
	print 'hex:', ' '.join([format(c, 'x') for c in bytearray(buffer[start:end])])
	print 'length:', i.length
	print '----'
	start += 1
	if not i:
		print 'test'
		break
	end += i.length
