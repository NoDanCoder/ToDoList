from zeep import Client
from itertools import zip_longest as zip_long

class IntDict(object):
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

    wsdl_url = 'http://www.dneonline.com/calculator.asmx?WSDL'
    client = Client(wsdl_url)

    def __init__(self):
        self._request_data = IntDict()

    def add(self, a, b):
        self._request_data.intA = a
        self._request_data.intB = b
        return self.client.service.Add(**self._request_data.config)

    def sub(self, a, b):
        self._request_data.intA = a
        self._request_data.intB = b
        return self.client.service.Subtract(**self._request_data.config)

    def mul(self, a, b):
        self._request_data.intA = a
        self._request_data.intB = b
        return self.client.service.Multiply(**self._request_data.config)

    def pot(self, a, b):
        return self.mul(b, self.pot(a-1, b)) if a > 1 else b

class SoapInts:

    operator = SoapOperation()

    def __init__(self, value):
        self.value = value

    def __sub__(self, other):

        self.value = self.value.replace(',', '.')
        other.value = other.value.replace(',', '.')
               
        # divide decimal of entire part
        first = [x[0] or x[1] for x in \
                zip_long(self.value.split('.'), '00')] 
        
        second = [x[0] or x[1] for x in \
                zip_long(other.value.split('.'), '00')]
    
        # fill zeros
        if len(first[1]) > len(second[1]):
            second[1] = ''.join([x[1] or '0' for x in zip_long(first[1], second[1])])
        elif len(first[1]) < len(second[1]):
            first[1] = ''.join([x[0] or '0' for x in zip_long(first[1], second[1])])

        # op decimal part
        potencia = len(first[1])
        max_scope = self.operator.pot(potencia, 10)
        if int(first[1]) < int(second[1]):
            first[0] = self.operator.sub(int(first[0]), 1)
            decimal_part = self.operator.sub(max_scope, int(second[1]))
            decimal_part = self.operator.add(int(first[1]), decimal_part)
        else:
            decimal_part = self.operator.sub(int(first[1]), int(second[1]))

        entire_part = self.operator.sub(int(first[0]), int(second[0]))
        return f'{entire_part}.{decimal_part}'


    def __add__(self, other):

        self.value = self.value.replace(',', '.')
        other.value = other.value.replace(',', '.')
        
        # divide decimal of entire part
        first = [x[0] or x[1] for x in \
                zip_long(self.value.split('.'), '00')] 
        
        second = [x[0] or x[1] for x in \
                zip_long(other.value.split('.'), '00')]


        # fill zeros
        if len(first[1]) > len(second[1]):
            second[1] = ''.join([x[1] or '0' for x in zip_long(first[1], second[1])])
        elif len(first[1]) < len(second[1]):
            first[1] = ''.join([x[0] or '0' for x in zip_long(first[1], second[1])])

        # sum decimal part
        potencia = len(second[1])
        decimal_part = self.operator.add(int(first[1]), int(second[1]))
        max_scope = self.operator.pot(potencia, 10)

        if decimal_part >= max_scope:
            first[0] = self.operator.add(1, int(first[0]))

        entire_part = self.operator.add(int(first[0]), int(second[0]))
        return f'{entire_part}.{decimal_part}'
