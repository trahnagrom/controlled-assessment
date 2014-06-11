import wx
from threading import Thread
import time
import requests
 
# begin wxGlade: extracode
EUR_USD = 1
EUR_GBP = 1
USD_GBP = 1
def myfunc(i):
    global EUR_USD
    global EUR_GBP
    global USD_GBP
    # For the following 3 commands credit goes to http://www.boxcontrol.net/write-simple-currency-converter-in-python.html#.UpkVvapyQQ-
    url = 'http://rate-exchange.appspot.com/currency?from=EUR&amp;to=USD&amp;q=1'
    r = requests.get(url)
    EUR_USD = r.json()['v']
    time.sleep(2)
    url = 'http://rate-exchange.appspot.com/currency?from=EUR&amp;to=GBP&amp;q=1'
    r = requests.get(url)
    EUR_GBP = r.json()['v']
    time.sleep(2)
    url = 'http://rate-exchange.appspot.com/currency?from=USD&amp;to=GBP&amp;q=1'
    r = requests.get(url)
    USD_GBP = r.json()['v']
 
t = Thread(target=myfunc,args=(1,))
t.start()
# end wxGlade
 
class MyFrame1(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MyFrame1.__init__
        kwds["style"] = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.EUR = wx.StaticText(self, wx.ID_ANY, "EUR")
        self.tc_EUR = wx.TextCtrl(self, wx.ID_ANY, "")
        self.USD = wx.StaticText(self, wx.ID_ANY, "USD")
        self.tc_USD = wx.TextCtrl(self, wx.ID_ANY, "")
        self.GBP = wx.StaticText(self, wx.ID_ANY, "GBP")
        self.tc_GBP = wx.TextCtrl(self, wx.ID_ANY, "")
 
        self.__set_properties()
        self.__do_layout()
 
        self.Bind(wx.EVT_TEXT, self.eh_EUR, self.tc_EUR)
        self.Bind(wx.EVT_TEXT, self.eh_USD, self.tc_USD)
        self.Bind(wx.EVT_TEXT, self.eh_GBP, self.tc_GBP)
        # end wxGlade
 
    def __set_properties(self):
        # begin wxGlade: MyFrame1.__set_properties
        self.SetTitle("CurrencyPy")
        # end wxGlade
 
    def __do_layout(self):
        # begin wxGlade: MyFrame1.__do_layout
        grid_sizer_1 = wx.GridSizer(3, 2, 2, 2)
        grid_sizer_1.Add(self.EUR, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(self.tc_EUR, 0, 0, 0)
        grid_sizer_1.Add(self.USD, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(self.tc_USD, 0, 0, 0)
        grid_sizer_1.Add(self.GBP, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)
        grid_sizer_1.Add(self.tc_GBP, 0, 0, 0)
        self.SetSizer(grid_sizer_1)
        grid_sizer_1.Fit(self)
        self.Layout()
        self.Centre()
        # end wxGlade
 
    def eh_EUR(self, event):  # wxGlade: MyFrame1.&lt;event_handler&gt;
        if self.tc_EUR.GetValue() != '':
            self.tc_USD.ChangeValue(str(float(self.tc_EUR.GetValue())*EUR_USD))
            self.tc_GBP.ChangeValue(str(float(self.tc_EUR.GetValue())*EUR_GBP))
            event.Skip()
    def eh_USD(self, event):  # wxGlade: MyFrame1.&lt;event_handler&gt;
        if self.tc_USD.GetValue() != '':
            self.tc_EUR.ChangeValue(str(float(self.tc_USD.GetValue())/EUR_USD))
            self.tc_GBP.ChangeValue(str(float(self.tc_USD.GetValue())*USD_GBP))
            event.Skip()
    def eh_GBP(self, event):  # wxGlade: MyFrame1.&lt;event_handler&gt;
        if self.tc_GBP.GetValue() != '':
            self.tc_EUR.ChangeValue(str(float(self.tc_GBP.GetValue())/EUR_GBP))
            self.tc_USD.ChangeValue(str(float(self.tc_GBP.GetValue())/USD_GBP))
            event.Skip()
# end of class MyFrame1
if __name__ == "__main__":
    app = wx.PySimpleApp(0)
    wx.InitAllImageHandlers()
    frame_2 = MyFrame1(None, -1, "")
    app.SetTopWindow(frame_2)
    frame_2.Show()
    app.MainLoop()
