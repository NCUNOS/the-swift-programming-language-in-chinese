#!/usr/bin/python
# coding:utf-8


import os


def iter(path):
    for root, dirs, files in os.walk(path):
        for fn in files:
            if fn.endswith(".html"):
                with open(root + '/' + fn, 'r') as f:
                    content = f.read()
                    content = content.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.1.3/ace.js"></script>', '<script src="http://cdn.bootcss.com/ace/1.1.3/ace.js"></script>').replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/ace/1.1.3/mode-javascript.js"></script>', '<script src="http://cdn.bootcss.com/ace/1.1.3/mode-javascript.js"></script>')
                    insert_pos = content.find("</li>", content.find("Generated using GitBook")) + 6
                    content = content[:insert_pos] + '''<li><p style="padding: 10px 15px;">翻譯無任何商業目的，僅供學習交流使用！</p></li>''' + content[insert_pos:]
                with open(root + '/' + fn, 'w') as f:
                    f.write(content)

iter(os.getcwd())
