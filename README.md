# Automated Attendance System using Computer Vision and Machine Learning
This Python project uses computer vision and machine learning techniques to automate attendance taking in classrooms or workplaces. The program captures live video of individuals entering a room and uses OpenCV, a popular computer vision library, to detect and extract facial features from the video frames. The extracted features are then passed through a pre-trained machine learning model, such as a Convolutional Neural Network (CNN), to recognize and identify individuals. The program records the attendance data in a database and generates reports that can be easily accessed and shared.

#### Methodology
The program follows the following steps to automate attendance taking:

1. Capture live video: The program captures live video of individuals entering a room using a camera or webcam.

2. Detect and extract facial features: The program uses OpenCV to detect and extract facial features, such as eyes, nose, and mouth, from the video frames. This process involves face detection, alignment, and normalization to ensure accurate recognition.

3. Recognize and identify individuals: The extracted facial features are passed through a pre-trained machine learning model, such as a CNN, to recognize and identify individuals. The model is trained on a dataset of labeled images to learn to recognize individuals accurately.

4. Record attendance data: The program records the attendance data, such as the name and time of the individual, in a database. The database can be easily accessed and updated.

5. Generate attendance reports: The program generates attendance reports that can be easily accessed and shared. The reports provide an overview of the attendance data, such as the number of individuals present, absent, or late.

#### Requirements
1.Python 3.6 or higher <br>
2. OpenCV <br>
3. TensorFlow <br>
4. Keras <br>
5. Pandas <br>
6. NumPy <br>

#### How to run the program
Clone the repository to your local machine.
Install the required packages 
Run the program using python attendance_system.py.
Open the attendance reports in a web browser.

#### Conclusion
Automating attendance-taking using computer vision and machine learning techniques can significantly reduce the time and effort required to maintain attendance records. This project demonstrates how OpenCV, TensorFlow, and Keras can be used to develop an automated attendance system that is fast, accurate, and efficient. The program records attendance data in a database and generates reports that can be easily accessed and shared. This system eliminates the need for manual attendance-taking, making it faster, more accurate, and more efficient
