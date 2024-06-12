import smtplib
import datetime
import random
my_email ="bhargavibanu06217@gmail.com"


gmail_server ="smtp.gmail.com"
port ="587"

server = smtplib.SMTP(gmail_server,port)
server.ehlo()
server.starttls()

server.login(my_email,"password")


print("Logged in successfully")

to=['bhargavibanu06217@gmail.com','1by19cv401@bmsit.in']

messgaes=[
"It takes courage to grow up and become who you really are." ,
"Your self-worth is determined by you. You don't have to depend on someone telling you who you are." ,
"Nothing is impossible. The word itself says 'I'm possible!'" ,
 "Keep your face always toward the sunshine, and shadows will fall behind you." ,
"You have brains in your head. You have feet in your shoes. You can steer yourself any direction you choose. You're on your own. And you know what you know. And you are the guy who'll decide where to go." ,
"Attitude is a little thing that makes a big difference." ,
"To bring about change, you must not be afraid to take the first step. We will fail when we fail to try." ,
"All our dreams can come true, if we have the courage to pursue them." ,
"Don't sit down and wait for the opportunities to come. Get up and make them." ,
"Champions keep playing until they get it right." ,
"I am lucky that whatever fear I have inside me, my desire to win is always stronger." ,
"You are never too old to set another goal or to dream a new dream." ,
"It is during our darkest moments that we must focus to see the light." ,
"Believe you can and you're halfway there." ,
"Life shrinks or expands in proportion to one’s courage." ,
"Just don't give up trying to do what you really want to do. Where there is love and inspiration, I don't think you can go wrong." ,
"Try to be a rainbow in someone's cloud." ,
"If you don't like the road you're walking, start paving another one." ,
"Real change, enduring change, happens one step at a time." ,
"All dreams are within reach. All you have to do is keep moving towards them." ,
"It is never too late to be what you might have been." ,
"When you put love out in the world it travels, and it can touch people and reach people in ways that we never even expected." ,
"Give light and people will find the way." ,
"It always seems impossible until it's done.", 
"Don’t count the days, make the days count.",
]
msg =random.choice(messgaes)
Subject= """Subject: Quote of the day"""
combine = f"{Subject}\n{msg}"

print("sending.............")
server.sendmail(from_addr=my_email, to_addrs=to, msg=combine) 
print("sent!!")
server.close()



