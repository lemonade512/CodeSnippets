#!/user/bin/python
# -*- coding: utf-8 -*-
'''
wx_center.py

Brings up a frame and centers it on the screen.

Author: Phillip Lemons
Date Modified: 2/18/14
'''

import wx

class Example(wx.Frame):

	def __init__(self, parent, title):
		super(Example, self).__init__(parent, title=title, size=(300,200))

		self.Centre()
		self.Show()

if __name__ == '__main__':

	app = wx.App()
	Example(None, title='Center')
	app.MainLoop()
