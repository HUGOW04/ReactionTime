import pyautogui as py

color = (75, 219, 106)


while True:
    if(py.pixelMatchesColor(600,600,color)):
        py.click()
        print("click") 
        break
    else:
        print("balls")
