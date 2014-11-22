#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
File: wx_layout_absolute

Creates a window that has a text control using an absolute layout.

Author: Phillip Lemons
Date: 2/20/14
'''

import wx

class Example(wx.Frame):

	def __init__(self, parent, title):
		super(Example, self).__init__(parent, title=title, size=(260, 180))

		panel = wx.Panel(self, -1)
		wx.TextCtrl(panel, pos=(3, 3), size=(250, 150))

		self.Centre()
		self.Show()


if __name__ == '__main__':

	app = wx.App()
	Example(None, title='')
	app.MainLoop()
