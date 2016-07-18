# coding=utf-8
import json
from time import sleep

import requests


class StarterApi(object):
    """
    :rtype: StarterApi
    """
    __obj = None

    @staticmethod
    def init(api_url):
        StarterApi.__obj = PrivateApi(api_url=api_url)

    @staticmethod
    def build_submit(service_id, data):
        return StarterApi.submit(
            StarterApi.build_task(service_id, data)
        )

    @staticmethod
    def submit(task):
        """
        :type task: Task
        """
        return StarterApi.__obj.submit(task)

    @staticmethod
    def build_task(service_id, data):
        t = Task()
        t.serviceId = service_id
        t.data = data
        return t


class PrivateApi:
    headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

    def __init__(self, api_url):
        self.api_url = api_url
        self.max_retries = 10

    def submit(self, task):
        """
        :type task: Task
        """
        url = self.api_url + '/services/' + task.serviceId + '/tasks'
        print('url = ' + str(url))
        last_e = None
        for idx in range(self.max_retries):
            try:
                return requests.post(
                    url=url,
                    data=json.dumps(task.__dict__),
                    headers=self.headers,
                    timeout=3
                )
            except requests.exceptions.ConnectionError as e:
                # При ошибках подключения пытаемся еще раз
                last_e = e
                sleep(1)
        raise last_e


class Task:
    serviceId = None
    data = {}
