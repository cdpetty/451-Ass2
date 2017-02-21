import pydasm

buffer = '\x0F\x08\x8F\x00\x5D\xDE'

offset = 0
while offset < len(buffer):
   i = pydasm.get_instruction(buffer[offset:], pydasm.MODE_32)
   if i.type == 107:
   	print('invalid')
   else:
   	print pydasm.get_instruction_string(i, pydasm.FORMAT_INTEL, 0)
   if not i:
     break
   offset += i.length