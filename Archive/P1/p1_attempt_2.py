import pydasm, binascii


def gen_one_byte():
    hex_vals = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for val1 in hex_vals:
        for val2 in hex_vals:
            hex_val = bytearray.fromhex(val1 + val2)
            yield str(hex_val)

def gen_str_from_byte(byte):
    return binascii.hexlify(byte)


def check_validity(byte):
    for one_byte1 in gen_one_byte():
        instruction = byte + one_byte1
        i = pydasm.get_instruction(instruction, pydasm.MODE_32)
        if not i or i.length > len(instruction):
            print gen_str_from_byte(instruction), 'is INVALID of length', len(instruction)
            if len(instruction) <= 4:
                pass
                check_validity(instruction)

def main():
    check_validity('')
     

if __name__=='__main__':
    main()

