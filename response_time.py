import sys
dec_count = 0
enc_count = 0
auth_count = 0
acl_count = 0
dec_total = 0
enc_total = 0
auth_total = 0
acl_total = 0
dec_high = 0
enc_high = 0
auth_high = 0
acl_high = 0

if len(sys.argv)>1:
	file = open(sys.argv[1],'r')
	for line in file.readlines():
		if line.find(" decode time: ")>0:
			tmpStr = line.split(' ')
			if tmpStr[len(tmpStr)-1]=='ms\n':
				dec_total+=int(tmpStr[len(tmpStr)-2])
				dec_count+=1
                                if dec_high < int(tmpStr[len(tmpStr)-2]):
                                        dec_high =  int(tmpStr[len(tmpStr)-2])
				print('dec time: '+tmpStr[len(tmpStr)-2])
		if line.find(' Authentication query time: ')>0:
			tmpStr = line.split(' ')
			if tmpStr[len(tmpStr)-1]=='ms\n':
				auth_total+=int(tmpStr[len(tmpStr)-2])
				auth_count+=1
                                if auth_high <  int(tmpStr[len(tmpStr)-2]):
                                        auth_high =  int(tmpStr[len(tmpStr)-2])
				print('auth time: '+tmpStr[len(tmpStr)-2])
		if line.find(" ACL query time: ")>0:
			tmpStr = line.split(' ')
			if tmpStr[len(tmpStr)-1]=='ms\n':
				acl_total+=int(tmpStr[len(tmpStr)-2])
				acl_count+=1
                                if acl_high <  int(tmpStr[len(tmpStr)-2]):
                                        acl_high =  int(tmpStr[len(tmpStr)-2])
				print('ACL time: '+tmpStr[len(tmpStr)-2])
		if line.find(' encode time: ')>0:
			tmpStr = line.split(' ')
			if tmpStr[len(tmpStr)-1]=='ms\n':
				enc_total+=int(tmpStr[len(tmpStr)-2])
				enc_count+=1
                                if enc_high <  int(tmpStr[len(tmpStr)-2]):
                                        rnc_high =  int(tmpStr[len(tmpStr)-2])
				print('enc time: '+tmpStr[len(tmpStr)-2])
file.close()
print('Decode average time:'+str(float(dec_total/dec_count))+'ms Total ms: '+str(dec_total)+' Counts:'+str(dec_count)+' The highest: '+str(dec_high))
print('Auth average time:'+str(float(auth_total/auth_count))+'ms  Total ms: '+str(auth_total)+' Counts:'+str(auth_count)+' The highest: '+str(auth_high))
print('ACL average query time:'+str(float(acl_total/acl_count))+'ms Total ms: '+str(acl_total)+' Counts:'+str(acl_count)+' The highest: '+str(acl_high))
print('enc average time:'+str(float(enc_total/enc_count))+' Total ms: '+str(enc_total)+' Counts:'+str(enc_count)+' The highest: '+str(enc_high))
