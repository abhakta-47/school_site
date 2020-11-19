from django.db import models
import datetime

# Create your models here.


# class due_list(models.Model):

#     student = models.ForeignKey("student", on_delete=models.CASCADE)

#     january = models.BooleanField()
#     february = models.BooleanField()
#     march = models.BooleanField()
#     april = models.BooleanField()
#     may = models.BooleanField()
#     june = models.BooleanField()
#     july = models.BooleanField()

#     def __str__(self):
#         return self.student


# class order(models.Model):

#     student = models.ForeignKey("student", on_delete=models.CASCADE)
#     ammount = models.IntegerField()
#     orderId = models.CharField(max_length=10)
#     success = models.BooleanField()
#     transactionId = models.CharField(max_length=10)

#     def __str__(self):
#         return self.orderId


def current_session():
    if datetime.date.today().month == 12:
        return (
            str(datetime.date.today().year + 1)
            + "-"
            + str(datetime.date.today().year + 2)
        )

    return str(datetime.date.today().year) + "-" + str(datetime.date.today().year + 1)


# Create your models here.


class price(models.Model):

    session = models.CharField(max_length=10, default=current_session())
    class_choices = [
        ("10", "10"),
        ("9", "9"),
        ("8", "8"),
        ("7", "7"),
        ("6", "6"),
        ("5", "5"),
        ("4", "4"),
        ("3", "3"),
        ("2", "2"),
        ("1", "1"),
        ("inf", "infant"),
        ("pre", "prepatory"),
    ]
    stu_class = models.CharField(max_length=3, choices=class_choices)

    tuition_fee = models.IntegerField(default=0)
    tiffin_Charges = models.IntegerField(default=0)
    conveyance_charges = models.IntegerField(default=0)
    computer_charges = models.IntegerField(default=0)
    others = models.IntegerField(default=0)
    session_charge = models.IntegerField(default=0)
    admission_fee = models.IntegerField(default=0)
    examination_fees = models.IntegerField(default=0)
    library_fee = models.IntegerField(default=0)
    saraswati_puja = models.IntegerField(default=0)
    cultural_fee = models.IntegerField(default=0)
    game_fee = models.IntegerField(default=0)
    electric_fee = models.IntegerField(default=0)
    badge = models.IntegerField(default=0)
    medical = models.IntegerField(default=0)
    ifrastructure_fee = models.IntegerField(default=0)

    admission_total = 0
    month_total = 0

    def formed_data(self):
        prices = self.__dict__
        prices.pop("_state")
        prices.pop("id")
        prices.pop("session")
        month_total = 0
        session_total = 0
        month_items = {}
        session_items = {}
        for field, value in prices.items():
            if field in ["tuition_fee", "tiffin_charges", "electric_fee"]:
                month_total = month_total + int(value)
                month_items[field] = value
            else:
                session_total = session_total + int(value)
                session_items[field] = value

        return {
            "month_total": month_total,
            "month_items": month_items.items(),
            "session_total": session_total,
            "session_items": session_items.items(),
        }

    def __str__(self):
        return self.stu_class + " " + self.session


class transaction(models.Model):
    date_time = models.DateTimeField(auto_now=True)
    student = models.ForeignKey("students.student", on_delete=models.CASCADE)
    billed_amount = models.IntegerField(verbose_name="billed amount")
    collected_amount = models.IntegerField(verbose_name="amount collected")
    trxn_no = models.CharField(max_length=10)
    details = models.TextField()
    mode = models.CharField(max_length=20, default="offline")

    def __str__(self):
        return str(self.date_time.date()) + " : " + str(self.student.name)
