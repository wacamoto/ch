'''
	B10209034 
	tavukizartma@gmail.com 
'''
def combine(str1, str2 = ''):
	if str1:
		for index,item in enumerate(str1):
			combine(str1[:index] + str1[index+1:],str2 + str1[index])
	else:
		print(str2)

if __name__ == '__main__':
	combine('abcde')
	#combine('\'\"\\')