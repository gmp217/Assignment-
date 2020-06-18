#prg1
print('1 SIMPLE CALUCULATOR\n')
print('1 add\n2 sub \n3 multiplication\n4 division\n5 modulus') 
print('6 exponent value\n7 floor division')
n=input('Enter choice: ')
if n in('1','2','3','4','5','6','7'):
	a=int(input('Enter first num '))
	b=int(input('Enter second num '))
	if n=='1':
		print(a+b)
	elif n=='2':
		print(a-b)
	elif n=='3':
		print(a*b)
	elif n=='4':
		print(a/b)
	elif n=='5':
		print(a%b)
	elif  n=='6':
		print(a**b)
	elif n=='7':
		print(a//b)
	else:
		print('invalid')