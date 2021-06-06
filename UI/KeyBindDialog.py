import wx
import string
import UI

class KeyBindDialog(wx.Dialog):
    def __init__(self, parent, desc = '', keybind = 'UNBOUND'):
        wx.Dialog.__init__(self, parent, -1, style = wx.WANTS_CHARS|wx.DEFAULT_DIALOG_STYLE)

        if not desc:
            print("Tried to make a KeyBindDialog for something with no desc")
            return

        self.Binding = ''
        self.SetKeymap();

        sizer = wx.BoxSizer(wx.VERTICAL);

        self.kbDesc = wx.StaticText( self, -1, desc,    style = wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND)
        # self.kbBind = wx.StaticText( self, -1, keybind, style = wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND)
        self.kbBind = wx.Button( self, -1, '', style = wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND)

        self.kbBind.SetLabelMarkup('<b><big><center>' + keybind + '</center></big></b>')

        sizer.Add( self.kbDesc, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.LEFT|wx.RIGHT, 15);
        sizer.Add( self.kbBind, 1, wx.ALIGN_CENTER|wx.ALIGN_CENTER_VERTICAL|wx.EXPAND|wx.ALL, 15);

        # Wrap everything in a vbox to add some padding
        vbox = wx.BoxSizer(wx.VERTICAL);
        vbox.Add(sizer, 0, wx.EXPAND|wx.ALL, 10);

        # clearly I'm thinking of this the wrong way.
        for i in (self.kbDesc, self.kbBind, self):
            i.Bind(wx.EVT_KEY_DOWN        , self.handleBind )
            i.Bind(wx.EVT_KEY_UP          , self.handleBind )
            i.Bind(wx.EVT_CHAR            , self.handleBind )

            i.Bind(wx.EVT_LEFT_DOWN       , self.handleBind )
            i.Bind(wx.EVT_MIDDLE_DOWN     , self.handleBind )
            i.Bind(wx.EVT_RIGHT_DOWN      , self.handleBind )
            i.Bind(wx.EVT_MOUSE_AUX1_DOWN , self.handleBind )
            i.Bind(wx.EVT_MOUSE_AUX2_DOWN , self.handleBind )

        buttonSizer = self.CreateStdDialogButtonSizer(wx.OK|wx.CLOSE)
        vbox.Add(buttonSizer)

        self.SetSizerAndFit(vbox);
        self.Layout()
        self.SetFocus()

    def ShowWindow(self, *args):
        # self.Populate(args);

        result = self.ShowModal()

        if (result == wx.OK or result == wx.APPLY): return self.Binding

    def Populate(self, parent, id, current):
        self.kbDesc.SetLabel(f"Press the Key Combo you'd like to use for {UI.Labels[id]}");
        self.kbBind.SetLabel(current);
        self.Fit();
        self.CentreOnParent();


    def handleBind(self, event):

        print("got evt")

        evtType = event.GetEventType();

        self.Binding = ''
        # check for each modifier key
        # TODO -- LCTRL vs RCTRL etcetc
        if (event.ControlDown()) : self.Binding = self.Binding + 'CTRL-'
        if (event.ShiftDown())   : self.Binding = self.Binding + 'SHIFT-'
        if (event.AltDown())     : self.Binding = self.Binding + 'ALT-'

        if (evtType == wx.EVT_KEY_DOWN or evtType == wx.EVT_KEY_UP or evtType == wx.EVT_CHAR):
            print("Got a keystroke")
            code = event.GetKeyCode()

            KeyToBind = self.Keymap[code]

        else:
            button = event.GetButton()
            KeyToBind = [
                '', # 'button zero' placeholder
                'LBUTTON',
                'MBUTTON',
                'RBUTTON',
                'BUTTON4',
                'BUTTON5',
            ][button]

        self.Binding = self.Binding + KeyToBind
        self.kbBind.SetLabel(self.Binding)
        self.Layout()

        event.Skip(1);

    # This keymap code was initially adapted from PADRE < http://padre.perlide.org/ >.
    def SetKeymap(self):
        # key choice list
        self.Keymap = {
                wx.WXK_BACK : 'BACKSPACE',
                wx.WXK_TAB : 'TAB',
                wx.WXK_SPACE : 'SPACE',
                wx.WXK_UP : 'UP',
                wx.WXK_DOWN : 'DOWN',
                wx.WXK_LEFT : 'LEFT',
                wx.WXK_RIGHT : 'RIGHT',
                wx.WXK_INSERT : 'INSERT',
                wx.WXK_DELETE : 'DELETE',
                wx.WXK_HOME : 'HOME',
                wx.WXK_END : 'END',
                wx.WXK_CAPITAL : 'CAPITAL',
                wx.WXK_PAGEUP : 'PAGEUP',
                wx.WXK_PAGEDOWN : 'PAGEDOWN',
                wx.WXK_PRINT : 'SYSRQ',
                wx.WXK_SCROLL : 'SCROLL',
                wx.WXK_MENU : 'APPS',
                wx.WXK_PAUSE : 'PAUSE',
                wx.WXK_NUMPAD0 : 'NUMPAD0',
                wx.WXK_NUMPAD1 : 'NUMPAD1',
                wx.WXK_NUMPAD2 : 'NUMPAD2',
                wx.WXK_NUMPAD3 : 'NUMPAD3',
                wx.WXK_NUMPAD4 : 'NUMPAD4',
                wx.WXK_NUMPAD5 : 'NUMPAD5',
                wx.WXK_NUMPAD6 : 'NUMPAD6',
                wx.WXK_NUMPAD7 : 'NUMPAD7',
                wx.WXK_NUMPAD8 : 'NUMPAD8',
                wx.WXK_NUMPAD9 : 'NUMPAD9',
                wx.WXK_NUMPAD_MULTIPLY : 'MULTIPLY',
                wx.WXK_NUMPAD_ADD : 'ADD',
                wx.WXK_NUMPAD_SUBTRACT : 'SUBTRACT',
                wx.WXK_NUMPAD_DECIMAL : 'DECIMAL',
                wx.WXK_NUMPAD_DIVIDE : 'DIVIDE',
                wx.WXK_NUMPAD_ENTER : 'NUMPADENTER',
                wx.WXK_F1 : 'F1',
                wx.WXK_F2 : 'F2',
                wx.WXK_F3 : 'F3',
                wx.WXK_F4 : 'F4',
                wx.WXK_F5 : 'F5',
                wx.WXK_F6 : 'F6',
                wx.WXK_F7 : 'F7',
                wx.WXK_F8 : 'F8',
                wx.WXK_F9 : 'F9',
                wx.WXK_F10 : 'F10',
                wx.WXK_F11 : 'F11',
                wx.WXK_F12 : 'F12',
                wx.WXK_F13 : 'F13',
                wx.WXK_F14 : 'F14',
                wx.WXK_F15 : 'F15',
                wx.WXK_F16 : 'F16',
                wx.WXK_F17 : 'F17',
                wx.WXK_F18 : 'F18',
                wx.WXK_F19 : 'F19',
                wx.WXK_F20 : 'F20',
                wx.WXK_F21 : 'F21',
                wx.WXK_F22 : 'F22',
                wx.WXK_F23 : 'F23',
                wx.WXK_F24 : 'F24',
                ord('~') : 'TILDE',
                ord('-') : '-',
                ord('=') : 'EQUALS',
                ord('[') : '[',
                ord(']') : ']',
                ord("\\") : "\\",
                ord(';') : ';',
                ord("'") : "'",
                ord(',') : 'COMMA',
                ord('.') : '.',
                ord('/') : '/', 
        }

        # Add alphanumerics
        for alphanum in (list(string.ascii_lowercase) + list(range(10))):
                self.Keymap[ord(str(alphanum))] = alphanum


