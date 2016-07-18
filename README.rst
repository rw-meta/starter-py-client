=========================
Starter Server API Client
=========================


Install
=======
pip starter-api install


Usage
=====
.. code-block:: python
StarterApi.init("http://HOST:PORT")
res = StarterApi.build_submit("YOUR_SERVICE", {"myparam": 1})
print('res = ' + str(res))
