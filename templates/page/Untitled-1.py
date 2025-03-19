import smtplib

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('amirmahdibasiri555@gmail.com', 'AMIR.MAHDI')
    print("Connected successfully!")
    server.quit()
except Exception as e:
    print(f"Error: {e}")