#!/usr/bin/env python

import requests
import os

FILE_NAME = "urls.txt"


def get_status():
    """
    This function go through each line in a file and prints out the http
    status code including redirects.
    """

    if os.path.exists(FILE_NAME):
        print "{} file exists".format(FILE_NAME)

        with open(FILE_NAME, 'r') as f:

            if os.stat(FILE_NAME).st_size == 0:
                print "oops!... {} file is empty".format(FILE_NAME)
                return

            for line in f.readlines():
                line = line.strip('\n')
                try:
                    r = requests.get(line)

                    if r.status_code:
                        print "\nStatus code for {}: {}".format(line, r.status_code)

                        if r.history:
                            for data in r.history:
                                print "Redirecting to {}".format(data.headers['Location'])
                                print "status code is: {}".format(data.status_code)
                    else:
                        print "\nNo status code for {}".format(r.code)

                except IOError:
                    print "\nConnection cannot be made to {}".format(line)

    else:
        print "{} file does not exist".format(FILE_NAME)

if __name__ == "__main__":

    get_status()
