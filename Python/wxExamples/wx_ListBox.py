#!/usr/bin/python
'''
wx_ListBox.py

Creates a frame with a list box. The list box contains 5 items. When
you select each of the different items the text on the right changes.

Author: Phillip Lemons
Date Modified: 2/16/2014
'''

import wx

hello_text = "Hello text"

goodbye_text = "Goodbye to you and your loved ones."

default_text = "This is the default text"

class Example(wx.Frame):

	def __init__(self, parent, title):
		super(Example, self).__init__(parent, title=title, size=(390, 350))

		self.InitUI()
		self.Centre()
		self.Show()

	def InitUI(self):

		panel = wx.Panel(self)

		vbox = wx.BoxSizer(wx.VERTICAL)
		hbox = wx.BoxSizer(wx.HORIZONTAL)

		self.lbox = wx.ListBox(panel, size=(100, 300))
		self.lbox.InsertItems([ "hello", "goodbye", "goodnight", "a", "b"], 0)
		hbox.Add(self.lbox, proportion=1, flag=wx.ALL|wx.EXPAND, border=5)
		self.Bind(wx.EVT_LISTBOX, self.OnSelect, self.lbox)

		self.stext = wx.StaticText(panel, label=default_text, size=(200,100),\
				                   style=wx.ST_NO_AUTORESIZE)
		hbox.Add(self.stext, flag=wx.ALL|wx.EXPAND, border = 5)

		vbox.Add(hbox, proportion=0, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, \
				 border=5)

		panel.SetSizer(vbox)

	def OnSelect(self, e):
		sel = self.lbox.GetSelection()
		text = self.lbox.GetString(sel)
		if(text == "hello"):
			self.stext.SetLabel(hello_text)
		elif(text == "goodbye"):
			self.stext.SetLabel(goodbye_text)
		else:
			self.stext.SetLabel(default_text)

if __name__ == "__main__":

	app = wx.App()
	Example(None, "test")
	app.MainLoop()
