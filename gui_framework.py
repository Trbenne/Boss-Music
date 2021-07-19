import wx
from main4 import Main
from windowcapture import WindowCapture

class MainWindow(wx.Frame):
    
    global string
    
    # initialize string for open windows list
    string = ""
    
    # build string for listing open windows
    for n in Main.wincap.win_list:
        string += n + "\n"
   
    game = "Demon's Souls (original)"
    
    main = Main()
   
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title)
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)

        # Setting up the Menu
        fileMenu = wx.Menu()

        # wx.ID_ABOUT and wx.ID_EXIT are standard IDs provided by wxWidgets.
        menuAbout = fileMenu.Append(wx.ID_ABOUT, "&About", "Information About Program")
        menuHelp = fileMenu.Append(wx.ID_HELP, "Help", " Get Sum Input Dog")
        fileMenu.AppendSeparator()
        menuExit = fileMenu.Append(wx.ID_EXIT, "E&xit", " Terminate Program")

        # Creating the Menubar
        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar) # Adding the MenuBar to the Frame content.
       
       
        # Button...
        self.button = wx.Button(self, -1, "Okay")
        self.quit = wx.Button(self, -1, "Quit")
        # Toggles Filter On and Off
        self.hsvgui = wx.ToggleButton(self, pos=(200,75), label="Filter")
       
        # Set Events
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnHelp, menuHelp)
        self.button.Bind(wx.EVT_BUTTON, self.onClicked)
        self.quit.Bind(wx.EVT_BUTTON, self.OnExit)
       
        self.ic = wx.TextCtrl(self, -1, pos=(76, 119))
        self.slaps = wx.TextCtrl(self, -1, pos=(363, 133))
       
        self.AddStaticText(pos = (362,5), label = "Tasty Jams")
       
        self.AddStaticText(pos = (450,163), label = "Current Windows")
       
        self.current_Program_Output = wx.TextCtrl(self, -1, string, size = (500,200),
                                    style = wx.TE_READONLY|wx.EXPAND|wx.TE_MULTILINE)
       
       
        self.addRadioButtons(["Demon's Souls (original)", "Dark Souls: Remastered",
                              "Dark Souls II", "Dark Souls III", "Manual"])
       
       

        self.addJamCheckBox(names = ["giorno.wav","joseph.wav","jotaro.wav","doomer.wav","jotaroVdio.wav",
                                      "where all the white women at?.wav","Manual"],
                            pos = (293,30))
               
        self.vbox.Add(self.current_Program_Output, 0, wx.EXPAND|wx.ALL, 25)
       
        self.hbox.Add(self.quit, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 10)
        self.hbox.Add(self.button, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 10)
        self.vbox.Add(self.hbox,0,wx.ALIGN_CENTER)

       
        self.SetSize(1000,550)
       
    # TODO: Change to StaticBox with RadioButtons so that u can change spacing...
    #           That will also help make the text input easier... meh
    def addRadioButtons(self, names):
        """
        Adds radio buttons for each bodypart on the right panel
        """
        self.vbox = wx.BoxSizer(wx.VERTICAL)
        self.visualization_radiobox = wx.RadioBox(
            self,
            label="Select Game",
            majorDimension=1, size = (175,140),
            style=wx.RA_SPECIFY_COLS,
            choices=names)
        self.vbox.Add(self.visualization_radiobox, 0, wx.SHAPED|wx.ALL, 10)

        self.SetSizerAndFit(self.vbox)
        self.Layout()
        self.Bind(wx.EVT_RADIOBOX, self.onRadioBox)
        return (self.vbox, self.visualization_radiobox)
   
    # TODO: Change to StaticBox with checklist buttons so that u can change spacing...
    #           That will also help make the text input easier... meh
    def addJamCheckBox(self, names, pos = (0,0)):
        """
        Adds checklistbox for music choices
        """
       
        self.tasty_jams = wx.CheckListBox(
            self,
            name="Select Soundtracks", pos = pos,
            size = (215,130),
            choices=names)
       
        self.tasty_jams.SetCheckedItems([0,1,2,3,4,5])
        # self.Layout()
        # self.Bind(wx.EVT_CHECKLISTBOX, self.onChecked)
        return (self.tasty_jams)
   
   
    def onRadioBox(self,e):
        print (self.visualization_radiobox.GetStringSelection(),' is clicked from Radio Box')
        self.game = self.visualization_radiobox.GetStringSelection()
        if self.game == "Manual":
            self.game = self.ic.GetValue()
           
           
    # # TODO: onChecked!!
    # def onChecked(self, e):
    #     global coolCats
    #     cb = e.GetEventObject()
    #     print (cb.GetName(),' is clicked')
       
    def ReeChecked(self):
        global coolCats
        global coolCatz
        coolCats = list(self.tasty_jams.GetCheckedStrings())
       
        coolCatz = []
        for s in coolCats:
            coolCat = s.replace("Manual", self.slaps.GetValue())
            coolCatz.append(coolCat)
        print(coolCatz)
       
       
    def AddStaticText(self, pos, label):
        # put some text
        self.st = wx.StaticText(self, -1, style = wx.LC_REPORT, size = (75,23),
                                pos = pos, label = label)
       
        # create font object
        font = self.st.GetFont()
       
        # increase text size
        font.PointSize += 2
       
        # make text bold
        font = font.Bold()
       
        # associate font with text
        self.st.SetFont(font)
           
     
    def onClicked(self, event):

        # change capture window to chosen game
        global wincap
       
        self.ReeChecked()
       
        # Checks if the filter is checked on
        isFilter = self.hsvgui.GetValue()
        print(isFilter)
       
        Main.wincap = WindowCapture(self.game)

        if self.game == "Demon's Souls (original)":
            Main.demonSouls()
        elif  self.game == "Dark Souls: Remastered":
            print("we should be running DSI now...")
        elif  self.game == "Dark Souls II":
            print("we should be running DSII now...")
        elif  self.game == "Dark Souls III":
            print("we should be running DSIII now...")
        else:
           self.game = self.ic.GetValue()
           wincap = WindowCapture(self.game)
           print("Manual Entry: ", self.game)
           Main.demonSouls()
            # TODO: make a manual output too...
   
    def OnAbout(self, e):
        # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
        dlg = wx.MessageDialog(self,
                        "This shit will play buteeful music when you fight bosses",
                        "About:")
        dlg.ShowModal() # Show It
        dlg.Destroy() # Destroy it when finished
       
    def OnHelp(self, e):
        # Message about all help stuffs and info
        dlg = wx.MessageDialog(self,
                        "Games:\n When inputing a manual game name, "
                        "refer to the textfield of current programs\n"
                        "\nTastey Jams:\n When inputing a manual jam, specify the path."
                        "ie: C://User//Paul_Blart//desktop"
                        "\n      Use double '//'s to avoid making the program angry\n"
                        "\nDemon's Souls:\n Demon's Souls' name must be adjusted in RPCS3 to 'Demon's Souls'",
                        "Helps:\n")
        dlg.ShowModal() # Show It
        dlg.Destroy() # Destroy it when finished
       
    def OnExit(self, e):
        global kill
        kill = True
        self.Close(True) # Close the frame

app = wx.App(False)
frame = MainWindow(None, "Epic Finishers")
frame.Show(True)
app.MainLoop()
# ! have to add in ability to use custom photos
#  and eventually even add filter to said photos
# if "Manual" photo, activate filter...
# They'll have to screenshot the filter and then make custom jpg...
#   Then add manual filter button with array for filter, (Gut the Demon() function)
# !* For Filter; just use filter on/off switch to make it. Then adjust Demon() accordingly.
#       Add filter help with instructions to not use it unless you know how to...
# use Victory Achieved??? for pog champ???