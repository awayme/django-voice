from django.conf import settings

BRAND_VIEW = getattr(settings, 'VOICE_BRAND_VIEW', 'djangovoice_home')
ALLOW_ANONYMOUS_USER_SUBMIT = getattr(
    settings, 'VOICE_ALLOW_ANONYMOUS_USER_SUBMIT', False)

if getattr(settings, 'PRIVATE_TITLE', None) and getattr(settings, 'PRIVATE_DESCRIPTION', None) and getattr(settings, 'PRIVATE_TYPE', None):
    PRIVATE_TITLE = getattr(settings, 'PRIVATE_TITLE', None)
    PRIVATE_DESCRIPTION = getattr(settings, 'PRIVATE_DESCRIPTION', None)
    PRIVATE_TYPE = getattr(settings, 'PRIVATE_TYPE', None)
