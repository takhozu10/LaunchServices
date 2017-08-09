#!/usr/bin/python

from LaunchServices import *

LSSetDefaultHandlerForURLScheme("mailto", "com.microsoft.outlook")
LSSetDefaultRoleHandlerForContentType("com.apple.ical.ics", kLSRolesAll, "com.microsoft.Outlook")
LSSetDefaultRoleHandlerForContentType("public.vcard", kLSRoleAll, "com.microsoft.Outloook")