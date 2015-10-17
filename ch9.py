'''
	B10209034 
	tavukizartma@gmail.com
'''
import sys

def postorder(s):
	for a in range(len(s)-1,-1,-1):
		if s[a] in ['+','-']:
			return postorder(s[:a]) + postorder(s[a+1:]) + [s[a]]
	for a in range(len(s)-1,-1,-1):
		if s[a] in ['*','/']:
			return postorder(s[:a]) + postorder(s[a+1:]) + [s[a]]
	return [float(s)]

def calPostorder(s):
	print(s)
	for a in s:
		if a in ['+','-','*','/']:
			position = s.index(a)
			operator = a
			n1 = s[position - 2]
			n2 = s[position - 1]
			break

	if operator == '+':
		cal = n1 + n2
	if operator == '-':
		cal = n1 - n2
	if operator == '*':
		cal = n1 * n2
	if operator == '/':
		cal = n1 / n2

	if len(s) > 3:
		return calPostorder(s[0:position - 2] + [cal] + s[position + 1:])
	else:
		return cal

if __name__ == '__main__':
	if len(sys.argv) > 1:
		cal = sys.argv[1]
	else:
		cal = input("\"only\" using '+', '-', '*', '/'   Example: 1.5+1.6*2-10+6*2\n: ")
	cal = calPostorder(postorder(cal))
	print(cal)