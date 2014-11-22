#!/usr/bin/python
'''
wx_scroll.py


This is an example of a wx Scroll window. It creates a window with the
text "This is a scroll window" and allows the user to scroll horizontally
and vertically.

Author: Phillip Lemons
Date Modified: 2/16/2014
'''

import wx

class ScrollbarFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'Scollbar Example', size=(300,200))
        self.scroll = wx.ScrolledWindow(self, -1)
        self.scroll.SetScrollbars(1, 1, 600, 400)

        self.InitUI()
        
    def InitUI(self):
        panel = wx.Panel(self.scroll, -1, size=(300,200))
        t = wx.StaticText(panel, -1, "This is a scroll window", (10,10))

app = wx.App()
frame = ScrollbarFrame()
frame.Show()
app.MainLoop()
