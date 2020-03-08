import http.client, urllib
from time import localtime, strftime
# download from http://code.google.com/p/psutil/
import psutil
import time

def doit():
	cpu_pc = list(psutil.process_iter())
	mem_avail_mb = psutil.avail_phymem()/1000000	
	params = urllib.urlencode({'field1': cpu_pc, 'field2': mem_avail_mb,'key':'YOURKEYHERE'})
	headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
	conn = httplib.HTTPConnection("api.thingspeak.com:80")
	
	try:
		conn.request("POST", "/update", params, headers)
		response = conn.getresponse()
		 
		data = response.read()
		conn.close()
	except:
		print ("connection failed")	

#sleep for 16 seconds (api limit of 15 secs)
if __name__ == "__main__":
	while True:
		doit()
		time.sleep(16) 
