import os, sys
from subprocess import Popen, PIPE

def begin_recursion(top_level_dir, license_file_path):
    try:
        filetype_filter = sys.argv[3]
    except IndexError:
        filetype_filter = ''
    for root, dirs, files in os.walk(top_level_dir):
        for file in files:
            if file.endswith(filetype_filter):
                #print file
                apply_license(license_file_path, root+'/'+file)

def apply_license(license_file_path, file_path):
    tmp_path = '/tmp/IdGuRTjGKKJ'
    output = Popen(["cp", "--preserve=all", file_path, tmp_path], stdout=PIPE).communicate()[0]
    tf = open(tmp_path, 'w')
    tf.write(open(license_file_path).read())
    tf.close()
    tf = open(tmp_path, 'a')
    tf.write(open(file_path).read())
    tf.close()
    output = Popen(["mv", "-f", tmp_path, file_path], stdout=PIPE).communicate()[0]
    print 'handled file: '+file_path

try:
    top_level_dir = sys.argv[1]
    license_file_path = sys.argv[2]
    begin_recursion(top_level_dir, license_file_path)
except IndexError:
    print 'python apply_license.py <top_level_directory> <license_file_path> [ file_extension_filter ]'

