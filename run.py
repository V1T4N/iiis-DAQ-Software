#-*- coding:utf-8 -*-
import datetime
import cv2
import numpy as np
import h5py
import sys
import shutil

cmd_line = sys.argv[1].split(",")
video_dir = cmd_line[0] #実行時の引数をビデオファイルの引数とする。
print(video_dir)
print(cmd_line)

todaydetail = datetime.datetime.today()
todaydetail = str(todaydetail.year) + str(todaydetail.month) + str(todaydetail.day) + str(todaydetail.hour) + str(todaydetail.minute) + str(todaydetail.second)

for j in range(1,int(cmd_line[1])+1):
    output_file = "out" + todaydetail +"split"+str(j) + ".h5"
    #output_file = video_file + ".h5"

    print(output_file)
    h5file = h5py.File(output_file,'w')

    print(video_dir + "\msCam" + str(j) + ".avi")
    cap = cv2.VideoCapture(video_dir + "\msCam" + str(j) + ".avi")
    video_frame = cap.get(cv2.CAP_PROP_FRAME_COUNT)


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

        print(j,"of" ,cmd_line[1],"frame",i,"/",video_frame)

    if(j == 1):
        data_temp = np.array(data)
        print(data_temp.shape)
    else:
        data_temp = np.concatenate([data_temp,data],axis = 0)
        print(data_temp.shape)



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
    print("out" + todaydetail +"split"+str(j) + ".h5")
    shutil.move(output_file, 'h5data')


output_file2 = "out" + todaydetail +"_" +str(j)+"file_merged" + ".h5"
h5file2 = h5py.File(output_file2,'w')

try:
    h5file2.create_dataset('object',data= data_temp)
    h5file2.flush()

except:
    _ = 0   

h5file2.flush()
h5file2.close()

print("merge completed")
print("out" + todaydetail +"_" +str(j)+"file_merged" + ".h5")
shutil.move(output_file2, 'h5data')