import pyautogui
import time

sitename = input("please input site name (ex: city of wilmington) : ")
siteNameButton = pyautogui.locateOnScreen("screenshot/siteName.png", confidence=0.8)
print(siteNameButton)
pyautogui.moveTo(siteNameButton)
pyautogui.click()

selectClient = [710, 570]
pyautogui.moveTo(selectClient)
pyautogui.write(sitename)
pyautogui.move(0, 50)
time.sleep(2)
pyautogui.click()

product_config = None
while product_config is None:
    product_config = pyautogui.locateOnScreen("screenshot/productConfiguration.PNG", confidence=0.8)

pyautogui.moveTo(product_config)
pyautogui.click()

munis_erp = None
while munis_erp is None:
    pyautogui.scroll(-5)
    munis_erp = pyautogui.locateOnScreen("screenshot/muniserp.PNG", confidence=0.9)

pyautogui.moveTo(munis_erp)
pyautogui.click()

environment = pyautogui.locateOnScreen("screenshot/environments.PNG", confidence=0.8)
pyautogui.moveTo(environment)
pyautogui.click()
pyautogui.move(0, 50)
pyautogui.click()

munis_config = None
while munis_config is None:
    munis_config = pyautogui.locateOnScreen("screenshot/muniserpconfig.PNG", confidence=0.8)

pyautogui.moveTo(munis_config)
pyautogui.click()
time.sleep(0.5)
# ctrl+F'thumbprint'
pyautogui.hotkey('ctrl', 'f')  # open chrome search
pyautogui.write('thumbprint')
time.sleep(0.2)
thumb = pyautogui.locateOnScreen("screenshot/thumbprint.PNG", confidence=0.9)
pyautogui.moveTo(thumb)
pyautogui.move(500,0)
pyautogui.doubleClick()
pyautogui.write('f111fd985f63a0834e16cb6fe43ef69787c310db')

save = None
while save is None:
    pyautogui.scroll(500)
    save = pyautogui.locateOnScreen('screenshot/save.PNG', confidence=0.9)

pyautogui.moveTo(save)
pyautogui.click()