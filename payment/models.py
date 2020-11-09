from django.db import models

# Create your models here.


class student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(auto_now=False, auto_now_add=False)
    stu_class = models.IntegerField()
    stu_sections = [
        ('A', 'Section A'),
        ('B', 'Section B'),
        ('C', 'Section C'),
        ('D', 'Section D')
    ]

    stu_section = models.CharField(
        max_length=2,
        choices=stu_sections,
        default='A',
    )

    def __str__(self):
        return self.first_name


class due_list(models.Model):

    student = models.ForeignKey('student', on_delete=models.CASCADE)

    january = models.BooleanField()
    february = models.BooleanField()
    march = models.BooleanField()
    april = models.BooleanField()
    may = models.BooleanField()
    june = models.BooleanField()
    july = models.BooleanField()

    def __str__(self):
        return self.student


class price_list(models.Model):

    month = models.CharField(max_length=50)
    tution_fee = models.IntegerField()
    tiffin_fee = models.IntegerField()
    car_fee = models.IntegerField()

    def __str__(self):
        return self.month


class order(models.Model):

    student = models.ForeignKey('student', on_delete=models.CASCADE)
    ammount = models.IntegerField()
    orderId = models.CharField(max_length=10)
    success = models.BooleanField()
    transactionId = models.CharField(max_length=10)

    def __str__(self):
        return self.orderId
