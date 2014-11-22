#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
wx_go_to_class.py

An example application that uses basic formatting. It also creates
a number of controls including check boxes, buttons, and static
text boxes.

Author: Phillip Lemons
Date Modified: 2/20/14
'''

import wx

class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title, size=(390, 350))

        self.panel = wx.Panel(self)

        font = wx.SystemSettings_GetFont(wx.SYS_SYSTEM_FONT)
        font.SetPointSize(9)

        self.st1 = wx.StaticText(self.panel, label='Class Name')
        self.st1.SetFont(font)
        self.tc = wx.TextCtrl(self.panel)
        self.st2 = wx.StaticText(self.panel, label='Matching Classes')
        self.st2.SetFont(font)
        self.tc2 = wx.TextCtrl(self.panel, style=wx.TE_MULTILINE)
        self.cb1 = wx.CheckBox(self.panel, label='Case Sensitive')
        self.cb1.SetFont(font)
        self.cb2 = wx.CheckBox(self.panel, label='Nested Classes')
        self.cb2.SetFont(font)
        self.cb3 = wx.CheckBox(self.panel, label='Non-Project classes')
        self.cb3.SetFont(font)
        self.btn1 = wx.Button(self.panel, label='Ok', size=(70, 30))
        self.btn2 = wx.Button(self.panel, label='Close', size=(70, 30))
        self.Bind(wx.EVT_BUTTON, self.OnClose, self.btn2)

        self._setup_layout()

        self.Centre()
        self.Show()

    def _setup_layout(self):

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)
        hbox1.Add(self.st1, flag=wx.RIGHT, border=8)
        hbox1.Add(self.tc, proportion=1)
        vbox.Add(hbox1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT|wx.TOP, border=10)

        vbox.Add((-1, 10))

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)
        hbox2.Add(self.st2)
        vbox.Add(hbox2, flag=wx.LEFT | wx.TOP, border=10)

        vbox.Add((-1,10))

        hbox3 = wx.BoxSizer(wx.HORIZONTAL)
        hbox3.Add(self.tc2, proportion=1, flag=wx.EXPAND)
        vbox.Add(hbox3, proportion=1, flag=wx.LEFT|wx.RIGHT|wx.EXPAND, 
                 border=10)

        vbox.Add((-1, 25))

        hbox4=wx.BoxSizer(wx.HORIZONTAL)
        hbox4.Add(self.cb1)
        hbox4.Add(self.cb2, flag=wx.LEFT, border=10)
        hbox4.Add(self.cb3, flag=wx.LEFT, border=10)
        vbox.Add(hbox4, flag=wx.LEFT, border=10)

        vbox.Add((-1, 25))

        hbox5 = wx.BoxSizer(wx.HORIZONTAL)
        hbox5.Add(self.btn1)
        hbox5.Add(self.btn2, flag=wx.LEFT|wx.BOTTOM, border=5)
        vbox.Add(hbox5, flag=wx.ALIGN_RIGHT|wx.RIGHT, border=10)

        self.panel.SetSizer(vbox)

    def OnClose(self, e):
        self.Close()

if __name__ == '__main__':

    app = wx.App()
    Example(None, title='Go To Class')
    app.MainLoop()
