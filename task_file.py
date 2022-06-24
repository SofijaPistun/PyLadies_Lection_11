import argparse

parser = argparse.ArgumentParser(description='Transliteration from Ukrainian letters to Latin letters')
parser.add_argument("input_file", type=str, help=("Input file to read"))
parser.add_argument("output_file", type=str, help=("Input file to write"))
parser.add_argument("-s", "--sentence", type=str, help=("Input your phrase for transliteration in quotation marks"), required=True)

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
    wrong_input_indicator = False
    for element in sentence:
        if element in dict_for_translit.keys():            
            translit_result = translit_result + dict_for_translit[element]
        elif element == ' ' or element == ',' or element == '.' or element == '!' or element == '?' or element == '-':
            translit_result = translit_result + element
        else:
            translit_result = translit_result + element
            wrong_input_indicator = True
    if wrong_input_indicator:        
        print('\nThe whole phrase or some of its parts were not entered in the letters of the Ukrainian alphabet. These parts remained unchanged.')
    return translit_result


def save_in_file(output_file, result):
    with open(output_file, mode='w', encoding='utf-8') as output_file:
        output_file.write(result)

dict_for_translit = create_dict_for_translit(args.input_file)
translit_result = transliterate(dict_for_translit, args.sentence)
save_in_file(args.output_file, translit_result)

print('Transliterated phrase: ', translit_result, '\n')
