#讀取APPLE 財報文件
apple =[]
with open('AAPLFinan.txt','r') as f:
	for line in f:
		apple.append(line)
		print(line)

#將APPLE財報寫入EXCEL檔
with open('AAPLFinan.csv','w') as f:
	for fn in apple:
		f.write(fn)
		
		
