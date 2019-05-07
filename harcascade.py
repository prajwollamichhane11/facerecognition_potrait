import cv2
import PIL
from PIL import Image
from PIL import ImageFilter

#defining cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
 
#loading a webcam
cap = cv2.VideoCapture(0)

while True:
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,1.3,5)
    
    #after faces are found
    for (x,y,w,h) in faces:
        #roi = region of the image 
        roi_color = img[y:y+h, x:x+w] #{starting_point:ending_point}
        eyes = eye_cascade.detectMultiScale(roi_color)
        
        
        im_x = x-55
        im_y = y-65
        im_w = x+w+70
        im_h = y+w+50
        tauko = (im_x,im_y,im_w,im_h)
        
        
        for(ex,ey,ew,eh) in eyes:
            #cv2.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,0,0) ,2)
            ''' '''
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27: #Meaning Quits on ESC pressing
        break
    elif k == ord('s'):
        cv2.imwrite('mypic.png',img)
        im = Image.open("./mypic.png")
        imout = im.filter(ImageFilter.DETAIL)
        imout = im.filter(ImageFilter.EDGE_ENHANCE_MORE)
        cropped_image = im.crop(tauko)
        blurred_image = im.filter(ImageFilter.GaussianBlur(radius = 2))
        blurred_image.paste(cropped_image,tauko)        
        blurred_image.save("pot_mypic.png")
        blurred_image.show()
    
cap.release()
cv2.destroyAllWindows()
