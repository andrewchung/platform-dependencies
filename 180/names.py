import itertools
from collections import defaultdict

# fake data from https://www.mockaroo.com
data = """last_name,first_name,country_code
Watsham,Husain,ID
Harrold,Alphonso,BR
Apdell,Margo,CN
Tomblings,Deerdre,RU
Wasielewski,Sula,ID
Jeffry,Rudolph,TD
Brenston,Luke,SE
Parrett,Ines,CN
Braunle,Kermit,PL
Halbard,Davie,CN"""


def group_names_by_country(data: str = data) -> defaultdict:
    countries = defaultdict(list)
    details = []
    final_list = []

    data = data.splitlines()
    data.pop(0)
    for name in data:
        details = name.split(',')
        final_list.append([details[1] + ' ' + details[0], details[2]])

    d1 = {x[0]: x[1] for x in final_list}

    for key, val in sorted(d1.items()):
        countries[val].append(key)

    return(defaultdict(int, countries))


if __name__ == '__main__':
    group_names_by_country(data)
