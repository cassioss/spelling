author = 'Cassio dos Santos Sousa'


class EnglishSpeller:

    def __init__(self):
        self.units = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten',
                      'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
                      'eighteen', 'nineteen']

        self.tens = [None, None, 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

        self.hundreds = ['hundred']

        self.thousands = ['thousand', 'million', 'billion', 'trillion']

        self.MAX_NUMBER = 1000000000000000

        self.MAX_NUMBER_SPELLED = 'one quadrillion'

    def spell_hundred(self, num):  # From 0 to 999
        if num == 0:
            return ''

        hundred = None
        ten = None

        if num >= 100:
            hundred_digit = num / 100
            hundred = self.units[hundred_digit] + ' ' + self.hundreds[0]
            num %= 100

        if num > 0:
            if num < 20:
                ten = self.units[num]

            else:
                ten = self.tens[num / 10] + ('' if num % 10 == 0 else '-' + self.units[num % 10])

        if hundred is None:
            return ten

        elif ten is None:
            return hundred

        return hundred + ' ' + ten

    @staticmethod
    def num_from_last_three_digits(num_str):
        last_three = num_str[-3:].lstrip('0')
        if last_three == '':
            last_three = '0'

        return int(last_three)

    def spell_out(self, num):

        if num >= self.MAX_NUMBER:
            raise ValueError('Function can only spell out numbers lower than ' + self.MAX_NUMBER_SPELLED)

        if num < 20:
            return self.units[num]

        num_str = str(num)
        current_thousand = None
        final_number = []

        while num_str is not None:
            three_digit_num = self.num_from_last_three_digits(num_str)
            spelled_out = self.spell_hundred(three_digit_num)

            if current_thousand is None:
                current_thousand = 0
                final_number.insert(0, spelled_out)

            else:
                if spelled_out != '':
                    termination = self.thousands[current_thousand]
                    final_number.insert(0, ' '.join([spelled_out, termination]))

                current_thousand += 1

            num_str = None if len(num_str) <= 3 else num_str[:-3]

        return str(final_number).replace('[', '').replace(']', '').replace("'", '')


s = EnglishSpeller()
print s.spell_out(12745091029128)
