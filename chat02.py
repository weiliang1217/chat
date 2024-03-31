def read_file(filename): #增設投幣孔，提供於'function外'調整欲讀取之filename
	info = []
	with open(filename,'r',encoding = 'utf-8-sig') as file: # utf-8-sig僅為一種特殊編碼原則
		for line in file:
			info.append(line.strip('\n')) #info =[] 清單中加入已被刪去"\n"的line 
	return info


def convert(info):
	new = []
	person = None # line中頭一筆是'非Allen與非Tom'的狀況，如果直接new append 加入時會產生crash，預設值
	allen_count_word = 0
	allen_count_sticker = 0
	allen_count_pic = 0
	viki_count_word = 0
	viki_count_sticker = 0
	viki_count_pic = 0
	for line in info:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		#print(s[0]) s清單中第一內容；s[1]=清單第二內容。
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_count_sticker += 1
			elif s[2] == '圖片':
				allen_count_pic +=1
			else:		
				for msg in s[2:]: #如果要每一筆相加時，
					allen_count_word += len(s[2:])
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_count_sticker += 1
			elif s[2] == '圖片':
				viki_count_pic += 1
			else:
				for msg in s[2:]:
					viki_count_word += len(s[2:])

	print(allen_count_word)
	print(allen_count_sticker)
	print(allen_count_pic)
	print(viki_count_word)
	print(viki_count_sticker)
	print(viki_count_pic)

	return new

	
def write_file(filename, info):
	with open (filename, 'w') as file: #將我們未來要輸出的檔案 as file
		for line in info:
			file.write(line + '\n')


def main():
	info = read_file('LINE-Viki.txt') # 可以想像成read_file中，初期的info=[]，經歷過'input.txt'投入並覆蓋成'新info'
	info = convert(info) # comvert中的return回存的'new'又在定義成info，此情況可以想像成'覆蓋更新info'
	write_file('output.txt',info) #
main()