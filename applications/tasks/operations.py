""" SOAP operations module """

# Third-part Utilities
from zeep import Client
from itertools import zip_longest as zip_long

# Local Utilities
def rindex(string, character):
    """ give index counting from right to left """
    try:
        index = string.index(character)
        return len(string) - index
    except ValueError:
        return 0

def normalize_float(arr, positions):
    """ fill with zeros not equial floating point lenght numbers """
    try:
        index = arr.index('.')
    except ValueError:
        return f"{''.join(arr)}.{'0' * (positions -1)}"
    tmp = ''.join( x[0] or '0' for x in zip_long(arr[index:], range(positions)) )
    return arr[:index] + tmp


# main SOAP operations secction
class IntDict(object):
    """ Dict only contains integer values """
    config = None

    def __init__(self):
        self.config = {}

    def __setattr__(self, key, value):
        if self.config is None:
            # set config directly
            super().__setattr__(key, value)
            return
        elif type(value) != int:
            raise TypeError('Only "int" type values are allowed')
        self.config[key] = value

    def __getattr__(self, key):
        return self.config[key]

class SoapOperation:
    """ class control communications with SOAP API """

    wsdl_url = 'http://www.dneonline.com/calculator.asmx?WSDL'
    client = Client(wsdl_url)

    def __init__(self):
        """ SoapOperation init method """
        self._request_data = IntDict()

    def add(self, a, b):
        """ add comm method """
        self._request_data.intA = a
        self._request_data.intB = b
        return self.client.service.Add(**self._request_data.config)

    def sub(self, a, b):
        """ substract comm method """
        self._request_data.intA = a
        self._request_data.intB = b
        return self.client.service.Subtract(**self._request_data.config)

    def mul(self, a, b):
        """ multiply comm method """
        self._request_data.intA = a
        self._request_data.intB = b
        return self.client.service.Multiply(**self._request_data.config)

    def pot(self, a, b):
        """ power comm method """
        return self.mul(a, self.pot(a, b-1)) if b > 1 else a

class SoapInts:
    """ class addapt inputs to SOAP requirements """

    operator = SoapOperation()

    def __init__(self, value):
        """ SoapInts init method """
        self.value = value

    def __sub__(self, other):
        """ Subtract addaptation method """
        
        sustraendo = list(str(other.value))

        if sustraendo[0] == '-':
            sustraendo = sustraendo[1:]
        else:
            sustraendo.insert(0, '-')

        other.value = ''.join(sustraendo)

        return self + other

    def __add__(self, other):
        """ Adding addaptation method """

        sumando = [str(self.value), str(other.value)]
        sumando = [x.replace(',', '.') for x in sumando]

        longest_decimal = max(rindex(x, '.') for x in sumando)

        if longest_decimal == 0:
            return self.operator.add(int(self.value), int(other.value))

        sumando = [normalize_float(x, longest_decimal) for x in sumando]
        sumando = [x.replace('.', '') for x in sumando]
        sumando = [int(x) for x in sumando]

        response = self.operator.add(*sumando)

        put_comma = list(str(response))
        put_comma.insert(-longest_decimal+1, '.')

        return ''.join(put_comma)
