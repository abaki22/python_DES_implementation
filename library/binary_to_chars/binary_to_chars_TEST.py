import binary_to_chars

output_1 = binary_to_chars.convert_to_chars('00100100')
output_2 = binary_to_chars.convert_to_chars('1100001010100010')
output_3 = binary_to_chars.convert_to_chars('111011011001010110011100')
output_4 = binary_to_chars.convert_to_chars('11110000100100001000110110001000')
output_5 = binary_to_chars.convert_to_chars('11101101100101011001110011110000100100001000110110001000')

if output_1[0] != '$':
    raise Exception('Expected ' + output_1[0] + ' to be $')

if output_2[0] != '¢':
    raise Exception('Expected ' + output_2[0] + ' to be ¢')

if output_3[0] != "한":
    raise Exception('Expected ' + output_3[0] + ' to be 한')

if output_4[0] != "𐍈":
    raise Exception('Expected ' + output_4[0] + ' to be 𐍈')

if output_5[0] != "한":
    raise Exception('Expected ' + output_5[0] + ' to be 한')

if output_5[1] != "𐍈": 
    raise Exception('Expected ' + output_5[1] + ' to be 𐍈')
