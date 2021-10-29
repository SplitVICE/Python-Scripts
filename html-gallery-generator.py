# https://stackoverflow.com/questions/11968976/list-files-only-in-the-current-directory
import os

def build_img_tag(f):
    str = "<a target='_blank' href='{0}'><img src='{0}' alt='{0}'></a>"
    return str.format(f)

def write_html():
    f = open("index.html", "w")

    content = "<style>img{width: 500px;}</style>"

    for img in img_tags:
        content += img

    f.write(content)
    f.close()

files = [f for f in os.listdir('.') if os.path.isfile(f)]
img_tags = []

for f in files:
    if ".py" not in f and "index.html" not in f:
        img_tags.append(build_img_tag(f))

write_html()
