import wx
import UI
from UI.CustomBindPaneParent import CustomBindPaneParent
from UI.KeySelectDialog import bcKeyButton, EVT_KEY_CHANGED
from UI.PowerBinderDialog import PowerBinderButton

### CustomBind subclasses for the individual bind types

class SimpleBindPane(CustomBindPaneParent):
    def __init__(self, page, init = {}):
        CustomBindPaneParent.__init__(self, page, init)

        self.Title = init.get('Title', '')

    def Serialize(self):
        return {
            'Type'     : 'SimpleBind',
            'Title'    : self.Title,
            'Contents' : self.Ctrls['BindContents'].GetValue(),
            'Key'      : self.Ctrls['BindKey'].GetLabel(),
        }

    def BuildBindUI(self, page):

        self.SetLabel(self.Title)
        pane = self.GetPane()

        BindSizer = wx.BoxSizer(wx.HORIZONTAL)

        BindContentsCtrl = wx.TextCtrl(pane, -1, self.Init.get('Contents', ''))
        BindContentsCtrl.Bind(wx.EVT_TEXT, self.onContentsChanged)

        BindSizer.Add(wx.StaticText(pane, -1, "Bind Contents:"),              0, wx.ALIGN_CENTER_VERTICAL)
        BindSizer.Add(BindContentsCtrl,                                       1, wx.EXPAND|wx.LEFT|wx.RIGHT, 5)
        BindSizer.Add(PowerBinderButton(pane, tgtTxtCtrl = BindContentsCtrl), 0)
        self.Ctrls['BindContents'] = BindContentsCtrl

        BindKeyCtrl = bcKeyButton(pane, -1, {
            'CtlName' : f"{self.bindclass}{self.unique_bind_id}BindKey",
            'Page'    : page,
            'Key'     : self.Init.get('Key', ''),
        })
        BindKeyCtrl.Bind(EVT_KEY_CHANGED, self.onKeyChanged)

        BindSizer.Add(wx.StaticText(pane, -1, "Bind Key:"), 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT|wx.RIGHT, 5)
        BindSizer.Add(BindKeyCtrl,                          0)
        self.Ctrls['BindKey'] = BindKeyCtrl
        UI.Labels[BindKeyCtrl.CtlName] = "Simple Bind " + self.unique_bind_id

        BindSizer.Layout()

        # border around the addr box
        border = wx.BoxSizer(wx.VERTICAL)
        border.Add(BindSizer, 1, wx.EXPAND|wx.ALL, 10)
        pane.SetSizer(border)
        self.checkIfWellFormed()

    def onContentsChanged(self, evt):
        self.checkIfWellFormed()

    def onKeyChanged(self, evt):
        self.checkIfWellFormed()

    def checkIfWellFormed(self):
        bc = self.Ctrls['BindContents']
        if bc.GetValue():
            bc.SetBackgroundColour(wx.NullColour)
        else:
            bc.SetBackgroundColour((255,200,200))

        bk = self.Ctrls['BindKey']
        if bk.GetLabel():
            bk.SetBackgroundColour(wx.NullColour)
        else:
            bk.SetBackgroundColour((255,200,200))

