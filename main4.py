import cv2 as cv
import time
from windowcapture import WindowCapture
from vision import Vision
from cannyEdge import EdgeFilter
from hsvfilter import HsvFilter
import pygame.mixer
import random
import wx

# initialize the WindowCapture class
wincap = WindowCapture()

# creates list of strings of open windows
wincap.homie()
# initialize coolCats list
coolCats = []
# initialize coolCatz list
coolCatz = []

# custom_filter_value = []

# Initialize manual_filter
manual_filter = False 
# Initialize custom_pics
custom_pics = False 

# initialize string for open windows list
string = ""
    
# build string for listing open windows
for n in wincap.win_list:
    string += n + "\n"

pygame.mixer.init()

# initialize Jojo's themes
pygame.mixer.music.set_volume(0.7)
# test = pygame.mixer.Sound('test.wav')
# johnathan = pygame.mixer.Sound('johnathan.wav') # johnny's Theme
# jotaro = pygame.mixer.Sound('jotaro.wav') # jotaro Theme
# josuke = pygame.mixer.Sound('josuke.wav') # Josuke
# giorno = pygame.mixer.Sound('giorno.wav') # Giorno Theme
# doomer = pygame.mixer.Sound('doomer.wav') # play doom metal music
# jotaroVDio = pygame.mixer.Sound('jotaroVDio.wav') # I have to come closer...
anime = pygame.mixer.Sound('godANDanime.wav')
pog_champ = pygame.mixer.Sound('pog.wav')

anime.set_volume(1)

hsv_filter = HsvFilter(0, 0, 0, 179, 255, 255, 0, 0, 0, 0)
hsv_filter2 = HsvFilter(0, 0, 0, 179, 255, 255, 0, 0, 0, 0)

rectTrue = False # global variable %
kill = False # global variable %

# initialize the Vision class
## this one is the trend setter, the identifier for hp
# initialize Vision class
# if wincap.name == "Demon's Souls" or wincap.name == "Screenshot (21).png - Paint":
#     vis = Vision('demon_souls_processed_1.jpg') # demon_souls_processed_1.jpg
#     # # initialize HP (This is the lowest the hp gets before the song plays)
#     # vision_hp = Vision('demon_souls_2.jpg') #demon_souls_processed_2.jpg
#     print("we're playing demon's souls")
#     hsv_filter = HsvFilter(0, 0, 0, 62, 33, 141, 32, 30, 0, 0)
#     # hsv_filter2 = HsvFilter(0, 160, 63, 179, 218, 198, 114, 45, 48, 0)
# elif wincap.name == "Dark Souls II":
#     print(wincap.name)
#     vis = Vision('photo1.jpg')
#     vision_hp = Vision('ds2_healf_2.jpg') # Or 22? if being bad...
#     print("DS2")
#     # limestone HSV filter
#     hsv_filter = HsvFilter(0, 0, 0, 179, 255, 255, 0, 0, 0, 0)
#     hsv_filter2 = HsvFilter(0, 160, 63, 179, 218, 198, 114, 45, 48, 0) # (0, 79, 36, 179, 152, 94, 0, 42, 29, 0)
#     #hsv_filter2 = HsvFilter(0, 0, 0, 179, 255, 255, 0, 0, 0, 0)
# elif wincap.name == "Dark Souls III" or wincap.name == "Screenshot (27).png - Paint":
#     print(wincap.name)
#     print("DS3")


# initialize the trackbar window
# vis.init_control_gui()
# vision_hp.init_control_gui()
   

def check_rectangles(rect1, rect2, rect3):
    """ 
    Checks if the boss' health bar is present and if there is at least a 
    minimum amount of health left.
    
    This requires 3 pictures;
    rect1: minimum health allowed before music
    rect2: edge detection of half full health bar
    rect3: edge detection of half empty health bar
    """
    
    global rectTrue, TastyJams, i # use global
    global boss
    global coolCatz
    global anime, pog_champ
    
    # if there is no matching hp and the boss' health bar is present, play music
    if rect1.size <= 2 and boss:
        
        # checks i, which is only used to check if anime has played once
        if i == False:
            anime.play()
            i = True
        
        # !!! % may be pointless, but rectTrue checks if min health is present
        rectTrue = False
            
        # initialize the random number
        rand = random.randint(1,2*len(coolCatz))
        
        # this if-else stream is to play a random theme
        if rand <= 2 and not pygame.mixer.music.get_busy():
            currentSound = coolCatz[0]
            pygame.mixer.music.load(coolCatz[0])
           
        elif rand <= 4 and not pygame.mixer.music.get_busy():
            currentSound = coolCatz[1]
            pygame.mixer.music.load(coolCatz[1])
       
        elif rand <= 6 and not pygame.mixer.music.get_busy():
            currentSound = coolCatz[2]
            pygame.mixer.music.load(coolCatz[2])
       
        elif rand <= 8 and not pygame.mixer.music.get_busy():
            currentSound = coolCatz[3]
            pygame.mixer.music.load(coolCatz[3])
       
        elif rand <= 10 and not pygame.mixer.music.get_busy():
            currentSound = coolCatz[4]
            pygame.mixer.music.load(coolCatz[4])
            
        elif rand <= 12 and not pygame.mixer.music.get_busy():
            currentSound = coolCatz[5]
            pygame.mixer.music.load(coolCatz[5])
        
        elif rand <= 14 and not pygame.mixer.music.get_busy():
            currentSound = coolCatz[6]
            pygame.mixer.music.load(coolCatz[6])
        
        if(rect1.size <= 2 and (rect2.size >= 1 or rect3.size >= 1)):
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.load(currentSound)
                pygame.mixer.music.play()
                # time.sleep(15)
                    
    # checks if the boss is dead, and makes sure that it 
    # only plays after boss fight by checking i
    if (not boss) and i:     
        # gives 5 second leeway to ensure pog_champ plays after 
        # other music at end of boss fight
        time.sleep(5) 
        pog_champ.play()
        time.sleep(pog_champ.get_length()) # delays everything until pog_champ has finished
        i = False # reset i so that anime and pog_champ will play next boss fight
        
    # check if there is a boss health bar present
    if rect2.size >= 1 or rect3.size >= 1:
        boss = True
    else:
        boss = False

        
# def TastyJams():

#     global coolCatz
#     global anime
#     global johnathan, jotaro, josuke, giorno, doomer, pog_champ
    
#     anime.set_volume(1)
#     anime.play()
    
#     # t_now = time.time() + 60
            
#     # while time.time() <= t_now:
        
#     # initialize the random number
#     rand = random.randint(0,9)
    
#     # currentSound = test
#     # pygame.mixer.music.load('test.wav')

#     # this if-else stream is to play a random theme
#     # this if-else stream is to play a random theme
#     if rand <= 1 and not pygame.mixer.music.get_busy():
#         currentSound = coolCatz[0]
#         pygame.mixer.music.load(coolCatz[0])
       
#     elif rand <= 3 and not pygame.mixer.music.get_busy():
#         currentSound = coolCatz[1]
#         pygame.mixer.music.load(coolCatz[1])
   
#     elif rand <= 5 and not pygame.mixer.music.get_busy():
#         currentSound = coolCatz[2]
#         pygame.mixer.music.load(coolCatz[2])
   
#     elif rand <= 7 and not pygame.mixer.music.get_busy():
#         currentSound = coolCatz[3]
#         pygame.mixer.music.load(coolCatz[3])
   
#     elif rand <= 9 and not pygame.mixer.music.get_busy():
#         currentSound = coolCatz[4]
#         pygame.mixer.music.load(coolCatz[4])
    
#     # if rand <= 0 and not pygame.mixer.music.get_busy():
#     #     currentSound = johnathan
#     #     pygame.mixer.music.load('johnathan.wav')
                  
                    

def rectCheck(rect):
    """  %
    function rectCheck will check to see if the minimum health is still there,
    once it is not there, it will play music.
    
    This version only requires one picture of the health bar, once health is
    low enough that it doesn't register, music begins
    
    """
   
    global rectTrue, TastyJams # use global
   
    # if there is no matching hp, but there was one last iteration, play music
    if rect.size < 1 and rectTrue:
                
        TastyJams()
        
        # reset rectTrue
        rectTrue = False
   
    # check if there is a health bar with matching hp
    if rect.size >= 1:
        rectTrue = True
    else:
        rectTrue = False
        
        
def Default(): # %%%
# TODO: Default Checks %%%
   
    global manual_filter # %%%
    global filterChoice # %%%
    global wincap
    global custom_filter_value
    global boss
    global kill
    global i
    
    # initialize the Vision class
    # min hp
    solo_hp = Vision('ds3_healf_2.jpg')
    
    # half empty health edges
    vision_limestone = Vision('darks3_edges_151.jpg') #'ds3_edges.jpg' _151, _81
    
    # half full health edges
    vision_limestone2 = Vision('lights3_edges.jpg')
    
    if custom_pics:
        solo_hp = Vision(str(frame.rectangle_pic_1.GetValue()))
        vision_limestone = Vision(frame.rectangle_pic_2.GetValue())
        vision_limestone2 = Vision(frame.rectangle_pic_3.GetValue())
    
    if manual_filter == True: # %%%
        # initialize the trackbar window %???
        solo_hp.init_control_gui()# %%%
        
        # initialize the trackbar window
        vision_limestone.init_control_gui()
        # TODO: make this adjustable to be on/off (Maybe only available by using manual default function?)
    
    # initialize boss and i as false so that the music won't run until a boss is present
    boss = False
    i = False
    
    # # HSV and edge filters for respective pictures
    # hsv_filter = HsvFilter(0, 67, 13, 179, 255, 169, 0, 0, 13, 0)
    # hsv_filter2 = HsvFilter(0, 0, 0, 179, 255, 255, 0, 1, 255, 7)
    # hsv_filter3 = HsvFilter(0, 0, 44, 179, 0, 255, 0, 85, 255, 63)
    # edge_filter = EdgeFilter(3,3,3,88,151) #88, 151 || 200,81
    # edge_filter2 = EdgeFilter(8,2,1,200,500)
    
    # continuously run
    while(True):
    
        # get an updated image of the game
        screenshot = wincap.get_screenshot()
        
        # pre-process the image %%%
        if manual_filter == True:
            
            # pre-process the image
            processed_image = solo_hp.apply_hsv_filter(screenshot) # %
            
            # pre-process the image
            processed_image2 = vision_limestone.apply_hsv_filter(screenshot)
            processed_image3 = vision_limestone.apply_hsv_filter(screenshot)
        
            # do edge detection
            edges_image = vision_limestone.apply_edge_filter(processed_image2)
            edges_image2 = vision_limestone2.apply_edge_filter(processed_image3)
            # Show processed image only if this is turned on...
            
        else:
            
            if filterChoice: #  %%%
                hsv_filter = HsvFilter( #  %%%
                    hMin=custom_filter_value[0], sMin=custom_filter_value[1],
                    vMin=custom_filter_value[2], hMax=custom_filter_value[3],
                    sMax=custom_filter_value[4], vMax=custom_filter_value[5],
                    sAdd=custom_filter_value[6], sSub=custom_filter_value[7],
                    vAdd=custom_filter_value[8], vSub=custom_filter_value[9])
                hsv_filter2 = HsvFilter( #  %%%
                    hMin=custom_filter_value[10], sMin=custom_filter_value[11],
                    vMin=custom_filter_value[12], hMax=custom_filter_value[13],
                    sMax=custom_filter_value[14], vMax=custom_filter_value[15],
                    sAdd=custom_filter_value[16], sSub=custom_filter_value[17],
                    vAdd=custom_filter_value[18], vSub=custom_filter_value[19])
                hsv_filter3 = HsvFilter( #  %%%
                    hMin=custom_filter_value[20], sMin=custom_filter_value[21],
                    vMin=custom_filter_value[22], hMax=custom_filter_value[23],
                    sMax=custom_filter_value[24], vMax=custom_filter_value[25],
                    sAdd=custom_filter_value[26], sSub=custom_filter_value[27],
                    vAdd=custom_filter_value[28], vSub=custom_filter_value[29])
                
                edge_filter = EdgeFilter(kernelSize=custom_filter_value[30], 
                    erodeIter=custom_filter_value[31], dilateIter=custom_filter_value[32], 
                    canny1=custom_filter_value[33], canny2=custom_filter_value[34])
                edge_filter2 = EdgeFilter(kernelSize=custom_filter_value[35], 
                    erodeIter=custom_filter_value[36], dilateIter=custom_filter_value[37], 
                    canny1=custom_filter_value[38], canny2=custom_filter_value[39])

            else:
                hsv_filter = HsvFilter(0, 67, 13, 179, 255, 169, 0, 0, 13, 0)
                hsv_filter2 = HsvFilter(0, 0, 0, 179, 255, 255, 0, 1, 255, 7)
                hsv_filter3 = HsvFilter(0, 0, 44, 179, 0, 255, 0, 85, 255, 63)
                edge_filter = EdgeFilter(3,3,3,88,151) #88, 151 || 200,81
                edge_filter2 = EdgeFilter(8,2,1,200,500)
                
            # pre-process the image
            processed_image = solo_hp.apply_hsv_filter(screenshot, hsv_filter) # %
            
            # pre-process the image
            processed_image2 = vision_limestone.apply_hsv_filter(screenshot, hsv_filter2)
            processed_image3 = vision_limestone.apply_hsv_filter(screenshot, hsv_filter3)
        
            # do edge detection
            edges_image = vision_limestone.apply_edge_filter(processed_image2, edge_filter)
            edges_image2 = vision_limestone2.apply_edge_filter(processed_image3, edge_filter2)

    
        # do object detection for each picture
        rectangles = solo_hp.find(processed_image, 0.95) # % 75 for full
        rectangles2 = vision_limestone.find(edges_image, 0.8)
        rectangles3 = vision_limestone2.find(edges_image2, 0.8)
        
        # count number of matches
        check_rectangles(rectangles, rectangles2, rectangles3)
        
      ############################################################
        
        # draw the detection results onto the original image
        output_image = solo_hp.draw_rectangles(screenshot, rectangles) # %
        edge = vision_limestone.draw_rectangles(screenshot, rectangles2)
        edge2 = vision_limestone.draw_rectangles(screenshot, rectangles3)
    
        # display the processed images
        # TODO: Only Show if manual filter is clicked on
        # if manual_filter or filterChoice:
        cv.imshow('Processed', processed_image)
        cv.imshow('Matches', output_image)
        cv.imshow('Edges', edges_image)
        # cv.imshow('Processed 2', processed_image2)
        # cv.imshow('Edges', edge)
    
    
        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('q') or kill:
            cv.destroyAllWindows()
            break
    

def DemonSouls():
    
    global manual_filter
    global filterChoice
    global wincap
    global custom_filter_value
    global boss
    global kill
    global i
    
    # initialize the Vision class
    ## this one is the trend setter
    solo_hp = Vision('demon_souls_processed_22.jpg')
    # TODO: Add Edges 
    vision_edges_1 = Vision('demon_souls_processed_22.jpg') # demon_edges_1.jpg
    vision_edges_2 = Vision('demon_souls_processed_22.jpg') # demon_edges_2.jpg
    
    if custom_pics:
        solo_hp = Vision(str(frame.rectangle_pic_1.GetValue()))
        vision_edges_1 = Vision(frame.rectangle_pic_2.GetValue())
        vision_edges_2 = Vision(frame.rectangle_pic_3.GetValue())

    
    if manual_filter == True: # %%%
        # initialize the trackbar window %???
        solo_hp.init_control_gui()# %%%
        vision_edges_1.init_control_gui() # %%%???
        vision_edges_2.init_control_gui() # %%%???
        # TODO: Do I need both pics???
    
    while(True):
    
        # get an updated image of the game
        screenshot = wincap.get_screenshot()
    
        # pre-process the image %%%
        if manual_filter == True:
            
            # solo_hp.edge GUI Stuff
            processed_image = solo_hp.apply_hsv_filter(screenshot) # %
            # Show processed image only if this is turned on...
            
        else:
            
            if filterChoice: #  %%%
                hsv_filter = HsvFilter( #  %%%
                    hMin=custom_filter_value[0], sMin=custom_filter_value[1],
                    vMin=custom_filter_value[2], hMax=custom_filter_value[3],
                    sMax=custom_filter_value[4], vMax=custom_filter_value[5],
                    sAdd=custom_filter_value[6], sSub=custom_filter_value[7],
                    vAdd=custom_filter_value[8], vSub=custom_filter_value[9])
                hsv_filter2 = HsvFilter( #  %%%
                    hMin=custom_filter_value[10], sMin=custom_filter_value[11],
                    vMin=custom_filter_value[12], hMax=custom_filter_value[13],
                    sMax=custom_filter_value[14], vMax=custom_filter_value[15],
                    sAdd=custom_filter_value[16], sSub=custom_filter_value[17],
                    vAdd=custom_filter_value[18], vSub=custom_filter_value[19])
                hsv_filter3 = HsvFilter( #  %%%
                    hMin=custom_filter_value[20], sMin=custom_filter_value[21],
                    vMin=custom_filter_value[22], hMax=custom_filter_value[23],
                    sMax=custom_filter_value[24], vMax=custom_filter_value[25],
                    sAdd=custom_filter_value[26], sSub=custom_filter_value[27],
                    vAdd=custom_filter_value[28], vSub=custom_filter_value[29])
                
                edge_filter = EdgeFilter(kernelSize=custom_filter_value[30], 
                    erodeIter=custom_filter_value[31], dilateIter=custom_filter_value[32], 
                    canny1=custom_filter_value[33], canny2=custom_filter_value[34])
                edge_filter2 = EdgeFilter(kernelSize=custom_filter_value[35], 
                    erodeIter=custom_filter_value[36], dilateIter=custom_filter_value[37], 
                    canny1=custom_filter_value[38], canny2=custom_filter_value[39])
            else:
                hsv_filter = HsvFilter(0, 160, 63, 179, 218, 198, 114, 45, 48, 0)
            processed_image = solo_hp.apply_hsv_filter(screenshot, hsv_filter)
        ###########################%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
   ## Here down needs review if it isn't replaced by DSIII code...
        # # pre-process the image
        # processed_image = vision_limestone.apply_hsv_filter(screenshot)
    
        # # do edge detection
        # edges_image = vision_limestone.apply_edge_filter(processed_image)
    
        # do object detection
        rectangles = solo_hp.find(processed_image, 0.7) # %
       
        rectCheck(rectangles) # %
       
    
        # draw the detection results onto the original image
        output_image = solo_hp.draw_rectangles(screenshot, rectangles) # %
    
        # display the processed image
        # if manual_filter:
        cv.imshow('Processed', processed_image)
        cv.imshow('Matches', output_image)

        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('q') or kill:
            cv.destroyAllWindows()
            break   
        
        
        # TODO: Demon's Souls: Remastered, DS1/DS1: Remastered
        
        
def DarkSoulsII():    
    
    global manual_filter # %%%
    global filterChoice # %%%
    global wincap
    global custom_filter_value
    global boss
    global kill
    global i
    
    solo_hp = Vision('photo1.jpg')
    # TODO: Add Edges 
    vision_edges_1 = Vision('ds2_healf_2.jpg') # Or 22? if being bad...
    vision_edges_2 = Vision('ds2_healf_2.jpg') # ds2_edges.jpg
    
    if custom_pics:
        solo_hp = Vision(str(frame.rectangle_pic_1.GetValue()))
        vision_edges_1 = Vision(frame.rectangle_pic_2.GetValue())
        vision_edges_2 = Vision(frame.rectangle_pic_3.GetValue())


    
    if manual_filter == True: # %%%
        # initialize the trackbar window %???
        solo_hp.init_control_gui()# %%%
        vision_edges_1.init_control_gui() # %%%???
        vision_edges_2.init_control_gui() # %%%???
        # TODO: Do I need both pics???
        
        
    # initialize boss and i as false so that the music won't run until a boss is present
    boss = False
    i = False
    
    # HSV and edge filters for respective pictures
    hsv_filter = HsvFilter(0, 67, 13, 179, 255, 169, 0, 0, 13, 0)
    hsv_filter2 = HsvFilter(0, 0, 0, 179, 255, 255, 0, 1, 255, 7)
    hsv_filter3 = HsvFilter(0, 0, 44, 179, 0, 255, 0, 85, 255, 63)
    edge_filter = EdgeFilter(3,3,3,88,151) #88, 151 || 200,81
    edge_filter2 = EdgeFilter(8,2,1,200,500)
    
    # continuously run
    while(True):
    
        # get an updated image of the game
        screenshot = wincap.get_screenshot()
        
        # pre-process the image %%%
        if manual_filter == True:
            
            # pre-process the image
            processed_image = solo_hp.apply_hsv_filter(screenshot) # %
            
            # pre-process the image
            processed_image2 = vision_edges_1.apply_hsv_filter(screenshot)
            processed_image3 = vision_edges_2.apply_hsv_filter(screenshot)
        
            # do edge detection
            edges_image = vision_edges_1.apply_edge_filter(processed_image2)
            edges_image2 = vision_edges_2.apply_edge_filter(processed_image3)
            # Show processed image only if this is turned on...
            
        else:
            
            if filterChoice: #  %%%
                hsv_filter = HsvFilter( #  %%%
                    hMin=custom_filter_value[0], sMin=custom_filter_value[1],
                    vMin=custom_filter_value[2], hMax=custom_filter_value[3],
                    sMax=custom_filter_value[4], vMax=custom_filter_value[5],
                    sAdd=custom_filter_value[6], sSub=custom_filter_value[7],
                    vAdd=custom_filter_value[8], vSub=custom_filter_value[9])
                hsv_filter2 = HsvFilter( #  %%%
                    hMin=custom_filter_value[10], sMin=custom_filter_value[11],
                    vMin=custom_filter_value[12], hMax=custom_filter_value[13],
                    sMax=custom_filter_value[14], vMax=custom_filter_value[15],
                    sAdd=custom_filter_value[16], sSub=custom_filter_value[17],
                    vAdd=custom_filter_value[18], vSub=custom_filter_value[19])
                hsv_filter3 = HsvFilter( #  %%%
                    hMin=custom_filter_value[20], sMin=custom_filter_value[21],
                    vMin=custom_filter_value[22], hMax=custom_filter_value[23],
                    sMax=custom_filter_value[24], vMax=custom_filter_value[25],
                    sAdd=custom_filter_value[26], sSub=custom_filter_value[27],
                    vAdd=custom_filter_value[28], vSub=custom_filter_value[29])
                
                edge_filter = EdgeFilter(kernelSize=custom_filter_value[30], 
                                          erodeIter=custom_filter_value[31], 
                                          dilateIter=custom_filter_value[32], 
                                          canny1=custom_filter_value[33], 
                                          canny2=custom_filter_value[34])
                edge_filter2 = EdgeFilter(kernelSize=custom_filter_value[35], 
                                          erodeIter=custom_filter_value[36], 
                                          dilateIter=custom_filter_value[37], 
                                          canny1=custom_filter_value[38], 
                                          canny2=custom_filter_value[39])
            else:
                hsv_filter = HsvFilter(0, 67, 13, 179, 255, 169, 0, 0, 13, 0)
                hsv_filter2 = HsvFilter(0, 0, 0, 179, 255, 255, 0, 1, 255, 7)
                hsv_filter3 = HsvFilter(0, 0, 44, 179, 0, 255, 0, 85, 255, 63)
                edge_filter = EdgeFilter(3,3,3,88,151) #88, 151 || 200,81
                edge_filter2 = EdgeFilter(8,2,1,200,500)
                
            # pre-process the image
            processed_image = solo_hp.apply_hsv_filter(screenshot, hsv_filter) # %
            
            # pre-process the image
            processed_image2 = vision_edges_1.apply_hsv_filter(screenshot, hsv_filter2)
            processed_image3 = vision_edges_2.apply_hsv_filter(screenshot, hsv_filter3)
        
            # do edge detection
            edges_image = vision_edges_1.apply_edge_filter(processed_image2, edge_filter)
            edges_image2 = vision_edges_2.apply_edge_filter(processed_image3, edge_filter2)

    
        # do object detection for each picture
        rectangles = solo_hp.find(processed_image, 0.95) # % 75 for full
        rectangles2 = vision_edges_1.find(edges_image, 0.8)
        rectangles3 = vision_edges_2.find(edges_image2, 0.8)
        
        # count number of matches
        check_rectangles(rectangles, rectangles2, rectangles3)
        
      ############################################################
        
        # draw the detection results onto the original image
        output_image = solo_hp.draw_rectangles(screenshot, rectangles) # %
        edge = vision_edges_1.draw_rectangles(screenshot, rectangles2)
        edge2 = vision_edges_2.draw_rectangles(screenshot, rectangles3)
    
        # display the processed images
        # TODO: Only Show if manual filter is clicked on
        # if manual_filter:
        cv.imshow('Processed', processed_image)
        cv.imshow('Matches', output_image)
        cv.imshow('Edges', edges_image)
        # cv.imshow('Processed 2', processed_image2)
        # cv.imshow('Edges', edge)
    
    
        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('q') or kill:
            cv.destroyAllWindows()
            break
    
   
def DarkSoulsIII():
    
    global manual_filter # %%%
    global filterChoice # %%%
    global wincap
    global custom_filter_value
    global boss
    global kill
    global i
    
    # initialize the Vision class
    # min hp
    solo_hp = Vision('ds3_healf_2.jpg')
    
    # half empty health edges
    vision_limestone = Vision('darks3_edges_151.jpg') #'ds3_edges.jpg' _151, _81
    
    # half full health edges
    vision_limestone2 = Vision('lights3_edges.jpg')
    
    if custom_pics:
        solo_hp = Vision(str(frame.rectangle_pic_1.GetValue()))
        vision_limestone = Vision(frame.rectangle_pic_2.GetValue())
        vision_limestone2 = Vision(frame.rectangle_pic_3.GetValue())

    
    if manual_filter == True: # %%%
        # initialize the trackbar window %???
        solo_hp.init_control_gui()# %%%
        
        # initialize the trackbar window
        vision_limestone.init_control_gui()
        # TODO: make this adjustable to be on/off (Maybe only available by using manual default function?)
    
    # initialize boss and i as false so that the music won't run until a boss is present
    boss = False
    i = False
    
    # HSV and edge filters for respective pictures
    hsv_filter = HsvFilter(0, 67, 13, 179, 255, 169, 0, 0, 13, 0)
    hsv_filter2 = HsvFilter(0, 0, 0, 179, 255, 255, 0, 1, 255, 7)
    hsv_filter3 = HsvFilter(0, 0, 44, 179, 0, 255, 0, 85, 255, 63)
    edge_filter = EdgeFilter(3,3,3,88,151) #88, 151 || 200,81
    edge_filter2 = EdgeFilter(8,2,1,200,500)
    
    # continuously run
    while(True):
    
        # get an updated image of the game
        screenshot = wincap.get_screenshot()
        
        # pre-process the image %%%
        if manual_filter == True:
            
            # pre-process the image
            processed_image = solo_hp.apply_hsv_filter(screenshot) # %
            
            # pre-process the image
            processed_image2 = vision_limestone.apply_hsv_filter(screenshot)
            processed_image3 = vision_limestone2.apply_hsv_filter(screenshot)
        
            # do edge detection
            edges_image = vision_limestone.apply_edge_filter(processed_image2)
            edges_image2 = vision_limestone2.apply_edge_filter(processed_image3)
            # Show processed image only if this is turned on...
            
        else:
            
            if filterChoice: #  %%%
                hsv_filter = HsvFilter( #  %%%
                    hMin=custom_filter_value[0], sMin=custom_filter_value[1],
                    vMin=custom_filter_value[2], hMax=custom_filter_value[3],
                    sMax=custom_filter_value[4], vMax=custom_filter_value[5],
                    sAdd=custom_filter_value[6], sSub=custom_filter_value[7],
                    vAdd=custom_filter_value[8], vSub=custom_filter_value[9])
                hsv_filter2 = HsvFilter( #  %%%
                    hMin=custom_filter_value[10], sMin=custom_filter_value[11],
                    vMin=custom_filter_value[12], hMax=custom_filter_value[13],
                    sMax=custom_filter_value[14], vMax=custom_filter_value[15],
                    sAdd=custom_filter_value[16], sSub=custom_filter_value[17],
                    vAdd=custom_filter_value[18], vSub=custom_filter_value[19])
                hsv_filter3 = HsvFilter( #  %%%
                    hMin=custom_filter_value[20], sMin=custom_filter_value[21],
                    vMin=custom_filter_value[22], hMax=custom_filter_value[23],
                    sMax=custom_filter_value[24], vMax=custom_filter_value[25],
                    sAdd=custom_filter_value[26], sSub=custom_filter_value[27],
                    vAdd=custom_filter_value[28], vSub=custom_filter_value[29])
                
                edge_filter = EdgeFilter(kernelSize=custom_filter_value[30], 
                                          erodeIter=custom_filter_value[31], 
                                          dilateIter=custom_filter_value[32], 
                                          canny1=custom_filter_value[33], 
                                          canny2=custom_filter_value[34])
                edge_filter2 = EdgeFilter(kernelSize=custom_filter_value[35], 
                                          erodeIter=custom_filter_value[36], 
                                          dilateIter=custom_filter_value[37], 
                                          canny1=custom_filter_value[38], 
                                          canny2=custom_filter_value[39])
                
            else:
                hsv_filter = HsvFilter(0, 67, 13, 179, 255, 169, 0, 0, 13, 0)
                hsv_filter2 = HsvFilter(0, 0, 0, 179, 255, 255, 0, 1, 255, 7)
                hsv_filter3 = HsvFilter(0, 0, 44, 179, 0, 255, 0, 85, 255, 63)
                edge_filter = EdgeFilter(3,3,3,88,151) #88, 151 || 200,81
                edge_filter2 = EdgeFilter(8,2,1,200,500)
                
            # pre-process the image
            processed_image = solo_hp.apply_hsv_filter(screenshot, hsv_filter) # %
            
            # pre-process the image
            processed_image2 = vision_limestone.apply_hsv_filter(screenshot, hsv_filter2)
            processed_image3 = vision_limestone2.apply_hsv_filter(screenshot, hsv_filter3)
        
            # do edge detection
            edges_image = vision_limestone.apply_edge_filter(processed_image2, edge_filter)
            edges_image2 = vision_limestone2.apply_edge_filter(processed_image3, edge_filter2)

    
        # do object detection for each picture
        rectangles = solo_hp.find(processed_image, 0.95) # % 75 for full
        rectangles2 = vision_limestone.find(edges_image, 0.8)
        rectangles3 = vision_limestone2.find(edges_image2, 0.8)
        
        # count number of matches
        check_rectangles(rectangles, rectangles2, rectangles3)
        
      ############################################################
        
        # draw the detection results onto the original image
        output_image = solo_hp.draw_rectangles(screenshot, rectangles) # %
        edge = vision_limestone.draw_rectangles(screenshot, rectangles2)
        edge2 = vision_limestone2.draw_rectangles(screenshot, rectangles3)
    
        # display the processed images
        # TODO: Only Show if manual filter is clicked on
        # if manual_filter:
        cv.imshow('Processed', processed_image)
        cv.imshow('Matches', output_image)
        cv.imshow('Edges', edges_image)
        # cv.imshow('Processed 2', processed_image2)
        # cv.imshow('Edges', edge)
    
    
        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('q') or kill:
            cv.destroyAllWindows()
            break
        
    
class MainWindow(wx.Frame):
    
    global string
   
    # set default game to Demon's Souls
    game = "Demon's Souls (original)"
    preset = "Demon's Souls (original)"
       
    def __init__(self, parent, title):
        
        global manual_filter # %%%
        
        wx.Frame.__init__(self, parent, title = title)
        self.CreateStatusBar() # A Statusbar in the bottom of the window

        # creating hbox and vbox for window
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
        # Set up button for custom photos
        self.photo_button = wx.ToggleButton(self, pos=(750,15), label="Custom Photos")
        # Toggles Filter On and Off
        self.hsvgui = wx.ToggleButton(self, pos=(270,237), label="Manual Filter")
       
        # Toggle custom filter usage
        self.custom_hsv = wx.ToggleButton(self, pos=(760,165), label="Custom Filter:")
                                                    # 50, 155
       
        # Set Events
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
        self.Bind(wx.EVT_MENU, self.OnHelp, menuHelp)
        self.button.Bind(wx.EVT_BUTTON, self.onClicked) 
        self.quit.Bind(wx.EVT_BUTTON, self.OnExit)
        self.photo_button.Bind(wx.EVT_TOGGLEBUTTON, self.OnPic)
       
       
        # creating manual text entries
        self.ic = wx.TextCtrl(self, -1, pos=(76, 119))
        self.slaps = wx.TextCtrl(self, -1, pos=(513, 133))
       
        # Adds user chosen filter option %%%
        self.custom_filter_1 = wx.TextCtrl(self, -1, size=(230,23), pos=(700,198))
        self.custom_filter_2 = wx.TextCtrl(self, -1, size=(230,23), pos=(700,228))
        self.custom_filter_3 = wx.TextCtrl(self, -1, size=(230,23), pos=(700,258))
        self.custom_edge_filter = wx.TextCtrl(self, -1, size=(230,23), pos=(700,288))
        
        # set default value for custom_filters
        self.custom_filter_1.SetValue("0, 0, 0, 179, 255, 255, 0, 0, 0, 0")
        self.custom_filter_2.SetValue("0, 0, 0, 179, 255, 255, 0, 0, 0, 0")
        self.custom_filter_3.SetValue("0, 0, 0, 179, 255, 255, 0, 0, 0, 0")
        self.custom_edge_filter.SetValue("5, 1, 1, 100, 200, 5, 1, 1, 100, 200")
        
        #   %%%
        # Text Boxes that take user input for uploading pictures
        self.R1 = wx.StaticText(self, -1, style = wx.LC_REPORT,
                                pos = (700,53), label = "Min Health Picture")
        self.R2 = wx.StaticText(self, -1, style = wx.LC_REPORT,
                                pos = (700,86), label = "Half Empty Outline")
        self.R3 = wx.StaticText(self, -1, style = wx.LC_REPORT,
                                pos = (715,119), label = "Half Full Outline")
        
        # make rectangle picture input boxes %%%
        self.rectangle_pic_1 = wx.TextCtrl(self, -1, pos = (805,50))
        self.rectangle_pic_2 = wx.TextCtrl(self, -1, pos = (805,83))
        self.rectangle_pic_3 = wx.TextCtrl(self, -1, pos = (805,116))
        self.rectangle_pic_1.Enable(False)
        self.rectangle_pic_2.Enable(False)
        self.rectangle_pic_3.Enable(False)
       
        # Add Static Text
        self.AddStaticText(pos = (519,5), label = "Tasty Jams")
        self.AddStaticText(pos = (260,50), label = "Manual Presets...")
        self.AddStaticText(pos = (450,285), label = "Current Windows")
       
        # outputs current programs and posts them in a read-only textbox
        self.current_Program_Output = wx.TextCtrl(self, -1, string, size = (500,200),
                                    style = wx.TE_READONLY|wx.EXPAND|wx.TE_MULTILINE)
       
        # adding radio buttons for game choices
        self.addRadioButtons(["Demon's Souls (original)", "Dark Souls: Remastered",
                              "Dark Souls II", "Dark Souls III", "Manual"])
      
        # adding check boxes for music selection
        self.addJamCheckBox(pos = (450,30), 
                            names = ["johnathan.wav","jotaro.wav","josuke.wav",
                                     "giorno.wav","doomer.wav","jotaroVDio.wav",
                                     "Manual"])
        # TODO: fix above .wav files
        
        #  %%%
        self.manual_options= wx.RadioBox(self, name = "Manual Entries",
                            choices = ["Demon's Souls (original)","Dark Souls",
                                       "Dark Souls: Remastered","Dark Souls II",
                                       "Dark Souls III","Default"],
                            pos = (240,75), majorDimension=1,style=wx.RA_SPECIFY_COLS)
        self.manual_options.Bind(wx.EVT_RADIOBOX, self.OnManual) #   %%%
        self.manual_options.Enable(False) #  %%%

        # Add Spacer and Current Programs Textbox to the vbox
        self.vbox.AddStretchSpacer()
        self.vbox.Add(self.current_Program_Output, 0, wx.EXPAND|wx.ALL, 25)
        
        # Add buttons to hbox
        self.hbox.Add(self.quit, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 10)
        self.hbox.Add(self.button, 0, wx.EXPAND|wx.LEFT|wx.RIGHT, 10)
        
        # Add vbox to hbox
        self.vbox.Add(self.hbox,0,wx.ALIGN_CENTER)

        # reset frame size because Idk where it gets changed
        self.SetSize(1050,650)
       
        
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
            size = (215,150),
            choices=names)
       
        self.tasty_jams.SetCheckedItems([0,1,2,3,4,5])
        # self.Layout()
        # self.Bind(wx.EVT_CHECKLISTBOX, self.onChecked)
        return (self.tasty_jams)
   
    
    def OnManual(self,e):
       
        self.preset = self.manual_options.GetStringSelection()
   
   
    def onRadioBox(self,e):
        
        self.game = self.visualization_radiobox.GetStringSelection()
        
        if self.game == "Manual":
            self.game = self.ic.GetValue()
            self.manual_options.Enable(True) #  %%%
        else:
            self.manual_options.Enable(False) #  %%%
       
    
    def OnPic(self, e): # %%%
        self.rectangle_pic_1.Enable(self.photo_button.GetValue())
        self.rectangle_pic_2.Enable(self.photo_button.GetValue())
        self.rectangle_pic_3.Enable(self.photo_button.GetValue())
        
    
    def ReeChecked(self):
        
        global coolCats
        global coolCatz
        
        coolCats = list(self.tasty_jams.GetCheckedStrings())
       
        coolCatz = []
        
        for s in coolCats:
            coolCat = s.replace("Manual", self.slaps.GetValue())
            coolCatz.append(coolCat)
                   
       
    def AddStaticText(self, pos, label, size = (75,23)):
        
        # put some text
        self.st = wx.StaticText(self, -1, style = wx.LC_REPORT, size = size,
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
        global manual_filter # %%%
        global filterChoice #  %%%
        global custom_filter_value #  %%%
        global custom_pics #  %%%
       
        self.ReeChecked()
               
        # Check which toggles are checked on # %%%
        manual_filter = self.hsvgui.GetValue()
        custom_pics = self.photo_button.GetValue()
        filterChoice = self.custom_hsv.GetValue() #  %%%
               
        if filterChoice: #  %%%
        
            string = self.custom_filter_1.GetValue() # %%%
            string_2 = self.custom_filter_2.GetValue()
            string_3 = self.custom_filter_3.GetValue()
            string_4 = self.custom_edge_filter.GetValue()
            
            custom_filter_value = list(eval(string)) #  %%% str(eval(string))
            
            for s in eval(string_2):
                custom_filter_value.append(s)
            for s in eval(string_3):
                custom_filter_value.append(s)
            for s in eval(string_4):
                custom_filter_value.append(s)
                
            if len(custom_filter_value) < 40:
            
                # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
                dlg = wx.MessageDialog(self,
                        "Counting Error, idiot:\n\n"
                        "You need to have 40 inputs for your custom filter to work",
                        "Sorry M8:")
                
                dlg.ShowModal() # Show It
                dlg.Destroy() # Destroy it when finished
                
                # break out of function...
                return

        wincap = WindowCapture(self.game)

        if self.game == "Demon's Souls (original)":
            DemonSouls()
            
        elif  self.game == "Dark Souls: Remastered":
            print("we should be running DSI now...")
        
        elif  self.game == "Dark Souls II":
            print("we should be running DSII now...")
            DarkSoulsII()
        
        elif  self.game == "Dark Souls III":
            DarkSoulsIII()
        
        else:
            self.game = self.ic.GetValue()
            wincap = WindowCapture(self.game)
        
            if self.preset == "Demon's Souls (original)":
                DemonSouls()
            
            elif  self.preset == "Dark Souls: Remastered":
                print("we should be running manual DSI now...")
            
            elif  self.preset == "Dark Souls II":
                DarkSoulsII()
            
            elif  self.preset == "Dark Souls III":
                DarkSoulsIII()
            
            elif self.preset == "Default":
                Default()
   
    # def OnPictures(self, e):
        
    #     # A message dialog box with an OK button. wx.OK is a standard ID in wxWidgets.
    #     dlg = wx.MessageDialog(self,
    #                     "YOLO Fam:\n\n"
    #                     "This has not been coded yet. \n"
    #                     "That button should have given you options to add custom photos\n"
    #                     "Sorry m8 working on it.",
    #                     "Sorry M8:")
        
    #     dlg.ShowModal() # Show It
        
    #     dlg.Destroy() # Destroy it when finished
   
    
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
                        "This allows you to use preset options for object detection "
                        "while also scanning a non-coded program (such as OBS)\n"
                        "\nTasty Jams:\n When inputing a manual jam, specify the path."
                        "ie: C://User//Paul_Blart//desktop"
                        "\n      Use double '//'s to avoid making the program angry\n"
                        "\nDemon's Souls:\n Demon's Souls' name must be adjusted"
                        " in RPCS3 to 'Demon's Souls (original)'\n"
                        "\nFilters:\n"
                        "     Manual Filter enables the filter toggle window, use this "
                        "to find the filter inputs for the Custom Filter options\n"
                        "     Custom Filter takes input for filter options for custom"
                        " photos.\n"
                        "The input goes from top to bottom..."
                        "\n          HSV Filter 1 (10 inputs)"
                        "\n          HSV Filter 2 (10 inputs)"
                        "\n          HSV Filter 3 (10 inputs)"
                        "\n          Edge Filters 1 and 2 (10 inputs)\n"
                        "This option and the custom photo option probably won't work "
                        "well if you don't know what's going on\n"
                        "\nCustom Photos:\n"
                        " This option allows you to use custom photos for object detection."
                        "The photos you use should be cropped screenshots of the "
                        "filtered image found using manual filter.\n",
                        "Helps:\n")
        
        dlg.ShowModal() # Show It
        dlg.Destroy() # Destroy it when finished
       
        
    def OnExit(self, e):
        
        global kill
        
        kill = True # stop the program output windows as well
        
        pygame.mixer.music.stop() # stop music if it's playing
        
        self.Close(True) # Close the frame


app = wx.App(False)
frame = MainWindow(None, "Epic Finishers")
frame.Show(True)
app.MainLoop()

# They'll have to screenshot the filter and then make custom jpg...
#   Then add manual filter button with array for filter
#       Add filter help with instructions to not use it unless you know how to...

# Change RPCS3 emulator to Demon's Souls (original) and change program to not change name of Demon's Souls
# Reorganize program to look nice

# TODO: Add instructions to help for custom filter order...
    ## If they only put an int and no comma, eval gets angry and str() didn't fix it...
    
# Increase volume for pog champ and god/anime .wav files

# maybe add custom threshold to all pics?

# Document, Document, Document!!!
# def Default():
    # if custom pics:
        # use custom pics
        # run rectCheck
    # else:
        # don't run rectCheck
        
# add hsv and edge filters and pics for demon's souls and dsII...