JSON_AS_ASCII = False

APP_NAME = 'WebInformation'

STATIC_BPNAME = 'Static'

from os.path import dirname, abspath
CURRENT_PATH = dirname(abspath(__file__))

from sys import version_info
#TIMEZONE config タイムゾーン設定
if version_info.minor >= 9:
    from zoneinfo import ZoneInfo
    JST = ZoneInfo("Asia/Tokyo")
else:
    from datetime import timedelta, timezone
    JST = timezone(timedelta(hours=+9), 'JST')

TIMEZONE = JST
