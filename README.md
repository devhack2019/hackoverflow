# Team HackOverflow
#### Ketan Karnakota <br> Aman Jaiswal <br> Ashish Arora <br> Mayur Atkade
### Smart Attendance &copy; (CV)

![N|Solid](http://smartattendanceapp.com/img/footerlogo.png)


Smart Attendance is a lite weight automatic attendance program powered by the latest technology of OpenCV, Siamese-One shot-neural network and other such powerful artificial neural networking tools to aid professors take an easy attendance in class.

  - No more lengthy roll calls
  - Prevent proxy attendances
  - Regular student checks to prevent walking out after roll call
  - Unattended accurate attendance
  - Magic

# Forthcoming New Features !

  - Professors get email copies of the same class' attendance just after class
  - Timetable updation to prevent empty classroom captures and power off times
  - Monthly/Weekly reports of students who are missing classes regularly


> The overriding design goal for Smart
> attendance is to make it as convinient
> as possible to take attendance without wasting too much time.

>Chewing over the idea,
> we stumbled upon a ludicrous idea... What if we don't need to take attendance at all and also placate the **Academic Staff and the Dean** giving them reports on attendance that they need xD

> #### **Thus we came up with this disingenuous idea.**


### Tech

Smart Attendance uses a number of open source projects to work properly:

* Face-Detection with python using openCV3 (Computer Vision) : OpenCV has Machine Learning Algorithms to detect faces within a picture.

* Segmentation : The detected faces are segmeted from the original picture and stored as seperate files.

* Deblurring : If the segmented images are not_clear/blurred, then we use a RNN (Recurrent Neural Network) to remove the excess blur from the pictures, which will eventually help in improving the performance of our network.

* Siamese : One-shot learning :  Currently most deep learning models need generally thousands of labeled samples per class. Data acquisition for most tasks is very expensive. The possibility to have models that could learn from one or a few samples is a lot more interesting than having the need of acquiring and labeling thousands of samples.

(Since our implementation of Siamese network uses FaceNet for image_encoding (Transfer Learning), it requires us to rescale our images to dimesions of 96*96 ) 


### Installation

Smart Attendance requires a few Open Source tools to run.

Install the dependencies and devDependencies and start the server.

```sh
$ cd smart_attendance
$ pip install -r requirements.txt

```

*For the models to work we need **nVidia Cuda** cores for a few functionality for ~100% accuracy. <br> Works otherwise too!*

### Advantages

+ Doesn't need to store or learn from too many images of student. Needs only **1 shot** of the student (picture) and works with close to perfect accuracy
+ Doesn't require much heavy computation compared to any other algorithms that need to process a lot of data to survive the task
+ Works with any reasonably powerful device for many camera periferals in different classrooms

### To Run

```sh
$ cd smart_attendance
$ $a=7
$ python3 face_detect_cv3.py Images/$a/$a.jpg
$ cd SRN-Deblur-master
$ python run_model.py --input_path=./../Images/$a/ --output_path=./../Images/$a/
$ cd ..
$ python3 resize.py
$ cd Face\ Recognition
$ python3 siamese.py
```

Or we have simplified the task for you just change the a value in the **run.sh** file given and then run this

```sh
$ ./run.sh
```

### Development

Want to contribute? Great!

Talk to us and we can work on it together

[Ketan Karnakota](mailto:160010031@iitdh.ac.in?subject=[GitHub]%20Source%20Smart_attendance%20Dev-reg)

Open your favorite Terminal and explore all you can look around till we get back to you :stuck_out_tongue_winking_eye:


### YouTube Video Link

[https://youtu.be/aLU2MQTyQoU]


### Todos

 - Write to us we can talk about it... Looking out for creative genius ideas

## License

Licensed to team:
+ [@ashisharora010](https://github.com/ashisharora010)
+ [@AmanJaiswal1503](https://github.com/AmanJaiswal1503)
+ [@MayurAtkade](https://github.com/MayurAtkade)
+ [@kketan227](https://github.com/kketan227)
