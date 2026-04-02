'''


'''


def tests(test1, test2):
	#
	if test1 == test2:
		#
		return test1
	else:
		#
		return test2
#
test1 = int(input('Please enter Marks for test one: '))
test2 = int(input('Please enter Marks for test two: '))

'''


'''
def courseWrk(cswork):
	#
	testsMark = tests(test1,test2)
	#
	avgtestsCswork = (cswork + testsMark)/2
	#
	fnltestsCswork = avgtestsCswork * (40/100)
	#
	print('..............................')
	#
	print('your final coursework marks is: ', fnltestsCswork)
	print('..............................')
#
cswork = int(input('Please enter your course work Marks: '))
#
courseWrk(cswork)
