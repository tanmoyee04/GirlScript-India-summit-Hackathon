import pyqrcode as qr
import png

s = "https://[Add_your_link_here]" 
url = qr.create(s)

url= qr.create(s) 
  
url.svg("myqr.svg", scale = 8) 

url.png('myqr.png', scale = 6) 
