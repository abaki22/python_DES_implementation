import file_parser

extracted_text_from_file = file_parser.parse("test_file.txt")

if extracted_text_from_file[2] != "l":
    raise Exception('Expected l, instead ' + extracted_text_from_file[2])

if extracted_text_from_file[23] != "?":
    raise Exception('Expected ?, instead ' + extracted_text_from_file[23])

if extracted_text_from_file[32] != "0":
    raise Exception('Expected 0, instead ' + extracted_text_from_file[32])