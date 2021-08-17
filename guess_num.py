import random 

r = random.randint(1, 100)
count = 0
while True:
	count = count + 1
	i = input('請輸入數字: ')
	i = int(i)
	if i == r:
		print('答對了')
		print('這是你猜的第', count, '次')
		break
	else:
	    if i > r :
	        print('比答案大')
	    else:
	        print('比答案小')
	print('這是你猜的第', count, '次')
