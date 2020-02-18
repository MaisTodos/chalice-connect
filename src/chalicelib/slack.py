import os
from uplink import Body, Consumer, json, post


SLACK_CLIENT_TOKEN = os.environ.get('SLACK_CLIENT_TOKEN', '')
SLACK_CLIENT_CHANNEL = os.environ.get('SLACK_CLIENT_CHANNEL', '')


@json
class SlackClient(Consumer):
    URL = 'https://hooks.slack.com/services/'

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('base_url', self.URL)
        super().__init__(*args, **kwargs)

    @post("{}/{}".format(SLACK_CLIENT_TOKEN, SLACK_CLIENT_CHANNEL))
    def message(self, data: Body): pass
