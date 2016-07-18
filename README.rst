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

    # simple build and submit task to server
    res = StarterApi.build_submit("YOUR_SERVICE", {"myparam": 1})
    print('res = ' + str(res))

    # build task object into variable and submit to server
    task = StarterApi.build_task("YOUR_SERVICE", {"myparam": 1})
    res = StarterApi.submit(task)
    print('res = ' + str(res))

