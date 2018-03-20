ROUTES_DATA_FILE = 'data/route-costs-4.txt'
PHONE_NUMBERS_FILE = 'data/phone-numbers-3.txt'

def get_routes_data():
    '''Open the given routes file and create a dictionary with the code as the key and the cost as the value'''
    f = open(ROUTES_DATA_FILE)
    dictionary = dict()
    for line in f.readlines():
        array = line.strip().split(',')
        dictionary[array[0]] = array[1]
    f.close()
    return dictionary

def check_single_phone_number_cost(phone_number):
    '''Returns the cost of a given phone number'''
    routes_data = get_routes_data()

    state_code = phone_number[0:5]
    area_code = phone_number[5:8]

    # Check largest possible match first
    if (state_code + area_code) in routes_data:
        return routes_data[state_code+area_code]
    elif state_code in routes_data:
        return routes_data[state_code]
    else:
        return 0

def get_phone_numbers():
    '''Open the given phonenumber file and creates a list with all the numbers'''
    f = open(PHONE_NUMBERS_FILE)
    array = list()
    for line in f.readlines():
        array.append(line.strip())
    f.close()
    return array

def main():
    # Senario 1
    print(check_single_phone_number_cost('+15124156620'))

if __name__ == '__main__':
    main()
