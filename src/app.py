import os
import re

from chalice import Chalice, Cron

from chalicelib.gitlab import GitlabClient
from chalicelib.slack import SlackClient


AUTHOS_LIST_IDS = os.environ.get('AUTHOS_LIST_IDS', '')
AUTHOS_LIST_IDS = re.findall(r'\d+', AUTHOS_LIST_IDS)


class Notification(object):
    AUTHORS = AUTHOS_LIST_IDS

    def send_to_slack(self):
        data = self._format_data()
        SlackClient().message(data)

    def _format_data(self):
        data = {
           	"text": "Fala meus consagrados, temos vários MR pendentes vamos ajudar!",
        	"username": "Fabiao",
        	"mrkdwn": True,
            "attachments": []
        }

        for author in self.AUTHORS:
            for item in GitlabClient().merge_requests(scope='all', author_id=author, state='opened'):
                text = item.get('description')[:40]

                if item.get('title').startswith('WIP'):
                    continue

                data['attachments'].append({
                    "title": '{} (#{})'.format(item.get('title'), item.get('id')),
                    "text": "<https://gitlab.com/{0}|{0}>".format(
                        item.get('references').get('full').split('!')[0],
                    ),
                    "title_link": item.get('web_url'),
                    "footer": 'criado por {}'.format(item.get('author').get('name')),
                    "footer_icon": item.get('author').get('avatar_url'),
                })

        return data


app = Chalice(app_name='connect')


@app.schedule(Cron(0, '12,17,20', '?', '*', 'MON-FRI', '*'))
def send_to_slack(event):
    Notification().send_to_slack()
