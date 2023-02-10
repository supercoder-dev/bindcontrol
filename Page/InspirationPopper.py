import wx
import UI
from Page import Page
from GameData import Inspirations
from UI.ControlGroup import ControlGroup

class InspirationPopper(Page):
    def __init__(self, parent):
        Page.__init__(self, parent)

        self.TabTitle = "Inspiration Popper"

        self.Init = {
            'EnableInspBinds'    : False,
            'EnableRevInspBinds' : False,
            'AccuracyKey'        : "SHIFT+A",
            'HealthKey'          : "SHIFT+S",
            'DamageKey'          : "SHIFT+D",
            'EnduranceKey'       : "SHIFT+Q",
            'DefenseKey'         : "SHIFT+W",
            'BreakFreeKey'       : "SHIFT+E",
            'ResistDamageKey'    : "SHIFT+SPACE",
            'ResurrectionKey'    : "SHIFT+TILDE",
            'RevAccuracyKey'     : "SHIFT+CTRL+A",
            'RevHealthKey'       : "SHIFT+CTRL+S",
            'RevDamageKey'       : "SHIFT+CTRL+D",
            'RevEnduranceKey'    : "SHIFT+CTRL+Q",
            'RevDefenseKey'      : "SHIFT+CTRL+W",
            'RevBreakFreeKey'    : "SHIFT+CTRL+E",
            'RevResistDamageKey' : "SHIFT+CTRL+SPACE",
            'RevResurrectionKey' : "SHIFT+CTRL+TILDE",
            'DisableTells'       : False,
        }
        for Insp in Inspirations:
            self.Init[f"{Insp}Border"]     = Inspirations[Insp]['bordercolor']
            self.Init[f"{Insp}Foreground"] = Inspirations[Insp]['bordercolor']
            self.Init[f"{Insp}Background"] = Inspirations[Insp]['color']

    def BuildPage(self):

        sizer = wx.BoxSizer(wx.VERTICAL)

        InspTabs = wx.Notebook(self, style = wx.NB_TOP, name = 'InspTabs')

        for tab in ('Basic Inspirations', 'Dual Inspirations', 'Team Inspirations', 'Dual Team Inspirations',):
            InspTabs.AddPage(wx.Panel(InspTabs), tab)

        self.InspRows =    ControlGroup(self, self, width=8, label = "Large Inspirations First")
        self.RevInspRows = ControlGroup(self, self, width=8, label = "Small Inspirations First")

        sizer.Add(InspTabs, 1, wx.EXPAND)

        for Insp in Inspirations:
            for order in ("", "Rev"):
                rowSet = self.RevInspRows if order else self.InspRows

                rowSet.AddControl(
                    ctlType = 'keybutton',
                    ctlName = f"{order}{Insp}Key",
                    tooltip = f"Choose the key combo to activate a {Insp} inspiration",
                )

                rowSet.AddControl(
                    ctlType = 'colorpicker',
                    ctlName = f"{order}{Insp}Border",
                    contents = Inspirations[Insp]['bordercolor'],
                )

                rowSet.AddControl(
                    ctlType = 'colorpicker',
                    ctlName = f"{order}{Insp}Background",
                    contents = Inspirations[Insp]['color'],
                )
                rowSet.AddControl(
                    ctlType = 'colorpicker',
                    ctlName = f"{order}{Insp}Foreground",
                    contents = Inspirations[Insp]['bordercolor'],
                )


        self.useCB = wx.CheckBox( self, -1, 'Enable Inspiration Popper Binds (prefer largest)')
        self.useCB.SetToolTip(wx.ToolTip(
            'Check this to enable the Inspiration Popper Binds, (largest used first)'))
        self.useCB.SetValue(self.Init['EnableInspBinds'])
        self.Ctrls['EnableInspBinds'] = self.useCB
        sizer.Add(self.useCB, 0, wx.ALL, 10)
        self.useCB.Bind(wx.EVT_CHECKBOX, self.OnEnableCB)

        sizer.Add(self.InspRows, 0, wx.EXPAND)

        sizer.AddSpacer(20)

        self.useRevCB = wx.CheckBox( self, -1,
                'Enable Reverse Inspiration Popper Binds (prefer smallest)')
        self.useRevCB.SetToolTip(wx.ToolTip(
            'Check this to enable the Reverse Inspiration Popper Binds, (smallest used first)'))
        self.useRevCB.SetValue(self.Init['EnableRevInspBinds'])
        self.Ctrls['EnableRevInspBinds'] = self.useRevCB
        sizer.Add(self.useRevCB, 0, wx.ALL, 10)
        self.useRevCB.Bind(wx.EVT_CHECKBOX, self.OnEnableRevCB)

        sizer.Add(self.RevInspRows, 0, wx.EXPAND)

        self.disableTellsCB = wx.CheckBox( self, -1,
                'Disable self-/tell feedback')
        self.disableTellsCB.SetToolTip(wx.ToolTip(
            'Check this box to avoid having your toon tell you whenever you pop an inspiration.'))
        self.disableTellsCB.SetValue(self.Init['DisableTells'])
        self.Ctrls['DisableTells'] = self.disableTellsCB
        sizer.Add(self.disableTellsCB, 0, wx.ALL, 10)
        self.disableTellsCB.Bind(wx.EVT_CHECKBOX, self.OnDisableTellCB)

        paddingSizer = wx.BoxSizer(wx.VERTICAL)
        paddingSizer.Add(sizer, flag = wx.ALL|wx.EXPAND, border = 16)
        self.SetSizerAndFit(paddingSizer)

        self.SynchronizeUI()


    def SynchronizeUI(self):
        self.OnEnableCB()
        self.OnEnableRevCB()
        self.OnDisableTellCB()

    def OnEnableCB(self, evt = None):
        controls = []
        for Insp in Inspirations:
            controls.append(f"{Insp}Key")
            controls.append(f"{Insp}Border")
            controls.append(f"{Insp}Background")
            controls.append(f"{Insp}Foreground")
        self.Freeze()
        self.DisableControls(self.useCB.IsChecked(), controls)
        if self.disableTellsCB.IsChecked():
            self.OnDisableTellCB()
        self.Thaw()
        if evt: evt.Skip()

    def OnEnableRevCB(self, evt = None):
        controls = []
        for Insp in Inspirations:
            controls.append(f"Rev{Insp}Key")
            controls.append(f"Rev{Insp}Border")
            controls.append(f"Rev{Insp}Background")
            controls.append(f"Rev{Insp}Foreground")
        self.Freeze()
        self.DisableControls(self.useRevCB.IsChecked(), controls)
        if self.disableTellsCB.IsChecked():
            self.OnDisableTellCB()
        self.Thaw()
        if evt: evt.Skip()

    def OnDisableTellCB(self, evt = None):
        enabled = not self.disableTellsCB.IsChecked()
        controls = []
        revcontrols = []
        for Insp in Inspirations:
            controls.append(f"{Insp}Border")
            controls.append(f"{Insp}Background")
            controls.append(f"{Insp}Foreground")
            revcontrols.append(f"Rev{Insp}Border")
            revcontrols.append(f"Rev{Insp}Background")
            revcontrols.append(f"Rev{Insp}Foreground")
        if self.useCB.IsChecked():
            self.DisableControls(enabled, controls)
        if self.useRevCB.IsChecked():
            self.DisableControls(enabled, revcontrols)
        if evt: evt.Skip()

    def PopulateBindFiles(self):
        ResetFile = self.Profile.ResetFile()

        for Insp in sorted(Inspirations):

            tiers = Inspirations[Insp]['tiers']
            # "reverse" order is as it is in gamebinds, smallest first
            reverseOrder = list(map(lambda s: f"inspexecname {s}", tiers))
            forwardOrder = reverseOrder[::-1]

            if not self.GetState("DisableTells"):
                bc = self.GetState(f'{Insp}Border')
                bg = self.GetState(f'{Insp}Background')
                fg = self.GetState(f'{Insp}Foreground')
                forwardOrder.insert(0, f'tell $name, {ChatColors(fg, bg, bc)}{Insp}')
                bc = self.GetState(f'Rev{Insp}Border')
                bg = self.GetState(f'Rev{Insp}Background')
                fg = self.GetState(f'Rev{Insp}Foreground')
                reverseOrder.insert(0, f'tell $name, {ChatColors(fg, bg, bc)}{Insp}')

            if self.GetState('EnableInspBinds'):
                ResetFile.SetBind(self.Ctrls[f"{Insp}Key"].MakeFileKeyBind(forwardOrder))
            if self.GetState('EnableRevInspBinds'):
                ResetFile.SetBind(self.Ctrls[f"Rev{Insp}Key"].MakeFileKeyBind(reverseOrder))

    UI.Labels.update({
        'Enable'             : "Enable Inspiration Popper",
        'AccuracyKey'        : "Accuracy Key",
        'HealthKey'          : "Health Key",
        'DamageKey'          : "Damage Key",
        'EnduranceKey'       : "Endurance Key",
        'DefenseKey'         : "Defense Key",
        'BreakFreeKey'       : "Break Free Key",
        'ResistDamageKey'    : "Resist Damage Key",
        'ResurrectionKey'    : "Resurrection Key",
        'RevAccuracyKey'     : "Accuracy Key",
        'RevHealthKey'       : "Health Key",
        'RevDamageKey'       : "Damage Key",
        'RevEnduranceKey'    : "Endurance Key",
        'RevDefenseKey'      : "Defense Key",
        'RevBreakFreeKey'    : "Break Free Key",
        'RevResistDamageKey' : "Resist Damage Key",
        'RevResurrectionKey' : "Resurrection Key",
    })
    for order in ("", "Rev"):
        for Insp in Inspirations:
            UI.Labels[f"{order}{Insp}Border"] = "Border"
            UI.Labels[f"{order}{Insp}Foreground"] = "Foreground"
            UI.Labels[f"{order}{Insp}Background"] = "Background"

def ChatColors(fg,bg,bd): return f'<color {fg}><bgcolor {bg}><bordercolor {bd}>'

