"""
Bruteforce .onion links to find dark web sites. 
This program is not recommended to be used, because it provides no security or protection, when trying the links.

Author: PiggyAwesome

"""


import requests, random, string, os, tkinter.messagebox; 

def coloured(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text);

tkinter.messagebox.showwarning("Warning","By continiung you are aware of the risks that this program may bring to you, and you agree that the author of this program is not responsible for any damages caused.");
total = int(input("Enter total links to find before ending: "));
file_ = input("Enter file to save valid links: ");

os.system("cls");
print(coloured(252, 3, 224, r"""




                            ~
                           /~
                     \  \ /**
                      \ ////
                      // //
                     // //
                   ///&//
                  / & /\ \
                /  & .,,  \
              /& %  :       \
            /&  %   :  ;     `\
           /&' &..%   !..    `.\
          /&' : &''" !  ``. : `.\
         /#' % :  "" * .   : : `.\
        I# :& :  !"  *  `.  : ::  I
        I &% : : !%.` '. . : : :  I
        I && :%: .&.   . . : :  : I
        I %&&&%%: WW. .%. : :     I
         \&&&##%%%`W! & '  :   ,'/
          \####ITO%% W &..'  #,'/
            \W&&##%%&&&&### %./
              \###j[\##//##}/
                 ++///~~\//_
                  \\ \ \ \  \_
                  /  /    \

                     d8b                 
                     Y8P                 
                                         
      .d88b. 88888b. 888 .d88b. 88888b.  
     d88""88b888 "88b888d88""88b888 "88b 
     888  888888  888888888  888888  888 
     Y88..88P888  888888Y88..88P888  888 
      "Y88P" 888  888888 "Y88P" 888  888 
                bruteforcer                      
                    """));
file_ = open(file_, "a");

found_links = [];
found = 0
while found <= total: 
    try: 
       chars = string.ascii_letters + string.digits + "";
       num = random.randint(5, 51);
       onion = "http://" + ''.join(random.choice(chars) for i in range(num)) + ".onion";
       response = requests.get(onion).text; 

       if response != 404: 
           found_links.append(onion); 
           print(coloured(250, 20, 20, onion));
           file_.write(onion + "\n");
       else: 
           print(coloured(60, 250, 50, onion));
    except KeyboardInterrupt:
        file_.close();
        exit();


print(f"Found {found} links:\n" +'\n'.join(found_links))