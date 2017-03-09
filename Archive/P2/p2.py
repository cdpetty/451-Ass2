import pydasm

with open('example.hex', 'r') as file:
	hex_str = file.read()
print '----INPUT----'
print hex_str
print '--END INPUT--'

def disassemble(hex_str):
	buffer = str(bytearray.fromhex(hex_str))
	start = 0
	end = 1
	print_data = []
	while end <= len(buffer):
		i = pydasm.get_instruction(buffer[start:end], pydasm.MODE_32)
		hex_str = ' '.join([format(c, 'x') for c in bytearray(buffer[start:end])])
		if not i:
			print_data.append([hex_str, 'BAD'])
		if i.length != end - start:
			pass
		else:
			print_data.append([hex_str, pydasm.get_instruction_string(i, pydasm.FORMAT_INTEL, 0)])
			#print 'length:', i.length
			start += i.length
		end += 1

	return print_data

def print_stuff(print_data):
	for row in print_data:
		print("{: <20} {: >30}".format(*row))	

answer_key = disassemble(hex_str)
print_stuff(answer_key)


def is_sublist(master, sub):
	if sub[0] not in master:
		return False

	m = master.index(sub[0])
	return master[m:] == sub


bad_offsets = []
key_offsets = []
offset_range = 16
if len(hex_str)*3 < 16:
	offset_range = len(hex_str)*3

for i in range(offset_range):
	offset_hex = disassemble(hex_str[(i+1)*3:])
	print "----Answer Key----"
	print_stuff(answer_key)
	print "----Subset----"
	print_stuff(offset_hex)

	counter = 0
	while counter < min(len(offset_hex), len(answer_key)) and  not is_sublist(answer_key, offset_hex[counter:]): #offset_hex[counter:] not in answer_key:
		counter += 1

	#The hex was not long enough to correct before reaching the end
	if counter != min(len(offset_hex), len(answer_key)):
		bad_offsets.append(counter)
		key_offset = answer_key.index(offset_hex[counter])
		key_offsets.append(key_offset)
		print "----Match----"
		print_stuff(offset_hex[counter:])
		print 'Key offset', key_offset,'\nSubset offset' , counter
	else:
		print 'Did not correct'

def print_stats_row(name, data):
	avg = sum(data) / len(data)
	data_range = max(data) - min(data)
	print name, '\t', avg, '\t', data_range, '\t', max(data), '\t', min(data)

if len(bad_offsets):
	print '----Correction Time----\n \tAvg\tRange\tMax\tMin'
	print_stats_row('Key', key_offsets)
	print_stats_row('Sub', bad_offsets)
else:
	print 'Input hex too short'