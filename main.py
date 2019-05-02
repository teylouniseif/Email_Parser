# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask
from email_poller import read_email_from_gmail
from datetime import datetime , timezone
from data_pusher import push_request
import os

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

dirname = os.path.dirname(__file__)
datefile = os.path.join(dirname, 'exec_date.txt')

start_time=datetime.now(timezone.utc)
try:
    with open(datefile, 'r') as file:
        start_time=datetime.strptime(file.read(), "%a %b %d %H:%M:%S %Y %z")
except:
    pass
with open(datefile, 'w') as file:
    file.write("%s"%datetime.now(timezone.utc).strftime("%a %b %d %H:%M:%S %Y %z"))
docs=read_email_from_gmail(start_time)
for doc in docs:
    push_request(doc)

# [END gae_python37_app]
