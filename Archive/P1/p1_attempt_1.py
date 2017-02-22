import pydasm, binascii


def gen_one_byte():
    hex_vals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for val1 in hex_vals:
        for val2 in hex_vals:
            hex_val = bytearray.fromhex(val1 + val2)
            yield str(hex_val)

def gen_str_from_byte(byte):
    return binascii.hexlify(byte)

def main():
    # Check one byte instructions
    for one_byte1 in gen_one_byte():
        instruction = one_byte1
        i = pydasm.get_instruction(instruction, pydasm.MODE_32)
        if not i or i.length > len(instruction):
            print gen_str_from_byte(instruction), 'is INVALID 1 byte instruction.'

    # Check two byte instructions
    for one_byte1 in gen_one_byte():
        for one_byte2 in gen_one_byte():
            instruction = one_byte1 + one_byte2
            i = pydasm.get_instruction(instruction, pydasm.MODE_32)
            if not i or i.length > len(instruction):
                print gen_str_from_byte(instruction), 'is INVALID 2 byte instruction.'
            

    # Check three byte instructions
    for one_byte1 in gen_one_byte():
        for one_byte2 in gen_one_byte():
            for one_byte3 in gen_one_byte():
                instruction = one_byte1 + one_byte2 + one_byte3
                i = pydasm.get_instruction(instruction, pydasm.MODE_32)
                if not i or i.length > len(instruction):
                    print gen_str_from_byte(instruction), 'is INVALID 3 byte instruction.'

    # Check four byte instructions
    for one_byte1 in gen_one_byte():
        for one_byte2 in gen_one_byte():
            for one_byte3 in gen_one_byte():
                for one_byte4 in gen_one_byte():
                    instruction = one_byte1 + one_byte2 + one_byte3 + one_byte4
                    i = pydasm.get_instruction(instruction, pydasm.MODE_32)
                    if not i or i.length > len(instruction):
                        print gen_str_from_byte(instruction), 'is INVALID 4 byte instruction.'

if __name__=='__main__':
    main()

