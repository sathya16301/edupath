from django.db import models
from django.contrib.auth.models import User


class Subject(models.Model):

    CATEGORY_CHOICES = [
        ('core', 'Core & Practical'),
        ('theory', 'Theoretical Foundations'),
        ('allied', 'Allied & Supporting'),
        ('emerging', 'Emerging Skills'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    youtube_link = models.URLField(blank=True, null=True)
    course_link = models.URLField(blank=True, null=True)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)

    def __str__(self):
        return self.name


class Quiz(models.Model):

    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    question = models.CharField(max_length=5000)
    option1 = models.CharField(max_length=2000)
    option2 = models.CharField(max_length=2000)
    option3 = models.CharField(max_length=2000)
    option4 = models.CharField(max_length=2000)
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question


class Progress(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'subject')

    def __str__(self):
        return f"{self.user.username} - {self.subject.name}"


class QuizScore(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.IntegerField()
    total = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.subject.name} ({self.score}/{self.total})"