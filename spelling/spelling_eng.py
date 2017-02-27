author = 'Cassio dos Santos Sousa'


def spell_out_english(num):

    if num >= 1000000000000000:
        raise ValueError('Function can only spell out numbers lower than one quadrillion')

    units = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    elevens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

    tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

    hundreds = ['hundred']

    thousands = ['thousand', 'million', 'billion', 'trillion']

    num_string = str(num)

    current_thousand = 0

    return units[num]
