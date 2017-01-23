from unit import GreatUnit

gu = GreatUnit()

result = gu.list_stepper([i for i in range(100000)], 100)

for i in result:
    print(i)
