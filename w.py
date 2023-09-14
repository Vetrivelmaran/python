# Conversion table of remainders to
# hexadecimal equivalent
conversion_table = {0: '0', 1: '1', 2: '2', 3: '3',
					4: '4', 5: '5', 6: '6', 7: '7',
					8: '8', 9: '9', 10: 'A', 11: 'B',
					12: 'C', 13: 'D', 14: 'E', 15: 'F'}


# function which converts decimal value
# to hexadecimal value
def decimalToHexadecimal(decimal):
	if(decimal <= 0):
		return ''
	remainder = decimal % 16
	return decimalToHexadecimal(decimal//16) + conversion_table[remainder]


decimal_number = 69
print("The hexadecimal form of", decimal_number,
	"is", decimalToHexadecimal(decimal_number))
