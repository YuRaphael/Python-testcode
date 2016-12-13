# Filename: backup_ver1.py

import os
import time

source=[r'D:\Program Files (x86)\EasyPHP-DevServer-14.1VC11\data\localweb\sy\testcode']
target_dir=[r'D:\Program Files (x86)\EasyPHP-DevServer-14.1VC11\data\localweb\sy\testcodebackup']
target = target_dir + time.strftime('%Y%m%d%H%M%S') + '.zip'
zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))


if os.system(zip_command) == 0:
	print 'Successful backup to', target
else:
	print 'Backup FAILED'