import unittest
from django.test import Client
from rest_framework import status

student_id = ''


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_getall_student(self):
        # Issue a GET request.
        response = self.client.get('/api/student/',content_type="application/json")
        # Check that the response is 200 OK.
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_student(self):
        data = {'student_code': 'T000001', 'first_name': 'testing',
                'last_name': 'fortest', 'Major': '5d3ec169076fd7e0de6afced'}
        response = self.client.post('/api/student/', data,content_type="application/json")
        global student_id
        student_id = response.json()["id"]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class SimpleTest2(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_student(self):
        response = self.client.get('/api/student/'+student_id+'/',content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["student_code"],'T000001')
        self.assertEqual(response.json()["first_name"],'testing')
        self.assertEqual(response.json()["last_name"],'fortest')
        self.assertEqual(response.json()["Major"],{'id':'5d3ec169076fd7e0de6afced','major_name':'Computer Engineering'})


class SimpleTest3(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_put_student(self):
        data2 = {'student_code': 'T000002', 'first_name': 'testing2',
                'last_name': 'fortest2', 'Major': '5d3ec169076fd7e0de6afced'}
        response = self.client.put('/api/student/'+student_id+'/',data2,content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["student_code"],'T000002')
        self.assertEqual(response.json()["first_name"],'testing2')
        self.assertEqual(response.json()["last_name"],'fortest2')
        self.assertEqual(response.json()["Major"],'5d3ec169076fd7e0de6afced')


class SimpleTest4(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_delete_student(self):
        response = self.client.delete('/api/student/'+student_id+'/',content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
