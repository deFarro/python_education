import osa


def convert_co_c(temp):
    client = osa.Client('http://www.webservicex.net/ConvertTemperature.asmx?WSDL')
    return client.service.ConvertTemp(temp, 'degreeFahrenheit', 'degreeCelsius')


def get_average_temp_in_c(file):
    with open(file) as file:
        acc = 0
        quantity = 0
        for line in file:
            quantity += 1
            acc += int(line.split(' ')[0])
        return convert_co_c(acc / quantity)


print(get_average_temp_in_c('temps.txt'))


def convert_to_rub(price, from_c):
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    return client.service.ConvertToNum('', from_c, 'RUB', price, '', '', '')


def count_trip_in_rub(file):
    with open(file) as file:
        result = dict()
        for line in file:
            line_as_list = line.strip().split(': ')
            price_as_list = line_as_list[1].split(' ')
            route = line_as_list[0]
            price = int(price_as_list[0])
            currency = price_as_list[1]
            result[route] = round(convert_to_rub(price, currency))
        return result


print(count_trip_in_rub('currencies.txt'))


def convert_mi_to_km(distance):
    client = osa.Client('http://www.webservicex.net/length.asmx?WSDL')
    return client.service.ChangeLengthUnit(distance, 'Miles', 'Kilometers')


def get_trip_distance_km(file):
    with open(file) as file:
        result = dict()
        for line in file:
            line_as_list = line.strip().split(': ')
            distance_as_list = line_as_list[1].split(' ')
            route = line_as_list[0]
            distance_mi = float(distance_as_list[0].replace(',', ''))
            result[route] = round(convert_mi_to_km(distance_mi), 2)
        return result


print(get_trip_distance_km('travel.txt'))
