from payment import models as payment_models
from students import models as student_models
import json

student_id = 1


def student_billing(student_id):
    student_instance = student_models.student.objects.get(id=student_id)
    due_instance = student_instance.due_set.all()[0]
    payment_info = due_instance.payment_info()

    prices = payment_models.objects.filter(stu_class=student_instance.stu_class)
    prices = prices[0].formed_data()

    # due = {}
    # paid = {}
    # due_session_table = {}
    # due_month_table = {}

    # paid = payment_info["paid"]
    # due = payment_info["due"]

    print(json.dumps(payment_info))

