# LADS-License-Authorization-and-Driver's-Saftey
#### Check Project details folder for the Detailed information about this project
This is the repository of my project LADS.\
**Theme** : Prevent Accidents due to unauthorized drivers and drowsy driving.\
**Product** : Mobility service providers can get the driver's quality history directly from the data and improve their employees.

For any commercial usage,Read License file!
#### Download the Necessary Large files Here
[Link for files](http://www.mediafire.com/folder/hsml89rboufxf/Files_for_LADS)
--> Store the downloaded files in the same directory where the repository is cloned.\
[Link for files(2)](https://drive.google.com/file/d/1VBvTwakjq43EC5cZS4Qd2D51RS8js5dc/view)
--> This is Entire Project, Extract the Files for usage




##### Recommended Configuration:
 4 GB Ram, 4-Core GPU , Storage-150MB
 ##### Minimum Configuration:
 4 GB Ram,4-Core CPU, Storage - 150MB
#### INSTALLATION GUIDE:
Use Anaconda for better experience:
1. create a virtual environment (Recommended)
```cmd
conda create -n environment_name python=3.7
```
2. activate virtual environment
```cmd
conda activate environment_name
```
2. Install requirements.txt
```cmd
pip install -r requirement.txt
```


#### Changes needed to be done before usage.
(Environment Python-3.7)
1. All the paths needed to be changed according to your requirements.
2. Install all the required packages.

#### Usage Guide.
##### Single time usage programs
1. To store the driver's/ user's image locally use StoringImages.py(Each click will correspond to each stored photo).
2. Train the image using TrainingImages.py(It trains all the photos that are stored in the database).\
NOTE: (scipy version should be scipy==1.1.0).
##### You can also skip the above step and directly run the appication and make the storing and training from the below application itself
3. Run Final.py program for usage of LADS application.

## Working Photos
**Detects Face(IF USER is Authorized it detects eye landamrks)\
Data is Encoded at the User end. Only admin can see the history of the user.**
<img src="LADS Images\LADS1.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 5px;" />
#### If USER is not Authorized It shows following options.
<img src="LADS Images\LADS2.png"
     alt="Markdown Monster icon"
     style="float: left; margin-right: 5px;" />
#### Tools used
1. Python for programming
2. OpenCV,Dlib,FaceRecognition,numpy
3. TransferLearning is used for Modeling
