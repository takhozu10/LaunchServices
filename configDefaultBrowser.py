#!/usr/bin/python

from LaunchServices import *

LSSetDefaultHandlerForURLScheme("http", "com.google.chrome")
LSSetDefaultHandlerForURLScheme("https", "com.google.chrome")