import pytesseract
from airtest.core.api import *
from PIL import Image
#from airtest.core.api import connect_device, install, uninstall
# -*- encoding=utf8 -*-
__author__ = "Rakesh_P"
auto_setup(__file__)
init_device("Android")
start_app("com.williamsinteractive.goldfish")

assert_exists(Template(r"tpl1695975834990.png", record_pos=(0.022, -0.004), resolution=(1600, 720)), "Launch the game on Android Devices.")
assert_exists(Template(r"tpl1695975834990.png", record_pos=(0.022, -0.004), resolution=(1600, 720)), "Graphic Animation is pass.")
sleep(30.0)
if exists(Template(r"tpl1696930914859.png", record_pos=(-0.014, 0.001), resolution=(1600, 720))):
    touch(Template(r"tpl1696930939988.png", record_pos=(0.219, -0.194), resolution=(1600, 720))) 
elif exists(Template(r"tpl1696934976881.png", record_pos=(0.042, -0.004), resolution=(1600, 720))):
    touch(Template(r"tpl1696934999687.png", record_pos=(0.295, -0.201), resolution=(1600, 720)))  
elif exists(Template(r"tpl1696934820064.png", record_pos=(0.028, -0.008), resolution=(1600, 720))):
    touch(Template(r"tpl1696934844016.png", record_pos=(0.216, -0.196), resolution=(1600, 720)))
else:
    print("No PopUp Displayed")
sleep(4.0)    
touch(Template(r"tpl1696085956954.png", record_pos=(0.46, -0.206), resolution=(1600, 720)))
assert_exists(Template(r"tpl1695974028310.png", record_pos=(0.026, -0.004), resolution=(1600, 720)), "Setting popup navigation is Pass.")
assert_exists(Template(r"tpl1695981138917.png", record_pos=(0.178, -0.145), resolution=(1600, 720)), "Music Icon is Enabled.")
touch(Template(r"tpl1695980483307.png", record_pos=(0.171, -0.141), resolution=(1600, 720)))
assert_exists(Template(r"tpl1695981386231.png", record_pos=(0.174, -0.142), resolution=(1600, 720)), "Music Icon is Disabled.")


assert_exists(Template(r"tpl1695981416932.png", record_pos=(0.176, -0.079), resolution=(1600, 720)), "SFX Icon is enabled.")
touch(Template(r"tpl1695980496636.png", record_pos=(0.176, -0.083), resolution=(1600, 720)))
assert_exists(Template(r"tpl1695981457510.png", record_pos=(0.176, -0.081), resolution=(1600, 720)), "SFX Icon is Disabled.")
assert_exists(Template(r"tpl1696310897599.png", record_pos=(-0.1, 0.174), resolution=(1600, 720)), "Terms of Service Link is Displayed.")
touch(Template(r"tpl1695834903168.png", record_pos=(-0.099, 0.173), resolution=(1600, 720)))        
sleep(6.0)
assert_exists(Template(r"tpl1695974471646.png", record_pos=(-0.131, -0.15), resolution=(1600, 720)), " Terms of Service Hyperlink Redirecting to the Correct Webpage Link.")
keyevent("back")
sleep(6.0)
swipe(Template(r"tpl1697007539161.png", record_pos=(0.118, -0.025), resolution=(1600, 720)), vector=[-3000, 720])
sleep(6.0)
assert_exists(Template(r"tpl1695976137773.png", record_pos=(0.188, -0.014), resolution=(1600, 720)), "Swipe Working Fine.")
sleep(6.0)
touch(Template(r"tpl1695741178474.png", record_pos=(0.158, -0.006), resolution=(1600, 720)))
sleep(4.0)
screenshot = snapshot("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\Screenshot.png")

# Bottom-right corner of the ROI
image = Image.open("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\Screenshot.png")

# Crop the image to the specified area
cropped_image = image.crop((368,0,562,70))

# Save the cropped image as a new file
cropped_image.save("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\cropped_image.png")

Initialamount= pytesseract.image_to_string("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\cropped_image.png")
s1 = Initialamount.replace(",", "")
num_iterations = 3
for i in range(num_iterations):
    touch(Template(r"tpl1697016673522.png", record_pos=(-0.321, 0.198), resolution=(1600, 720)))
screenshot = snapshot("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\screenshot1.png")
image = Image.open("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\Screenshot1.png")
cropped_Bet_image = image.crop((395,630,570,695))

# Save the cropped image as a new Betfile
cropped_Bet_image.save("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\cropped_Bet_image.png")
Betamount= pytesseract.image_to_string("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\cropped_Bet_image.png")
s2 = Betamount.replace(",", "")
touch(Template(r"tpl1697017355214.png", record_pos=(0.425, 0.181), resolution=(1600, 720)))
sleep(6.0)
# 3) Capture the New Amount
screenshot = snapshot("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\Screenshot2.png")
#sleep(4.0)
 # Bottom-right corner of the ROI
image = Image.open("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\Screenshot2.png")
# Crop the image to the specified area
cropped_NewAmt_image = image.crop((368,0,562,70))
# Save the cropped image as a new Amount file
cropped_NewAmt_image.save("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\cropped_NewAmt_image.png")
Newamount = pytesseract.image_to_string("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\cropped_NewAmt_image.png")
sleep(6.0)
s3 = Newamount.replace(",", "")
assert_not_equal("s1", "s3", "After Spin InitialBalance Amount will be Change to NewBalance Amount."+ s3)
assert_not_equal("s2", "s3", "Displaying Accurate BetAmount."+ s2)
assert_exists(Template(r"tpl1695976429479.png", record_pos=(-0.015, -0.206), resolution=(1600, 720)), "Sales Icon is Displyed.")
touch(Template(r"tpl1695972359685.png", record_pos=(-0.016, -0.206), resolution=(1600, 720)))
if exists(Template(r"tpl1696086536283.png", record_pos=(0.039, -0.005), resolution=(1600, 720))):
    touch(Template(r"tpl1696086550554.png", record_pos=(0.296, -0.201), resolution=(1600, 720)))
else:
    keyevent("back")
assert_exists(Template(r"tpl1695979508006.png", record_pos=(-0.398, 0.201), resolution=(1600, 720)), "Paytable Icon is Displyed.")
touch(Template(r"tpl1695886107079.png", record_pos=(-0.398, 0.201), resolution=(1600, 720)))
sleep(3.0)
assert_exists(Template(r"tpl1695979574566.png", record_pos=(0.228, 0.194), resolution=(1600, 720)), "NextIcon is Displyed.")
touch(Template(r"tpl1695886137302.png", record_pos=(0.225, 0.19), resolution=(1600, 720)))
sleep(3.0)
assert_exists(Template(r"tpl1695979619081.png", record_pos=(-0.178, 0.188), resolution=(1600, 720)), "Prev Icon is Displyed.")
touch(Template(r"tpl1695886176153.png", record_pos=(-0.177, 0.189), resolution=(1600, 720)))
sleep(3.0)
assert_exists(Template(r"tpl1695979663244.png", record_pos=(0.024, 0.188), resolution=(1600, 720)), "Return to Game Icon is Displyed.")
touch(Template(r"tpl1695886193957.png", record_pos=(0.022, 0.189), resolution=(1600, 720)))
# num_iterations = 3
# # Use a for loop to decrement the value
# for i in range(num_iterations):
#     touch(Template(r"tpl1695823952108.png", record_pos=(-0.318, 0.197), resolution=(1600, 720))) 
#     touch(Template(r"tpl1695822164062.png", record_pos=(0.417, 0.175), resolution=(1600, 720)))
# sleep(10.0)
# if exists(Template(r"tpl1696325242188.png", record_pos=(0.019, -0.004), resolution=(1600, 720))):
#     touch(Template(r"tpl1696084658447.png", record_pos=(0.029, 0.157), resolution=(1600, 720)))    
#     touch(Template(r"tpl1696087988897.png", record_pos=(0.026, 0.16), resolution=(1600, 720)))
# else:
#     print("No PopUp is Displayed")
#1) Capture the Initial Amount
screenshot = snapshot("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\Screenshot.png")

# Bottom-right corner of the ROI
image = Image.open("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\Screenshot.png")

# Crop the image to the specified area
cropped_image = image.crop((368,0,562,70))

# Save the cropped image as a new file
cropped_image.save("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\cropped_image.png")

Initialamount= pytesseract.image_to_string("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\cropped_image.png")

# 2)Capture the Total Bet Amount
sleep(6.0)
screenshot = snapshot("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\screenshot1.png")

image = Image.open("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\Screenshot1.png")

cropped_Bet_image = image.crop((395,630,570,695))

# Save the cropped image as a new Betfile
cropped_Bet_image.save("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\cropped_Bet_image.png")

Betamount= pytesseract.image_to_string("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\cropped_Bet_image.png")
sleep(6.0)

#Click on Spin Button
touch(Template(r"tpl1695295257681.png", record_pos=(0.412, 0.166), resolution=(1600, 720)))
sleep(10.0)
# 3) Capture the New Amount
screenshot = snapshot("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\Screenshot2.png")
#sleep(4.0)

 # Bottom-right corner of the ROI
image = Image.open("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\Screenshot2.png")

# Crop the image to the specified area
cropped_NewAmt_image = image.crop((368,0,562,70))

# Save the cropped image as a new Amount file
cropped_NewAmt_image.save("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\cropped_NewAmt_image.png")

Newamount = pytesseract.image_to_string("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\cropped_NewAmt_image.png")

# 4) Capture the Winning Amount
# Save the cropped image as a new Win file
sleep(8.0)
screenshot = snapshot("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\Screenshot3.png")
#sleep(8.0)
image = Image.open("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\Screenshot3.png")
# Crop the image to the specified area
cropped_win_image = image.crop((1000,656,1173,693))
cropped_win_image.save("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\cropped_Win_image.png")
winAmount = pytesseract.image_to_string("C:\\Users\\Rakesh_P\\Desktop\\Casino.air\\cropped_Win_image.png")

#assert_not_equal("s1", "s3", "After Spin Initial Amount is not Equal to New Amount.")
Value4=0
print("Initial Amount :>>>>>>>>>>>>>>>>> "+ Initialamount)
print("Betting Amount :>>>>>>>>>>>>>>>>> "+ Betamount)
print("New Amount :>>>>>>>>>>>>>>>>> "+ Newamount)
print("Winning Amount :>>>>>>>>>>>>>>>>> "+ winAmount)
s1 = Initialamount.replace(",", "")
s2 = Betamount.replace(",", "")
s3 = Newamount.replace(",", "")
s4 = winAmount.replace(",", "")
value1 = int(s1)
value2 = int(s2)
value3 = int(s3)
if (len(s4)==0):
    assert_not_equal("s1", "s2", "Bet Amount is Deducted the Balance Amounr."+ s2)
else:
    value4 = int(s4)
    if (value4 > 0):  
        assert_not_equal("s1", "s4", "Winning Amount is Credited to Balance Amount "+ s3)
#print (len(s4))
#print(len(s3))
if (len(s4)==0):
    print("Final Loss Amount"+(s2))
else:
    value4 = int(s4)
    if (value4 > 0):   
        print("Final win Amount :>>>>>>>>>>>> "+str((value1-value2)+value4))
    else:
        print("Final Loss Amount :>>>>>>>>>> "+ str(value1-value2))
touch(Template(r"tpl1696083823055.png", record_pos=(-0.411, -0.205), resolution=(1600, 720)))
sleep(10.0)    
if exists(Template(r"tpl1696087305016.png", record_pos=(0.023, -0.005), resolution=(1600, 720))):
    touch(Template(r"tpl1696087318518.png", record_pos=(0.22, -0.194), resolution=(1600, 720)))
else:
    keyevent("back")
sleep(6.0)
touch(Template(r"tpl1696085604284.png", record_pos=(0.459, -0.206), resolution=(1600, 720)))
assert_exists(Template(r"tpl1696085651426.png", record_pos=(0.173, -0.141), resolution=(1600, 720)), "Music Icon is Disabled.")
touch(Template(r"tpl1696083906194.png", record_pos=(0.174, -0.138), resolution=(1600, 720)))
assert_exists(Template(r"tpl1696428501651.png", record_pos=(0.174, -0.139), resolution=(1600, 720)), "Music Icon is Enable.")

assert_exists(Template(r"tpl1696085735464.png", record_pos=(0.174, -0.08), resolution=(1600, 720)), "SFX Icon is Disabled.")
touch(Template(r"tpl1696083918563.png", record_pos=(0.174, -0.081), resolution=(1600, 720)))
assert_exists(Template(r"tpl1696428560697.png", record_pos=(0.172, -0.083), resolution=(1600, 720)), "SFX Icon is Enable.")
touch(Template(r"tpl1696083942458.png", record_pos=(0.221, -0.203), resolution=(1600, 720)))
keyevent("back")
touch(Template(r"tpl1696083993978.png", record_pos=(0.107, 0.058), resolution=(1600, 720)))
home()
touch(Template(r"tpl1696592568768.png", record_pos=(-0.004, 0.433), resolution=(720, 1600)))
touch(Template(r"tpl1696588480392.png", record_pos=(0.04, -0.079), resolution=(720, 1600)))
touch(Template(r"tpl1696588495430.png", record_pos=(0.382, -0.743), resolution=(720, 1600)))
home()
start_app("com.williamsinteractive.goldfish")
sleep(4.0)
screenshot=snapshot("C:\\Users\\Rakesh_P\\Desktop\wifi.air\\screenshot4.png")
image = Image.open("C:\\Users\\Rakesh_P\\Desktop\\wifi.air\\screenshot4.png")

# Crop the image to the specified area
Cropped_image = image.crop((592,0,1075,63))

# Save the cropped image as a new file
Cropped_image.save("C:\\Users\\Rakesh_P\\Desktop\\wifi.air\\Cropped_image.png")
ErrorMessage= pytesseract.image_to_string("C:\\Users\\Rakesh_P\\Desktop\\wifi.air\\Cropped_image.png")
assert_exists(Template(r"tpl1696593541257.png", record_pos=(0.011, -0.198), resolution=(1600, 720)), "No Internet Connection is Available")
home()
touch(Template(r"tpl1696592568768.png", record_pos=(-0.004, 0.433), resolution=(720, 1600)))
touch(Template(r"tpl1696588480392.png", record_pos=(0.04, -0.079), resolution=(720, 1600)))
touch(Template(r"tpl1696588495430.png", record_pos=(0.382, -0.743), resolution=(720, 1600)))
home()
#uninstall("com.williamsinteractive.goldfish")

