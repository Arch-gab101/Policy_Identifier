#MTA to relay email in realtime and extract metadata for policy activation and content for definition triggers.
import smtplib
import email.message
from email.message import EmailMessage

mail = EmailMessage()
