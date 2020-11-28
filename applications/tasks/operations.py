from zeep import Client

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
        first = int(self.value)
        second = [int(x) for x in other.value.split('.')]
        response = self.operator.sub(first, second[0])

        if len(second) > 1:
            decimal_places = self.operator.pot(len(str(second[1])), 10)
            second[1] = self.operator.sub(decimal_places, second[1])
            return f'{response-1}.{second[1]}'

        return str(response)
