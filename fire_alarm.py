import cv2
import numpy as np
import smtplib
import threading
import os
from playsound import playsound

# Initialize status flags and counters
Alarm_Status = False
Email_Status = False
Fire_Reported = 0

# Function to play alarm in loop
def play_alarm_sound_function():
    while Alarm_Status:
        playsound('alarm-sound.mp3')

# Function to send the email notification
def send_email_function():
    recipientEmail = 'rojitpokha25@gmail.com'
    recipientEmail = recipientEmail.lower()

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login("pokharelrojit45@gmail.com", "password")  # Use app password if 2FA is enabled
        message = "Subject: Fire Alert!\n\nFire has been detected in the area. Please take necessary actions."
        server.sendmail("pokharelrojit45@gmail.com", recipientEmail, message)
        print(f"Email sent successfully to {recipientEmail}")
        server.quit()
    except Exception as e:
        print(f"FAILED!!\n not sent to: {e}")
        server.quit()

# Function to release resources on exit
def cleanup():
    global Alarm_Status
    Alarm_Status = False
    if video.isOpened():
        video.release()
    cv2.destroyAllWindows()
    print("Exiting...")

# Main code
try:
    video = cv2.VideoCapture("videoplayback.mp4")

    if not video.isOpened():
        print("Error opening video file")
        exit()

    while True:
        grabbed, frame = video.read()
        if not grabbed:
            print("Exiting... frame not grabbed")
            break
        
        # Resize the frame for consistent processing
        frame = cv2.resize(frame, (960, 540))
        # Apply Gaussian blur and convert to HSV color space
        blurred = cv2.GaussianBlur(frame, (21, 21), 0)
        hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
        # Define color range for detecting fire (red/orange)
        lower = np.array([18, 50, 50], dtype='uint8')
        upper = np.array([35, 255, 255], dtype='uint8')
        # Apply the mask to the original
        mask = cv2.inRange(hsv, lower, upper)
        # Apply the mask to the original frame
        output = cv2.bitwise_and(frame, frame, mask=mask)
        # Count the number of pixels in the mask
        count = cv2.countNonZero(mask)
        # If the count is greater than 15000, it means fire is detected
        if count > 15000:
            Fire_Reported += 1
        # Display the processed output frame
        cv2.imshow("Fire Detection", output)
        
        # Check for key press
        if Fire_Reported >= 1:
            # Start playing the sound and sending email once
            if not Alarm_Status:
                Alarm_Status = True
                threading.Thread(target=play_alarm_sound_function, daemon=True).start()
                threading.Thread(target=send_email_function, daemon=True).start()

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

except KeyboardInterrupt:
    pass
finally:
    cleanup()
