from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from user.models import GlobalUser

def UsernameUniqueValidator(username):

    if GlobalUser.objects.filter(username=username).exists():
        raise ValidationError('The username is already taken', code='invalid')
    return username 