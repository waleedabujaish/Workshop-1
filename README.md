# Workshop 1:

## Setup Instructions
This project is designed to run with **Python 3.11.8**. To create an isolated environment and manage dependencies efficiently, it's recommended to use a virtual environment. Follow these steps to set up your environment:

1. **Install virtualenv:**
   If you haven't installed virtualenv yet, you can do so using pip. Run the following command:

```bash
   pip install virtualenv
```

   then run these commands to set the enviroment
```bash
    virtualenv venv
    venv\Scripts\activate
```
2. **Install Dependencies:**
With the virtual environment activated, install the project's dependencies by running:
```bash
pip install -r requirements.txt
```

In the repository, you'll find three files. Each one serves a different purpose, and you can execute them by running a simple Python command. Here's an overview of the files and how to use them:

1. open_cam.py: This script activates your camera using OpenCV. To run it, execute the following command:
```bash
python open_cam.py
```

2. hand_landmarks.py: Utilizing both OpenCV and MediaPipe, this code detects hand landmarks and visualizes them. Run it with:
```bash
python hand_landmarks.py
```

3. pose_landmarks.py: Similar to the hand landmarks script, this one uses OpenCV and MediaPipe to identify and illustrate body landmarks. Execute it using:
```bash
python pose_landmarks.py
```
Feel free to run each script and explore its functionalities. Your experimentation and interaction with the code are highly encouraged.

Thank you for engaging with this project!

