import wx

PADDING = 5

class ControlGroup(wx.StaticBoxSizer):

    def __init__(self, parent, label):
        wx.StaticBoxSizer.__init__(self, wx.VERTICAL, parent, label = label)

        self.Add(wx.StaticBox( parent, -1), wx.VERTICAL)

        self.InnerSizer = wx.FlexGridSizer(0,2,PADDING,PADDING)
        self.Add(self.InnerSizer, 0, wx.ALIGN_RIGHT, PADDING)

    def AddLabeledControl(self, module = '',
            ctltype = '', value = '',
            contents = '', tooltip = '', callback = None):
        sizer = self.InnerSizer
        State = module.State

        text = wx.StaticText(module, -1, value + ':')

        if ctltype == ('keybutton'):
            control = wx.Button( module, -1, State[value])
            control.Bind(wx.EVT_BUTTON, lambda p: self.KeyPickerDialog(p))
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
        elif ctltype == ('spinbox'):
            control = wx.SpinCtrl(module, 0, -1)
            control.SetValue(State[value])
            control.SetRange(contents)
        elif ctltype == ('dirpicker'):
            control = wx.DirPickerCtrl(
                module, -1, State[value], State[value], 
                wx.DefaultPosition, wx.DefaultSize,
                wx.DIRP_USE_TEXTCTRL|wx.ALL,
            )
        else: die("wtf?!  I don't know how to make a type")
        if tooltip:
            control.SetToolTip( wx.ToolTip(tooltip))

        sizer.Add( text,    0, wx.ALIGN_RIGHT|wx.ALIGN_CENTER_VERTICAL)
        sizer.Add( control, 0, wx.ALL|wx.EXPAND)

        self.Layout

        return control

    def KeyPickerDialog(self, p):
        parent = p.parent
        value  = p.value

        newKey = UI.KeyBindDialog.showWindow(parent, value, parent[value])

        # TODO -- check for conflicts
        # otherThingWithThatBind = checkConflicts(newKey)

        # update the associated profile var
        parent[value] = newKey

        # re-label the button
        wx.Window.FindWindowById(Utility.id(value)).SetLabel(newKey)
