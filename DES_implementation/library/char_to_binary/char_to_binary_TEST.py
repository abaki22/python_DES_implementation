import char_to_binary

output_1 = char_to_binary.convert_to_binary('$')
output_2 = char_to_binary.convert_to_binary('¢')
output_3 = char_to_binary.convert_to_binary('한')
output_4 = char_to_binary.convert_to_binary('𐍈')

if output_1 != '00100100':
    raise Exception('Expected ' + output_1 + ' to be 00100100')

if output_2 != '1100001010100010':
    raise Exception('Expected ' + output_2 + ' to be 1100001010100010')

if output_3 != "111011011001010110011100":
    raise Exception('Expected ' + output_3 + ' to be 111011011001010110011100')

if output_4 != "11110000100100001000110110001000":
    raise Exception('Expected ' + output_4 + ' to be 11110000100100001000110110001000')