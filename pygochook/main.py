import aiohttp
import asyncio
import typing


class MsgSender:
    """A class to send simply send messages via Google Chat Webhooks."""

    def __init__(self, msg: str, google_chat_webhook_urls: typing.Union[str, list], connection_limit: int=100):
        """Send a message to one or multiple google chat webhook urls.
        It uses `aiohttp` and `asyncio` to send the requests in an async matter.

        Args:
            msg (str): The message to send to Google Chats.
            google_chat_webhook_urls (typing.Union[str, list]): A single URL or list of URLs of Google Chat Incoming Webhooks.
            connection_limit (int): The maximum number of connections. Defaults to 100.
        """
        self.google_chat_webhook_urls = google_chat_webhook_urls
        self.msg = msg
        self.connection_limit = connection_limit

    # -------------------------------- #
    # ---------- Properties ---------- #
    # -------------------------------- #

    @property
    def google_chat_webhook_urls(self):
        return self._google_chat_webhook_urls

    @google_chat_webhook_urls.setter
    def google_chat_webhook_urls(self, url):
        """Will convert 

        Args:
            url ([type]): [description]
        """
        if isinstance(url, list):
            self._google_chat_webhook_urls = list(set(url))  # remove duplicates in the list
        else:
            self._google_chat_webhook_urls = [url]

    # ------------------------------------- #
    # ---------- Private Methods ---------- #
    # ------------------------------------- #

    async def _send_to_google_url(self, session, url):

        bot_message = {"text": self.msg}

        message_headers = {"Content-Type": "application/json; charset=UTF-8"}

        async with session.post(url, headers=message_headers, json=bot_message) as response:
            response = await response.json()

            return response

    async def _send_to_all_google_urls(self):
        connector = aiohttp.TCPConnector(limit=self.connection_limit)
        async with aiohttp.ClientSession(connector=connector) as session:
            google_chat_responses = []
            for url in self.google_chat_webhook_urls:
                google_chat_responses.append(
                    self._send_to_google_url(
                        session,
                        url,
                    )
                )
            responses = await asyncio.gather(*google_chat_responses, return_exceptions=True)
            return responses

    # ------------------------------------ #
    # ---------- Public Methods ---------- #
    # ------------------------------------ #

    def send(self) -> list:
        """Will send the message to the google chat webhooks.

        Returns:
            list: A list of requests responses as json representation.
        """
        return asyncio.run(self._send_to_all_google_urls())