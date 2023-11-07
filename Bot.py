from fbchat import Client
from fbchat.models import *

# กำหนดคลาสคำสั่งสำหรับการรับข้อความ
class MyBot(Client):
    def onMessage(self, mid, message):
        if message.author_id != self.uid:  # ตรวจสอบว่าข้อความมาจากเพื่อน
            self.markAsRead(message.thread_id)  # ทำเครื่องหมายข้อความว่าอ่านแล้ว
            self.markAsDelivered(message.thread_id, message.uid)  # ทำเครื่องหมายข้อความว่าส่งสำเร็จ
            print(f"Received message: {message.text}")

            # ตอบกลับเฉพาะข้อความจากเพื่อน
            response = "สวัสดี! นี่คือการตอบกลับอัตโนมัติ"
            self.send(Message(text=response), thread_id=message.thread_id, thread_type=message.thread_type)

# กำหนดอีเมลและรหัสผ่านของบัญชี Facebook ของคุณ
email = input('Email: ')
password = input('Password: ')

# สร้างอินสแตนซ์ของบอทและเริ่มเชื่อมต่อ
bot = MyBot(email, password)
bot.listen()  # เริ่มการรับข้อควา
