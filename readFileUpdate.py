data = []
count = 0
length = 0
Total_length = 0
go = 'N'
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		print(len(data))
	length = len(data)
	print('\n....................................')
	print(length, 'reviews in the file.')
	print('....................................\n')
	while count < length:
		print('\nreview ', count + 1,'\n')
		print(data[count])
		print('\n', len(data[count]))
		go = 'N'
		while True:
			if go == 'Y' or go == 'Q':
				break
			else:
				print('\n***************************************************************************\n')
				go = input('input Y for go to next review or Q for quit!......')
		if go == 'Q':
			print('Quit read!')
			break
		count += 1


	