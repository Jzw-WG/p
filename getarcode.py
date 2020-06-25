def get_qrcode_from_image(self):
        gray = cv2.cvtColor(self.src_image, cv2.COLOR_BGR2GRAY)

        cv2.imshow('1',gray)
        cv2.waitKey()
        gradX = cv2.Sobel(gray, cv2.CV_32F, 1, 0,-1)
        gradY = cv2.Sobel(gray, cv2.CV_32F, 0, 1,-1)

        # 3，将过滤得到的X方向像素值减去Y方向的像素值：

        gradient = cv2.subtract(gradX, gradY)

        # 4，先缩放元素再取绝对值，最后转换格式为8bit型

        gradient = cv2.convertScaleAbs(gradient)

        # 5，均值滤波取二值化：

        blurred = cv2.blur(gradient, (9, 9))
        (_, thresh) = cv2.threshold(blurred, 160, 160, cv2.THRESH_BINARY)

        cv2.imshow('1',blurred)
        cv2.waitKey()
        # 6，腐蚀和膨胀的函数：

        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (21, 7))
        closed = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

        closed = cv2.erode(closed, None, iterations = 4)
        closed = cv2.dilate(closed, None, iterations = 4)

        # 7，找到边界findContours函数

        cnts,hierarchy = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

        # 8，计算出包围目标的最小矩形区域：

        c = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
        rect = cv2.minAreaRect(c)
        box = np.int0(cv2.boxPoints(rect))
        if box.any() != None:
        # 这下面的3步得到扫描区域，扫描区域要比检测出来的位置要大
            min = np.min(box, axis=0)
            max = np.max(box, axis=0)

            roi = self.src_image[min[1] - 10:max[1] + 10, min[0] - 10:max[0] + 10]
            print (roi.shape)
            cv2.imshow('1',roi)
            cv2.waitKey()
            # 把区域里的二维码传换成RGB，并把它转换成pil里面的图像，因为zbar得调用pil里面的图像，而不能用opencv的图像
            roi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
            pil = Image.fromarray(self.src_image).convert('L')
            width, height = pil.size
            raw = pil.tobytes()