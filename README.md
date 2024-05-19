# Interview Proxy Detection System

## Overview
The Interview Proxy Detection System is a Python-based application designed to detect and flag the use of proxy methods by applicants during online interviews. The system aims to maintain the integrity of the interview process by identifying unauthorized activities.

## Features
- **Real-time Monitoring:** Continuously tracks the interviewee's system for suspicious activities.
- **Application Detection:** Identifies running applications and processes that may indicate proxy usage.
- **User Alerts:** Notifies the interviewer of detected suspicious activities.
- **Logging:** Maintains logs of monitored activities for review and analysis.

## Installation
### Prerequisites
- Python 3.6 or higher
- pip (Python package installer)

### Required Libraries
Install the necessary libraries using pip:
```bash
pip install -r requirements.txt
```
### Cloning the Repository
Clone the repository to your local machine:
```bash
git clone https://github.com/bhargava-k/Interview-Proxy-Detection-system.git
cd Interview-Proxy-Detection-system
```
## Usage
### Configuration
Ensure that all configurations are set correctly in `config.json` (if applicable). Modify any paths or settings as required.

### Running the System
To start the monitoring system, run:
```bash
python app.py
```
## Project Structure
```
Interview-Proxy-Detection-system/
├── templates/
│ ├── index.html
├── app.py
├── client_data.csv
├── requirements.txt
└── README.md
```
## Logging
The system logs all monitored activities in a `logs` directory. Each log file is timestamped for easy reference.

## Security
Ensure secure data transmission and storage by configuring appropriate security measures. Use encryption and secure protocols as needed.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
