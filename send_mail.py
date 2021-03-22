import smtplib
from email.mime.text import MIMEText


def send_mail(employee, department, rating, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '483075a9a91cc5'
    password = '807345839b7d17'
    message = f"<h3>New Feedback Submission</h3><ul><li>Employee name: {employee}</li><li>Department: {department}</li><li>Rating: {rating}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'sender-email@example.com'
    receiver_email = 'receiver-email@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Employee Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
