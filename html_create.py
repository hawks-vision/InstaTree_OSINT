#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 root <root@hawks-vision>
#
# Distributed under terms of the MIT license.
def html_create(k):
    rf=open("temp.html","rt")
    dt=rf.read()
    dt=dt.replace('template',k)
    k=k+".html"
    rf.close()
    rf=open(k,"wt")
    rf.write(dt)
    rf.close()



