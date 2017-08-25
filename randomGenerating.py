import sys
import random

def printrandom(big):
	num = random.randint(0,int(big))
	print '\n###########################'
	print '----------------------------'
	print 'Your Number Generated is ' + str(num)
	print '----------------------------\n'
	

def main():
	rrange = sys.argv[1]
	printrandom(rrange)

	while True:
		ans = raw_input('Would You Like To Continue ? (y/n)\n')
		if(ans == 'y') or (ans == 'Y'):
			snum = raw_input ('\nPlease Give Me The Largest Range\n')
			printrandom(snum)
			
		elif(ans == 'n') or (ans == 'N'):
			break
		else: 
			print 'Please type either y or n\n' 

	print '\nGoodbye And Have A Nice Day !'
	print '###########################\n'

if __name__ == '__main__':
	main()

