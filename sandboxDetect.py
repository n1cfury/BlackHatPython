


def banner():
	print "[***]	sandbox detection p118	[***]"


class LASTINPUTINFO(ctypes.Structure):
	_fields_ = [("cbsize",ctypes.c_uint),("dwTime",ctypes.c_ulong)]

def get_last_input():
	struct_lastinputinfo = LASTINPUTINFO()
	struct_lastinputinfo.cbSize = ctypes.sizeof(LASTINPUTINFO)
	user32.GetLastInputInfo(ctypes.byref(struct_lastinputinfo))
	run_time = kernel32.GetTickCount()
	elapsed = run_time = sturct_lastinputinfo.dwTime
	

def get_key_presses():

def detect_sandbox():
