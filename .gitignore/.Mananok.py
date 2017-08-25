import os
def banner() :
    print('''
  \033[91m------------------------------------------------------------------------------------------------------------
\033[91m|   \033[97m____  ___                                 ______                 ________           ______                \033[91m|
\033[91m| \033[97m___   |/  /_____ _____________ ________________  /__               ___  __/______________  /_______         \033[91m|
\033[91m| \033[97m__  /|_/ /_  __ `/_  __ \  __ `/_  __ \  __ \_  //_/  ________     __  /  _  __ \  __ \_  /__  ___/         \033[91m|
\033[91m| \033[97m_  /  / / / /_/ /_  / / / /_/ /_  / / / /_/ /  ,<     _/_____/     _  /   / /_/ / /_/ /  / _(__  )          \033[91m|
\033[91m| \033[97m/_/  /_/  \__,_/ /_/ /_/\__,_/ /_/ /_/\____//_/|_|                 /_/    \____/\____//_/  /____/           \033[91m|
\033[91m|                                                                                                             \033[91m|
\033[91m -------------------------------------------------------------------------------------------------------------
\033[91m|                               \033[93mCodec By MoH-CHiGi === www.facebook.com/mohvara                               \033[91m|
\033[91m -------------------------------------------------------------------------------------------------------------
''')
    print(" ") 

def moh() :
    def back() :
        banner()
        print ("\033[92m--------------------------------------------------")
        print ("\033[96m[*] Select the number you want from these options : ")
        print ("\033[92m--------------------------------------------------")
        print ("\033[95m[1] \033[92mTools Hack - System - ")
        print ("\033[95m[2] \033[92mTools Hack - site - ")
        print ("\033[95m[3] \033[92mTools Scan - site - ")
        print ("\033[95m[4] \033[92mOther Tools ")
        print ("                                             ")
        
    back()
    
    the_choice = int(input ('\033[95m[+] \033[01;31mChoose The Number you want ===> \033[92m '))

    if the_choice == 1 :
        os.system ('clear')
        print ("\033[97m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print ("\033[97m++[ ---------------------|                       \033[96mTools Hack - System                    \033[97m|--------------------- ]++") 
        print ("\033[97m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print ("                                             ")
        print ("\033[93m[1] \033[92mVenom ")
        print ("\033[93m[2] \033[92mThe Fat Rat ")
        print ("\033[93m[3] \033[92mCobalt-Strike ")
        print ("\033[93m[4] \033[92mEmpire ")
        print ("\033[93m[5] \033[92mShellter                             \033[91mrun this tool (Open Terminal and write this ==> sudo shellter ")
        print ("\033[93m[6] \033[92msetoolkit ")
        print ("\033[93m[7] \033[92mNetool ")
        print ("\033[93m[00] \033[92mBack ")
        print ("                                             ")
        print ("\033[97m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print ("                                             ")
        the_choice2 = int(input ('\033[95m[+] \033[01;31mChoose The Number you want ===> \033[92m ')) 
        print ("                                             ")
    
        if the_choice2 == 1 :
            os.system ("sudo git clone https://github.com/r00t-3xp10it/venom.git ")
        if the_choice2 == 2 :
            os.system ("sudo git clone https://github.com/Screetsec/TheFatRat.git ")
        if the_choice2 == 3 :
            os.system ("sudo git clone https://github.com/killswitch-GUI/CobaltStrike-ToolKit.git ")
        if the_choice2 == 4 :
            os.system ("sudo git clone https://github.com/EmpireProject/Empire.git ")
        if the_choice2 == 5 :
            os.system ("sudo apt-get update ")
            os.system ("sudo apt-get install shellter ")
        if the_choice2 == 6 :
            os.system ("sudo git clone https://github.com/trustedsec/social-engineer-toolkit.git ")
        if the_choice2 == 7 :
            os.system ("sudo git clone https://github.com/r00t-3xp10it/netool-toolkit.git ")
        if the_choice2 == 00 :
            os.system ('clear')
            moh()
    if the_choice == 2 :
        os.system ('clear')
        print ("\033[97m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print ("\033[97m++[ ---------------------|                       \033[96mTools Hack - site -                     \033[97m|--------------------- ]++") 
        print ("\033[97m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print ("                                             ")
        print ("\033[95m[1] \033[92mDzjecter ")
        print ("\033[95m[2] \033[92mJoomla Tools ")
        print ("\033[95m[3] \033[92mWordpress Tools ")
        print ("\033[95m[4] \033[92mDrupal Tools ")
        print ("\033[95m[5] \033[92mOpencart Tools ")        
        print ("\033[95m[6] \033[92mmagento Tools ")
        print ("\033[95m[7] \033[92mAfter Upload Your Shell ")
        print ("\033[95m[8] \033[92mGs_Boot ")
        print ("\033[95m[9] \033[92mD.R.S Boot ")
        print ("\033[95m[10] \033[92mLocal Root Server 2010-2016 ")
        print ("\033[95m[00] \033[92mBack ")        
        print ("                                             ")
        print ("\033[97m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print ("                                             ")
        the_choice5 = int(input ('\033[95m[+] \033[01;31mChoose The Number you want ===> \033[92m ')) 
        print ("                                             ")
        if the_choice5 == 1 :
            os.system ("sudo git clone https://github.com/joker25000/Dzjecter.git ")        
        if the_choice5 == 2 :
            os.system ("sudo git clone https://github.com/hussien-x/fucking_joomla.git ")
        if the_choice5 == 3 :
            os.system ("sudo git clone https://github.com/9nasghost/simpel-exploit-wordpress.git ")
        if the_choice5 == 4 :
            os.system ("sudo git clone https://github.com/9nasghost/Drupal.git ")
        if the_choice5 == 5 :
            os.system ("sudo git clone https://github.com/9nasghost/opencart-2017.git ")
        if the_choice5 == 6 :
            os.system ("sudo git clone https://github.com/9nasghost/magento-add-admin.git ")
        if the_choice5 == 7 :
            os.system ("sudo git clone https://github.com/9nasghost/after-upload-your-shell.git ")
        if the_choice5 == 8 :
            os.system ("sudo git clone https://github.com/9nasghost/fllaga-boot.git ")
        if the_choice5 == 9 :
            os.system ("sudo git clone https://github.com/9nasghost/D.R.S-DZ-boot.git ")
        if the_choice5 == 10 :
            os.system ("sudo git clone https://github.com/FireFart/dirtycow.git ")
        if the_choice5 == 00 :
            os.system ('clear')
            moh()

    if the_choice == 3 :
        os.system ('clear')
        print ("\033[97m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print ("\033[97m++[ ---------------------|                       \033[96mTools Scan - site -                     \033[97m|--------------------- ]++") 
        print ("\033[97m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print ("                                             ")
        print ("\033[93m[1] \033[92mVega ")
        print ("\033[93m[2] \033[92mBurp Suite ")
        print ("\033[93m[3] \033[92mRED HAWK ")
        print ("\033[93m[4] \033[92mUniscan ")
        print ("\033[93m[5] \033[92mWPSeku ")
        print ("\033[93m[6] \033[92mNmap ")
        print ("\033[93m[7] \033[92mNikto ")
        print ("\033[93m[00] \033[92mBack ")
        print ("                                             ")
        print ("\033[97m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print ("                                             ")
        the_choice3 = int(input ('\033[95m[+] \033[01;31mChoose The Number you want ===> \033[92m ')) 
        print ("                                             ")

        if the_choice3 == 1 :
            os.system ("sudo git clone https://github.com/vega/vega.git ")
        if the_choice3 == 2 :
            os.system ("sudo git clone https://github.com/irsdl/BurpSuiteJSBeautifier.git ")
        if the_choice3 == 3 :
            os.system ("sudo git clone https://github.com/Tuhinshubhra/RED_HAWK.git ")
        if the_choice3 == 4 :
            os.system ("sudo git clone https://github.com/poerschke/Uniscan.git ")
        if the_choice3 == 5 :
            os.system ("sudo git clone https://github.com/m4ll0k/WPSeku.git ")
        if the_choice3 == 6 :
            os.system ("sudo git clone https://github.com/nmap/nmap.git ")
        if the_choice3 == 7 :
            os.system ("sudo git clone https://github.com/sullo/nikto.git ")
        if the_choice3 == 00 :
            os.system ('clear')
            moh()


    if the_choice == 4 :
        os.system ('clear')
        print ("\033[97m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print ("\033[97m         ++[ ---------------------|                       \033[96mOther Tools                           \033[97m|--------------------- ]++") 
        print ("\033[97m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print ("                                             ")
        print ("\033[95m[1] \033[92mEmail-finder                       \033[91m(For run This Tools Use Python3)")
        print ("\033[95m[2] \033[92mGeany                              \033[91m(Best Notepad For Linux)")
        print ("\033[95m[3] \033[92mDagon                              \033[91m(Hash cracker/Advanced Hash Manipulation)")
        print ("\033[95m[4] \033[92mcupp                               \033[91m(Make Specific worldlists)")
        print ("\033[95m[00] \033[92mBack ")
        print ("                                             ")
        print ("\033[97m++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print ("                                             ")
        the_choice4 = int(input ('\033[95m[+] \033[01;31mChoose The Number you want ===> \033[92m '))    
        print ("                                             ")
        if the_choice4 == 1 :
            os.system ("sudo git clone https://github.com/lamanihani/email-finder.git ")
        if the_choice4 == 2 :
            os.system ("sudo git clone https://github.com/geany/geany.git ")
        if the_choice4 == 3 :
            os.system ("sudo git clone https://github.com/Ekultek/Dagon.git ")
        if the_choice4 == 4 :
            os.system ("sudo git clone https://github.com/Mebus/cupp.git ")
        if the_choice4 == 00 :
            os.system ('clear')
            moh()
    else :
        print ("Choose The Number wla Ni5lak Mo5 -_-")
try :
    os.mkdir ("Tools")
    os.chdir ("Tools")
    moh ()
except :
    os.chdir ("Tools")
    moh ()
   
    
