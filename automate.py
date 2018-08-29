from selenium import webdriver
def whatsapp(*args):
    driver=webdriver.Firefox()
    driver.get("https://web.whatsapp.com/")
    input("Press Enter After Scanning")  
    count=int(input ("Repeat how many times:"))
    msg=input("Enter message:")
    for arg in args:       
        print("Sending to \t"+arg)
        user=driver.find_element_by_xpath('//span[@title="{}"]'.format(arg)) #Selecting the user
        user.click()       
        for i in range(count):
            msgbox=driver.find_element_by_class_name('_2S1VP') #Filling the message
            msgbox.send_keys(msg)
            sendBtn=driver.find_element_by_class_name('_35EW6')#Clicking send button
            sendBtn.click()        
            
        
whatsapp()
