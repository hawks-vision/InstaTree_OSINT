#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 root <root@hawks-vision>
#
# Distributed under terms of the MIT license.

import followers
import tag_by_user_highlight
import tag_users
import instaloader
import json
import copy
import js_create 
#Profile = instaloader.Profile()
inObj = instaloader.Instaloader()
inObj.interactive_login(input("Enter your Username:"))
PROFILE = input("Enter the Target_name:")
L=instaloader.Profile.from_username(inObj.context,PROFILE)
ReqType=input("Select an option \n1.followers of target\n2.Tagged users and their highlight\n3.Tagged users alone:")
print("\n",ReqType)
if ReqType == "1":
    followers.followers(L,inObj,PROFILE)
elif ReqType == "2":
    tag_by_user_highlight.tag_highlight(L,inObj,PROFILE)
elif ReqType == "3":
    tag_users.tag_users(L,inObj,PROFILE)
else:
    print("Select a valid option")
print("Process Completed-------Open the html file to view the output")
