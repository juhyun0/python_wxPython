# -*- coding: utf-8 -*-

import wx

class MyFrame(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self, parent=None, title="Window Colour")

		self.Bind(wx.EVT_LEFT_DOWN, self.OnMouseLButtonDown)
		self.Bind(wx.EVT_RIGHT_DOWN, self.OnMouseRButtonDown)

	def OnMouseLButtonDown(self, event):
		frame.SetBackgroundColour(wx.Colour(0,0,255,0)) #파랑

	def OnMouseRButtonDown(self, event):
		frame.SetBackgroundColour(wx.Colour(255,0,0,0)) #빨강

if __name__=="__main__":
	app=wx.App()
	frame=MyFrame()
	frame.Show()

	app.MainLoop()
