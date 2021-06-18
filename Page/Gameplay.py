import wx
import UI
import Utility
import BindFile
from Utility import BLF

from UI.ControlGroup import ControlGroup
from Page import Page

ordinals = ("First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth")

class Gameplay(Page):

    def __init__(self, parent):
        Page.__init__(self, parent)
        self.TabTitle = "Gameplay"
        self.Init = {
            'FPSEnable': True,
            'FPSBindKey': "P",
            'NetgraphBindKey': 'N',
            'TPSEnable'   : True,
            'TPSSelMode'  : "Teammates, then pets",
            'TeamSelect1' : 'UNBOUND',
            'TeamSelect2' : 'UNBOUND',
            'TeamSelect3' : 'UNBOUND',
            'TeamSelect4' : 'UNBOUND',
            'TeamSelect5' : 'UNBOUND',
            'TeamSelect6' : 'UNBOUND',
            'TeamSelect7' : 'UNBOUND',
            'TeamSelect8' : 'UNBOUND',

            'ChatEnable'               : 1,
            'Message'              : "afk Typing Message",
            'StartChat'            : 'ENTER',
            'SlashChat'            : '/',
            'StartEmote'           : ';',
            'AutoReply'            : 'BACKSPACE',
            'TellTarget'           : 'COMMA',
            'QuickChat'            : "'",
            'TypingNotifierEnable' : 1,
            'TypingNotifier'       : '',

            'EnablePet' : True,
            'SelNextPet' : 'UNBOUND',
            'SelPrevPet' : 'UNBOUND',
            'IncPetSize' : 'UNBOUND',
            'DecPetSize' : 'UNBOUND',
            'EnableTeam' : True,
            'SelNextTeam' : 'A',
            'SelPrevTeam' : 'G',
            'IncTeamSize' : 'P',
            'DecTeamSize' : 'H',
            'IncTeamPos'  : '4',
            'DecTeamPos'  : '8',
            'Reset'       : '',
        }

    def BuildPage(self):
        topSizer = wx.BoxSizer(wx.HORIZONTAL)

        leftSizer = wx.BoxSizer(wx.VERTICAL)
        rightSizer = wx.BoxSizer(wx.VERTICAL)

        ##### header
        headerSizer = wx.FlexGridSizer(0,2,10,10)

        enablecb = wx.CheckBox( self, -1, 'Enable Team/Pet Select')
        enablecb.SetToolTip( wx.ToolTip('Check this to enable the Team/Pet Select Binds') )
        self.Ctrls['EnableTeamPetSelectBinds'] = enablecb

        helpbutton = wx.BitmapButton(self, -1, Utility.Icon('Help'))
        helpbutton.Bind(wx.EVT_BUTTON, self.help)

        headerSizer.Add(enablecb, 0, wx.ALIGN_CENTER_VERTICAL)
        headerSizer.Add(helpbutton, wx.ALIGN_RIGHT, 0)

        leftSizer.Add(headerSizer, 0, wx.EXPAND|wx.ALL, 10)

        ##### direct-select keys
        TPSDirectBox = ControlGroup(self, self, 'Direct Team/Pet Select')

        TPSDirectBox.AddControl(
            ctlName = 'TPSSelMode',
            ctlType = 'choice',
            contents = ['Teammates, then pets','Pets, then teammates','Teammates Only','Pets Only'],
            tooltip = 'Choose the order in which teammates and pets are selected with sequential keypresses',
        )
        for selectid in (1,2,3,4,5,6,7,8):
            TPSDirectBox.AddControl(
                ctlName = f"TeamSelect{selectid}",
                ctlType = 'keybutton',
                tooltip = f"Choose the key that will select team member / pet {selectid}",
            )
        leftSizer.Add(TPSDirectBox, 0, wx.EXPAND|wx.ALL, 10)

        ##### Team Select Binds
        TeamSelBox = ControlGroup(self, self, 'Team Select')
        TeamSelBox.AddControl(
            ctlName ='SelNextTeam',
            ctlType = 'keybutton',
            tooltip = 'Choose the key that will select the next teammate from the currently selected one',
        )
        TeamSelBox.AddControl(
            ctlName ='SelPrevTeam',
            ctlType = 'keybutton',
            tooltip = 'Choose the key that will select the previous teammate from the currently selected one',
        )
        TeamSelBox.AddControl(
            ctlName ='IncTeamSize',
            ctlType = 'keybutton',
            tooltip = 'Choose the key that will increase the size of your teammate rotation',
        )
        TeamSelBox.AddControl(
            ctlName ='DecTeamSize',
            ctlType = 'keybutton',
            tooltip = 'Choose the key that will decrease the size of your teammate rotation',
        )
        TeamSelBox.AddControl(
            ctlName ='IncTeamPos',
            ctlType = 'keybutton',
            tooltip = 'Choose the key that will move you to the next higher slot in the team rotation',
        )
        TeamSelBox.AddControl(
            ctlName ='DecTeamPos',
            ctlType = 'keybutton',
            tooltip = 'Choose the key that will move you to the next lower slot in the team rotation',
        )
        TeamSelBox.AddControl(
            ctlName ='Reset',
            ctlType = 'keybutton',
            tooltip = 'Choose the key that will reset your team rotation to solo',
        )
        leftSizer.Add(TeamSelBox, 0, wx.EXPAND|wx.ALL, 10)



        ##### Pet Select Binds
        PetSelBox = ControlGroup(self, self, 'Pet Select')

        PetSelBox.AddControl(
            ctlName = 'SelNextPet',
            ctlType = 'keybutton',
            tooltip = 'Choose the key that will select the next pet from the currently selected one',
        )
        PetSelBox.AddControl(
            ctlName = 'SelPrevPet',
            ctlType = 'keybutton',
            tooltip = 'Choose the key that will select the previous pet from the currently selected one',
        )
        PetSelBox.AddControl(
            ctlName = 'IncPetSize',
            ctlType = 'keybutton',
            tooltip = 'Choose the key that will increase the size of your pet/henchman group rotation',
        )
        PetSelBox.AddControl(
            ctlName = 'DecPetSize',
            ctlType = 'keybutton',
            tooltip = 'Choose the key that will decrease the size of your pet/henchman group rotation',
        )
        rightSizer.Add(PetSelBox, 0, wx.EXPAND|wx.ALL, 10)

        ##### FPS Keys
        controlsBox = ControlGroup(self, self, "FPS / Netgraph")
        controlsBox.AddControl(
            ctlName = 'FPSEnable',
            ctlType = 'checkbox',
            callback = self.OnFPSEnable,
        )
        controlsBox.AddControl(
            ctlName = 'FPSBindKey',
            ctlType = 'keybutton',
        )
        controlsBox.AddControl(
            ctlName = 'NetgraphBindKey',
            ctlType = 'keybutton',
        )
        rightSizer.Add(controlsBox, 0, wx.EXPAND|wx.ALL, 10)

        chatBindBox = ControlGroup(self, self, 'Chat Binds')

        chatBindBox.AddControl(
            ctlName   = 'ChatEnable',
            ctlType = 'checkbox',
            tooltip = 'Enable / Disable chat binds',
        )
        for b in (
            ['StartChat',  'Activates the Chat bar'],
            ['SlashChat',  'Activates the Chat bar with a slash already typed'],
            ['StartEmote', 'Activates the Chat bar with "/em" already typed'],
            ['AutoReply',  'AutoReplies to incoming tells'],
            ['TellTarget', 'Starts a /tell to your current target'],
            ['QuickChat',  'Activates QuickChat'],
        ):
            chatBindBox.AddControl(
                ctlName = b[0],
                ctlType = 'keybutton',
                tooltip = b[1],
            )
        chatBindBox.AddControl(
            ctlName = 'TypingNotifierEnable',
            ctlType = 'checkbox',
            tooltip = "Check this to enable the Typing Notifier",
        )
        chatBindBox.AddControl(
            ctlName = 'TypingNotifier',
            ctlType = 'text',
            tooltip = "Choose the message to display when you are typing chat messages or commands",
        )

        rightSizer.Add(chatBindBox, 0, wx.EXPAND|wx.ALL, 10)

        topSizer.Add(leftSizer, 0, wx.ALL|wx.EXPAND, 10)
        topSizer.Add(rightSizer, 0, wx.ALL|wx.EXPAND, 10)
        paddingSizer = wx.BoxSizer(wx.VERTICAL)
        paddingSizer.Add(topSizer, flag = wx.ALL|wx.EXPAND, border = 16)
        self.SetSizerAndFit(paddingSizer)


    def OnFPSEnable(self, evt):
        self.Ctrls['FPSBindKey'].Enable(evt.EventObject.IsChecked())
        self.Ctrls['NetgraphBindKey'].Enable(evt.EventObject.IsChecked())

    def PopulateBindFiles(self):

        ResetFile = self.Profile.ResetFile()

        ### FPS/Netgraph
        ResetFile.SetBind(self.Ctrls['FPSBindKey']     .KeyBind.MakeFileKeyBind('++showfps++netgraph'))
        ResetFile.SetBind(self.Ctrls['NetgraphBindKey'].KeyBind.MakeFileKeyBind('++netgraph'))

        # TeamSel (1)
        # TODO -- check versus citybinder output, seems to be working but...?
        if (self.GetState('TPSSelMode') != "Pets Only"):
            selmethod = "teamselect"
            selnummod = 0
            selmethod1 = "petselect"
            selnummod1 = 1
            if (self.GetState('TPSSelMode') == "Pets, then teammates"):
                selmethod = "petselect"
                selnummod = 1
                selmethod1 = "teamselect"
                selnummod1 = 0
            selresetfile = self.Profile.GetBindFile("tps","reset.txt")
            for i in ('1','2','3','4','5','6','7','8'):
                selfile = self.Profile.GetBindFile("tps",f"sel{i}.txt")
                ResetFile.   SetBind(self.Ctrls[f"TeamSelect{i}"].KeyBind.MakeFileKeyBind([f"{selmethod} {int(i) - selnummod}", BLF(self.Profile,'tps',f"sel{i}.txt")]))
                selresetfile.SetBind(self.Ctrls[f"TeamSelect{i}"].KeyBind.MakeFileKeyBind([f"{selmethod} {int(i) - selnummod}", BLF(self.Profile,'tps',f"sel{i}.txt")]))
                for j in ('1','2','3','4','5','6','7','8'):
                    if (i == j):
                        selfile.SetBind(self.Ctrls[f"TeamSelect{j}"].KeyBind.MakeFileKeyBind([f"{selmethod1} {int(j) - selnummod1}", BLF(self.Profile,'tps',"reset.txt")]))
                    else:
                        selfile.SetBind(self.Ctrls[f"TeamSelect{j}"].KeyBind.MakeFileKeyBind([f"{selmethod} {int(j) - selnummod}"  , BLF(self.Profile,'tps',f"sel{j}.txt")]))

        else:
            selmethod = "teamselect"
            selnummod = 0
            if (self.GetState('TPSSelMode') == "Pets Only"):
                selmethod = "petselect"
                selnummod = 1
            for i in (1,2,3,4,5,6,7,8):
                ResetFile.SetBind(self.Ctrls['sel1'].KeyBind.MakeFileKeyBind("selmethod " + (i - selnummod)))

        ResetFile = self.Profile.ResetFile()

        notifier = self.GetState('TypingNotifier')

        # TypingNotifier
        ResetFile.SetBind(self.Ctrls['StartChat'] .KeyBind.MakeFileKeyBind(['show chat', 'startchat', notifier]))
        ResetFile.SetBind(self.Ctrls['SlashChat'] .KeyBind.MakeFileKeyBind(['show chat', 'slashchat', notifier]))
        ResetFile.SetBind(self.Ctrls['StartEmote'].KeyBind.MakeFileKeyBind(['show chatem ' + notifier]))
        ResetFile.SetBind(self.Ctrls['AutoReply'] .KeyBind.MakeFileKeyBind(['autoreply', notifier]))
        ResetFile.SetBind(self.Ctrls['TellTarget'].KeyBind.MakeFileKeyBind(['show chat', 'beginchat /tell $target, ', notifier]))
        ResetFile.SetBind(self.Ctrls['QuickChat'] .KeyBind.MakeFileKeyBind(['quickchat', notifier]))

    def findconflicts(self):
        Utility.CheckConflict(self,"FPSBindkey","FPS Display Toggle")

        Utility.CheckConflict(self,"StartChat", "Start Chat Key")
        Utility.CheckConflict(self,"SlashChat", "Slashchat Key")
        Utility.CheckConflict(self,"StartEmote","Emote Key")
        Utility.CheckConflict(self,"AutoReply", "Autoreply Key")
        Utility.CheckConflict(self,"TellTarget","Tell Target Key")
        Utility.CheckConflict(self,"QuickChat", "Quickchat Key")

    def bindisused(self):
        return self.GetState('Enable')

    UI.Labels.update({
        'FPSEnable'  : "Enable the FPS/Netgraph binds",
        'FPSBindKey' : "Turn on FPS",
        'NetgraphBindKey' : 'Turn on Netgraph',

        'ChatEnable' : 'Enable Chat Binds',
        'Message' : '"afk typing" message',
        'StartChat' : 'Start Chat (no "/")',
        'SlashChat' : 'Start Chat (with "/")',
        'StartEmote' : 'Begin emote (types "/em")',
        'AutoReply' : 'AutoReply to incoming /tell',
        'TellTarget' : 'Send /tell to current target',
        'QuickChat' : 'QuickChat',
        'TypingNotifierEnable' : 'Enable Typing Notifier',
        'TypingNotifier' : 'Typing Notifier',
    })

    for i in range(1,9):
        UI.Labels[f'TeamSelect{i}'] = f"Select {ordinals[i-1]} Team Member / Pet"
