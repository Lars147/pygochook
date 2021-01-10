.. _faq:

Frequently Asked Questions
==========================

.. _max_async_req:

Why is the maximum number of concurrent requests limited by default?
--------------------------------------------------------------------

As PyGoChook uses `aiohttp`_ to handle requests asynchronously, it has the 
same limitations and defaults. As described in their `documentation`_, this 
number is sufficient for most cases. The maximum number can be modified by 
the argument `connection_limit` of the `MsgSender` (see ...). The optimal 
number depends very much on your internet connection, hardware etc.


.. _aiohttp: https://docs.aiohttp.org/en/stable
.. _documentation: https://docs.aiohttp.org/en/stable/http_request_lifecycle.html?highlight=100#how-to-use-the-clientsession

