password = 'a123456'
pw = input()
i = 1
tries = 2

while i < 4:
	if pw == password:
		print('登入成功')
		break
	else: 
		print('還剩',tries,'次機會')
	i = i + 1
	tries = tries -1
	pw = input()