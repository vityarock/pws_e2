from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
import datetime
import threading

# Create your models here.
class Message(models.Model):
    subject = models.CharField("Тема", max_length=128)
    body = models.TextField("Сообщение")
    sender = models.EmailField("Адрес отправителя", max_length=254)
    receiver = models.EmailField("Адрес получателя", max_length=254)
    delay = models.SmallIntegerField("Отправить через (Секунды)")
    send_status = models.BooleanField("Отправлено", default = False)
    sending_time = models.DateTimeField("Отправлено в ", auto_now=False, auto_now_add=False, default=timezone.now)


    def __str__(self):
        return f'from: {self.sender} to:{self.receiver} subject: {self.subject} body: {self.body} send: {self.sending_time}'


    def send_message(self):
        try:
            send_mail(
            self.subject,
            self.body,
            'vityarock@yandex.ru',
            [self.receiver],
            fail_silently=False,
            )
            self.send_status = True
        except Exception:
        	self.send_status = False




    def save(self, *args, **kwargs):
        timer = threading.Timer(self.delay, Message.send_message, args=(self, ), kwargs=None)
        timer.start()
        super(Message, self).save(*args, **kwargs)


    class Meta:
        ordering = ['-id']
