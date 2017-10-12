import argparse
import logging


class ServiceBase(object):
    service_name = ''

    def __init__(self, arguments):
        self.arguments = arguments
        self.parser = argparse.ArgumentParser(description='{} service launcher')
        self.parser.add_argument('-c ', '--config-file', )
        self.pid = None
        self.add_arguments()

    def add_arguments(self):
        """Override to add additional arguments"""
        return

