country = input('where are you from: ')
age = input('how old are you: ')
age = int(age)
if country == 'taiwan':
	if age >= 18:
		print('you can drive')
	else :
		print('you can not drive')
else:
	print('thanks')