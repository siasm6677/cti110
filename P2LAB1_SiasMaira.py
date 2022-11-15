gas_milage = float(input()) # car's gas milage (miles/gallon)

gas_cost = float(input()) # cost of gas (dollars/gallon)

distance1 = 20 / (gas_milage / gas_cost) # 20 miles driven
distance2 = 75 / (gas_milage / gas_cost) # 75 miles driven
distance3 = 500 / (gas_milage / gas_cost) #500 miles driven

print(f'{distance1:.2f} {distance2:.2f} {distance3:.2f}')
