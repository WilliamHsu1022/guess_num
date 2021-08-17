import random 

r = random.randint(1, 100)
while True:
	i = input('請輸入數字: ')
	i = int(i)
	if i == r:
		print('答對了')
		break
	else:
	    if i > r :
	        print('比答案大')
	    else:
	        print('比答案小') 
