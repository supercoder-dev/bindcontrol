from PowerBindCmd import PowerBindCmd
import wx


####### Target Friend
class TargetFriendCmd(PowerBindCmd):
    def BuildUI(self, dialog):
        targetFriendSizer = wx.BoxSizer(wx.HORIZONTAL)
        targetFriendSizer.Add(wx.StaticText(dialog, -1, "Target Friend:"), 0,
                wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 4)
        self.targetFriendModeChoice = wx.Choice(dialog, -1, choices = ['Near','Far','Next','Prev'])
        self.targetFriendModeChoice.SetSelection(0)
        targetFriendSizer.Add(self.targetFriendModeChoice, 0, wx.ALIGN_CENTER_VERTICAL)

        return targetFriendSizer

    def MakeBindString(self, dialog):
        choice = self.targetFriendModeChoice
        index  = choice.GetSelection()
        mode   = choice.GetString(index)
        return "targetfriend" + mode.lower()
