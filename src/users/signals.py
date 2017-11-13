from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User
from datetime import datetime, timedelta

from badges.models import Pioneer

def check_date(sender, user, **kwargs):
    user = User.objects.get(username=user)
    if user.date_joined < (datetime.now() - timedelta(days=365)):
        try:
            pioneer = user.pioneer
        except:
            pioneer = Pioneer()
            pioneer.user = user
            pioneer.save()

user_logged_in.connect(check_date)
