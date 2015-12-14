import hashlib

secretKey = 'yzbqklnj'
md5Hash = hashlib.md5()
i = 0

while 1 == 1:
    fullKey = secretKey + str(i)
    i += 1
    if str(hashlib.md5(fullKey.encode('utf-8')).hexdigest()).startswith('00000'):
        print "MD5:", hashlib.md5(fullKey.encode('utf-8')).hexdigest(),"Answer", fullKey
        break

