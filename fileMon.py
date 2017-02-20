import tempfile, threading, win32file, win32con, os

dirs_to_monitor = ["C:\\WINDOWS\\Temp", tempfile.gettempdir()]
FILE_CREATED = 1
FILE_DELETED = 2
FILE_MODIFIED = 3
FILE_RENAMED_FROM = 4
FILE_RENAMED_TO = 5

def banner():
	print "[***]	File Monitor p144	[***]"
	print""

def start_monitor(path_to_watch):
	FILE_LIST_DIRECTORY = 0X0001
	h_directory = win32file.CreateFile(
		path_to_watch,
		FILE_LIST_DIRECTORY,
		win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE | win32con.FILE_SHARE_DELETE,
		None,
		win32con.OPEN_EXISTING,
		win32con.FILE_FLAG_BACKUP_SEMANTICS,
		None)
	while 1:
		try:
			resutls = win32file.ReadDirectoryChangesW(
				h_directory,
				1024,
				True
				win32con.FILE_NOTIFY_CHANGE_FILE_NAME |
				win32con.FILE_NOTIFY_CHANGE_DIR_NAME |
				win32con.FILE_NOTIFY_CHANGE_ATTRIBUTES |
				win32con.FILE_NOTIFY_CHANGE_SIZE |
				win32con.FILE_NOTIFY_CHANGE_LAST_WRITE |
				win32con.FILE_NOTIFY_CHANGE_SECURITY,
				None,
				None)
			for action, file_name in results:
				full_filename = os.path.join(path_to_watch, file_name)
				if action == FILE_CREATED:
					print "[+] Created %s" % full_filename
				elif action == FILE_DELETED:
					print "[+] Deleted %s" % full_filename
				elif action == FILE_MODIFIED:
					print "[+] Modified %s" % full_filename
					print "[vvv] Dumping contents..."
				try:
					fd = open(full_filename, "rb")
					contents=fd.read()
					fd.close()
					print contents
					print "[^^^] Dump Complete..."
				except:
					print "[!!!] Dump Failed."
				elif action == FILE_RENAMED_FROM:
					PRINT "[ > ] Renamed from: %s" % full_filename
				elif action == FILE_RENAMED_TO:
					PRINT "[ < ] Renamed to: %s" % full_filename
				else:
					PRINT "[???] Unknown: %s" % full_filename
		except:
			pass

def main():
	banner()
	start_monitor(path_to_watch)

if __name__ == '__main__':
	main()