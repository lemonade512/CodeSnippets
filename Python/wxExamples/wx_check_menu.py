#!/usr/bin/python
# -*- coding: utf

'''
wx_check_menu.py
ZetCode wxPython tutorial

This example creates a checked menu item.

author: Jan Bodnar
website: www.zetcode.com
last modified: 2/20/14
'''

import wx

class Example(wx.Frame):

	def __init__(self, *args, **kwargs):
		super(Example, self).__init__(*args, **kwargs)

		self.InitMenus()

	def InitMenus(self):

		menubar = wx.MenuBar()
		fileMenu = wx.Menu()
		viewMenu = wx.Menu()

		fileMenu.Append(wx.ID_NEW, '&New')

		self.shst = viewMenu.Append(wx.ID_ANY, 'Show statusbar', \
				                    'Show Statusbar', kind=wx.ITEM_CHECK)
		self.shtl = viewMenu.Append(wx.ID_ANY, 'Show toolbar', \
				                    'Show Toolbar', kind=wx.ITEM_CHECK)

		viewMenu.Check(self.shst.GetId(), True)
		viewMenu.Check(self.shtl.GetId(), True)

		self.Bind(wx.EVT_MENU, self.ToggleStatusBar, self.shst)
		self.Bind(wx.EVT_MENU, self.ToggleToolBar, self.shtl)

		menubar.Append(fileMenu, '&File')
		menubar.Append(viewMenu, '&View')
		self.SetMenuBar(menubar)

		self.toolbar = self.CreateToolBar()
		self.toolbar.AddLabelTool(1, '', wx.Bitmap('Icons/exit.png'))
		self.toolbar.Realize()

		self.statusbar = self.CreateStatusBar()
		self.statusbar.SetStatusText('Ready')

		self.SetSize((350, 250))
		self.SetTitle('Check menu item')
		self.Centre()
		self.Show(True)

	def ToggleStatusBar(self, e):

		if self.shst.IsChecked():
			self.statusbar.Show()
		else:
			self.statusbar.Hide()

	def ToggleToolBar(self, e):

		if self.shtl.IsChecked():
			self.toolbar.Show()
		else:
			self.toolbar.Hide()

def main():

	ex = wx.App()
	Example(None)
	ex.MainLoop()

if __name__ == '__main__':
	main()
