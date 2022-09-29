from PowerBindCmd import PowerBindCmd
import wx


####### Target Enemy
class TargetEnemyCmd(PowerBindCmd):
    def BuildUI(self, dialog):
        targetEnemySizer = wx.BoxSizer(wx.HORIZONTAL)
        targetEnemySizer.Add(wx.StaticText(dialog, -1, "Target Enemy:"), 0,
                wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 4)
        self.targetEnemyModeChoice = wx.Choice(dialog, -1, choices = ['Near','Far','Next','Prev'])
        self.targetEnemyModeChoice.SetSelection(0)
        targetEnemySizer.Add(self.targetEnemyModeChoice, 0, wx.ALIGN_CENTER_VERTICAL)

        return targetEnemySizer

    def MakeBindString(self, dialog):
        choice = self.targetEnemyModeChoice
        index  = choice.GetSelection()
        mode   = choice.GetString(index)
        return "targetenemy" + mode.lower()

