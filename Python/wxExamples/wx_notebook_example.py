''' 
wx_notebook_example.py

This is an example of using the wx Notebook class. It creates
3 different tabs at the top of the window that can be switched
between.

Author: Phillip Lemons
Date Modified: 2/15/2014
'''

import wx

class PageOne(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		t = wx.StaticText(self, -1, "This is a PageOne object", (20,20))

class PageTwo(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		t = wx.StaticText(self, -1, "This is a PageTwo object", (40,40))

class PageThree(wx.Panel):
	def __init__(self, parent):
		wx.Panel.__init__(self, parent)
		t = wx.StaticText(self, -1, "This is a PageThree object", (60,60))

class MainFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, None, title="Simple Notebook Example")

		p = wx.Panel(self)
		nb = wx.Notebook(p)

		page1 = PageOne(nb)
		page2 = PageTwo(nb)
		page3 = PageThree(nb)

		nb.AddPage(page1, "Page 1")
		nb.AddPage(page2, "Page 2")
		nb.AddPage(page3, "Page 3")

		sizer = wx.BoxSizer()
		sizer.Add(nb, 1, wx.EXPAND)
		p.SetSizer(sizer)

if __name__ == "__main__":
	app = wx.App()
	MainFrame().Show()
	app.MainLoop()
