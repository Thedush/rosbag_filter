import rosbag
import string
import numpy as np
import time
from std_msgs.msg import Float64, String
from matplotlib import pyplot as plt
bag = rosbag.Bag('checking1.bag')
#bag = rosbag.Bag('checking2.bag')
bagContents = bag.read_messages()
bagName = bag.filename



listOfTopics = []
for topic, msg, t in bag.read_messages():
    if topic not in listOfTopics:
			listOfTopics.append(topic)

print listOfTopics
# listOfTopics = ['/pan_controller/recorded_position','/joint5/recorded_position', '/joint6/recorded_position',
#                 '/joint7/recorded_position', '/joint8/recorded_position', 
#                 '/joint1/recorded_position', '/joint2/recorded_position',
#                 '/joint3/recorded_position', '/joint4/recorded_position']
#for topicName in listOfTopics:
old = 0
switch =False
filtername= bagName.strip('.bag') + '_filter.bag'
print filtername
with rosbag.Bag(filtername, 'w') as outbag:
	for message in listOfTopics:
		data_value = []
		time =[]
		for subtopic, msg, t in bag.read_messages(message):
			msgString = str(msg)
			msgList = string.split(msgString, '\n')
			
			for nameValuePair in msgList:
							splitPair = string.split(nameValuePair, ':')
							for i in range(len(splitPair)):	#should be 0 to 1
								splitPair[i] = string.strip(splitPair[i])
							#print splitPair[1]
							new =float(splitPair[1])
							data_value.append(new)
			time.append(t)
					
		def movingaverage(values,window):
			weights = np.repeat(1.0,window)/ window
			smas = np.convolve(values,weights,'valid')
			return smas
		#print data_value
		#time.sleep(2)
		data = movingaverage(data_value,20)
		#break
		#print len(slope_list), len (data_value)
		print message,len(data_value),len(data),len(time)
		x = np.arange(0,len(data))
		plt.title("Filter") 
		plt.xlabel("x axis Data") 
		plt.ylabel("y axis Time") 
		plt.plot(x,data) 
		plt.show()
		#print data[0],time[0]
		for i in range(len(data)):
			value = Float64()
			value.data = data[i]
			outbag.write(message, value,time[i])
						
						

		

bag.close()
