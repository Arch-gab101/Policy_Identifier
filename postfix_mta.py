#MTA to relay email in realtime and extract metadata for policy activation and content for definition triggers.
import smtplib
import email.message
from email.message import EmailMessage
import dotenv
from dotenv import load_dotenv
import os

load_dotenv()


host = os.getenv('server')
port = os.getenv('port')

mail = EmailMessage()


