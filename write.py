import rosbag
import string
import numpy as np
import time
from std_msgs.msg import Int32, String
from matplotlib import pyplot as plt
#bag = rosbag.Bag('Dance1.bag')
bag = rosbag.Bag('large_talk7.bag')
bagContents = bag.read_messages()
# bagName = bag.filename

# percentage = .2

# listOfTopics = []
# for topic, msg, t in bag.read_messages():
#     if topic not in listOfTopics:
# 			listOfTopics.append(topic)

# print listOfTopics



with rosbag.Bag('output.bag', 'w') as outbag:
	for topic, msg, t in bag.read_messages():
  			str = String()
  			str.data = str(0.001)
  			print (msg,topic,t)
  			outbag.write(topic, str,t)
  			#s=False
    		
        # if topic == "/tf" and msg.transforms:
        #     outbag.write(topic, msg, msg.transforms[0].header.stamp)
        # else:
        #     outbag.write(topic, msg, msg.header.stamp if msg._has_header else t)
'''
#for topicName in listOfTopics:
old = 0
switch =False
for message in listOfTopics:
	slope_list = []
	
	for subtopic, msg, t in bag.read_messages(message):
		msgString = str(msg)
		msgList = string.split(msgString, '\n')
		
		for nameValuePair in msgList:
						splitPair = string.split(nameValuePair, ':')
						for i in range(len(splitPair)):	#should be 0 to 1
							splitPair[i] = string.strip(splitPair[i])
						new =float(splitPair[1])
						slope = abs(new - old)

						#print slope
						old = new
						if(switch == False):
							switch = True
						else:	
							slope_list.append(slope)
					#ata_value.append(splitPair[1])

	print message,max(slope_list)
	time.sleep(2)
	#break
	#print len(slope_list), len (data_value)
	Max = max(slope_list)	
				
	limit = max(slope_list) * percentage
	threshold = Max - limit
	old=0
	new=0
	data_value = []
	count =0
	for subtopic, msg, t in bag.read_messages(message):
		msgString = str(msg)
		msgList = string.split(msgString, '\n')
		
			
	
		for nameValuePair in msgList:
						splitPair = string.split(nameValuePair, ':')
						for i in range(len(splitPair)):	#should be 0 to 1
							splitPair[i] = string.strip(splitPair[i])
						new =float(splitPair[1])
						slope = abs(new - old)
						if(count == 0):
							count = count+1
							slope =0
						if(threshold>slope):
							data_value.append(new)
							print new,slope,'*'
							old= new
						else:
							data_value.append(old)
							print old,slope
							old = old
						#print new
						
						#time.sleep(1)

						# if(switch == False):
					# 	switch = True
					# else:	
					# 	slope_list.append(slope)
	#break
	count = 0
	#print data_value
	x = np.arange(0,len(data_value))
	plt.title("Matplotlib demo") 
	plt.xlabel("x axis caption") 
	plt.ylabel("y axis caption") 
	plt.plot(x,data_value) 
	plt.show()

	o=0
	for i in data_value:
		n=i
		slo= abs(n- o)
		print slo
		o=n
	break
		#print i
	#for subtopic, msg, t in bag.read_messages(message):
	#print message, max(slope_list)
	#print min(slope_list)
#	switch = False

	
	# for pair in slope_list:
	# 				value= (pair[1])
					#print value

'''
bag.close()