# coding=utf-8

__author__ = 'zarzen'

import os
import re
import subprocess


def check_video_name(name):
    name_flv = re.compile(r'.*.flv')
    name_mp4 = re.compile(r'.*.mp4')

    if name_flv.match(name):
        return True
    elif name_mp4.match(name):
        return True
    else:
        return False


def list_video_name(root_dir):
    _files = os.listdir(root_dir)
    _returns = _files[:]
    for _file in _files:
        if not check_video_name(_file):
            _returns.remove(_file)
    return _returns

def convert_to_mp3(video_name):
    mp3_name = video_name + r'.mp3'

    if os.path.exists(mp3_name):
        os.remove(mp3_name)

    #需要对空格做转义, 或者是使用脚本前先去空
    convert_command = r'ffmpeg -i %s -f mp3 -ab 128000 -vn %s' % (video_name, mp3_name)

    p = subprocess.Popen(convert_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    print p.stdout.readlines()
    for line in p.stdout.readlines():
        print(line)

def test_check_video_name():
    test_name = "xx.doc"

    if check_video_name(test_name):
        print("yes")
    else:
        print "not"


def rename_file(old_name):
    new_name = "".join(old_name.split())
    os.rename(old_name, new_name)

if __name__ == "__main__":

    test_check_video_name()

    _dir = r'/Users/zarzen/Documents/Temp/托福阅读零起点基础'

    for _file in list_video_name(_dir):
        rename_file(_dir+'/'+_file)

    for _file in list_video_name(_dir):
        print(_file)
        convert_to_mp3(_dir+'/'+_file)
