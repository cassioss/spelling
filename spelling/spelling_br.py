# coding=utf-8

author = 'Cassio dos Santos Sousa'


def spell_out_english(num):

    if num >= 1000000000000000:
        raise ValueError('Function can only spell out numbers lower than one quadrillion')

    units = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']

    elevens = ['onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove']

    tens = ['dez', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']

    hundreds = ['cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos', 'setecentos', 'oitocentos', 'novecentos']

    thousands = ['thousand', 'million', 'billion', 'trillion']

    num_string = str(num)

    current_thousand = 0

    return units[num]
