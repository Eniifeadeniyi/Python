print(f'Celsius{"Fahrenheit":>15}')

for celsius in range(0,101):
	fahrenheit = (9 / 5) * celsius + 32
	fahrenheit = round(fahrenheit,1) 
	print(f'{celsius} {fahrenheit:>20}')