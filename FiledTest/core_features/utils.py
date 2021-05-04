from django.utils import timezone
from django.core.exceptions import ValidationError



def check_date(date):
    if date < timezone.now().date():
        raise ValidationError("Date cannot be in the past")
