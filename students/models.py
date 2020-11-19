from django.db import models
import datetime


def current_session():
    if datetime.date.today().month == 12:
        return (
            str(datetime.date.today().year + 1)
            + "-"
            + str(datetime.date.today().year + 2)
        )

    return str(datetime.date.today().year) + "-" + str(datetime.date.today().year + 1)


# Create your models here.


class student(models.Model):

    # general details
    name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50, blank=True)
    mother_name = models.CharField(max_length=50, blank=True)
    guardian_name = models.CharField(max_length=50)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender_choices = [("M", "Male"), ("F", "Female"), ("O", "Other")]
    gender = models.CharField(max_length=1, choices=gender_choices, default="M")
    reg_no = models.CharField(max_length=50)

    # class details
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
    stu_class = models.CharField(
        max_length=3, choices=class_choices, verbose_name="class"
    )

    stu_sec = models.CharField(max_length=1, verbose_name="section")
    stu_roll = models.IntegerField(verbose_name="Roll No.")

    # address
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True)
    post = models.CharField(max_length=50, blank=True)
    pin = models.IntegerField()
    dist = models.CharField(max_length=50, default="East Medinipur")
    state = models.CharField(max_length=50, default="West Bengal")

    # contact
    primary_number = models.CharField(max_length=10)
    whatsapp_number = models.CharField(max_length=10, blank=True)
    mail = models.CharField(max_length=50, blank=True)

    status = models.BooleanField(default=True)
    teaching_allowance = models.BooleanField(blank=True)

    def __str__(self):
        return self.name


def due_default():
    return {
        "admission": "false",
        "january": "false",
        "february": "false",
        "march": "false",
        "april": "false",
        "may": "false",
        "june": "false",
        "july": "false",
        "august": "false",
        "september": "false",
        "october": "false",
        "november": "false",
        "december": "false",
    }


class due(models.Model):

    # student = models.ForeignKey("student", on_delete=models.CASCADE)
    # session = models.CharField(max_length=10, default=current_session())

    # due = models.JSONField(default=due_default)

    student = models.ForeignKey("students.student", on_delete=models.CASCADE)
    session_yr = models.CharField(max_length=10, default=current_session())

    session = models.CharField(max_length=20, default="due")
    january = models.CharField(max_length=20, default="due")
    february = models.CharField(max_length=20, default="due")
    march = models.CharField(max_length=20, default="due")
    april = models.CharField(max_length=20, default="due")
    may = models.CharField(max_length=20, default="due")
    june = models.CharField(max_length=20, default="due")
    july = models.CharField(max_length=20, default="due")
    august = models.CharField(max_length=20, default="due")
    september = models.CharField(max_length=20, default="due")
    october = models.CharField(max_length=20, default="due")
    november = models.CharField(max_length=20, default="due")
    december = models.CharField(max_length=20, default="due")

    deposit = models.IntegerField(default=0, blank=False)

    def payment_info(self):
        due = self.__dict__
        k = 0
        curr_month = datetime.date.today().month
        month_counter = 0

        month_list = [
            "session",
            "january",
            "february",
            "march",
            "april",
            "may",
            "june",
            "july",
            "august",
            "september",
            "october",
            "november",
            "december",
        ]

        if self.session == "due":
            due_session = True
        else:
            due_session = False

        paid_months = {}
        due_months = []

        for field, value in due.items():

            if field in month_list:

                month_counter = month_counter + 1
                if value != "due":
                    paid_months[field] = value
                    k = k + 1
                else:
                    due_months.append(field)

            if month_counter > curr_month:
                # print("breaked !!!")
                break
        return {
            "due": due_months,
            "paid": paid_months,
            "due_session": due_session,
            "deposit": self.deposit,
        }

    def __str__(self):
        return self.student.name
