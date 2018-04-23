#library of openCV
import cv2

#first, we define main program as a function    
def main():

    #here 0 means the first webcam, you can use 1 to sepcify the second, and so on
    _cap = cv2.VideoCapture(0)
    
    #if you want to specify webcam resolution
    #x (horizontal)
    #x = 1024
    #_cap.set(3,x);
    #y (vertical)
    #y=768
    #_cap.set(4,y)

    try:
        while(True): #repeartly do the following except 1) press q or 2) exception
            
            ret, _frame = _cap.read() #read a frame from the webcam
                        
            _my_name = "Dan Shor"
            
            cv2.putText(_frame,'Name: - %s'%_my_name,(100, 100),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
            
            cv2.imshow("My Mirror", _frame)#show the image in a windows
                                    
            if cv2.waitKey(1) & 0xFF == ord('q'): #specify how to quit the program
                break
   
    except (KeyboardInterrupt, SystemExit):
        print("wrong exit") 

    _cap.release() # When everything done, release the capture
    
    cv2.destroyAllWindows() #destroy the cv windows
        
    print ("Main program finished") #specify that main program is finished

#here is the start of the main program
if __name__ == '__main__':
    main()