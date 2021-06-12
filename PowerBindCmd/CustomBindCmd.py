from PowerBindCmd import PowerBindCmd
import wx


####### Custom Bind
class CustomBindCmd(PowerBindCmd):
    def BuildUI(self, dialog):
        self.customBindName = wx.TextCtrl(dialog, -1)
        self.customBindName.SetHint('Custom Bind Text')

        return self.customBindName

    def MakeBindString(self, dialog):
        return self.customBindName.GetValue()
