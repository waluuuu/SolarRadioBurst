## 基于多源数据的太阳活动定位与爆发预判

### Solar activity localization and outburst prediction based on multi-source data

Ⅰ. 项目介绍(Project Introduction)：  
   中科院科创计划项目之一。
   现在完成：有无爆发的检测、二型爆、三型爆、其它类型爆发的检测。
   太阳射电爆发一共有五种类型，依照频谱特性的不同可以分为I、II、III、IV、V型爆发。每种类型的爆发如下图所示。
   ![image](https://user-images.githubusercontent.com/51266570/150719173-14f03ae5-09b1-4273-ae0b-2ba004c7b89c.png)
   
   使用深度学习，将使用learmonth天文台数据训练好的网络，用于culgoora天文台爆发检测； 
   编写软件，选择图片，自动检测（现在有BUG，本次检测的结果，只有在检测下一张图片时才会显示）； 
   花费大量的时间制作了数据集，但是还不完善，I型爆和IV型爆没有细分，涵盖的噪声情况较少，容易把噪声识别为爆发。

   * 1.数据获取(Data collection)：  
   从澳大利亚国家气象局下载learmonth和culgoora两个天文台原始数据和日志，根据日志进行图片分割，制作了数据集  
   * 2.数字图像预处理(Digital image preprocessing)：  
   尝试了自适应二值化、图像形态学、通道归一化、直方图均衡等方法  
   最终使用通道归一化，直方图均衡和图像分割处理数据  
     *（1）通道归一化(Channel normalization)
     
     主要目的是减小条纹状噪声，从而掩盖条纹状噪声后面的突发变得更加可识别。公式如下：
     
     ![image](https://user-images.githubusercontent.com/51266570/150720319-a3a013b9-d117-48bb-9e88-1b8e16663991.png)
    
     其中f表示频谱的数据矩阵，g是通道归一化之后的处理结果。fLM是每个通道的均值。图 2.1展示了一个通道去噪后的例子。可以发现，对比图2.1中的两张图，条纹噪声得到了明显的改善，II型爆发的特征更加明显了。
      
      ![image](https://user-images.githubusercontent.com/51266570/150720934-30b8d808-48a6-42fb-ba82-89f6569a780f.png)
      
      ![image](https://user-images.githubusercontent.com/51266570/150721085-3d9c32de-6e05-4641-aab0-ed201fca24d2.png)

       图2.1.1 通道归一化处理前后对比图
       
      *（2）直方图均衡(Histogram equalization)
      
      对于m行n列的矩阵利用公式2.2求出图像像素总数，并利用公式2.3进行归一化
      
      ![image](https://user-images.githubusercontent.com/51266570/150720768-7b75376a-6919-4382-91b1-37d1c5ddda35.png)
      
      ![image](https://user-images.githubusercontent.com/51266570/150720802-b851ab5a-1a25-4b3e-98ab-be16bc9c8d7f.png)
      
      接着计算图像的灰度级的累计分布hp，并求出增强图像g的均衡值。
      
      ![image](https://user-images.githubusercontent.com/51266570/150720833-cfb178a6-dce1-4f1b-b3b4-375f151e3628.png)
      
      ![image](https://user-images.githubusercontent.com/51266570/150720842-25c395e5-ca96-477a-800d-45a61730b62c.png)
      
      使输入图像的直方图分布变的均匀，这样就会使图像的灰度级增加，从而可达到增强局部的对比度而不影响整体的对比度的效果，这对于背景和前景都太亮或者太暗的图像非常有用。
      
      ![image](https://user-images.githubusercontent.com/51266570/150721177-a80c6ff1-81f5-454c-8d08-5a3e1024162d.png)
      
      ![image](https://user-images.githubusercontent.com/51266570/150721194-6bb1ad3b-9b2a-42bc-9b23-2cde144e1aab.png)

      图2.1.2 直方图均衡处理前后对比图
      
      *（3）图像分割(Image segmentation)
      
      首先根据天文台的日志文件，确定日志中标明的爆发的时间，然后在原始文件中找到对应的时间，进行分割。原始数据使用uint8格式，用大端法存储。我们使用bytestream.read函数和numpy.frombuffer函数从中二进制文件中读取文件，提取header信息，并判断是否为所需的时段。
      
      
      ![QQ截图20220124122517](https://user-images.githubusercontent.com/51266570/150721886-5a518c36-7824-4680-9426-1f9a89001afd.png)
      
      图2.1.3Culgoora天文台的数据存储格式图
      


   * 3.深度学习模型(Deep learning model)：
   
     使用神经网络对太阳射电爆发图片进行分类，使用滑窗法进行爆发的检测  
     四分类模型是完成下列四种类型的分类：无爆发、II型爆、III型爆、其他类型的爆发。
     以下将以四分类模型为例，说明神经网络的构建过程。
     参考AlexNet的结构，本研究使用了相同结构的卷积神经网络，如下图所示，包含了三个卷积层和与之相对应的最大池化层，最后连接两个全连接层。
     
     ![image](https://user-images.githubusercontent.com/51266570/150722055-f69994db-fdc7-463f-9724-311a96aac934.png)
     
     图2.2.1 CNN网络结构图
     
   所有爆发的输入均为800×200的射电频谱图，在送入CNN网络之前，经过下采样，转换成400×100的图像。CNN的卷积层统一使用3×3的卷积，池化层统一使用2×2的池化核。卷积层和第一个密集连接层使用relu作为激活函数，最后一层使用softmax作为激活函数。
   经过C1层之后，获得32个特征图，每个大小为398×198，经过池化层之后，大小变为199×99。C2-P2、C3-P3也类似。
     
     ![image](https://user-images.githubusercontent.com/51266570/150722252-94ab4999-7901-4967-95bb-86d65bf0b898.png)

     图2.2.2 CNN网络参数图
     
   对于四分类，我们使用了通道归一化，通道归一化+直方图均衡两种方法处理，得到的结果如下所示
     
     ![QQ截图20220124123405](https://user-images.githubusercontent.com/51266570/150722610-e59ed31b-3a80-4260-89c2-845d2a0e1d6d.png)
     
     ![image](https://user-images.githubusercontent.com/51266570/150722635-ce82c03e-fb4d-40a2-8880-f94909787419.png)![image](https://user-images.githubusercontent.com/51266570/150722648-54f20665-f62d-4d2e-9ea0-a00e06b4926d.png)
     
   四分类准确率(a)与损失函数 (b)

   * 4.成果展示(Achievement display)： 
   
   我们通过使用python中的pyqt5包实现了对太阳射电爆发频谱图中爆发区域识别的可视化界面搭建：
   
   首先，点击“选择图片”按钮，完成对太阳射电频谱图的选择。
   
   ![image](https://user-images.githubusercontent.com/51266570/150722803-6479f6a6-b0ed-43b2-89a8-076af3602d6a.png)
   
   然后点击“太阳爆发检测”按钮，软件会进入对太阳射电频谱图的准备的等待阶段。
   
   ![image](https://user-images.githubusercontent.com/51266570/150722808-ccdbb8bf-a55c-4bc1-94f6-5c21e38d91e7.png)

   在完成对图片的预处理之后，软件就会进入对太阳射电频谱图爆发区域的检测阶段。在完成图片检测之后，软件会弹出识别成功的提示，并显示对爆发区域个数的统计结果。
   最后，点击“爆发检测显示”按钮，就会展示识别过后的太阳射电频谱图，并且可以点击“放大”“缩小”按钮和拖动滑动条完成对识别的爆发区域的浏览。
   
   ![image](https://user-images.githubusercontent.com/67349250/150627222-cb874f11-a02a-455b-b472-ee2d30c6ae33.png)
   
   对太阳射电爆发进行可视化检测
   
   * 5.成果总结(Summary of results)
   
   综合上文的内容，目前团队的主要成果如下：
   我们从澳大利亚的两个天文台上获取了数据，经过分割后得到了共计42968张图片，运用多次筛选之后得到的数据，在使用通道归一化、通道归一化+直方图均衡对数据进行处理后，成功完成了太阳射电爆发的二分类和四分类。其中二分类（有爆发、无爆发）的准确率最高为100%，四分类（II型爆发、III型爆发、其他爆发、无爆发）的准确率最高为95.8%。为了方便太阳射电爆发的检测，我们为此编写了软件，实现了检测的可视化。

   
   * 6.其它(other)：
   
   * 前期的代码在这个仓库https://github.com/han-fuyun/previous
   * 所用数据：https://pan.baidu.com/s/1VPMdLJr0kdztrYTKFOsPsw 提取码：qlsj 

Ⅱ. 成员分工：

   * 韩富韵：制作数据集、图像处理、搭建并训练神经网络、网站demo

   * 李恩泽：撰写报告、制作数据集、训练神经网络

   * 何若璞：编写软件、图像处理、网站维护、搭建并训练神经网络
