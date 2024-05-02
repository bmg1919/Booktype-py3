# -*- coding: utf-8 -*-
from urllib.parse import urljoin, urlencode
import hashlib

from django.conf import settings


def get_profile_image(user, size=100):
    """
    This checks is the user has a profile image. If does, we use
    the user uploaded image. Otherwise we use gravatar default image
    for the given user.

    :Args:
      - user (:class: `django.contrib.auth.models.User`): User instance
      - size: Desired size for the profile image

    :Returns:
      Profile image path
    """

    profile = user.profile

    if not profile.image:
        name = 'blank'
        try:
            name = '{}/account/images/{}'.format(
                settings.STATIC_URL, settings.DEFAULT_PROFILE_IMAGE)
        except AttributeError:
            name = '{}{}'.format(settings.STATIC_URL, 'account/images/anonymous.png')

        default = urljoin(settings.BOOKTYPE_URL, name)

        # return 'https://www.gravatar.com/avatar/%s?%s' % (
        #     hashlib.md5(
        #         profile.user.email.encode('utf-8').lower()
        #     ).hexdigest(),
        #     urlencode({'d': default, 's': str(size)})
        # )
        return default

    filename = profile.image.name

    monk = '{}{}{}'.format(settings.DATA_URL, settings.PROFILE_IMAGE_UPLOAD_DIR, filename.split('/')[-1])

    return '{}{}{}'.format(settings.DATA_URL, settings.PROFILE_IMAGE_UPLOAD_DIR, filename.split('/')[-1])
