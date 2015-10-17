'''
	B10209034 
	tavukizartma@gmail.com 
'''
def combine(str1, str2 = ''):
	if str1:
		for i in range(len(str1)):
			combine(str1[:i] + str1[i+1:],str2 = str2 + str1[i])
	else:
		print(str2)

if __name__ == '__main__':
	combine('abcde')
	#combine('\'\"\\')