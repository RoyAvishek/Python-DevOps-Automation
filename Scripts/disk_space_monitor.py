import psutil
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body):
    # Email configuration
    sender = 'your_email@gmail.com'
    receiver = 'recipient_email@gmail.com'
    password = 'your_email_password'
    
    # Create the email message
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = receiver

    # Send the email using SMTP
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())
    server.quit()

def check_disk_space(path, threshold):
    # Get disk usage information
    disk_usage = psutil.disk_usage(path)
    usage_percentage = disk_usage.percent

    # Check if disk usage exceeds the threshold
    if usage_percentage > threshold:
        # Compose email subject and body
        subject = 'Disk Space Alert'
        body = f'Disk space utilization is {usage_percentage}% which exceeds the threshold of {threshold}%'
        # Send email alert
        send_email(subject, body)

# Set the path to monitor and the threshold percentage
path_to_monitor = '/'
threshold_percentage = 80

# Check disk space and send email if exceeded the threshold
check_disk_space(path_to_monitor, threshold_percentage)
