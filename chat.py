def read_file(filename): #增設投幣孔，提供於'function外'調整欲讀取之filename
	info = []
	with open(filename,'r',encoding = 'utf-8-sig') as file: # utf-8-sig僅為一種特殊編碼原則
		for line in file:
			info.append(line.strip('\n')) #info =[] 清單中加入已被刪去"\n"的line 
	return info

def convert(info):
	new = []
	person = None # line中頭一筆是'非Allen與非Tom'的狀況
	for line in info:
		if line	== 'Allen':
			person = 'Allen'
			continue # elif 、new.append函式皆跳過，並從line中第二筆進行
		elif line == 'Tom':
			person = 'Tom'
			continue

		new.append(person + ': ' + line)
	return new
	
def write_file(filename, info):
	with open (filename, 'w') as file: #將我們未來要輸出的檔案 as file
		for line in info:
			file.write(line + '\n')



def main():
	info = read_file('input.txt') # 可以想像成read_file中，初期的info=[]，經歷過'input.txt'投入並覆蓋成'新info'
	info = convert(info) # comvert中的return回存的'new'又在定義成info，此情況可以想像成'覆蓋更新info'
	write_file('output.txt',info) #
main()