
# importing the module
import pywhatkit
 
# using Exception Handling to avoid
# unprecedented errors
try:
   
  # sending message to receiver
  # using pywhatkit
  pywhatkit.sendwhatmsg("+6282225881729",
                        "Hello from GeeksforGeeks",
                        0, 0, 1)
  print("Successfully Sent!")
 
except:
   
  # handling exception
  # and printing error message
  print("An Unexpected Error!")