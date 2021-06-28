from django.db import models

# Create your models here.

class QuestionTypes(models.TextChoices):
    text = "short answer"
    mcq  = "Multiple choice question"
    scq  = "Single choice question"

class Poll(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField(auto_now=True)
    end_date = models.DateTimeField()
    description = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.title

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now=True)
    question_type = models.CharField(choices = QuestionTypes.choices, max_length=24)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Response(models.Model):
    response_text = models.CharField(max_length=1000)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.response_text
