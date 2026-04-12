from django.db import models

class Register(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    mobile_number = models.IntegerField()
    birth_date = models.DateField()
    qualification = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.middle_name} {self.first_name}"
    
class Comment(models.Model):
    author = models.ForeignKey(Register, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')
    likes = models.ManyToManyField(Register, related_name='liked_comments', blank=True)

    def __str__(self):
        return f'Comment by {self.author.first_name} on {self.timestamp.strftime("%Y-%m-%d")}'

    @property
    def like_count(self):
        return self.likes.count()
    
class Question(models.Model):
    set_number = models.IntegerField()
    text = models.CharField(max_length=500)

    def __str__(self):
        return f"Set {self.set_number}: {self.text}"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.text} - {self.text}"
    
class Event(models.Model):
    user = models.ForeignKey(Register, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start = models.DateTimeField()
    end = models.DateTimeField(null=True, blank=True)
    
    EVENT_TYPE_CHOICES = [
        ('study', 'Study Session'),
        ('exam', 'Exam'),
    ]
    event_type = models.CharField(max_length=10, choices=EVENT_TYPE_CHOICES, default='study')

    def __str__(self):
        return f'{self.title} for {self.user.middle_name}'