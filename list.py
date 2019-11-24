# list 清單

twice =['娜璉', '定延', '志效', '多賢', '彩瑛', 'mina', 'sana']
print(twice)
print(twice[0])
print(twice[1])
print(twice[2])
print(twice[3])
print(twice[4])
print(twice[5])
print(twice[6])
print('twice成員:', twice)
print('twice成員目前有幾人:', len(twice))
twice.append('momo')
print('twice成員:', twice)
print(twice[7])
print('momo' in twice, '加入到twice了' )
print('twice成員目前有幾人:', len(twice))
twice.append('tzuyu')
print('twice成員:', twice)
print(twice[8])
print('tzuyu' in twice, '加入到twice了' )
print('twice成員目前有幾人:', len(twice))
while True:
	name = input('請輸入藝人姓名,並確認是否是twice成員:')
	a = print(name in twice) 
	break
