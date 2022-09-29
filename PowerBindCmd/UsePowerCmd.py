from PowerBindCmd import PowerBindCmd
import wx


####### Use Power
class UsePowerCmd(PowerBindCmd):
    def BuildUI(self, dialog):
        outerSizer = wx.BoxSizer(wx.HORIZONTAL)

        usePowerSizer = wx.GridBagSizer(5,5)
        usePowerSizer.Add(wx.StaticText(dialog, -1, "Method:"), (0,0), flag=wx.ALIGN_CENTER_VERTICAL)
        self.usePowerRBToggle = wx.RadioButton(dialog, -1, "Toggle", style=wx.RB_GROUP|wx.ALIGN_CENTER_VERTICAL)
        usePowerSizer.Add(self.usePowerRBToggle, (0,1))
        self.usePowerRBOn = wx.RadioButton(dialog, -1, "On", style=wx.ALIGN_CENTER_VERTICAL)
        usePowerSizer.Add(self.usePowerRBOn, (0,2))
        self.usePowerRBOff = wx.RadioButton(dialog, -1, "Off", style=wx.ALIGN_CENTER_VERTICAL)
        usePowerSizer.Add(self.usePowerRBOff, (0,3))
        usePowerSizer.Add(wx.StaticText(dialog, -1, "Power:"), (1,0), flag=wx.ALIGN_CENTER_VERTICAL)
        self.usePowerName = wx.ComboBox(dialog, -1, choices=self.GetPowers())
        usePowerSizer.Add(self.usePowerName, (1,1), (1,3), flag=wx.EXPAND)
        usePowerSizer.AddGrowableCol(3)

        outerSizer.Add(usePowerSizer, 1, wx.ALIGN_CENTER_VERTICAL)

        return outerSizer

    def MakeBindString(self, dialog):
        if self.usePowerRBToggle.GetValue():
            method = "powexecname"
        elif self.usePowerRBOn.GetValue():
            method = "powexectoggleon"
        elif self.usePowerRBOff.GetValue():
            method = "powexectoggleoff"
        else:
            pass # halt and catch fire

        return f"{method} {self.usePowerName.GetValue()}"

    def GetPowers(self):
        profile = wx.Window.FindWindowByName("Profile")
        return profile.General.GetPowers() or []

