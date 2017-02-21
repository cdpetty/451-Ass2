import pydasm

buffer = '\x0F\x08\x8F\x00\x5D\xDE'

offset = 0
while offset < len(buffer):
   i = pydasm.get_instruction(buffer[offset:], pydasm.MODE_32)
   print vars(i)
   if i.type == 107:
   	print('invalid')
   else:
   	print pydasm.get_instruction_string(i, pydasm.FORMAT_INTEL, 0)
   if not i:
     break
   offset += i.length

print '--------------------------------'
print '--------------------------------'
print '--------------------------------'
print '--------------------------------'
i = pydasm.get_instruction('\x0F', pydasm.MODE_32)
print vars(i)


def gen_two_bytes():
    hex_vals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for val1 in hex_vals:
        for val2 in hex_vals:
            yield '\\x' + val1 + val2

def main():
    for two_bytes in gen_two_bytes():
        i = pydasm.get_instruction(two_bytes, pydasm.MODE_32)
        if i:
            print two_bytes, i.length
        else:
            print two_bytes, 'INVALID'

     

if __name__=='__main__':
    main()
