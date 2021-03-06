#! /usr/bin/env python

from __future__ import print_function
from __future__ import absolute_import
from common_utils import *

# 1 time setup
create_test_directory("/tmp")
generate_random_files(16*1024) # too small will fail

# test(s)
start_test("override receiver hostname")
url = start_receiver("-noexit_on_bad_flags -hostname ::1") # will get escaped
print("Url is " + b2s(url));
if not url.startswith(s2b("wdt://[::1]")):
    error("Hostname part of url didn't change still " + url)
run_sender("")
check_transfer_status()
exit(verify_transfer_success())
