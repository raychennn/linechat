#讀取檔案
def read_file(filename):
	lines = []
	with open (filename , 'r' , encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines

#計數
def convert(lines):
	allen_word_count = 0
	allen_sticker_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	allen_picture_count = 0
	viki_picture_count = 0
	person = None
	for line in lines:
		s = line.split(' ') #切割
		time = s[0]
		person = s[1]
		if person == 'Allen':
			if s[2] =='貼圖':
				allen_sticker_count += 1
			elif s[2] == '圖片':
				allen_picture_count +=1
			else:
				for m in s[2:]:
					allen_word_count += len(m)
		elif person == 'Viki':
			if s[2] =='貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_picture_count +=1
			else:
				for m in s[2:]:
					viki_word_count += len(m)
	print('Allen說了：' , allen_word_count ,'個字，傳了', allen_sticker_count ,'張貼圖傳了',allen_picture_count,'張照片')
	print('Viki說了：' , viki_word_count ,'個字，傳了', viki_sticker_count ,'張貼圖傳了',viki_picture_count,'張照片')
#重寫新檔
def write_file(filename, lines):
	with open(filename , 'w') as f:
		for line in lines:
			f.write(line + '\n')

#主要程式
def main():
	lines = read_file('Line-Viki.txt')
	lines = convert(lines)
	#write_file('output.txt',lines)
main()