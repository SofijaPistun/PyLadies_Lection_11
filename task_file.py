import argparse

parser = argparse.ArgumentParser(description='Transliteration')
parser.add_argument("-s", "--sentence", type=str, help=("Input your phrase for transliteration"), required=True)
parser.add_argument("input_file", type=str, help=("Input file to read"))
parser.add_argument("output_file", type=str, help=("Input file to write"))

args = parser.parse_args()

def create_dict_for_translit(input_file):
    with open(input_file , encoding='utf-8') as input_file_1:
        content = input_file_1.read()
        list = content.splitlines()
        dict_for_translit = {}
        for row in list:
            dict_for_translit[row[0]] = row[2:]
        return dict_for_translit

    
def transliterate(dict_for_translit, sentence):
    sentence = list(sentence)
    translit_result = ''
    for element in sentence:
        translit_result = translit_result + dict_for_translit[element]
    return translit_result


def save_in_file(output_file, result):
    with open(output_file, mode='w', encoding='utf-8') as output_file:
        output_file.write(result)

dict_for_translit = create_dict_for_translit(args.input_file)
translit_result = transliterate(dict_for_translit, args.sentence)
save_in_file(args.output_file, translit_result)

print(translit_result)
