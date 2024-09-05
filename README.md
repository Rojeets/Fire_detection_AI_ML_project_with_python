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
   git clone https://github.com/your-username/fire-detection.git
   cd fire-detection
