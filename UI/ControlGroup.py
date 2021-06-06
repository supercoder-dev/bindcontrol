import wx
import UI

from UI.KeyBindDialog import KeyBindDialog

class ControlGroup(wx.StaticBoxSizer):

    def __init__(self, parent, label):
        wx.StaticBoxSizer.__init__(self, wx.VERTICAL, parent, label = label)

        self.Parent = parent
        # self.Add(wx.StaticBox( parent, -1), wx.VERTICAL)

        self.InnerSizer = wx.FlexGridSizer(0,2,3,3)
        self.Add(self.InnerSizer, 0, wx.ALIGN_RIGHT|wx.ALL, 16)

    def AddLabeledControl(self, module = '',
            ctltype = '', value = '',
            contents = '', tooltip = '', callback = None):
        sizer = self.InnerSizer
        State = module.State
        padding = 2

        label = UI.Labels.get(value, value)
        text = wx.StaticText(module, -1, label + ':')

        if ctltype == ('keybutton'):
            control = wx.Button( module, -1, State[value])
            control.Bind(wx.EVT_BUTTON, self.KeyPickerDialog)
            control.KeyBindDesc = label

        elif ctltype == ('combo'):
            control = wx.ComboBox(
                module, -1, State[value],
                wx.DefaultPosition, wx.DefaultSize,
                contents,
                wx.CB_READONLY)
            if callback:
                control.Bind(wx.EVT_COMBOBOX, callback )

        elif ctltype == ('text'):
            control = wx.TextCtrl(module, -1, State[value])

        elif ctltype == ('checkbox'):
            control = wx.CheckBox(module, -1)
            control.SetValue(bool(State[value]))
            padding = 10

        elif ctltype == ('spinbox'):
            control = wx.SpinCtrl(module, -1)
            control.SetValue(State[value])
            control.SetRange(*contents)

        elif ctltype == ('dirpicker'):
            control = wx.DirPickerCtrl(
                module, -1, State[value], State[value], 
                wx.DefaultPosition, wx.DefaultSize,
                wx.DIRP_USE_TEXTCTRL|wx.ALL,
            )
        else: die(f"wtf?!  Got a ctltype that I don't know: {ctltype}")
        if tooltip:
            control.SetToolTip( wx.ToolTip(tooltip))

        sizer.Add( text,    0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        sizer.Add( control, 0, wx.ALL|wx.EXPAND, padding)

        self.Layout

        return control

    def KeyPickerDialog(self, evt):
        button = evt.EventObject

        dlg = KeyBindDialog(self.Parent, button.KeyBindDesc, button.Label)

        newKey = dlg.ShowWindow()

        # TODO -- check for conflicts
        # otherThingWithThatBind = checkConflicts(newKey)

        # TODO - update the associated page State
        # page.State[value] = newKey

        # re-label the button
        evt.EventObject.SetLabel(newKey)
