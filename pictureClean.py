import os
import re

tex_file_path = ''
image_dir_path = ''

with open(tex_file_path, 'r') as file:
    tex_content = file.read()

used_images = re.findall(r'\\includegraphics\[.*\]{(.*)}', tex_content)
# 如果图片使用相对路径或绝对路径 请使用以下代码
# used_images = re.findall(r'\\includegraphics\[.*\]{(.*)}', tex_content)
# used_images = [os.path.basename(image) for image in used_images]

# print(used_images)

for filename in os.listdir(image_dir_path):
    if filename not in used_images:
        print(filename)
        # 如果要删除图片，请取消下面一行的注释
        os.remove(os.path.join(image_dir_path, filename))
