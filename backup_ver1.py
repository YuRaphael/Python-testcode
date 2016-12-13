# Filename: backup_ver1.py

import os
import time

source=r'D:\Program Files (x86)\EasyPHP-DevServer-14.1VC11\data\localweb\sy\testcode' 
target_dir=r'D:\Program Files (x86)\EasyPHP-DevServer-14.1VC11\data\localweb\sy\testcodebackup' 
target = r'D:'+'\\'+time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = r'"C:\Program Files\7-Zip\7z.exe" a %s %s' %(target, ''.join(r'd:\kk'))


if os.system(zip_command) == 0:
	print 'Successful backup to', target
else:
	print 'Backup FAILED'