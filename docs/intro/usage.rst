.. _intro-usage:

==================
Usage Examples
==================

Send a message to a Google Chat::

    >>> import pygochook
    >>> message = "This is awesome!"
    >>> gchat_webhook_url = "https://chat.googleapis.com/..."
    >>> gchat_msg_sender = pygochook.MsgSender(message, gchat_webhook_url)
    >>> gchat_msg_sender.send()
    [{...}]     # response message from google chat


Or send a message to multiple Google Chats::

    >>> import pygochook
    >>> message = "This is awesome! I can send even to multiple chats!"
    >>> gchat_webhook_urls = [
    ...     "https://chat.googleapis.com/...",
    ...     "https://chat.googleapis.com/..."
    ... ]
    >>> gchat_msg_sender = pygochook.MsgSender(message, gchat_webhook_urls)
    >>> gchat_msg_sender.send()
    [{...}, {...}]     # response message from google chat


With the use of `aiohttp` the requests will be performed asynchronously. Hence, it does not matter if you send the message to one or multiple Google Chats with respect to response time.

An example::

    >>> import pygochook
    >>> @timer
    ... def to_one_chat(msg, url):
    ...     gchat_sender = pygochook.MsgSender(msg, url)
    ...     return gchat_sender.send()
    ... 
    >>> @timer
    ... def to_multi_chats(msg, urls):
    ...     gchat_sender = pygochook.MsgSender(msg, urls)
    ...     return gchat_sender.send()
    ... 
    >>> message = "Time does not even matter!"
    >>> url = "https://chat.googleapis.com/..."
    >>> urls = [
    ...     "https://chat.googleapis.com/...",
    ...     ...,
    ...     ...,
    ...     "https://chat.googleapis.com/..."
    ... ]   # 10 Chat API-URLs
    >>>
    >>> to_one_chat(message, url)   # send to one chat
    Total execution time: 454 ms
    >>>
    >>> to_multi_chat(message, url)   # send to 10 chats
    Total execution time: 2007 ms


Because of the asynchronous structure, the total function execution time is as long as the longest response time.