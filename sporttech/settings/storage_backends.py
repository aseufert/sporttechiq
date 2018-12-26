from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    '''
    Need these or else you'll get SuspicousOperation error
    '''

    location = 'static/'

    def _clean_name(self, name):
        return name

    def _normalize_name(self, name):
        if not name.endswith('/'):
            name += ""

        name = self.location + name
        return name


class MediaStorage(S3Boto3Storage):
    file_overwrite = False
    location = 'media/'

    def _clean_name(self, name):
        return name

    def _normalize_name(self, name):
        if not name.endswith('/'):
            name += ""

        name = self.location + name
        return name

    settings.MEDIA_URL = '//{}/{}/'.format(settings.CLOUD_FRONT_CUSTOM_DOMAIN, location)