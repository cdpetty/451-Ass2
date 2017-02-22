import pydasm

with open('example.hex', 'r') as file:
	hex_str = file.read()

print hex_str

buffer = str(bytearray.fromhex(hex_str))
offset = 0

while offset < len(buffer):
	i = pydasm.get_instruction(buffer[offset:], pydasm.MODE_32)
	print pydasm.get_instruction_string(i, pydasm.FORMAT_INTEL, 0)
	if not i:
    		break
	offset += i.length