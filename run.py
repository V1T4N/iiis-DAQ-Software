#-*- coding:utf-8 -*-
import datetime
import cv2
import numpy as np
import h5py
import sys
import shutil

video_file = sys.argv[1] #実行時の引数をビデオファイルの引数とする。
print(video_file)

todaydetail = datetime.datetime.today()
todaydetail = str(todaydetail.year) + str(todaydetail.month) + str(todaydetail.day) + str(todaydetail.hour) + str(todaydetail.minute) + str(todaydetail.second)


output_file = "out" + todaydetail + ".h5"
#output_file = video_file + ".h5"

print(output_file)
h5file = h5py.File(output_file,'w')


cap = cv2.VideoCapture(video_file)


i = 0
while(cap.isOpened()):# 動画終了まで繰り返し 
    try:
        ret, frame = cap.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#グレースケールに変換
        gray_frame = np.reshape(gray_frame, (1, *gray_frame.shape))#(1,px,px)に変換
        #print(gray_frame.shape)

    except:
        break

    
    try:
        if (i == 0):
            data = np.array(gray_frame)
            
        else:
            #data = np.dstack((data,frame))
            data = np.concatenate([data,gray_frame],axis = 0)  #フレームをaxis = 0　方向に重ねていく
    except:
        break
    
        # qキーが押されたら途中終了
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    i = i + 1



try:
    h5file.create_dataset('object',data= data)
    h5file.flush()

except:
    _ = 0    


h5file.flush()
h5file.close()
cap.release()
cv2.destroyAllWindows()
print("completed")
print( "output file = " +"out" + todaydetail + ".h5")

shutil.move(output_file, 'h5data')