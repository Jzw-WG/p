import cv2
import numpy as np
import matplotlib.pyplot as plt    # Python的2D绘图库

# 读取图像
"""
RGB 与 BGR:R代表红，red ;  G代表绿，green; B代表蓝，blue。RGB模式就是，色彩数据模式，R在高位，G在中间，B在低位。BGR正好相反。
使用函数cv2.imread(filepath,flags)读入一副图片
filepath：要读入图片的完整路径
flags：读入图片的标志 
cv2.IMREAD_COLOR：默认参数，读入一副彩色图片，忽略alpha通道
cv2.IMREAD_GRAYSCALE：读入灰度图片
cv2.IMREAD_UNCHANGED：顾名思义，读入完整图片，包括alpha通道
import numpy as npimport cv2img = cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)
"""
img = cv2.imread('C:\\Users\\Administrator\\Desktop\\asd\\1.jpg')    # cv2.imread()接口读图像，读进来直接是BGR 格式数据格式在 0~255，通道格式为(H,W,C)
KIKI_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # cv2.cvtColor() 颜色空间转换函数。 cv2.COLOR_BGR2RGB 将BGR转为RGB颜色空间

# 灰度化处理图像
grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)   # cv2.cvtColor() 颜色空间转换函数。 cv2.COLOR_BGR2GRAY 将BGR转为灰色颜色空间

# 先通过高斯滤波降噪
"""
C++: void GaussianBlur(InputArray src, OutputArray dst, Size ksize, double sigmaX, double sigmaY=0, int borderType=BORDER_DEFAULT )
InputArray src: 输入图像，可以是Mat类型，图像深度为CV_8U、CV_16U、CV_16S、CV_32F、CV_64F。 

OutputArray dst: 输出图像，与输入图像有相同的类型和尺寸。
double sigmaX: 高斯核函数在X方向上的标准偏差 
double sigmaY: 高斯核函数在Y方向上的标准偏差，如果sigmaY是0，则函数会自动将sigmaY的值设置为与sigmaX相同的值，如果sigmaX和sigmaY都是0，这两个值将由ksize.width和ksize.height计算而来。具体可以参考getGaussianKernel()函数查看具体细节。建议将size、sigmaX和sigmaY都指定出来。 
int borderType=BORDER_DEFAULT: 推断图像外部像素的某种便捷模式，有默认值BORDER_DEFAULT，如果没有特殊需要不用更改，具体可以参考borderInterpolate()函数。

Size ksize: 高斯内核大小，这个尺寸与前面两个滤波kernel尺寸不同，
ksize.width和ksize.height可以不相同但是这两个值必须为正奇数，如果这两个值为0，他们的值将由sigma计算。
"""
gaussian = cv2.GaussianBlur(grayImage, (3,3), 0)

# 再通过拉普拉斯算子做边缘检测
"""
cv2.CV_16S：depth参数，输出图像的深度（数据类型），可以使用-1，与原图像保持一致 .目标图像的深度必须大于等于原图像的深度；

Laplacian函数求完导数后会有负值，还有会大于255的值。而原图像是uint8，即8位无符号数，所以Laplacian建立的图像位数不够，会有截断。因此要使用16位有符号的数据类型，即cv2.CV_16S。

ksize是算子的大小，必须为奇数。默认为1。
"""
"""
convertScaleAbs():在经过处理后，要用convertScaleAbs()函数将其转回原来的uint8形式。否则将无法显示图像，而只是一副灰色的窗口。
"""
dst = cv2.Laplacian(gaussian, cv2.CV_16S, ksize=3)
LOG = cv2.convertScaleAbs(dst)

# 用来正常显示中文标签
"""
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
"""
plt.rcParams['font.sans-serif'] = ['SimHei']

# 显示图形
"""
u'': 保持源码文件的utf-8不变.这个u表示将后面跟的字符串以unicode格式存储。
python会根据代码第一行标称的utf-8编码识别代码中的汉字’哈’，然后转换成unicode对象
"""
titles = [u'原始图像', u'LOG算子']   #列表
images = [KIKI_img, LOG]
"""
plt.subplot: 其中各个参数也可以用逗号,分隔开。第一个参数代表子图的行数；
第二个参数代表该行图像的列数； 第三个参数代表每行的第几个图像。

plt.xticks([-1,0,1],['-1','0','1']) : 第一个：对应X轴上的值，第二个：显示的文字
"""
for i in range(2):
    plt.subplot(1, 2, i + 1), plt.imshow(images[i],'gray')  # camp参数  gray : 显示灰度图（如果没有则是热量图）
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
