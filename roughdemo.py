import numpy as np
import cv2
import pandas as pd
import PIL
from PIL import Image
	# for color image
Y_ax=[]
X_ax=[]
def click_event(event, x, y, flags, params): 
  
	# checking for right mouse clicks      
	if event==cv2.EVENT_RBUTTONDOWN or event == cv2.EVENT_LBUTTONDOWN: 

		print(x, ' ', y)
		red_image = PIL.Image.open(r"C:\Users\91759\Desktop\screenshot.jpg")
		red_image_rgb = red_image.convert("RGB")
		rgb_pixel_value = red_image_rgb.getpixel((x,y))
		print("color is ",rgb_pixel_value)
		params.append(rgb_pixel_value)
		print('Colors Seleted till now',params)

		font = cv2.FONT_HERSHEY_SIMPLEX 
		b = img[y, x, 0] 
		g = img[y, x, 1] 
		r = img[y, x, 2] 
		cv2.putText(img, str(b) + ',' +
					str(g) + ',' + str(r), 
					(x,y), font, 1, 
					(255, 255, 0), 2) 
		cv2.imshow('image', img)
		
#import xlsxwriter  

if __name__=="__main__": 
  
	# reading the image 

	img = cv2.imread(r"C:\Users\91759\Desktop\screenshot.jpg", 1)
	#img = cv2.imread(r"C:\Users\91759\Desktop\bar.png", 1)
  
	# displaying the image 
	cv2.imshow('image', img)
	print('Close the image window after selecting the color') 
	z=[]
	cv2.setMouseCallback('image', click_event,z)
	#print(h) 
	print(z)
	# wait for a key to be pressed to exit 
	cv2.waitKey(0) 
	save_path=r"C:\Users\91759\Desktop\lama.xlsx"
	# close the window 
	cv2.destroyAllWindows()
	
	Curves={}
	writer=pd.ExcelWriter(save_path, engine='xlsxwriter')
	for i in range(len(z)):
		color = z[i]
		X=[]
		Y=[]
		print(color)
		im = Image.open(r"C:\Users\91759\Desktop\screenshot.jpg")
		rgb_im = im.convert('RGB')
		df=pd.DataFrame()		
		print(rgb_im.size[0])
		for x in range(0,rgb_im.size[0]):
			for y in range(0,rgb_im.size[1]):
				r, g, b = rgb_im.getpixel((x, y))
				if (r,g,b) == color:
					temp=[x,rgb_im.size[1]-y]
					X.append(temp)
		df=pd.DataFrame(X,columns=["X","Y"])
		df.to_excel(writer,sheet_name='Color'+str(i+1),index=False)
	writer.save()
