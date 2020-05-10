from django.db import models

class Question(models.Model):
    class Answer(models.IntegerChoices):
        ANSWER_1=1
        ANSWER_2=2
        ANSWER_3=3
        ANSWER_4=4

    question = models.TextField()
    image=models.ImageField(upload_to='%Y/%m/%d/',blank=True)
    answer_1=models.CharField(max_length=500)
    answer_2=models.CharField(max_length=500)
    answer_3=models.CharField(max_length=500)
    answer_4 = models.CharField(max_length=500)
    correct_answer = models.IntegerField(choices=Answer.choices)

    def __str__(self):
        return 'Question : ' + self.question