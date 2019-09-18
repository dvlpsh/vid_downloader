#!/usr/bin/env python3
import os

def download():
	urls = open('vid_list', 'r')
	urls.read()
	urls.close()
	get_vids = os.system("youtube-dl --output '~/Downloads/%(title)s-%(id)s.%(ext)s' -a vid_list --recode-video 'mkv' ")
	
download()
