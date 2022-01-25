## Solar activity localization and outburst prediction based on multi-source data

### Solar activity localization and outburst prediction based on multi-source data

Ⅰ. Project Introduction：  
   One of the projects of the Science and Technology Innovation Program of the Chinese Academy of Sciences. To complete now: detection of presence or absence of outbreaks, detection of Type II bursts, Type III bursts, and detection of other types of bursts. There are five types of solar radio bursts, which can be divided into I, II, III, IV, and V-type bursts according to different spectral characteristics. Each type of burst is shown in the diagram below.
   
   ![image](https://user-images.githubusercontent.com/51266570/150719173-14f03ae5-09b1-4273-ae0b-2ba004c7b89c.png)
   
  Using deep learning, the network trained with the data of the Learmonth Observatory will be used for the outbreak detection of the culgoora Observatory; write software, select pictures, and automatically detect (there is a bug now, the results of this detection will only be detected when the next picture is detected Display);
  It took a lot of time to make the data set, but it is not perfect, there is no subdivision of Type I burst and Type IV burst, covering less noise, it is easy to identify the noise as burst.

   * 1.Data collection：  
   The original data and logs of the two observatories, learmonth and culgoora, were downloaded from the National Bureau of Meteorology of Australia, and the images were segmented according to the logs to create a data set. 
   * 2.Digital image preprocessing：  
   Tried adaptive binarization, image morphology, channel normalization, histogram equalization and other methods
   finally used channel normalization, histogram equalization and image segmentation to process data  
     *（1）Channel normalization
     
     The main purpose is to reduce the streak noise so that the bursts behind the streak noise become more recognizable. The formula is as follows:
     
     ![image](https://user-images.githubusercontent.com/51266570/150720319-a3a013b9-d117-48bb-9e88-1b8e16663991.png)
    
     Where f represents the data matrix of the spectrum, and g is the processing result after channel normalization. fLM is the mean of each channel. 
     Figure 2.1 shows an example after channel denoising. It can be found that comparing the two images in Figure 2.1, the streak noise has been significantly improved, and the characteristics of Type II bursts are more obvious.
      
      ![image](https://user-images.githubusercontent.com/51266570/150720934-30b8d808-48a6-42fb-ba82-89f6569a780f.png)
      
      ![image](https://user-images.githubusercontent.com/51266570/150721085-3d9c32de-6e05-4641-aab0-ed201fca24d2.png)

       Figure 2.1.1 Comparison before and after channel normalization
       
      *（2）Histogram equalization
      
      For a matrix with m rows and n columns, use formula 2.2 to find the total number of image pixels, and use formula 2.3 for normalization
      
      ![image](https://user-images.githubusercontent.com/51266570/150720768-7b75376a-6919-4382-91b1-37d1c5ddda35.png)
      
      ![image](https://user-images.githubusercontent.com/51266570/150720802-b851ab5a-1a25-4b3e-98ab-be16bc9c8d7f.png)
      
      Next, the cumulative distribution hp of gray levels of the image is calculated, and the equilibrium value of the enhanced image g is obtained.
      
      ![image](https://user-images.githubusercontent.com/51266570/150720833-cfb178a6-dce1-4f1b-b3b4-375f151e3628.png)
      
      ![image](https://user-images.githubusercontent.com/51266570/150720842-25c395e5-ca96-477a-800d-45a61730b62c.png)
      
      Make the histogram distribution of the input image uniform, which will increase the gray level of the image, so as to achieve the effect of enhancing the local contrast without affecting the overall contrast. It is very useful for the background and foreground images which is too bright or too dark . 
      
      ![image](https://user-images.githubusercontent.com/51266570/150721177-a80c6ff1-81f5-454c-8d08-5a3e1024162d.png)
      
      ![image](https://user-images.githubusercontent.com/51266570/150721194-6bb1ad3b-9b2a-42bc-9b23-2cde144e1aab.png)

      Figure 2.1.2 Comparison before and after histogram equalization processing
      
      *（3）Image segmentation
      
      First, according to the log file of the observatory, determine the time of the eruption marked in the log, and then find the corresponding time in the original file and divide it. The raw data is in uint8 format and is stored in big endian. We use the bytestream.read function and numpy.frombuffer function to read the file from the binary file, extract the header information, and determine whether it is the desired period.
      
      
      ![QQ截图20220124122517](https://user-images.githubusercontent.com/51266570/150721886-5a518c36-7824-4680-9426-1f9a89001afd.png)
      
      Figure 2.1.3 Data storage format of Culgoora Observatory
      


   * 3.Deep learning model：
   
      Using neural network to classify solar radio burst pictures and using sliding window method to detect bursts.
      The four-classification model is to complete the following four types of classification: no burst, type II burst, type III burst, and other types of bursts.
      The following will take the four-class model as an example to illustrate the construction process of the neural network.
      Referring to the structure of AlexNet, this study uses a convolutional neural network with the same structure, as shown in the figure below, which contains three convolutional layers and the corresponding maximum pooling layer, and finally connects two fully connected layers.
     
     ![image](https://user-images.githubusercontent.com/51266570/150722055-f69994db-fdc7-463f-9724-311a96aac934.png)
     
     Figure 2.2.1 CNN network structure diagram
     
      The input for all bursts is an 800×200 radio spectrogram, which is downsampled and converted to a 400×100 image before being fed into the CNN network. The convolution layer of CNN uniformly uses 3×3 convolution kernel, and the pooling layer uniformly uses 2×2 pooling kernel. The convolutional layer and the first densely connected layer use relu as the activation function, and the last layer uses softmax as the activation function.
      After the C1 layer, 32 feature maps are obtained, each with a size of 398×198, and after the pooling layer, the size becomes 199×99. C2-P2 and C3-P3 are similar.
     
     ![image](https://user-images.githubusercontent.com/51266570/150722252-94ab4999-7901-4967-95bb-86d65bf0b898.png)

     Figure 2.2.2 CNN network parameter map
     
      For four classifications, we use channel normalization, channel normalization + histogram equalization, and the results are as follows:
     
     ![QQ截图20220125111207](https://user-images.githubusercontent.com/51266570/150904081-103ab13f-2dd9-4549-ab34-85acc3487e80.png)

     
     ![image](https://user-images.githubusercontent.com/51266570/150722635-ce82c03e-fb4d-40a2-8880-f94909787419.png)![image](https://user-images.githubusercontent.com/51266570/150722648-54f20665-f62d-4d2e-9ea0-a00e06b4926d.png)
     
   Four classification accuracy (a) and loss function (b)

   * 4.Achievement display： 
   
   By using the pyqt5 package in python, we have realized the construction of a visual interface for identifying the eruption area in the solar radio burst spectrum:
   
   First, click the "Select Image" button to complete the selection of the solar radio spectrum.
   
   ![image](https://user-images.githubusercontent.com/51266570/150722803-6479f6a6-b0ed-43b2-89a8-076af3602d6a.png)
   
   Then click the "Sun Burst Detection" button, and the software will enter the waiting stage of preparing the solar radio spectrum.
   
   ![image](https://user-images.githubusercontent.com/51266570/150722808-ccdbb8bf-a55c-4bc1-94f6-5c21e38d91e7.png)

   After completing the preprocessing of the image, the software will enter the stage of detecting the burst area of the solar radio spectrum. After completing the picture detection, the software will pop up a prompt of successful identification and display the statistical results of the number of burst areas.
   
   ![image](https://user-images.githubusercontent.com/67349250/150627222-cb874f11-a02a-455b-b472-ee2d30c6ae33.png)
   
   Visual detection of solar radio bursts
   
   Finally, click the "Outbreak Detection Display" button to display the identified solar radio spectrum, and you can click the "Zoom in" and "Zoom out" buttons and drag the slider to complete the browsing of the identified burst area.
   
   * 5.Summary of results
   
   Based on the above content, the main achievements of the current team are as follows:
   We obtained data from two observatories in Australia, and obtained a total of 42,968 pictures after segmentation. After using the data obtained after multiple screening, we used channel normalization , channel normalization + histogram equalization to process the data, successfully completed the two-class and four-classification of solar radio bursts. Among them, the accuracy rate of the second classification (with outbreak, no outbreak) is the highest 100%, and the accuracy of the fourth classification (type II outbreak, type III outbreak, other outbreaks, no outbreak) is the highest 95.8%. In order to facilitate the detection of solar radio bursts, we have written software for this and realized the visualization of the detection.

   
   * 6.Other：
   
   * The previous code is in this repository:https://github.com/han-fuyun/previous
   * Data used:https://pan.baidu.com/s/1VPMdLJr0kdztrYTKFOsPsw Extraction code:qlsj 

Ⅱ. Division of labor among members：
   * Ruopu He: writing software, image processing, website maintenance, building and training neural networks

   * Fuyun Han: making datasets, image processing, building and training neural networks, website demo

   * Enze Li: Writing reports, making datasets, training neural networks

   
