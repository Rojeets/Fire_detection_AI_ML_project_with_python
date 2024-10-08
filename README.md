# Fire Detection System

## Description

This project is a fire detection system that uses video processing to detect flames and trigger alerts. The system uses OpenCV for video capture and processing, `playsound` for audio alerts, and `smtplib` for sending email notifications. The system continuously monitors video feed for fire, plays an alarm sound, and sends an email alert when fire is detected.

## Features

1. Detects fire in a video stream by analyzing color ranges.
2. Plays an alarm sound when fire is detected.
3. Sends an email notification alert when fire is detected.
4. Provides a simple graphical interface for monitoring the detection process.

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Rojeets/Fire_detection_AI_ML_project_with_python.git
   cd Fire_detection_AI_ML_project_with_python
2. Set Up a Virtual Environment:

   ```bash
   python -m venv venv
   # On Linux
   source venv/bin/activate
   # On Windows
   venv\Scripts\activate
3. Install Dependencies:

         pip install -r requirements.txt
   
4. Set Up Environment Variables:

   For security reasons, store your email credentials and other sensitive data as environment variables. You can create a .env file or set them directly in your environment. Example .env file:
   
         EMAIL_USER=your-email@gmail.com
         EMAIL_PASS=your-email-password
   Make sure to load these variables in your script using a library like python-dotenv if you choose to use a .env file.

6. Prepare the Alarm Sound File:

   Ensure you have an alarm sound file named alarm-sound.mp3 in the project directory.

## Usage
1. Run the Application:


         python app.py
2. Monitor the Output:
   
   The video feed will be displayed in a window titled "Fire Detection".
   If fire is detected, an alarm sound will play, and an email alert will be sent.
3. Stop the Application:
   
   Press q in the video display window to stop the application.
   You can also stop it using Ctrl+C in the terminal.
## Code Explanation
   app.py: Main application file that handles video capture, fire detection, alarm sound, and email notifications.
   play_alarm_sound_function(): Plays an alarm sound in a loop when a fire is detected.
   send_email_function(): Sends an email notification when a fire is detected.
   cleanup(): Releases resources and performs cleanup on exit.
   Troubleshooting
   No Video Feed: Ensure that the video file videoplayback.mp4 is in the correct directory and accessible.
   Email Not Sent: Verify your email credentials and ensure that your email provider allows sending emails via SMTP.
## Contributing
1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes.
4. Commit your changes (git commit -am 'Add new feature').
5. Push to the branch (git push origin feature-branch).
6. Create a new Pull Request.
## Contact
   For any questions or feedback, you can reach out to your-email@gmail.com.



### Notes:
- **Security:** Ensure sensitive data (like email credentials) is managed securely and avoid hardcoding them directly in the script.

This `README.md` should provide clear instructions for setting up, running, and contributing to the project.



