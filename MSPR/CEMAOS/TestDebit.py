import os
import time
import speedtest
import datetime

def test():
	s = speedtest.Speedtest()
	s.get_servers()
	s.get_best_server()
	s.download()
	s.upload()
	res = s.results.dict()
	return res["download"], res["upload"], res["ping"]

    

# def main():
# 	# write to csv
# 	divide = 1024*1024
# 	with open('file.csv', 'a') as f:
# 		d, u, p = test()
# 		f.write('{},{:.2f},{:.2f},{}\n'.format(datetime.datetime.now(),d/divide, u/divide, p))
	
# 	print('Ok for connection : ' + str(datetime.datetime.now()) + '\n')
d, u, p = test()
print(d, u, p)