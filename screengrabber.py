import win32gui, win32ui, win32con, win32api

def banner():		#This script didnt use functions, so it could be used as one later
	print "[***]	screen grabber p115		[***]"

hdesktop = win32gui.GetDesktopWindow()
width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
height = win32api.GetSystemMetrics(win32con.SM_CVIRTUALSCREEN)
left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)
desktop_dc = win32gui.GetWindowDC(hdesktop)
img_dc = win32ui.CreateDCFromhandle(desktop_dc)
mem_dc = img_dc.CreateCompatibleDC()
screenshot = win32us.CreateBitmap()
screenshot.CreateCompatibleBitmap(img_dc, width, height)
mem_dc.SelectObject(screenshot)
mem_dc_BitBlt((0,0), (width, height), img_dc, (left,top), win32con.SRCCOPY)
screenshot.SaveBitmapFile(mem_dc, 'c:\\WINDOWS\\Temp\\screenshot.bmp')
mem_dc.DeleteDC()
win32gui.DeleteObject(screenshot.GetHandle())
