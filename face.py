########### Python 2.7 #############
import httplib, urllib, base64,json,pickle,glob,time,csv,os,time

os.chdir('C:/Users/aftab/Desktop/facerecognition/')

headers = {
    # Request headers
    'Content-Type': 'application/octet-stream',
    'Ocp-Apim-Subscription-Key': '92db9bf775fb44c1a014910840805169'
	#8f37250321f247d495ce049f5a04afb5
}

params = urllib.urlencode({
    # Request parameters
    'returnFaceId': 'true',
    'returnFaceLandmarks':'true',
    'returnFaceAttributes':'age,gender,headPose,smile,facialHair'
})

userid_list = ['filename'];
age_list = ['PredictedAge'];
gender_list = ['PredictedGender'];
sideburns_list = ['sideburns'];
moustache_list = ['moustache'];
beard_list = ['beard'];

underLipTop_y_list = ['underLipTop_y']
underLipTop_x_list = ['underLipTop_x']
noseTip_y_list = ['noseTip_y']
noseTip_x_list = ['noseTip_x']
upperLipBottom_y_list = ['upperLipBottom_y']
upperLipBottom_x_list = ['upperLipBottom_x']
noseLeftAlarTop_y_list = ['noseLeftAlarTop_y']
noseLeftAlarTop_x_list = ['noseLeftAlarTop_x']
eyebrowLeftOuter_y_list = ['eyebrowLeftOuter_y']
eyebrowLeftOuter_x_list = ['eyebrowLeftOuter_x']
eyeLeftBottom_y_list = ['eyeLeftBottom_y']
eyeLeftBottom_x_list = ['eyeLeftBottom_x']
pupilLeft_y_list = ['pupilLeft_y']
pupilLeft_x_list = ['pupilLeft_x']
upperLipTop_y_list = ['upperLipTop_y']
upperLipTop_x_list = ['upperLipTop_x']
eyeLeftInner_y_list = ['eyeLeftInner_y']
eyeLeftInner_x_list = ['eyeLeftInner_x']
eyeRightInner_y_list = ['eyeRightInner_y']
eyeRightInner_x_list = ['eyeRightInner_x']
eyeLeftTop_y_list = ['eyeLeftTop_y']
eyeLeftTop_x_list = ['eyeLeftTop_x']
mouthLeft_y_list = ['mouthLeft_y']
mouthLeft_x_list = ['mouthLeft_x']
noseRightAlarTop_y_list = ['noseRightAlarTop_y']
noseRightAlarTop_x_list = ['noseRightAlarTop_x']
eyebrowRightInner_y_list = ['eyebrowRightInner_y']
eyebrowRightInner_x_list = ['eyebrowRightInner_x']
noseLeftAlarOutTip_y_list = ['noseLeftAlarOutTip_y']
noseLeftAlarOutTip_x_list = ['noseLeftAlarOutTip_x']
noseRightAlarOutTip_y_list = ['noseRightAlarOutTip_y']
noseRightAlarOutTip_x_list = ['noseRightAlarOutTip_x']
noseRootRight_y_list = ['noseRootRight_y']
noseRootRight_x_list = ['noseRootRight_x']
eyeLeftOuter_y_list = ['eyeLeftOuter_y']
eyeLeftOuter_x_list = ['eyeLeftOuter_x']
underLipBottom_y_list = ['underLipBottom_y']
underLipBottom_x_list = ['underLipBottom_x']
eyeRightTop_y_list = ['eyeRightTop_y']
eyeRightTop_x_list = ['eyeRightTop_x']
eyeRightOuter_y_list = ['eyeRightOuter_y']
eyeRightOuter_x_list = ['eyeRightOuter_x']
noseRootLeft_y_list = ['noseRootLeft_y']
noseRootLeft_x_list = ['noseRootLeft_x']
eyebrowRightOuter_y_list = ['eyebrowRightOuter_y']
eyebrowRightOuter_x_list = ['eyebrowRightOuter_x']
eyeRightBottom_y_list = ['eyeRightBottom_y']
eyeRightBottom_x_list = ['eyeRightBottom_x']
eyebrowLeftInner_y_list = ['eyebrowLeftInner_y']
eyebrowLeftInner_x_list = ['eyebrowLeftInner_x']
mouthRight_y_list = ['mouthRight_y']
mouthRight_x_list = ['mouthRight_x']
pupilRight_y_list = ['pupilRight_y']
pupilRight_x_list = ['pupilRight_x']

filename = 'C:/Users/aftab/Desktop/facerecognition/image/b00d2b74d389a4e254f9454679e29d02.jpg'
path="C:/Users/aftab/Desktop/facerecognition/image"

for filename in glob.iglob(path+'/*.jpg'):
   print("\n")
   print("-------------------------------")
   print(filename)
   time.sleep(5)
   f = open(filename, "rb")
   body = f.read()
   f.close()
   conn = httplib.HTTPSConnection('api.projectoxford.ai')
   conn.request("POST", "https://api.projectoxford.ai/face/v1.0/detect?%s" % params, body, headers)
   response = conn.getresponse()
   data = response.read()
   jsondata = json.loads(data)
   if(len(data) > 2):
	   print(jsondata)
	   
	   if("Internal server error" in data):
		print("Hit Internal server error...urghhh!!!")
		sleep(10);
		#continue;
	   else:	
		   if "faceId" in data:
			faceId = jsondata[0]['faceId']
		   else:
			faceId = "unknown"
			
		   if "age" in data:	
			age = jsondata[0]['faceAttributes']['age']
		   else:
			age = "unknown"
		   
		   if "gender" in data:
			gender = jsondata[0]['faceAttributes']['gender']
		   else:
			gender = "unknown"
			
		   if "sideburns" in data:
			sideburns = jsondata[0]['faceAttributes']['facialHair']['sideburns']
		   else:
			sideburns = "unknown"	
			
		   if "moustache" in data:
			moustache = str(jsondata[0]['faceAttributes']['facialHair']['moustache'])
		   else:
			moustache = "unknown"

		   if "underLipTop" in data:
			underLipTop_y = str(jsondata[0]['faceLandmarks']['underLipTop']['y'])
		   else:
			underLipTop_y = "unknown"		
			
		   if "underLipTop" in data:
			underLipTop_x = str(jsondata[0]['faceLandmarks']['underLipTop']['x']) 
		   else: 
			underLipTop_x = "unknown"
			
		   if "noseTip" in data:
			noseTip_y = str(jsondata[0]['faceLandmarks']['noseTip']['y']) 
		   else: 
			noseTip_y = "unknown"

		   if "noseTip" in data:
			noseTip_x = str(jsondata[0]['faceLandmarks']['noseTip']['x']) 
		   else: 
			noseTip_x = "unknown"

		   if "upperLipBottom" in data:
			upperLipBottom_y = str(jsondata[0]['faceLandmarks']['upperLipBottom']['y']) 
		   else: 
			upperLipBottom_y = "unknown"

		   if "upperLipBottom" in data:
			upperLipBottom_x = str(jsondata[0]['faceLandmarks']['upperLipBottom']['x']) 
		   else: 
			upperLipBottom_x = "unknown"

		   if "noseLeftAlarTop" in data:
			noseLeftAlarTop_y = str(jsondata[0]['faceLandmarks']['noseLeftAlarTop']['y']) 
		   else: 
			noseLeftAlarTop_y = "unknown"

		   if "noseLeftAlarTop" in data:
			noseLeftAlarTop_x = str(jsondata[0]['faceLandmarks']['noseLeftAlarTop']['x']) 
		   else: 
			noseLeftAlarTop_x = "unknown"

		   if "eyebrowLeftOuter" in data:
			eyebrowLeftOuter_y = str(jsondata[0]['faceLandmarks']['eyebrowLeftOuter']['y']) 
		   else: 
			eyebrowLeftOuter_y = "unknown"

		   if "eyebrowLeftOuter" in data:
			eyebrowLeftOuter_x = str(jsondata[0]['faceLandmarks']['eyebrowLeftOuter']['x']) 
		   else: 
			eyebrowLeftOuter_x = "unknown"

		   if "eyeLeftBottom" in data:
			eyeLeftBottom_y = str(jsondata[0]['faceLandmarks']['eyeLeftBottom']['y']) 
		   else: 
			eyeLeftBottom_y = "unknown"

		   if "eyeLeftBottom" in data:
			eyeLeftBottom_x = str(jsondata[0]['faceLandmarks']['eyeLeftBottom']['x']) 
		   else: 
			eyeLeftBottom_x = "unknown"

		   if "pupilLeft" in data:
			pupilLeft_y = str(jsondata[0]['faceLandmarks']['pupilLeft']['y']) 
		   else: 
			pupilLeft_y = "unknown"

		   if "pupilLeft" in data:
			pupilLeft_x = str(jsondata[0]['faceLandmarks']['pupilLeft']['x']) 
		   else: 
			pupilLeft_x = "unknown"

		   if "upperLipTop" in data:
			upperLipTop_y = str(jsondata[0]['faceLandmarks']['upperLipTop']['y']) 
		   else: 
			upperLipTop_y = "unknown"

		   if "upperLipTop" in data:
			upperLipTop_x = str(jsondata[0]['faceLandmarks']['upperLipTop']['x']) 
		   else: 
			upperLipTop_x = "unknown"

		   if "eyeLeftInner" in data:
			eyeLeftInner_y = str(jsondata[0]['faceLandmarks']['eyeLeftInner']['y']) 
		   else: 
			eyeLeftInner_y = "unknown"

		   if "eyeLeftInner" in data:
			eyeLeftInner_x = str(jsondata[0]['faceLandmarks']['eyeLeftInner']['x']) 
		   else: 
			eyeLeftInner_x = "unknown"

		   if "eyeRightInner" in data:
			eyeRightInner_y = str(jsondata[0]['faceLandmarks']['eyeRightInner']['y']) 
		   else: 
			eyeRightInner_y = "unknown"

		   if "eyeRightInner" in data:
			eyeRightInner_x = str(jsondata[0]['faceLandmarks']['eyeRightInner']['x']) 
		   else: 
			eyeRightInner_x = "unknown"

		   if "eyeLeftTop" in data:
			eyeLeftTop_y = str(jsondata[0]['faceLandmarks']['eyeLeftTop']['y']) 
		   else: 
			eyeLeftTop_y = "unknown"

		   if "eyeLeftTop" in data:
			eyeLeftTop_x = str(jsondata[0]['faceLandmarks']['eyeLeftTop']['x']) 
		   else: 
			eyeLeftTop_x = "unknown"

		   if "mouthLeft" in data:
			mouthLeft_y = str(jsondata[0]['faceLandmarks']['mouthLeft']['y']) 
		   else: 
			mouthLeft_y = "unknown"

		   if "mouthLeft" in data:
			mouthLeft_x = str(jsondata[0]['faceLandmarks']['mouthLeft']['x']) 
		   else: 
			mouthLeft_x = "unknown"

		   if "noseRightAlarTop" in data:
			noseRightAlarTop_y = str(jsondata[0]['faceLandmarks']['noseRightAlarTop']['y']) 
		   else: 
			noseRightAlarTop_y = "unknown"

		   if "noseRightAlarTop" in data:
			noseRightAlarTop_x = str(jsondata[0]['faceLandmarks']['noseRightAlarTop']['x']) 
		   else: 
			noseRightAlarTop_x = "unknown"

		   if "eyebrowRightInner" in data:
			eyebrowRightInner_y = str(jsondata[0]['faceLandmarks']['eyebrowRightInner']['y']) 
		   else: 
			eyebrowRightInner_y = "unknown"

		   if "eyebrowRightInner" in data:
			eyebrowRightInner_x = str(jsondata[0]['faceLandmarks']['eyebrowRightInner']['x']) 
		   else: 
			eyebrowRightInner_x = "unknown"

		   if "noseLeftAlarOutTip" in data:
			noseLeftAlarOutTip_y = str(jsondata[0]['faceLandmarks']['noseLeftAlarOutTip']['y']) 
		   else: 
			noseLeftAlarOutTip_y = "unknown"

		   if "noseLeftAlarOutTip" in data:
			noseLeftAlarOutTip_x = str(jsondata[0]['faceLandmarks']['noseLeftAlarOutTip']['x']) 
		   else: 
			noseLeftAlarOutTip_x = "unknown"

		   if "noseRightAlarOutTip" in data:
			noseRightAlarOutTip_y = str(jsondata[0]['faceLandmarks']['noseRightAlarOutTip']['y']) 
		   else: 
			noseRightAlarOutTip_y = "unknown"

		   if "noseRightAlarOutTip" in data:
			noseRightAlarOutTip_x = str(jsondata[0]['faceLandmarks']['noseRightAlarOutTip']['x']) 
		   else: 
			noseRightAlarOutTip_x = "unknown"

		   if "noseRootRight" in data:
			noseRootRight_y = str(jsondata[0]['faceLandmarks']['noseRootRight']['y']) 
		   else: 
			noseRootRight_y = "unknown"

		   if "noseRootRight" in data:
			noseRootRight_x = str(jsondata[0]['faceLandmarks']['noseRootRight']['x']) 
		   else: 
			noseRootRight_x = "unknown"

		   if "eyeLeftOuter" in data:
			eyeLeftOuter_y = str(jsondata[0]['faceLandmarks']['eyeLeftOuter']['y']) 
		   else: 
			eyeLeftOuter_y = "unknown"

		   if "eyeLeftOuter" in data:
			eyeLeftOuter_x = str(jsondata[0]['faceLandmarks']['eyeLeftOuter']['x']) 
		   else: 
			eyeLeftOuter_x = "unknown"

		   if "underLipBottom" in data:
			underLipBottom_y = str(jsondata[0]['faceLandmarks']['underLipBottom']['y']) 
		   else: 
			underLipBottom_y = "unknown"

		   if "underLipBottom" in data:
			underLipBottom_x = str(jsondata[0]['faceLandmarks']['underLipBottom']['x']) 
		   else: 
			underLipBottom_x = "unknown"

		   if "eyeRightTop" in data:
			eyeRightTop_y = str(jsondata[0]['faceLandmarks']['eyeRightTop']['y']) 
		   else: 
			eyeRightTop_y = "unknown"

		   if "eyeRightTop" in data:
			eyeRightTop_x = str(jsondata[0]['faceLandmarks']['eyeRightTop']['x']) 
		   else: 
			eyeRightTop_x = "unknown"

		   if "eyeRightOuter" in data:
			eyeRightOuter_y = str(jsondata[0]['faceLandmarks']['eyeRightOuter']['y']) 
		   else: 
			eyeRightOuter_y = "unknown"

		   if "eyeRightOuter" in data:
			eyeRightOuter_x = str(jsondata[0]['faceLandmarks']['eyeRightOuter']['x']) 
		   else: 
			eyeRightOuter_x = "unknown"

		   if "noseRootLeft" in data:
			noseRootLeft_y = str(jsondata[0]['faceLandmarks']['noseRootLeft']['y']) 
		   else: 
			noseRootLeft_y = "unknown"

		   if "noseRootLeft" in data:
			noseRootLeft_x = str(jsondata[0]['faceLandmarks']['noseRootLeft']['x']) 
		   else: 
			noseRootLeft_x = "unknown"

		   if "eyebrowRightOuter" in data:
			eyebrowRightOuter_y = str(jsondata[0]['faceLandmarks']['eyebrowRightOuter']['y']) 
		   else: 
			eyebrowRightOuter_y = "unknown"

		   if "eyebrowRightOuter" in data:
			eyebrowRightOuter_x = str(jsondata[0]['faceLandmarks']['eyebrowRightOuter']['x']) 
		   else: 
			eyebrowRightOuter_x = "unknown"

		   if "eyeRightBottom" in data:
			eyeRightBottom_y = str(jsondata[0]['faceLandmarks']['eyeRightBottom']['y']) 
		   else: 
			eyeRightBottom_y = "unknown"

		   if "eyeRightBottom" in data:
			eyeRightBottom_x = str(jsondata[0]['faceLandmarks']['eyeRightBottom']['x']) 
		   else: 
			eyeRightBottom_x = "unknown"

		   if "eyebrowLeftInner" in data:
			eyebrowLeftInner_y = str(jsondata[0]['faceLandmarks']['eyebrowLeftInner']['y']) 
		   else: 
			eyebrowLeftInner_y = "unknown"

		   if "eyebrowLeftInner" in data:
			eyebrowLeftInner_x = str(jsondata[0]['faceLandmarks']['eyebrowLeftInner']['x']) 
		   else: 
			eyebrowLeftInner_x = "unknown"

		   if "mouthRight" in data:
			mouthRight_y = str(jsondata[0]['faceLandmarks']['mouthRight']['y']) 
		   else: 
			mouthRight_y = "unknown"

		   if "mouthRight" in data:
			mouthRight_x = str(jsondata[0]['faceLandmarks']['mouthRight']['x']) 
		   else: 
			mouthRight_x = "unknown"

		   if "pupilRight" in data:
			pupilRight_y = str(jsondata[0]['faceLandmarks']['pupilRight']['y']) 
		   else: 
			pupilRight_y = "unknown"

		   if "pupilRight" in data:
			pupilRight_x = str(jsondata[0]['faceLandmarks']['pupilRight']['x']) 
		   else: 
			pupilRight_x = "unknown"	
			
		   #print(age);
		   #print(gender);
		   userid=filename.split("/")
		   userid=userid[5]
		   userid=userid.split("\\")
		   #print(userid[1])
		   userid_list.append(userid[1])
		   age_list.append(age)
		   gender_list.append(gender)
		   sideburns_list.append(sideburns)
		   moustache_list.append(moustache)
		   underLipTop_y_list.append(underLipTop_y)
		   underLipTop_x_list.append(underLipTop_x)
		   noseTip_y_list.append(noseTip_y) 
		   noseTip_x_list.append(noseTip_x) 
		   upperLipBottom_y_list.append(upperLipBottom_y) 
		   upperLipBottom_x_list.append(upperLipBottom_x) 
		   noseLeftAlarTop_y_list.append(noseLeftAlarTop_y) 
		   noseLeftAlarTop_x_list.append(noseLeftAlarTop_x) 
		   eyebrowLeftOuter_y_list.append(eyebrowLeftOuter_y) 
		   eyebrowLeftOuter_x_list.append(eyebrowLeftOuter_x) 
		   eyeLeftBottom_y_list.append(eyeLeftBottom_y) 
		   eyeLeftBottom_x_list.append(eyeLeftBottom_x) 
		   pupilLeft_y_list.append(pupilLeft_y) 
		   pupilLeft_x_list.append(pupilLeft_x) 
		   upperLipTop_y_list.append(upperLipTop_y) 
		   upperLipTop_x_list.append(upperLipTop_x) 
		   eyeLeftInner_y_list.append(eyeLeftInner_y) 
		   eyeLeftInner_x_list.append(eyeLeftInner_x) 
		   eyeRightInner_y_list.append(eyeRightInner_y) 
		   eyeRightInner_x_list.append(eyeRightInner_x) 
		   eyeLeftTop_y_list.append(eyeLeftTop_y) 
		   eyeLeftTop_x_list.append(eyeLeftTop_x) 
		   mouthLeft_y_list.append(mouthLeft_y) 
		   mouthLeft_x_list.append(mouthLeft_x) 
		   noseRightAlarTop_y_list.append(noseRightAlarTop_y) 
		   noseRightAlarTop_x_list.append(noseRightAlarTop_x) 
		   eyebrowRightInner_y_list.append(eyebrowRightInner_y) 
		   eyebrowRightInner_x_list.append(eyebrowRightInner_x) 
		   noseLeftAlarOutTip_y_list.append(noseLeftAlarOutTip_y) 
		   noseLeftAlarOutTip_x_list.append(noseLeftAlarOutTip_x) 
		   noseRightAlarOutTip_y_list.append(noseRightAlarOutTip_y) 
		   noseRightAlarOutTip_x_list.append(noseRightAlarOutTip_x) 
		   noseRootRight_y_list.append(noseRootRight_y) 
		   noseRootRight_x_list.append(noseRootRight_x) 
		   eyeLeftOuter_y_list.append(eyeLeftOuter_y) 
		   eyeLeftOuter_x_list.append(eyeLeftOuter_x) 
		   underLipBottom_y_list.append(underLipBottom_y) 
		   underLipBottom_x_list.append(underLipBottom_x) 
		   eyeRightTop_y_list.append(eyeRightTop_y) 
		   eyeRightTop_x_list.append(eyeRightTop_x) 
		   eyeRightOuter_y_list.append(eyeRightOuter_y) 
		   eyeRightOuter_x_list.append(eyeRightOuter_x) 
		   noseRootLeft_y_list.append(noseRootLeft_y) 
		   noseRootLeft_x_list.append(noseRootLeft_x) 
		   eyebrowRightOuter_y_list.append(eyebrowRightOuter_y) 
		   eyebrowRightOuter_x_list.append(eyebrowRightOuter_x) 
		   eyeRightBottom_y_list.append(eyeRightBottom_y) 
		   eyeRightBottom_x_list.append(eyeRightBottom_x) 
		   eyebrowLeftInner_y_list.append(eyebrowLeftInner_y) 
		   eyebrowLeftInner_x_list.append(eyebrowLeftInner_x) 
		   mouthRight_y_list.append(mouthRight_y) 
		   mouthRight_x_list.append(mouthRight_x) 
		   pupilRight_y_list.append(pupilRight_y) 
		   pupilRight_x_list.append(pupilRight_x)
		   #output_list = [];
		   #output_list.append(filename)
		   #output_list.append(age)
		   #output_list.append(gender)
		   #wr = csv.writer(resultFile, dialect='excel')
		   #wr.writerow(age_list)
		   conn.close()
		   resultFile = open("pythonoutput.csv",'wb')
		   wr = csv.writer(resultFile, dialect='excel')
		   #wr.writerow(age_list)
		   rows = zip(userid_list,age_list,gender_list,sideburns_list,moustache_list,underLipTop_y_list,underLipTop_x_list,noseTip_y_list,noseTip_x_list,upperLipBottom_y_list,upperLipBottom_x_list,noseLeftAlarTop_y_list,noseLeftAlarTop_x_list,eyebrowLeftOuter_y_list,eyebrowLeftOuter_x_list,eyeLeftBottom_y_list,eyeLeftBottom_x_list,pupilLeft_y_list,pupilLeft_x_list,upperLipTop_y_list,upperLipTop_x_list,eyeLeftInner_y_list,eyeLeftInner_x_list,eyeRightInner_y_list,eyeRightInner_x_list,eyeLeftTop_y_list,eyeLeftTop_x_list,mouthLeft_y_list,mouthLeft_x_list,noseRightAlarTop_y_list,noseRightAlarTop_x_list,eyebrowRightInner_y_list,eyebrowRightInner_x_list,noseLeftAlarOutTip_y_list,noseLeftAlarOutTip_x_list,noseRightAlarOutTip_y_list,noseRightAlarOutTip_x_list,noseRootRight_y_list,noseRootRight_x_list,eyeLeftOuter_y_list,eyeLeftOuter_x_list,underLipBottom_y_list,underLipBottom_x_list,eyeRightTop_y_list,eyeRightTop_x_list,eyeRightOuter_y_list,eyeRightOuter_x_list,noseRootLeft_y_list,noseRootLeft_x_list,eyebrowRightOuter_y_list,eyebrowRightOuter_x_list,eyeRightBottom_y_list,eyeRightBottom_x_list,eyebrowLeftInner_y_list,eyebrowLeftInner_x_list,mouthRight_y_list,mouthRight_x_list,pupilRight_y_list,pupilRight_x_list)
		   for row in rows:
			   wr.writerow(row)
		#else:
		#   print("do nothing!")
   

print(age_list)
print(gender_list)
print(userid_list)
print(sideburns_list)
print(moustache_list)
print(underLipTop_y_list)
print(underLipTop_x_list)

resultFile = open("pythonoutput.csv",'wb')
wr = csv.writer(resultFile, dialect='excel')
#wr.writerow(age_list)
rows = zip(userid_list,age_list,gender_list,sideburns_list,moustache_list,underLipTop_y_list,underLipTop_x_list,noseTip_y_list,noseTip_x_list,upperLipBottom_y_list,upperLipBottom_x_list,noseLeftAlarTop_y_list,noseLeftAlarTop_x_list,eyebrowLeftOuter_y_list,eyebrowLeftOuter_x_list,eyeLeftBottom_y_list,eyeLeftBottom_x_list,pupilLeft_y_list,pupilLeft_x_list,upperLipTop_y_list,upperLipTop_x_list,eyeLeftInner_y_list,eyeLeftInner_x_list,eyeRightInner_y_list,eyeRightInner_x_list,eyeLeftTop_y_list,eyeLeftTop_x_list,mouthLeft_y_list,mouthLeft_x_list,noseRightAlarTop_y_list,noseRightAlarTop_x_list,eyebrowRightInner_y_list,eyebrowRightInner_x_list,noseLeftAlarOutTip_y_list,noseLeftAlarOutTip_x_list,noseRightAlarOutTip_y_list,noseRightAlarOutTip_x_list,noseRootRight_y_list,noseRootRight_x_list,eyeLeftOuter_y_list,eyeLeftOuter_x_list,underLipBottom_y_list,underLipBottom_x_list,eyeRightTop_y_list,eyeRightTop_x_list,eyeRightOuter_y_list,eyeRightOuter_x_list,noseRootLeft_y_list,noseRootLeft_x_list,eyebrowRightOuter_y_list,eyebrowRightOuter_x_list,eyeRightBottom_y_list,eyeRightBottom_x_list,eyebrowLeftInner_y_list,eyebrowLeftInner_x_list,mouthRight_y_list,mouthRight_x_list,pupilRight_y_list,pupilRight_x_list)
for row in rows:
	wr.writerow(row)