# GuardianRide--Driver-Safety-Accountability-System-

Guardian Ride is an innovative application designed to enhance safety and accountability within taxi rental services by evaluating driver performance in real time. Employing machine learning technology, Guardian Ride assesses drivers based on attentiveness, alertness, and adherence to traffic regulations during journeys. This README provides an overview of Guardian Ride's functionality, features, and implementation.

## How Does It Work?

Guardian Ride uses advanced computer vision technology to analyze the driver's behavior and detect potential safety risks. Here's a breakdown of how it works:

### 1. Face Detection
Guardian Ride first locates the driver's face in the camera view using specialized computer vision algorithms.

### 2. Keypoint Prediction
Once the face is detected, Guardian Ride predicts key facial landmarks such as eyes, nose, and mouth to track movement and orientation accurately.

### 3. Computed Scores

**- EAR (Eye Aspect Ratio):** Determines if the driver's eyes are open wide or starting to close, alerting to potential drowsiness.

**- Gaze Score:** Monitors the direction of the driver's gaze to ensure focus on the road ahead.

**- Head Pose:** Checks for proper head alignment to prevent distracted driving.

**- PERCLOS (PERcentage of CLOSure eye time):** Tracks the frequency and duration of eye closures, indicating fatigue or drowsiness.

### 4. Driver States

**- Driving Properly:** No issues detected, and no alerts are triggered. Driver is alert and focused.

**- Asleep:** Warns the driver if prolonged eye closures suggest the possibility of falling asleep at the wheel.

**- Distracted:** Provides gentle reminders to refocus attention if the head pose suggests distraction or inattentiveness.

### 5. Face Recognition

**- Camera Installation:** Guardian Ride incorporates a camera positioned on the windshield, directly facing the driver, enabling continuous monitoring throughout the journey.

**- Driver Identification:** Utilizing advanced facial recognition algorithms with Haarcascade_frontalface_default.xml, Guardian Ride accurately identifies drivers based on facial features.

**- Pre-Registration:** Before deployment, employers register all drivers within the system, ensuring accurate identification and eliminating cases where the algorithm misclassifies unregistered individuals.

**- Violation Tracking:** If a driver commits a traffic violation, government-installed cameras capture the car's license plate and timestamp, leading to a fine. Subsequently, the employer or owner can identify the driver responsible for the infraction while driving the specific vehicle at that time, facilitating appropriate accountability measures.

## Features

- **Real-time Driver Monitoring:** Continuous assessment of driver alertness and behavior
- **Advanced Facial Recognition:** Accurate driver identification and monitoring
- **Multi-State Detection:** Comprehensive classification of driver states
- **Eye Tracking Technology:** Precise monitoring of eye movements and closure patterns
- **Head Pose Analysis:** Detection of proper driving posture and attention
- **Safety Alert System:** Immediate notifications for dangerous driving conditions

## Installation and Setup

### Prerequisites
- Python version 3.10.0
- Compatible webcam or camera
- Required dependencies as listed in requirements.txt

### Installation Steps

**Step 1:** Clone the Guardian Ride repository from GitHub
```bash
git clone https://https://github.com/ShadAlam22/GuardianRide--Driver-Safety-Accountability-System.git
cd GuardianRide--Driver-Safety-Accountability-System
```

**Step 2:** Install Python version 3.10.0
- Download and install from official Python website
- Verify installation: `python --version`

**Step 3:** Install required dependencies
```bash
pip install -r requirements.txt
```

**Step 4:** Run the application
```bash
python app.py
```

## Usage

1. Ensure your camera is properly connected and positioned to face the driver
2. Register drivers in the system (if using pre-registration feature)
3. Launch the application using Python 3.10.0
4. The system will begin real-time monitoring and provide alerts as needed

## Technical Requirements

- **Python:** Version 3.10.0 (Required)
- **Camera:** USB webcam or integrated camera
- **Operating System:** Windows, macOS, or Linux
- **Hardware:** Sufficient processing power for real-time image analysis

---

**Guardian Ride - Making Roads Safer Through Intelligent Driver Monitoring**
