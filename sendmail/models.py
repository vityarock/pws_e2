from django.db import models
from django.utils import timezone
from django.core.mail import send_mail
import datetime
import threading

# Create your models here.
class Message(models.Model):
    subject = models.CharField("Тема", max_length=128)
    body = models.TextField("Сообщение", max_length=2048)
    sender = models.EmailField("Адрес отправителя", max_length=254, blank=True, null=True)
    receiver = models.EmailField("Адрес получателя", max_length=254)
    delay = models.SmallIntegerField("Отправить через (Секунды)")
    send_status = models.BooleanField("Отправлено", default = False)
    sending_time = models.DateTimeField("Отправлено в ", auto_now=False, auto_now_add=False, default=timezone.now)


    def __str__(self):
        return f'from: to:{self.receiver} | subject: {self.subject} | body: {self.body} '


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
            self.save()
        except OSError:
            self.send_status = False
            self.save()    


    def save(self, *args, **kwargs):
        if not self.id:
            timer = threading.Timer(self.delay, Message.send_message, args=(self, ), kwargs=None)
            timer.start()

        super(Message, self).save(*args, **kwargs)


    class Meta:
        ordering = ['-id']
#TODO: add favicon, new migration, create div in frontend