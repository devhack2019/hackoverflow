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

* #1 That you won't understand so I wouldn't make an attempt
* #2 The stuff that I don't understand so everything else is out of question
* [AngularJS] - HTML enhanced for web apps!
* [Ace Editor] - awesome web-based text editor
* [markdown-it] - Markdown parser done right. Fast and easy to extend.
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [node.js] - evented I/O for the backend
* [Express] - fast node.js network app framework [@tjholowaychuk]
* [Gulp] - the streaming build system
* [Breakdance](http://breakdance.io) - HTML to Markdown converter
* [jQuery] - duh


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



### Todos

 - Write to us we can talk about it... Looking out for creative genius ideas

## License

Licensed to team:
+ [@ashisharora010](https://github.com/ashisharora010)
+ [@AmanJaiswal1503](https://github.com/AmanJaiswal1503)
+ [@MayurAtkade](https://github.com/MayurAtkade)
+ [@kketan227](https://github.com/kketan227)
