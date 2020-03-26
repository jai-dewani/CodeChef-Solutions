# days = [4, 5, 6, 7, 2, 3, 4, 5, 7, 1, 2, 3, 5, 6, 7, 1, 3, 4, 5, 6, 1, 2, 3, 4, 6, 7, 1, 2, 4, 5, 6, 7, 2, 3, 4, 5, 7, 1, 2, 3, 5, 6, 7, 1, 3, 4, 5, 6, 1, 2, 3, 4, 6, 7, 1, 2, 4, 5, 6, 7, 2, 3, 4, 5, 7, 1, 2, 3, 5, 6, 7, 1, 3, 4, 5, 6, 1, 2, 3, 4, 6, 7, 1, 2, 4, 5, 6, 7, 2, 3, 4, 5, 7, 1, 2, 3, 5, 6, 7, 1, 2, 3, 4, 5, 7, 1, 2, 3, 5, 6, 7, 1, 3, 4, 5, 6, 1, 2, 3, 4, 6, 7, 1, 2, 4, 5, 6, 7, 2, 3, 4, 5, 7, 1, 2, 3, 5, 6, 7, 1, 3, 4, 5, 6, 1, 2, 3, 4, 6, 7, 1, 2, 4, 5, 6, 7, 2, 3, 4, 5, 7, 1, 2, 3, 5, 6, 7, 1, 3, 4, 5, 6, 1, 2, 3, 4, 6, 7, 1, 2, 4, 5, 6, 7, 2, 3, 4, 5, 7, 1, 2, 3, 5, 6, 7, 1, 3, 4, 5, 6, 7, 1, 2, 3, 5, 6, 7, 1, 3, 4, 5, 6, 1, 2, 3, 4, 6, 7, 1, 2, 4, 5, 6, 7, 2, 3, 4, 5, 7, 1, 2, 3, 5, 6, 7, 1, 3, 4, 5, 6, 1, 2, 3, 4, 6, 7, 1, 2, 4, 5, 6, 7, 2, 3, 4, 5, 7, 1, 2, 3, 5, 6, 7, 1, 3, 4, 5, 6, 1, 2, 3, 4, 6, 7, 1, 2, 4, 5, 6, 7, 2, 3, 4, 5, 7, 1, 2, 3, 5, 6, 7, 1, 3, 4, 5, 6, 1, 2, 3, 4, 5, 6, 7, 1, 3, 4, 5, 6, 1, 2, 3, 4, 6, 7, 1, 2, 4, 5, 6, 7, 2, 3, 4, 5, 7, 1, 2, 3, 5, 6, 7, 1, 3, 4, 5, 6, 1, 2, 3, 4, 6, 7, 1, 2, 4, 5, 6, 7, 2, 3, 4, 5, 7, 1, 2, 3, 5, 6, 7, 1, 3, 4, 5, 6, 1, 2, 3, 4, 6, 7, 1, 2, 4, 5, 6, 7, 2, 3, 4, 5, 7, 1, 2, 3, 5, 6, 7, 1, 3, 4, 5, 6, 1, 2, 3, 4, 6, 7, 1, 2]
table = [0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0]
total = sum(table)
for _ in range(int(input())):
	m1,y1 = map(int,input().split())
	m2,y2 = map(int,input().split())
	year = 400
	ans = 0
	if m1>2:
		y1 += 1
	if m2 <2:
		y2 -= 1
	if y1>y2:
		print(0)
		continue
	if y2-y1<400:
		mod_y1 = y1%year
		mod_y2 = y2%year
		if mod_y1<=mod_y2:
			ans += sum(table[mod_y1:mod_y2+1])
		else:
			ans += sum(table[mod_y1:]) + sum(table[:mod_y2+1])
	else:
		ans += ((y2-y1)//400)*total
		mod_y1 = y1%year
		mod_y2 = y2%year
		if mod_y1<=mod_y2:
			ans += sum(table[mod_y1:mod_y2+1])
		else:
			ans += sum(table[mod_y1:]) + sum(table[:mod_y2+1])
	print(ans)