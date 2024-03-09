#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name='John Doe', job='General Management'):
        self.name = name
        self.job = job

    @property
    def name(self):
        """The name property"""
        return self._name

    @name.setter
    def name(self, name):
        """Name must be a string between 1 and 25 characters in length"""
        if isinstance(name, str) and 1 <= len(name) <= 25:
            self._name = name.title()  # Convert name to title case
        else:
            print("Name must be a string between 1 and 25 characters.")

    @property
    def job(self):
        """The job property"""
        return self._job

    @job.setter
    def job(self, job):
        """Job must be in the list of approved jobs"""
        if job in APPROVED_JOBS:
            self._job = job
        else:
            print("Job must be in list of approved jobs.")