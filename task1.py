""" You can ignore these comments :D
#1) txt fayl o`quvchi va uni ichidagi so'zlarni sonni qaytaruvchi raqamni yozing. 
#tushunmadim nimda ma'noda aytilgan funksya yaratish kerakmi yo fayldan ma'lumot o'qish kerakmi? (sonini qaytaruvchi??) (so'zlardi qanaqa raqami ascii tablemi erpdayam tolim ma'lumot yoq ekan)"""
#qwertyu

"""\_______________ main code __________________/"""

filename = 'sometvhing.txt'
try:
	with open(filename,'r') as f:
		lines = f.read()
		letters = 'qwertyuiopasdfghjklxcvbnm'
		count = 0
		for i in lines:
			if i.lower() in letters:
				count += 1
	print(f"The count of words in {filename}: {count}")
except FileNotFoundError:
	print(f"{filename}NotFoundError")
