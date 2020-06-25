import numpy as np 
import cv2 
import time 
import datetime

def camera(): 
    cap = cv2.VideoCapture("trans.mp4")#打开一个视频 
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')#设置保存图片格式 
    out = cv2.VideoWriter(datetime.datetime.now().strftime("%A_%d_%B_%Y_%I_%M_%S%p")+'.avi',fourcc, 10.0, (768,576))#分辨率要和原视频对应 
    
    # ShiTomasi 角点检测参数 
    feature_params = dict( maxCorners = 100, 
                        qualityLevel = 0.05, 
                        minDistance = 7, 
                        blockSize = 7 ) 
    
    # lucas kanade光流法参数 
    lk_params = dict( winSize  = (15,15), 
                    maxLevel = 2, 
                    criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)) 
    
    # 创建随机颜色 
    color = np.random.randint(0,255,(100,3)) 
    
    # 获取第一帧，找到角点 
    ret, old_frame = cap.read() 
    #找到原始灰度图 
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY) 
    
    #获取图像中的角点，返回到p0中 
    p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params) 
    
    # 创建一个蒙版用来画轨迹 
    mask = np.zeros_like(old_frame) 
    
    while(1): 
        ret,frame = cap.read() #读取图像帧 
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #灰度化 
    
        # 计算光流 
        p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params) 
        # 选取好的跟踪点 
        good_new = p1[st==1] 
        good_old = p0[st==1] 
    
        # 画出轨迹 
        for i,(new,old) in enumerate(zip(good_new,good_old)): 
            a,b = new.ravel()#多维数据转一维,将坐标转换后赋值给a，b 
            c,d = old.ravel() 
            mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)#画直线 
            frame = cv2.circle(frame,(a,b),5,color[i].tolist(),-1)#画点 
        img = cv2.add(frame,mask) # 将画出的线条进行图像叠加 
    
        cv2.imshow('frame',img)  #显示图像 
    
        out.write(img)#保存每一帧画面 
    
        k = cv2.waitKey(30) & 0xff #按Esc退出检测 
        if k == 27: 
            break 
    
        # 更新上一帧的图像和追踪点 
        old_gray = frame_gray.copy() 
        p0 = good_new.reshape(-1,1,2) 
    
    
    out.release()#释放文件 
    cap.release() 
    cv2.destoryAllWindows()#关闭所有窗口 

def picture():
    old_frame = cv2.imread("3.jpg")
    frame = cv2.imread("3.jpg")
    # ShiTomasi 角点检测参数 
    feature_params = dict( maxCorners = 100, 
                        qualityLevel = 0.05, 
                        minDistance = 7, 
                        blockSize = 7 ) 
    
    # lucas kanade光流法参数 
    lk_params = dict( winSize  = (15,15), 
                    maxLevel = 2, 
                    criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)) 
    
    # 创建随机颜色 
    color = np.random.randint(0,255,(100,3)) 
    
    #找到原始灰度图 
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY) 
    
    #获取图像中的角点，返回到p0中 
    p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params) 
    
    # 创建一个蒙版用来画轨迹 
    mask = np.zeros_like(old_frame) 
    
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) #灰度化 

    # 计算光流 
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params) 
    # 选取好的跟踪点 
    good_new = p1[st==1] 
    good_old = p0[st==1] 

    # 画出轨迹 
    for i,(new,old) in enumerate(zip(good_new,good_old)): 
        a,b = new.ravel()#多维数据转一维,将坐标转换后赋值给a，b 
        c,d = old.ravel() 
        mask = cv2.line(mask, (a,b),(c,d), color[i].tolist(), 2)#画直线 
        frame = cv2.circle(frame,(a,b),1,color[i].tolist(),-1)#画点 
    img = cv2.add(frame,mask) # 将画出的线条进行图像叠加 

    cv2.imshow('frame',img)  #显示图像 

    cv2.waitKey(0) 
    
    cv2.destoryAllWindows()#关闭所有窗口 

if __name__ == "__main__":
    picture()
