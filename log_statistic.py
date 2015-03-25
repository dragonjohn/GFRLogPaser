import sys
timeList = []
timeCount = []
peak = 0
peakTime = ''
nadir = 0
nadirTime = ''
average = 0.0

if len(sys.argv)>1:
	file = open(sys.argv[1],'r')
	for line in file.readlines():
		if line.find(" decode time: ")>0:
			if line[:19] in timeList:
				idx = timeList.index(line[:19])
				timeCount[idx] = timeCount[idx]+1
			else:
				# add to time list
				timeList.append(line[:19])
				timeCount.append(1)
	file.close()
	
if timeCount:
	peak = timeCount[0]
	nadir = timeCount[0]
	for idx, item in enumerate(timeCount):
		if item > peak:
			peak = item
			peakTime = timeList[idx]
		if item < nadir:
			nadir = item
			nadirTime = timeList[idx]
		average+=item

print 'Peak time:'+peakTime+'('+str(peak)+'), Nadir time: '+nadirTime+'('+str(nadir)+'), Average:('+str(float(average/len(timeCount)))+')'
