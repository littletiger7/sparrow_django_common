import jwt

from sparrow_django_common.utils.get_settings_value import GetSettingsValue


class DecodeJwt(object):
    """decode_jwt"""

    def __init__(self, ):
        self.settings_value = GetSettingsValue()
        self.run_env = self.settings_value.get_settings_value('RUN_ENV')
        self.secret = self.settings_value.get_middleware_value(
            'JWT_AUTHENTICATION_MIDDLEWARE', 'JWT_SECRET')[self.run_env]

    def decode_jwt(self, token):
        secret = self.secret
        try:
            payload = jwt.decode(token, secret, algorithms='HS256')
        except Exception as ex:
            raise ex
        return payload
