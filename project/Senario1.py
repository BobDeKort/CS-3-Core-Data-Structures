def getRoutesList():
    f = open('data/route-costs-4.txt')
    array = list()
    for line in f.readlines():
        array.append(line.strip())
    f.close()
    return array

def findCostOfOneNumber():
    

def main():
    routes = getRoutesList()
    print(routes)

if __name__ == '__main__':
    main()
