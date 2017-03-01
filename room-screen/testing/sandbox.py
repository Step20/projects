import string,random
s = string.ascii_lowercase + string.digits
userid = ''.join(random.sample(s,4))
name = 'Jamiro'
data = 'hey'
data = userid + data
dictionary = {userid:name}
print(dictionary)
print(dictionary[userid] + ':' + data[4:])

userid = ''.join(random.sample(s,4))
name = 'volmar'
data = 'ho'
data = userid + data
dictionary.update({userid:name})
print(dictionary)
print(dictionary[userid] + ':' + data[4:])
