import os

from uplink import Body, Consumer, Query, get, json, returns


GILAB_PRIVATE_TOKEN = os.environ.get('GILAB_PRIVATE_TOKEN', '')


class GitlabClient(Consumer):
    URL = 'https://gitlab.com/api/v4/'

    def __init__(self, *args, **kwargs):
        kwargs.setdefault("base_url", self.URL)
        super().__init__(*args, **kwargs)
        self.session.headers.update(
            {"PRIVATE-TOKEN": GILAB_PRIVATE_TOKEN}
        )

    @json
    @returns.json
    @get("merge_requests/")
    def merge_requests(self,
            author_id: Query("author_id") = None,
            scope: Query("scope") = None,
            state: Query("state") = None):
        pass
