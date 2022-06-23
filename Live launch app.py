from tkinter import *
from tkinter import ttk
from tkinter import messagebox

import webbrowser
import datetime


# FONCTIONS ET VARIABLES D'USAGE
start = False

league_list = ["World","MSI","LCK","LPL","LCS","LJL","LEC","European Masters","LFL","LCO","LLA","CBLOL","LCL","PCS","TCL","All-Star","CBLOL Academy","College Championship","EBL","Elite Series","Hitpoint Masters","PG Nationals","LCK Academy","LCK Challengers","LCS Academy","Proving Grounds","Greek Legends League","Liga Portuguesa","NLC","Ultraliga","Prime League","SuperLiga","LCS Amateur Circuit"]

league_ip = {
"World"                      : "https://lolesports.com",
"MSI"                        : "https://lolesports.com",
"LCK"                        : "https://lolesports.com/live/lck",
"LPL"                        : "https://lolesports.com/live/lpl",
"LCS"                        : "https://lolesports.com",
"LJL"                        : "https://lolesports.com",
"LEC"                        : "https://lolesports.com/live/lec",
"European Masters"           : "https://lolesports.com",
"LFL"                        : "https://lolesports.com/live/otp_/lfl",
"LCO"                        : "https://lolesports.com/live/lco",
"LLA"                        : "https://lolesports.com/live/lla",
"CBLOL"                      : "https://lolesports.com/live/cblol-brazil/cblol",
"LCL"                        : "https://lolesports.com",
"PCS"                        : "https://lolesports.com",
"TCL"                        : "https://lolesports.com/live/turkiye-sampiyonluk-ligi",
"All-Star"                   : "https://lolesports.com",
"CBLOL Academy"              : "https://lolesports.com/live/cblol_academy",
"College Championship"       : "https://lolesports.com/live/college_championship/lcs",
"EBL"                        : "https://lolesports.com/live/esports_balkan_league/fortuna",
"Elite Series"               : "https://lolesports.com/live/elite_series/",
"Hitpoint Masters"           : "https://lolesports.com",
"PG Nationals"               : "https://lolesports.com/live/pg_nationals",
"LCK Academy"                : "https://lolesports.com",
"LCK Challengers"            : "https://lolesports.com/live/lck_challengers_league",
"LCS Academy"                : "https://lolesports.com/live/lcs-academy/pathtolcs",
"Proving Grounds"            : "https://lolesports.com",
"Greek Legends League"       : "https://lolesports.com/live/greek_legends",
"Liga Portuguesa"            : "https://lolesports.com/live/liga_portuguesa/",
"NLC"                        : "https://lolesports.com/live/nlc",
"Ultraliga"                  : "https://lolesports.com/live/ultraliga",
"Prime League"               : "https://lolesports.com/live/primeleague",
"SuperLiga"                  : "https://lolesports.com/live/superliga",
"LCS Amateur Circuit"        : "https://lolesports.com/live/lcs_amateur/academy"
}

leagues = [
["World",False,0,0],
["MSI",False,0,0],
["LCK",False,0,0],
["LPL",False,0,0],
["LCS",False,0,0],
["LJL",False,0,0],
["LEC",False,0,0],
["European Masters",False,0,0],
["LFL",False,0,0],
["LCO",False,0,0],
["LLA",False,0,0],
["CBLOL",False,0,0],
["LCL",False,0,0],
["PCS" ,False,0,0],
["TCL",False,0,0],
["All-Star",False,0,0],
["CBLOL Academy",False,0,0],
["College Championship",False,0,0],
["EBL",False,0,0],
["Elite Series",False,0,0],
["Hitpoint Masters",False,0,0],
["PG Nationals",False,0,0],
["LCK Academy",False,0,0],
["LCK Challengers",False,0,0],
["LCS Academy",False,0,0],
["Proving Grounds",False,0,0],
["Greek Legends League",False,0,0],
["Liga Portuguesa",False,0,0],
["NLC",False,0,0],
["Ultraliga",False,0,0],
["Prime League",False,0,0],
["SuperLiga",False,0,0],
["LCS Amateur Circuit",False,0,0]
]

def set_start():
    global start

    start_ok = True

    for l in leagues :
        if l[1] == True :
            start_ok = True
            break
        else :
            start_ok = False

    if start :
        start = False
        start_button["text"] = "START"
    else :
        if not start_ok  : # SI ON NE SELECTIONNE AUCUNE LEAGUE AVANT DE START
            messagebox.showinfo(title='WARNING',message='You need to pick at least one league before starting.')
        else :
            start = True
            start_button["text"] = "STOP"

def open_site():
    global start

    if start :

        now = datetime.datetime.now()

        i = 0
        for l in leagues :
            if l[1] == True :
                if now.hour >= l[2] and now.minute >= l[3]:
                    # ON RESET LA LEAGUE UNE FOIS LANCÉE
                    leagues[i][1] = False
                    leagues[i][2] = 0
                    leagues[i][3] = 0
                    webbrowser.open(league_ip[l[0]])
            else :
                i += 1

        if i >= len(leagues) :
            # SI TOUTES LES LEAGUES ON ÉTAIT LANCÉE ALORS ON STOP LE PROGRAMME
            start = False
            start_button["text"] = "START"

    window.after(100,open_site)

def check_schedule():
    webbrowser.open("https://lolesports.com/schedule?leagues=lec,european-masters,lfl,cblol-brazil,lck,lcl,lco,lcs,ljl-japan,lla,lpl,pcs,turkiye-sampiyonluk-ligi,worlds,all-star,cblol_academy,college_championship,esports_balkan_league,elite_series,hitpoint_masters,pg_nationals,lck_academy,lck_challengers_league,lcs-academy,proving_grounds,greek_legends,liga_portuguesa,nlc,ultraliga,primeleague,superliga,lcs_amateur,msi")

def add_league():

    do = True

    if league_cbb.get() not in league_ip.keys() : # AUTRE CHOSE D'ECRIT DANS LA COMBOBOX
        messagebox.showinfo(title='WARNING',message='You need to select a league.')
        do = False

    if do :

        time = (hour_entry.get(),minute_entry.get())

        if time[0] == '' : time = ("10",time[1])   # HEURE VIDE
        if time[1] == '' : time = (time[0],"00")   # MINUTE VIDE
        if time[0].isdigit() == False or int(time[0]) >= 24 :    # HEURE INVALIDE
            time = (00,time[1])
            hour_entry.delete(0,END)
            hour_entry.insert(0,"00")
        if time[1].isdigit() == False or int(time[1]) >= 60 :    # MINUTE INVALIDE
            time = (time[0],00)
            minute_entry.delete(0,END)
            minute_entry.insert(0,"00")

        hour   = int(time[0])
        minute = int(time[1])

        i = 0
        for l in leagues :
            if l[0] == league_cbb.get():
                # ON MET "TRUE" A LA LEAGUE SELECTIONNÉE ET ON CHANGE L'HORAIRE DU MATCH
                leagues[i][1] = True
                leagues[i][2] = hour
                leagues[i][3] = minute
            else :
                i += 1

def supp_league():

    do = True

    if league_cbb.get() not in league_ip.keys() : # AUTRE CHOSE D'ECRIT DANS LA COMBOBOX
        messagebox.showinfo(title='WARNING',message='You need to select a league.')
        do = False

    if do :

        i = 0
        for l in leagues :
            if l[0] == league_cbb.get():
                # ON MET "FALSE" A LA LEAGUE SELECTIONNÉE ET ON RESET L'HORAIRE DU MATCH
                leagues[i][1] = False
                leagues[i][2] = 0
                leagues[i][3] = 0
            else :
                i += 1

def show_selected_league():
    msg = ''

    for l in leagues :
        if l[1] == True :
            # SI LE MATCH EST "TRUE", DONC SELECTIONNÉ, ON AJOUTE AU MESSAGE LA LEAGUE ET SON HORAIRE
            msg += l[0]+' at '+str(l[2])+' : '+str(l[3])+'\n'

    if msg == '' : msg = 'NONE'

    messagebox.showinfo(title='SELECTED LEAGUES',message=msg)
##################


# INITIALISATION
window = Tk()

# FENETRE #
window.title("LIVE LAUNCH APP")
window.geometry("1080x720")
window.minsize(1080,720)
window.maxsize(1080,720)
window.iconbitmap("icon.ico")
window.config(background='#3F3F3F',cursor="tcross")

# TEXT #
title1 = Label(window, text="LEAGUE OF LEGENDS", font=("Berlin Sans FB", 40), bg='#3F3F3F', fg='white')
title1.place(x=300,y=40)

title2 = Label(window, text="ESPORT LIVE LAUNCH APP", font=("Berlin Sans FB", 40), bg='#3F3F3F', fg='white')
title2.place(x=225,y=120)

league_text = Label(window, text="What league is it ?", font=("Berlin Sans FB", 15), bg='#3F3F3F', fg='white')
league_text.place(x=200,y=300)

time_text = Label(window, text="When does the match start ?", font=("Berlin Sans FB", 15), bg='#3F3F3F', fg='white')
time_text.place(x=600,y=300)

# BUTTONS #
league_cbb = ttk.Combobox(window, values = league_list, font=("Berlin Sans FB",15))
league_cbb.place(x=200,y=350)

add_button = Button(window, text="+", font=("Berlin Sans FB", 15), bg='#3F3F3F', fg='white', command=add_league)
add_button.place(x=170,y=350,height=30)

supp_button = Button(window, text="-", font=("Berlin Sans FB", 15), bg='#3F3F3F', fg='white', command=supp_league)
supp_button.place(x=470,y=350,height=30)

hour_entry = Entry(window, font=("Berlin Sans FB", 15), bg='#3F3F3F', fg='white',cursor="tcross")
hour_text  = Label(window, text="HOUR", font=("Berlin Sans FB", 15), bg='#3F3F3F', fg='white')
hour_entry.place(x=600,y=350,width=75)
hour_text.place(x=680,y=350)
hour_entry.insert(0,"10")

minute_entry = Entry(window, font=("Berlin Sans FB", 15), bg='#3F3F3F', fg='white',cursor="tcross")
minute_text  = Label(window, text="MINUTE", font=("Berlin Sans FB", 15), bg='#3F3F3F', fg='white')
minute_entry.place(x=600,y=400,width=75)
minute_text.place(x=680,y=400)
minute_entry.insert(0,"00")

schedule_button = Button(window, text="SCHEDULE", font=("Berlin Sans FB", 15), bg='white', fg='#3F3F3F', command=check_schedule)
schedule_button.place(x=800,y=375)

see_button = Button(window, text="SEE SELECTED LEAGUE", font=("Berlin Sans FB", 15), bg='white', fg='#3F3F3F', command=show_selected_league)
see_button.place(x=425,y=580)

start_button = Button(window, text="START", font=("Berlin Sans FB", 25), bg='white', fg='#3F3F3F', command=set_start)
start_button.place(x=470,y=640)
################


# LOOP
window.after(100,open_site)
window.mainloop()




