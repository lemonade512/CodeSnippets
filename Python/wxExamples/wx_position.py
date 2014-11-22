#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
File: wx_move.py

This creates a frame and moves it to a position on the screen.

Author: Phillip Lemons
Date: 2/20/14
'''

import wx

class Example(wx.Frame):

	def __init__(self, parent, title):
		super(Example, self).__init__(parent, title=title, size=(300,200))

		self.Move((800,250))
		#self.Move((0,0))       #Moves the window to top left and maximizes it
		#self.Maximize()
		self.Show()

if __name__ == '__main__':

	app = wx.App()
	Example(None, title='Move')
	app.MainLoop()
