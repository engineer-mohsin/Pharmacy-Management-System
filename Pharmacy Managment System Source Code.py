from  tkinter import *
from time import strftime
import tempfile
import random,os
from tkinter import messagebox
class Bill_App:
    display_time = strftime('%H : %M : %S \n %A \n  %d-%B-%Y ')
    def __init__(self):
        self.root = root
        self.root.geometry('1596x830+0+0')
        self.root.title ('Software Project')
        self.root.iconbitmap('Icon.ico')
        bg_color = '#FFCBA4'
        title = Label(self.root,text="\U0001F494Pharmacy Managment System\U0001F494 ",bd=5,relief=GROOVE,bg=bg_color,fg='black',font=('Playball',40),pady=2).pack(fill=X)
# |----------------| All Variables |----------------|
# |----------------| Tablets Variables |----------------|
        self.Panadol = IntVar()
        self.Ponistan = IntVar()
        self.Atenolol = IntVar()
        self.Baclofen = IntVar()
        self.Brofen = IntVar()
        self.Cefaclor = IntVar()
        self.Etoposide = IntVar()
        self.Morphin = IntVar()
        self.Oxicodon = IntVar()
        self.Advil = IntVar()
        self.Emoxil = IntVar()
        self.Disprin = IntVar()
        self.Avil = IntVar()
        self.Septran = IntVar()
        self.Regix = IntVar()
# |----------------| Syrup Variables |----------------|
        self.Panadol_S = IntVar()
        self.Esticof = IntVar()
        self.Hydrolin = IntVar()
        self.Ascoril = IntVar()
        self.Brofen_S = IntVar()
        self.Cofcol = IntVar()
        self.Lazoran = IntVar()
        self.Morphin_S = IntVar()
        self.Payodin = IntVar()
        self.Advil_S = IntVar()
        self.Emoxil_S = IntVar()
        self.Coftin = IntVar()
        self.Coscopin = IntVar()
        self.Cofride_T = IntVar()
        self.Calcium_P = IntVar()
# |----------------| Injections Variables |----------------|
        self.Calcium_C = IntVar()
        self.Neorobion = IntVar()
        self.Decadron = IntVar()
        self.Avil_I = IntVar()
        self.Elther = IntVar()
        self.Senether = IntVar()
        self.Ethenex = IntVar()
        self.Bether = IntVar()
        self.Ceftef = IntVar()
        self.Arther = IntVar()
        self.Ether = IntVar()
        self.Insoether = IntVar()
        self.Artihuk = IntVar()
        self.Articare = IntVar()
        self.Dexa_M_X = IntVar()
# |----------------| Equipments Variables |----------------|
        self.S_Gloves = IntVar()
        self.Sanitizer = IntVar()
        self.Dettol = IntVar()
        self.S_Mask = IntVar()
        self.I_V_Set = IntVar()
        self.Syring = IntVar()
        self.Tape = IntVar()
        self.S_Cap = IntVar()
        self.Knee_Brace = IntVar()
        self.Ankle_Brace = IntVar()
        self.Heal_Brace = IntVar()
        self.Elastic_Crepe = IntVar()
        self.Whool = IntVar()
        self.Saniplast = IntVar()
        self.Thermometer = IntVar()
# |----------------| Total Bill Variables |----------------|
        self.Tablets_price = StringVar()
        self.Syrups_price = StringVar()
        self.Injections_price = StringVar()
        self.Equipments_price = StringVar()
        self.Grand_Total_price = StringVar()
# |----------------| Customer Menu Variables |----------------|
        self.Bill_id = StringVar()
        x=random.randint(1111111,9999999)
        self.Bill_id .set(str(x))
        self.Search_bill = StringVar()
        self.Name = StringVar()
        self.Contact = StringVar()

# |----------------| Customer Details Frame |----------------|
        self.bg_color = '#FBE7A1'
        self.Frame_1 = LabelFrame(self.root,bd=4,text='Customer Details',font=('times new roman',12,'bold'),fg='black',bg=self.bg_color)
        self.Frame_1.place(x=0,y=90,relwidth=1)
        # |----------------| Customer Bill ID |----------------|
        cust_bill_id_lbl = Label(self.Frame_1,text='Bill ID',font=('Baskerville Old Face',14,'bold'),bg=self.bg_color).grid(row=0,column=0,padx=40,pady=5)
        cust_bill_id_txt = Entry(self.Frame_1,width=20,textvariable=self.Bill_id,font='arial,11',bd=3,relief=SUNKEN).grid(row=0,column=1,pady=5,padx=10)
        # |----------------| Search Button |----------------|
        search_btn = Button(self.Frame_1,command=self.Find_bill,text='Search',width=9,bd=3,font=('Comic Sans MS', 9),padx=-2,pady=-2,fg='black',bg='#EDEDEB').grid(row=0,column=2)
        # |----------------| Customer Name |----------------|
        cust_name_lbl = Label(self.Frame_1,text='Name' ,font=('Baskerville Old Face',14,'bold'),bg=self.bg_color).grid(row=0,column=3,padx=40,pady=5)
        cust_name_txt = Entry(self.Frame_1,width=20,textvariable=self.Name,font='arial,11',bd=3,relief=SUNKEN).grid(row=0,column=4,pady=5,padx=10)
        # |----------------| Customer Phone |----------------|
        cust_phone_lbl = Label(self.Frame_1,text='Contact',font=('Baskerville Old Face',14,'bold'),bg=self.bg_color).grid(row=0,column=5,padx=40,pady=5)
        cust_phone_txt = Entry(self.Frame_1,width=20,textvariable=self.Contact,font='arial,11',bd=3,relief=SUNKEN).grid(row=0,column=6,pady=5,padx=10)
        # |----------------| Date , Time & Day |----------------|
        Bill_App.Time_dis(self)
        Bill_App.Date_Day_dis(self)
        # |----------------| Price list|----------------|
        price_lst_btn = Button(self.Frame_1,text='Price',command=self.Price_lst,width=10,bg=self.bg_color,fg='black',bd=4,relief=GROOVE).grid(row=0,column=9,padx=10,pady=0)

# |----------------| Details Menu Frame |----------------|
        bg_color = '#D8D56A'
        Frame_0 = LabelFrame(self.root,bd=5,text='Details Menu',font=('times new roman',12,'bold'),fg='black',bg=bg_color)
        Frame_0.place(x=0,y=155,relwidth=1,height=590) 

# |----------------| Bill Frame |----------------|
        bg_color = '#EDEDEB'
        Frame_6 = Frame(self.root,bd=5,relief=GROOVE)
        Frame_6.place(x=25,y=190,width=450,height=520)  
        bill_title = Label(Frame_6,text='Bill Area',font=('Monotype Corsiva', 25),bd=7,relief=GROOVE,bg='#EDEDEB').pack(fill=X)
        scrol_y = Scrollbar(Frame_6,orient=VERTICAL)
        self.txtarea = Text(Frame_6,yscrollcommand=scrol_y.set,background='#CCFFFF')
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

# |----------------| Tablets Frame |----------------|
        bg_color = '#F79AEE'
        Frame_2 = LabelFrame(self.root,bd=5,text='Tablets',font=('times new roman',10,'bold'),fg='black',bg=bg_color)
        Frame_2.place(x=490.,y=190,width=262.5,height=520)   
        # |----------------| Panadol Label |----------------|
        panadol_lbl = Label(Frame_2,text='Panadol',font=('Baskerville Old Face',14),bg=bg_color).grid(row=0,column=0,padx=30,pady=1.5,sticky='w')
        panadol_txt = Entry(Frame_2,width=8,font='arial,10',textvariable=self.Panadol,bd=3,relief=SUNKEN).grid(row=0,column=1,pady=2.5,padx=10)
        # |----------------| Ponistan Label |----------------|
        ponistan_lbl = Label(Frame_2,text='Ponistan',font=('Baskerville Old Face',14),bg=bg_color).grid(row=1,column=0,padx=30,pady=1.5,sticky='w')
        ponistan_txt = Entry(Frame_2,width=8,font='arial,10',textvariable=self.Ponistan,bd=3,relief=SUNKEN).grid(row=1,column=1,pady=2.5,padx=10)
        # |----------------| Atenolol Label |----------------|
        atenolol_lbl = Label(Frame_2,text='Atenolol',font=('Baskerville Old Face',14),bg=bg_color).grid(row=2,column=0,padx=30,pady=1.5,sticky='w')
        atenolol_txt = Entry(Frame_2,width=8,font='arial,10',textvariable=self.Atenolol,bd=3,relief=SUNKEN).grid(row=2,column=1,pady=2.5,padx=10)
        # |----------------| Baclofen Label |----------------|
        baclofen_lbl = Label(Frame_2,text='Baclofen',font=('Baskerville Old Face',14),bg=bg_color).grid(row=3,column=0,padx=30,pady=1.5,sticky='w')
        baclofen_txt = Entry(Frame_2,width=8,font='arial,10',textvariable=self.Baclofen,bd=3,relief=SUNKEN).grid(row=3,column=1,pady=2.5,padx=10)
        # |----------------| Brofen Label |----------------|
        brofen_lbl = Label(Frame_2,text='Brofen',font=('Baskerville Old Face',14),bg=bg_color).grid(row=4,column=0,padx=30,pady=1.5,sticky='w')
        brofen_txt = Entry(Frame_2,width=8,font='arial,10',textvariable=self.Brofen,bd=3,relief=SUNKEN).grid(row=4,column=1,pady=2.5,padx=10)
        # |----------------| Cefaclor Label |----------------|
        cefaclor_lbl = Label(Frame_2,text='Cefaclor',font=('Baskerville Old Face',14),bg=bg_color).grid(row=5,column=0,padx=30,pady=1.5,sticky='w')
        cefaclor_txt = Entry(Frame_2,width=8,font='arial,10',textvariable=self.Cefaclor,bd=3,relief=SUNKEN).grid(row=5,column=1,pady=2.5,padx=10)
        # |----------------| Etoposide Label |----------------|
        etoposide_lbl = Label(Frame_2,text='Etoposide',font=('Baskerville Old Face',14),bg=bg_color).grid(row=6,column=0,padx=30,pady=1.5,sticky='w')
        etoposide_txt = Entry(Frame_2,width=8,font='arial,10',textvariable=self.Etoposide,bd=3,relief=SUNKEN).grid(row=6,column=1,pady=2.5,padx=10)
        # |----------------| Morphine Label |----------------|
        morphine_lbl = Label(Frame_2,text='Morphine ',font=('Baskerville Old Face',14),bg=bg_color).grid(row=7,column=0,padx=30,pady=1.5,sticky='w')
        morphine_txt = Entry(Frame_2,width=8,font='arial,10',textvariable=self.Morphin,bd=3,relief=SUNKEN).grid(row=7,column=1,pady=2.5,padx=10)
        # |----------------| Oxycodon Label |----------------|
        oxycodon_lbl = Label(Frame_2,text='Oxycodon',font=('Baskerville Old Face',14),bg=bg_color).grid(row=8,column=0,padx=30,pady=1.5,sticky='w')
        oxycodon_txt = Entry(Frame_2,width=8,font='arial,10',textvariable=self.Oxicodon,bd=3,relief=SUNKEN).grid(row=8,column=1,pady=2.5,padx=10)
        # |----------------| Advil Label |----------------|
        advil_lbl = Label(Frame_2,text='Advil',font=('Baskerville Old Face',14),bg=bg_color).grid(row=9,column=0,padx=30,pady=1.5,sticky='w')
        advil_txt = Entry(Frame_2,width=8,font='arial,10',textvariable=self.Advil,bd=3,relief=SUNKEN).grid(row=9,column=1,pady=2.5,padx=10)
        # |----------------| Emoxil Label |----------------|
        emoxil_lbl = Label(Frame_2,text='Emoxil',font=('Baskerville Old Face',14),bg=bg_color).grid(row=10,column=0,padx=30,pady=1.5,sticky='w')
        emoxil_txt = Entry(Frame_2,width=8,font='arial,10',textvariable=self.Emoxil,bd=3,relief=SUNKEN).grid(row=10,column=1,pady=2.5,padx=10)
        # |----------------| Disprin Label |----------------|
        disprin_lbl = Label(Frame_2,text='Disprin',font=('Baskerville Old Face',14),bg=bg_color).grid(row=11,column=0,padx=30,pady=1.5,sticky='w')
        disprin_txt = Entry(Frame_2,width=8,font='arial,10',textvariable=self.Disprin,bd=3,relief=SUNKEN).grid(row=11,column=1,pady=2.5,padx=10)
        # |----------------| Avil Label |----------------|
        avil_lbl = Label(Frame_2,text='Avil',font=('Baskerville Old Face',14),bg=bg_color).grid(row=12,column=0,padx=30,pady=1.5,sticky='w')
        avil_txt = Entry(Frame_2,width=8,font='arial,10',textvariable=self.Avil,bd=3,relief=SUNKEN).grid(row=12,column=1,pady=2.5,padx=10)
        # |----------------| Septran Label |----------------|
        septran_lbl = Label(Frame_2,text='Septran',font=('Baskerville Old Face',14),bg=bg_color).grid(row=13,column=0,padx=30,pady=1.5,sticky='w')
        septran_txt = Entry(Frame_2,width=8,font='arial,10',textvariable=self.Septran,bd=3,relief=SUNKEN).grid(row=13,column=1,pady=2.5,padx=10)
        # |----------------| Regix Label |----------------|
        regix_lbl = Label(Frame_2,text='Regix',font=('Baskerville Old Face',14),bg=bg_color).grid(row=14,column=0,padx=30,pady=1.5,sticky='w')
        regix_txt = Entry(Frame_2,width=8,font='arial,10',textvariable=self.Regix,bd=3,relief=SUNKEN).grid(row=14,column=1,pady=2.5,padx=10)
# |----------------| Syrup Frame |----------------|
        bg_color = '#FCCEC5'
        Frame_3 = LabelFrame(self.root,bd=5,text='Syrup',font=('times new roman',10,'bold'),fg='black',bg=bg_color)
        Frame_3.place(x=765,y=190,width=262.5,height=520)   
        # |----------------| Panadol-S Label |----------------|
        panadol_s_lbl = Label(Frame_3,text='Panadol-S ',font=('Baskerville Old Face',14),bg=bg_color).grid(row=0,column=0,padx=30,pady=1.5,sticky='w')
        panadol_s_txt = Entry(Frame_3,width=8,font='arial,10',textvariable=self.Panadol_S,bd=3,relief=SUNKEN).grid(row=0,column=0,pady=2.5,padx=160)
        # |----------------| Esticof Label |----------------|
        esticof_lbl = Label(Frame_3,text='Esticof',font=('Baskerville Old Face',14),bg=bg_color).grid(row=1,column=0,padx=30,pady=1.5,sticky='w')
        esticof_txt = Entry(Frame_3,width=8,font='arial,10',textvariable=self.Esticof,bd=3,relief=SUNKEN).grid(row=1,column=0,pady=2.5,padx=160)
        # |----------------| Hydrolin Label |----------------|
        hydrolin_lbl = Label(Frame_3,text='Hydrolin',font=('Baskerville Old Face',14),bg=bg_color).grid(row=2,column=0,padx=30,pady=1.5,sticky='w')
        hydrolin_txt = Entry(Frame_3,width=8,font='arial,10',textvariable=self.Hydrolin,bd=3,relief=SUNKEN).grid(row=2,column=0,pady=2.5,padx=160)
        # |----------------| Ascoril Label |----------------|
        ascoril_lbl = Label(Frame_3,text='Ascoril',font=('Baskerville Old Face',14),bg=bg_color).grid(row=3,column=0,padx=30,pady=1.5,sticky='w')
        ascoril_txt = Entry(Frame_3,width=8,font='arial,10',textvariable=self.Ascoril,bd=3,relief=SUNKEN).grid(row=3,column=0,pady=2.5,padx=160)
        # |----------------| Brofen-S Label |----------------|
        brofen_s_lbl = Label(Frame_3,text='Brofen-S',font=('Baskerville Old Face',14),bg=bg_color).grid(row=4,column=0,padx=30,pady=1.5,sticky='w')
        brofen_s_txt = Entry(Frame_3,width=8,font='arial,10',textvariable=self.Brofen_S,bd=3,relief=SUNKEN).grid(row=4,column=0,pady=2.5,padx=160)
        # |----------------| Cofcol Label |----------------|
        cofcol_lbl = Label(Frame_3,text='Cofcol',font=('Baskerville Old Face',14),bg=bg_color).grid(row=5,column=0,padx=30,pady=1.5,sticky='w')
        cofcol_txt = Entry(Frame_3,width=8,font='arial,10',textvariable=self.Cofcol,bd=3,relief=SUNKEN).grid(row=5,column=0,pady=2.5,padx=160)
        # |----------------| Lazoran Label |----------------|
        lazoran_lbl = Label(Frame_3,text='Lazoran',font=('Baskerville Old Face',14),bg=bg_color).grid(row=6,column=0,padx=30,pady=1.5,sticky='w')
        lazoran_txt = Entry(Frame_3,width=8,font='arial,10',textvariable=self.Lazoran,bd=3,relief=SUNKEN).grid(row=6,column=0,pady=2.5,padx=160)
        # |----------------| Morphine-S Label |----------------|
        morphine_s_lbl = Label(Frame_3,text='Morphine-S ',font=('Baskerville Old Face',14),bg=bg_color).grid(row=7,column=0,padx=30,pady=1.5,sticky='w')
        morphine_s_txt = Entry(Frame_3,width=8,font='arial,10',textvariable=self.Morphin_S,bd=3,relief=SUNKEN).grid(row=7,column=0,pady=2.5,padx=160)
        # |----------------| Payodin Label |----------------|
        payodin_lbl = Label(Frame_3,text='Payodin',font=('Baskerville Old Face',14),bg=bg_color).grid(row=8,column=0,padx=30,pady=1.5,sticky='w')
        payodin_txt = Entry(Frame_3,width=8,font='arial,10',textvariable=self.Payodin,bd=3,relief=SUNKEN).grid(row=8,column=0,pady=2.5,padx=160)
        # |----------------| Advil-S Label |----------------|
        advil_s_lbl = Label(Frame_3,text='Advil-S',font=('Baskerville Old Face',14),bg=bg_color).grid(row=9,column=0,padx=30,pady=1.5,sticky='w')
        advil_s_txt = Entry(Frame_3,width=8,font='arial,10',textvariable=self.Advil_S,bd=3,relief=SUNKEN).grid(row=9,column=0,pady=2.5,padx=160)
        # |----------------| Emoxil-S Label |----------------|
        emoxil_s_lbl = Label(Frame_3,text='Emoxil-S',font=('Baskerville Old Face',14),bg=bg_color).grid(row=10,column=0,padx=30,pady=1.5,sticky='w')
        emoxil_s_txt = Entry(Frame_3,width=8,font='arial,10',textvariable=self.Emoxil_S,bd=3,relief=SUNKEN).grid(row=10,column=0,pady=2.5,padx=160)
        # |----------------| Cuftin Label |----------------|
        cuftin_lbl = Label(Frame_3,text='Cuftin',font=('Baskerville Old Face',14),bg=bg_color).grid(row=11,column=0,padx=30,pady=1.5,sticky='w')
        cuftin_txt = Entry(Frame_3,width=8,font='arial,10',textvariable=self.Coftin,bd=3,relief=SUNKEN).grid(row=11,column=0,pady=2.5,padx=160)
        # |----------------| Coscopin Label |----------------|
        coscopin_lbl = Label(Frame_3,text='Coscopin',font=('Baskerville Old Face',14),bg=bg_color).grid(row=12,column=0,padx=30,pady=1.5,sticky='w')
        coscopin_txt = Entry(Frame_3,width=8,font='arial,10',textvariable=self.Coscopin,bd=3,relief=SUNKEN).grid(row=12,column=0,pady=2.5,padx=160)
        # |----------------| Cofride-T Label |----------------|
        cofride_t_lbl = Label(Frame_3,text='Cofride-T',font=('Baskerville Old Face',14),bg=bg_color).grid(row=13,column=0,padx=30,pady=1.5,sticky='w')
        cofride_t_txt = Entry(Frame_3,width=8,font='arial,10',textvariable=self.Cofride_T,bd=3,relief=SUNKEN).grid(row=13,column=0,pady=2.5,padx=160)
        # |----------------| Calcium-P Label |----------------|
        calcium_p_lbl = Label(Frame_3,text='Calcium-P',font=('Baskerville Old Face',14),bg=bg_color).grid(row=14,column=0,padx=30,pady=1.5,sticky='w')
        calcium_p_txt = Entry(Frame_3,width=8,font='arial,10',textvariable=self.Calcium_P,bd=3,relief=SUNKEN).grid(row=14,column=0,pady=2.5,padx=160)
# |----------------| Injection Frame |----------------|
        bg_color = '#B17CF7'
        Frame_4 = LabelFrame(self.root,bd=5,text='Injection',font=('times new roman',12,'bold'),fg='black',bg=bg_color)
        Frame_4.place(x=1040,y=190,width=262.5,height=520)   
        # |----------------| Calcium-C Label |----------------|
        calcium_c_lbl = Label(Frame_4,text='Calcium-C ',font=('Baskerville Old Face',14),bg=bg_color).grid(row=0,column=0,padx=30,pady=1.5,sticky='w')
        calcium_c_txt = Entry(Frame_4,width=8,font='arial,10',textvariable=self.Calcium_C,bd=3,relief=SUNKEN).grid(row=0,column=0,pady=2.5,padx=160)
        # |----------------| Neorobion Label |----------------|
        neorobion_lbl = Label(Frame_4,text='Neorobion',font=('Baskerville Old Face',14),bg=bg_color).grid(row=1,column=0,padx=30,pady=1.5,sticky='w')
        neorobion_txt = Entry(Frame_4,width=8,font='arial,10',textvariable=self.Neorobion,bd=3,relief=SUNKEN).grid(row=1,column=0,pady=2.5,padx=160)
        # |----------------| Decadron Label |----------------|
        decadron_lbl = Label(Frame_4,text='Decadron',font=('Baskerville Old Face',14),bg=bg_color).grid(row=2,column=0,padx=30,pady=1.5,sticky='w')
        decadron_txt = Entry(Frame_4,width=8,font='arial,10',textvariable=self.Decadron,bd=3,relief=SUNKEN).grid(row=2,column=0,pady=2.5,padx=160)
        # |----------------| Avil Label |----------------|
        avil_I_lbl = Label(Frame_4,text='Avil',font=('Baskerville Old Face',14),bg=bg_color).grid(row=3,column=0,padx=30,pady=1.5,sticky='w')
        avil_I_txt = Entry(Frame_4,width=8,font='arial,10',textvariable=self.Avil_I,bd=3,relief=SUNKEN).grid(row=3,column=0,pady=2.5,padx=160)
        # |----------------| Elther Label |----------------|
        elther_lbl = Label(Frame_4,text='Elther',font=('Baskerville Old Face',14),bg=bg_color).grid(row=4,column=0,padx=30,pady=1.5,sticky='w')
        elther_txt = Entry(Frame_4,width=8,font='arial,10',textvariable=self.Elther,bd=3,relief=SUNKEN).grid(row=4,column=0,pady=2.5,padx=160)
        # |----------------| Senether Label |----------------|
        senether_lbl = Label(Frame_4,text='Senether',font=('Baskerville Old Face',14),bg=bg_color).grid(row=5,column=0,padx=30,pady=1.5,sticky='w')
        senether_txt = Entry(Frame_4,width=8,font='arial,10',textvariable=self.Senether,bd=3,relief=SUNKEN).grid(row=5,column=0,pady=2.5,padx=160)
        # |----------------| Ethenex Label |----------------|
        ethenex_lbl = Label(Frame_4,text='Ethenex ',font=('Baskerville Old Face',14),bg=bg_color).grid(row=6,column=0,padx=30,pady=1.5,sticky='w')
        ethenex_txt = Entry(Frame_4,width=8,font='arial,10',textvariable=self.Ethenex,bd=3,relief=SUNKEN).grid(row=6,column=0,pady=2.5,padx=160)
        # |----------------| Bether Label |----------------|
        bether_lbl = Label(Frame_4,text='Bether',font=('Baskerville Old Face',14),bg=bg_color).grid(row=7,column=0,padx=30,pady=1.5,sticky='w')
        bether_txt = Entry(Frame_4,width=8,font='arial,10',textvariable=self.Bether,bd=3,relief=SUNKEN).grid(row=7,column=0,pady=2.5,padx=160)
        # |----------------| Ceftef Label |----------------|
        ceftef_lbl = Label(Frame_4,text='Ceftef',font=('Baskerville Old Face',14),bg=bg_color).grid(row=8,column=0,padx=30,pady=1.5,sticky='w')
        ceftef_txt = Entry(Frame_4,width=8,font='arial,10',textvariable=self.Ceftef,bd=3,relief=SUNKEN).grid(row=8,column=0,pady=2.5,padx=160)
        # |----------------| Arther Label |----------------|
        arther_lbl = Label(Frame_4,text='Arther',font=('Baskerville Old Face',14),bg=bg_color).grid(row=9,column=0,padx=30,pady=1.5,sticky='w')
        arther_txt = Entry(Frame_4,width=8,font='arial,10',textvariable=self.Arther,bd=3,relief=SUNKEN).grid(row=9,column=0,pady=2.5,padx=160)
        # |----------------| Ether Label |----------------|
        ether_lbl = Label(Frame_4,text='Ether',font=('Baskerville Old Face',14),bg=bg_color).grid(row=10,column=0,padx=30,pady=1.5,sticky='w')
        ether_txt = Entry(Frame_4,width=8,font='arial,10',textvariable=self.Ether,bd=3,relief=SUNKEN).grid(row=10,column=0,pady=2.5,padx=160)
        # |----------------| Insoether Label |----------------|
        insoether_lbl = Label(Frame_4,text='Insoether',font=('Baskerville Old Face',14),bg=bg_color).grid(row=11,column=0,padx=30,pady=1.5,sticky='w')
        insoether_txt = Entry(Frame_4,width=8,font='arial,10',textvariable=self.Insoether,bd=3,relief=SUNKEN).grid(row=11,column=0,pady=2.5,padx=160)
        # |----------------| Artihuk Label |----------------|
        artihuk_lbl = Label(Frame_4,text='Artihuk',font=('Baskerville Old Face',14),bg=bg_color).grid(row=12,column=0,padx=30,pady=1.5,sticky='w')
        artihuk_txt = Entry(Frame_4,width=8,font='arial,10',textvariable=self.Artihuk,bd=3,relief=SUNKEN).grid(row=12,column=0,pady=2.5,padx=160)
        # |----------------| Artecare Label |----------------|
        artecare_lbl = Label(Frame_4,text='Artecare',font=('Baskerville Old Face',14),bg=bg_color).grid(row=13,column=0,padx=30,pady=1.5,sticky='w')
        artecare_txt = Entry(Frame_4,width=8,font='arial,10',textvariable=self.Articare,bd=3,relief=SUNKEN).grid(row=13,column=0,pady=2.5,padx=160)
        # |----------------| Dexa.M.Xol Label |----------------|
        dexa_m_xol_lbl = Label(Frame_4,text='Dexa.M.X',font=('Baskerville Old Face',14),bg=bg_color).grid(row=14,column=0,padx=30,pady=1.5,sticky='w')
        dexa_m_xol_txt = Entry(Frame_4,width=8,font='arial,10',textvariable=self.Dexa_M_X,bd=3,relief=SUNKEN).grid(row=14,column=0,pady=2.5,padx=160)
# |----------------| Equipments Frame |----------------|
        bg_color = '#7EE4FC'
        Frame_5 = LabelFrame(self.root,bd=5,text='Equipments',font=('times new roman',12,'bold'),fg='black',bg=bg_color)
        Frame_5.place(x=1315,y=190,width=264.5,height=520)   
        # |----------------| S-Gloves Label |----------------|
        s_gloves_lbl = Label(Frame_5,text='S-Gloves ',font=('Baskerville Old Face',14),bg=bg_color).grid(row=0,column=0,padx=30,pady=1.5,sticky='w')
        s_gloves_txt = Entry(Frame_5,width=8,font='arial,10',textvariable=self.S_Gloves,bd=3,relief=SUNKEN).grid(row=0,column=0,pady=2.5,padx=163)
        # |----------------| Sanitizer Label |----------------|
        sanitizer_lbl = Label(Frame_5,text='Sanitizer',font=('Baskerville Old Face',14),bg=bg_color).grid(row=1,column=0,padx=30,pady=1.5,sticky='w')
        sanitizer_txt = Entry(Frame_5,width=8,font='arial,10',textvariable=self.Sanitizer,bd=3,relief=SUNKEN).grid(row=1,column=0,pady=2.5,padx=163)
        # |----------------| Dettol Label |----------------|
        detol_lbl = Label(Frame_5,text='Dettol',font=('Baskerville Old Face',14),bg=bg_color).grid(row=2,column=0,padx=30,pady=1.5,sticky='w')
        detol_txt = Entry(Frame_5,width=8,font='arial,10',textvariable=self.Dettol,bd=3,relief=SUNKEN).grid(row=2,column=0,pady=2.5,padx=163)
        # |----------------| S-Mask Label |----------------|
        s_mask_lbl = Label(Frame_5,text='S-Mask',font=('Baskerville Old Face',14),bg=bg_color).grid(row=3,column=0,padx=30,pady=1.5,sticky='w')
        s_mask_txt = Entry(Frame_5,width=8,font='arial,10',textvariable=self.S_Mask,bd=3,relief=SUNKEN).grid(row=3,column=0,pady=2.5,padx=163)
        # |----------------| I.V Set Label |----------------|
        i_v_set_lbl = Label(Frame_5,text='I.V Set',font=('Baskerville Old Face',14),bg=bg_color).grid(row=4,column=0,padx=30,pady=1.5,sticky='w')
        i_v_set_txt = Entry(Frame_5,width=8,font='arial,10',textvariable=self.I_V_Set,bd=3,relief=SUNKEN).grid(row=4,column=0,pady=2.5,padx=163)
        # |----------------| Syringe Label |----------------|
        syringe_lbl = Label(Frame_5,text='Syringe',font=('Baskerville Old Face',14),bg=bg_color).grid(row=5,column=0,padx=30,pady=1.5,sticky='w')
        syringe_txt = Entry(Frame_5,width=8,font='arial,10',textvariable=self.Syring,bd=3,relief=SUNKEN).grid(row=5,column=0,pady=2.5,padx=163)
        # |----------------| Tape Label |----------------|
        tape_lbl = Label(Frame_5,text='Tape ',font=('Baskerville Old Face',14),bg=bg_color).grid(row=6,column=0,padx=30,pady=1.5,sticky='w')
        tape_txt = Entry(Frame_5,width=8,font='arial,10',textvariable=self.Tape,bd=3,relief=SUNKEN).grid(row=6,column=0,pady=2.5,padx=163)
        # |----------------| S-Cap Label |----------------|
        s_cap_lbl = Label(Frame_5,text='S-Cap',font=('Baskerville Old Face',14),bg=bg_color).grid(row=7,column=0,padx=30,pady=1.5,sticky='w')
        s_cap_txt = Entry(Frame_5,width=8,font='arial,10',textvariable=self.S_Cap,bd=3,relief=SUNKEN).grid(row=7,column=0,pady=2.5,padx=163)
        # |----------------| Knee Brace Label |----------------|
        knee_brace_lbl = Label(Frame_5,text='Knee Brace',font=('Baskerville Old Face',14),bg=bg_color).grid(row=8,column=0,padx=30,pady=1.5,sticky='w')
        knee_brace_txt = Entry(Frame_5,width=8,font='arial,10',textvariable=self.Knee_Brace,bd=3,relief=SUNKEN).grid(row=8,column=0,pady=2.5,padx=163)
        # |----------------| Ankle Brace Label |----------------|
        ankle_brace_lbl = Label(Frame_5,text='Ankle Brace',font=('Baskerville Old Face',14),bg=bg_color).grid(row=9,column=0,padx=30,pady=1.5,sticky='w')
        ankle_brace_txt = Entry(Frame_5,width=8,font='arial,10',textvariable=self.Ankle_Brace,bd=3,relief=SUNKEN).grid(row=9,column=0,pady=2.5,padx=163)
        # |----------------| Heal Brace Label |----------------|
        heal_brace_lbl = Label(Frame_5,text='Heal Brace',font=('Baskerville Old Face',14),bg=bg_color).grid(row=10,column=0,padx=30,pady=1.5,sticky='w')
        heal_brace_txt = Entry(Frame_5,width=8,font='arial,10',textvariable=self.Heal_Brace,bd=3,relief=SUNKEN).grid(row=10,column=0,pady=2.5,padx=163)
        # |----------------| Elastic Crepe Label |----------------|
        elastic_crepe_lbl = Label(Frame_5,text='Elastic Crepe',font=('Baskerville Old Face',14),bg=bg_color).grid(row=11,column=0,padx=30,pady=1.5,sticky='w')
        elastic_crepe_txt = Entry(Frame_5,width=8,font='arial,10',textvariable=self.Elastic_Crepe,bd=3,relief=SUNKEN).grid(row=11,column=0,pady=2.5,padx=163)
        # |----------------| Whool Label |----------------|
        whool_lbl = Label(Frame_5,text='Whool',font=('Baskerville Old Face',14),bg=bg_color).grid(row=12,column=0,padx=30,pady=1.5,sticky='w')
        whool_txt = Entry(Frame_5,width=8,font='arial,10',textvariable=self.Whool,bd=3,relief=SUNKEN).grid(row=12,column=0,pady=2.5,padx=163)
        # |----------------| Saniplast Label |----------------|
        saniplast_lbl = Label(Frame_5,text='Saniplast',font=('Baskerville Old Face',14),bg=bg_color).grid(row=13,column=0,padx=30,pady=1.5,sticky='w')
        saniplast_txt = Entry(Frame_5,width=8,font='arial,10',textvariable=self.Saniplast,bd=3,relief=SUNKEN).grid(row=13,column=0,pady=2.5,padx=163)
        # |----------------| Thermometer Label |----------------|
        thermometer_lbl = Label(Frame_5,text='Thermometer',font=('Baskerville Old Face',14),bg=bg_color).grid(row=14,column=0,padx=30,pady=1.5,sticky='w')
        thermometer_txt = Entry(Frame_5,width=8,font='arial,10',textvariable=self.Thermometer,bd=3,relief=SUNKEN).grid(row=14,column=0,pady=2.5,padx=163)      

# |----------------| Billing Menu Frame |----------------|
        bg_color = '#FFCBA4'
        fg_color = 'black'
        Frame_7 = LabelFrame(self.root,bd=4,text='Billing Menu',font=('times new roman',12,'bold'),fg=fg_color,bg=bg_color)
        Frame_7.place(x=0,y=741,relwidth=1,height=85)
        # |----------------| Tablets Price |----------------|
        tablets_lbl = Label(Frame_7,text='Tablets Price :',font=('Century',11,'bold'),bg=bg_color,fg=fg_color).grid(row=0,column=0,padx=20,pady=0)
        tablets_txt = Entry(Frame_7,width=20,textvariable=self.Tablets_price,font=('Comic Sans MS',9),bd=2,relief=SUNKEN,).grid(row=0,column=1,padx=10,pady=0)
        # |----------------| Syrup Price |----------------|
        syrups_lbl = Label(Frame_7,text='Syrup Price :',font=('Century',11,'bold'),bg=bg_color,fg=fg_color).grid(row=1,column=0,padx=15,pady=0)
        syrups_txt = Entry(Frame_7,width=20,textvariable=self.Syrups_price,font=('Comic Sans MS',9),bd=2,relief=SUNKEN,).grid(row=1,column=1,padx=10,pady=1)
        # |----------------| Injections Price |----------------|
        Injections_lbl = Label(Frame_7,text='Injections Price :',font=('Century',11,'bold'),bg=bg_color,fg=fg_color).grid(row=0,column=2,padx=10,pady=1.5)
        Injections_txt = Entry(Frame_7,width=20,textvariable=self.Injections_price,font=('Comic Sans MS',9),bd=2,relief=SUNKEN,).grid(row=0,column=3,padx=10,pady=1)
        # |----------------| Equipments Price |----------------|
        Equipments_lbl = Label(Frame_7,text='Equipments Price :',font=('Century',11,'bold'),bg=bg_color,fg=fg_color).grid(row=1,column=2,padx=10,pady=1)
        Equipments_txt = Entry(Frame_7,width=20,textvariable=self.Equipments_price,font=('Comic Sans MS',9),bd=2,relief=SUNKEN,).grid(row=1,column=3,padx=10,pady=1)
        # |----------------| Total Price |----------------|
        bg_color = '#FFCBA4'
        Frame_total = LabelFrame(self.root,bd=4,text='Total',font=('times new roman',12,'bold'),fg=fg_color,bg=bg_color)
        Frame_total.place(x=680,y=741,width=373,height=85)
        Total_lbl = Label(Frame_total,text='Total Price :',font=('Century',18,'bold'),bg=bg_color,fg=fg_color).grid(row=0,column=4,padx=17,pady=10)
        Total_txt = Entry(Frame_total,width=12,textvariable=self.Grand_Total_price,font=('Comic Sans MS',14),bd=2,relief=SUNKEN,).grid(row=0,column=5,padx=15,pady=7)
 
# |----------------| Button Frame |----------------------------------------------------------------------------|
        bg_color = '#FFCBA4'
        Frame_btn = LabelFrame(self.root,bd=4,text='Buttons',font=('times new roman',12,'bold'),fg='black',bg=bg_color)
        Frame_btn.place(x=1050,y=741,width=549,height=85)

        # |----------------| Total Button |----------------|
        Total_btn= Button(Frame_btn,text='Total',command=self.TOTAL_PRICE,font=('Arial',12),width=9,bg='dark blue',fg='white',pady=-2).grid(row=0,column=0,padx=10,pady=10)
        # |----------------|  Generate Bill Button |----------------|
        Bill_btn= Button(Frame_btn,command=self.B_A,text='Receipt',font=('Arial',12),width=9,bg='dark blue',fg='white',pady=-2).grid(row=0,column=1,padx=7,pady=10)
        # |----------------|  Print Bill Button |----------------|
        Bill_btn= Button(Frame_btn,text='Print',command=self.Print_Bill,font=('Arial',12),width=11,bg='dark blue',fg='white',pady=-2).grid(row=0,column=2,padx=6,pady=10)
        # |----------------|  Clear Button |----------------|
        clear_btn= Button(Frame_btn,text='Clear',command=self.Clear_Data,font=('Arial',12),width=9,bg='dark blue',fg='white',pady=-2).grid(row=0,column=3,padx=6,pady=10)
        # |----------------|  Exit Button |----------------|
        exit_btn= Button(Frame_btn,text='Exit',command=self.Exit_Win,font=('Arial',12),width=8,bg='#FF0000',fg='white',pady=-2).grid(row=0,column=4,padx=6,pady=10)
# ===================| Bill Calling Point |===================
        self.Welcome()
# ===================| Billing Menu Calculation |===================
    def TOTAL_PRICE(self):
# ===================| Tablets Calculation |===================
        self.T_Pana = (self.Panadol.get()*30)
        self.T_Poni = (self.Ponistan.get()*30)
        self.T_Aten = (self.Atenolol.get()*40)
        self.T_Baclo = (self.Baclofen.get()*125)
        self.T_Bro = (self.Brofen.get()*60)
        self.T_Cefac = (self.Cefaclor.get()*800)
        self.T_Etopo = (self.Etoposide.get()*470)
        self.T_Morph = (self.Morphin.get()*340)
        self.T_Oxi = (self.Oxicodon.get()*300)
        self.T_Advi = (self.Advil.get()*15)
        self.T_Emox = (self.Emoxil.get()*15)
        self.T_Dis = (self.Disprin.get()*23)
        self.T_Avi = (self.Avil.get()*8)
        self.T_Septra = (self.Septran.get()*40)
        self.T_Reg = (self.Regix.get()*27)
        self.Total_Tablet_Price = float( 
                                         self.T_Pana   +
                                         self.T_Poni   +
                                         self.T_Aten   +
                                         self.T_Baclo  +
                                         self.T_Bro    +
                                         self.T_Cefac  +
                                         self.T_Etopo  +
                                         self.T_Morph  +
                                         self.T_Oxi    +
                                         self.T_Advi   +
                                         self.T_Emox   +
                                         self.T_Dis    +
                                         self.T_Avi    +
                                         self.T_Septra +
                                         self.T_Reg
                                        )
        self.Tablets_price.set(str(f'Rs. {self.Total_Tablet_Price}0/-'))
# ===================| Syrup Calculation |===================
        self.S_pana_s = (self.Panadol_S.get()*98)
        self.S_Esti = (self.Esticof.get()*60)
        self.S_Hydr = (self.Hydrolin.get()*70)
        self.S_Asco = (self.Ascoril.get()*120)
        self.S_Bro_s = (self.Brofen_S.get()*100)
        self.S_Cofc= (self.Cofcol.get()*95)
        self.S_Lazo = (self.Lazoran.get()*115)
        self.S_Morph= (self.Morphin_S.get()*1800)
        self.S_Payo = (self.Payodin.get()*60)
        self.S_Advi_s = (self.Advil_S.get()*75)
        self.S_Emox_s = (self.Emoxil_S.get()*110)
        self.S_Coft= (self.Coftin.get()*45)
        self.S_Cosco= (self.Coscopin.get()*112)
        self.S_Cofri = (self.Cofride_T.get()*212)
        self.S_Calciu = (self.Calcium_P.get()*85)
        self.Total_Syrup_Price = float( 
                                         self.S_pana_s +
                                         self.S_Esti   +
                                         self.S_Hydr   +
                                         self.S_Asco   +
                                         self.S_Bro_s  +
                                         self.S_Cofc   +
                                         self.S_Lazo   +
                                         self.S_Morph  +
                                         self.S_Payo   +
                                         self.S_Advi_s +
                                         self.S_Emox_s +
                                         self.S_Coft   +
                                         self.S_Cosco  +
                                         self.S_Cofri  +
                                         self.S_Calciu
                                        )
        self.Syrups_price.set(str(f'Rs. {self.Total_Syrup_Price}0/-'))
# ===================| Injections Calculation |===================
        self.I_Calc =(self.Calcium_C.get()*300)
        self.I_Neo =(self.Neorobion.get()*28)
        self.I_Dec =(self.Decadron.get()*28)
        self.I_AI =(self.Avil_I.get()*12)
        self.I_Elthr =(self.Elther.get()*160)
        self.I_Sene =(self.Senether.get()*12)
        self.I_Ethen =(self.Ethenex.get()*600)
        self.I_Bethe =(self.Bether.get()*250)
        self.I_Ceft =(self.Ceftef.get()*140)
        self.I_Arth =(self.Arther.get()*215)
        self.I_Ether =(self.Ether.get()*57)
        self.I_Insoet =(self.Insoether.get()*22)
        self.I_Artih =(self.Artihuk.get()*325)
        self.I_Artica =(self.Articare.get()*26)
        self.I_Dexa =(self.Dexa_M_X.get()*25)
        self.Total_Injection_Price = float( 
                                            self.I_Calc     +
                                            self.I_Neo      +
                                            self.I_Dec      +
                                            self.I_AI       +
                                            self.I_Elthr    +
                                            self.I_Sene     +
                                            self.I_Ethen    +
                                            self.I_Bethe    +
                                            self.I_Ceft     +
                                            self.I_Arth     +
                                            self.I_Ether    +
                                            self.I_Insoet   +
                                            self.I_Artih    +
                                            self.I_Artica   +
                                            self.I_Dexa
                                        )
        self.Injections_price.set(str(f'Rs. {self.Total_Injection_Price}0/-'))
# ===================| Equipments Calculation |===================
        self.E_SG = (self.S_Gloves.get()*50)
        self.E_Sanit = (self.Sanitizer.get()*70)
        self.E_Dett = (self.Dettol.get()*125)
        self.E_SM = (self.S_Mask.get()*15)
        self.E_IV = (self.I_V_Set.get()*30)
        self.E_Syr = (self.Syring.get()*15)
        self.E_Tap = (self.Tape.get()*35)
        self.E_SC = (self.S_Cap.get()*50)
        self.E_KB = (self.Knee_Brace.get()*150)
        self.E_AB = (self.Ankle_Brace.get()*150)
        self.E_HB = (self.Heal_Brace.get()*150)
        self.E_EC = (self.Elastic_Crepe.get()*180)
        self.E_Wool = (self.Whool.get()*80)
        self.E_Sanip = (self.Saniplast.get()*5)
        self.E_Therm = (self.Thermometer.get()*100)
        self.Total_Equipment_Price = float( 
                                            self.E_SG     +
                                            self.E_Sanit  +
                                            self.E_Dett   +
                                            self.E_SM     +
                                            self.E_IV     +
                                            self.E_Syr    +
                                            self.E_Tap    +
                                            self.E_SC     +
                                            self.E_KB     +
                                            self.E_AB     +
                                            self.E_HB     +
                                            self.E_EC     +
                                            self.E_Wool   +
                                            self.E_Sanip  +
                                            self.E_Therm  
                                        )
        self.Equipments_price.set(str(f'Rs. {self.Total_Equipment_Price}0/-'))
# ===================| Grand Total Calculation |===================
        self.G_Total_Price = float(
                                  (self.Total_Tablet_Price)+
                                  (self.Total_Syrup_Price)+
                                  (self.Total_Injection_Price)+
                                  (self.Total_Equipment_Price)
                                  )
        self.Grand_Total_price.set(str(f'Rs. {self.G_Total_Price}0/-'))
# ===================| Billing Area Setting |===================
    def Welcome(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,f'\t\t        MOHSIN\'s\n\t      (Pharmacy Managment System)\n\t\t     (0300-1358167)')
        self.txtarea.insert(END,f'\n====================================================')
        self.txtarea.insert(END,f'\nBill ID : {self.Bill_id.get()}         {self.display_date} |{self.display_time}')
        self.txtarea.insert(END,f'\nName    : {self.Name.get()}	 	               ')
        self.txtarea.insert(END,f'\nContact : {self.Contact.get()}')
        self.txtarea.insert(END,f'\n----------------------------------------------------')
        self.txtarea.insert(END,f'\n    Discription          Qty         Amount     ')
        self.txtarea.insert(END,f'\n====================================================')
# ===================| Generat Bill Button Setting |===================
    def B_A(self):
        if self.Name.get() =='' or self.Contact.get() == '':
                messagebox.showerror('Error','Enter Customer Details!')
        elif self.Grand_Total_price.get() == '':
                messagebox.showerror('Error','Please total the Bill!')
        elif self.Grand_Total_price.get() == 'Rs. 0.00/-':
                messagebox.showerror('Error','No Item Selected!')
        else:
                self.Welcome()
        # ===================| Tablets Bill Setting |===================
                if self.Panadol.get()!=0:
                        self.txtarea.insert(END,f'\n     Panadol              {self.Panadol.get()}           {self.T_Pana}.0     ')
                if self.Ponistan.get()!=0:
                        self.txtarea.insert(END,f'\n     Ponistan             {self.Ponistan.get()}           {self.T_Poni}.0     ')
                if self.Atenolol.get()!=0:
                        self.txtarea.insert(END,f'\n     Atenolol             {self.Atenolol.get()}           {self.T_Aten}.0     ')
                if self.Baclofen.get()!=0:
                        self.txtarea.insert(END,f'\n     Baclofen             {self.Baclofen.get()}           {self.T_Baclo}.0     ')
                if self.Brofen.get()!=0:
                        self.txtarea.insert(END,f'\n     Brofen               {self.Brofen.get()}           {self.T_Bro}.0     ')
                if self.Cefaclor.get()!=0:
                        self.txtarea.insert(END,f'\n     Cefaclor             {self.Cefaclor.get()}           {self.T_Cefac}.0     ')
                if self.Etoposide.get()!=0:
                        self.txtarea.insert(END,f'\n     Etoposide            {self.Etoposide.get()}           {self.T_Etopo}.0     ')
                if self.Morphin.get()!=0:
                        self.txtarea.insert(END,f'\n     Morphin              {self.Morphin.get()}           {self.T_Morph}.0     ')
                if self.Oxicodon.get()!=0:
                        self.txtarea.insert(END,f'\n     Oxicodon             {self.Oxicodon.get()}           {self.T_Oxi}.0     ')
                if self.Advil.get()!=0:
                        self.txtarea.insert(END,f'\n     Advil                {self.Advil.get()}           {self.T_Advi}.0     ')
                if self.Emoxil.get()!=0: 
                        self.txtarea.insert(END,f'\n     Emoxil               {self.Emoxil.get()}           {self.T_Emox}.0     ')
                if self.Disprin.get()!=0:
                        self.txtarea.insert(END,f'\n     Disprin              {self.Disprin.get()}           {self.T_Dis}.0     ')
                if self.Avil.get()!=0:
                        self.txtarea.insert(END,f'\n     Avil                 {self.Avil.get()}           {self.T_Avi}.0     ')
                if self.Septran.get()!=0:
                        self.txtarea.insert(END,f'\n     Septran              {self.Septran.get()}           {self.T_Septra}.0     ')
                if self.Regix.get()!=0:
                        self.txtarea.insert(END,f'\n     Regix                {self.Regix.get()}           {self.T_Reg}.0     ')
        # ===================| Syrups Bill Setting |===================
                if self.Panadol_S.get()!=0:
                        self.txtarea.insert(END,f'\n     Panadol-S            {self.Panadol_S.get()}           {self.S_pana_s}.0     ')
                if self.Esticof.get()!=0:
                        self.txtarea.insert(END,f'\n     Esticof              {self.Esticof.get()}           {self.S_Esti}.0     ')
                if self.Hydrolin.get()!=0:
                        self.txtarea.insert(END,f'\n     Hydrolin             {self.Hydrolin.get()}           {self.S_Hydr}.0     ')
                if self.Ascoril.get()!=0:
                        self.txtarea.insert(END,f'\n     Ascoril              {self.Ascoril.get()}           {self.S_Asco}.0     ')
                if self.Brofen_S.get()!=0:
                        self.txtarea.insert(END,f'\n     Brofen-S             {self.Brofen_S.get()}           {self.S_Bro_s}.0     ')
                if self.Cofcol.get()!=0:
                        self.txtarea.insert(END,f'\n     Cofcol               {self.Cofcol.get()}           {self.S_Cofc}.0     ')
                if self.Lazoran.get()!=0:
                        self.txtarea.insert(END,f'\n     Lazoran              {self.Lazoran.get()}           {self.S_Lazo}.0     ')
                if self.Morphin_S.get()!=0:
                        self.txtarea.insert(END,f'\n     Morphin-S            {self.Morphin_S.get()}           {self.S_Morph}.0     ')
                if self.Payodin.get()!=0:
                        self.txtarea.insert(END,f'\n     Payodin              {self.Payodin.get()}           {self.S_Payo}.0     ')
                if self.Advil_S.get()!=0:
                        self.txtarea.insert(END,f'\n     Advil-S              {self.Advil_S.get()}           {self.S_Advi_s}.0     ')
                if self.Emoxil_S.get()!=0: 
                        self.txtarea.insert(END,f'\n     Emoxil-S             {self.Emoxil_S.get()}           {self.S_Emox_s}.0     ')
                if self.Coftin.get()!=0:
                        self.txtarea.insert(END,f'\n     Coftin               {self.Coftin.get()}           {self.S_Coft}.0     ')
                if self.Coscopin.get()!=0:
                        self.txtarea.insert(END,f'\n     Coscopin             {self.Coscopin.get()}           {self.S_Cosco}.0     ')
                if self.Cofride_T.get()!=0:
                        self.txtarea.insert(END,f'\n     Cofride-T            {self.Cofride_T.get()}           {self.S_Cofri}.0     ')
                if self.Calcium_P.get()!=0:
                        self.txtarea.insert(END,f'\n     Calcium_P            {self.Calcium_P.get()}           {self.S_Calciu}.0     ')
        # ===================| Injections Bill Setting |===================
                if self.Calcium_C.get()!=0:
                        self.txtarea.insert(END,f'\n     Calcium-C            {self.Calcium_C.get()}           {self.I_Calc}.0     ')
                if self.Neorobion.get()!=0:
                        self.txtarea.insert(END,f'\n     Neorobion            {self.Neorobion.get()}           {self.I_Neo}.0     ')
                if self.Decadron.get()!=0:
                        self.txtarea.insert(END,f'\n     Decadron             {self.Decadron.get()}           {self.I_Dec}.0     ')
                if self.Avil_I.get()!=0:
                        self.txtarea.insert(END,f'\n     Avil-I               {self.Avil_I.get()}           {self.I_AI}.0     ')
                if self.Elther.get()!=0:
                        self.txtarea.insert(END,f'\n     Elther               {self.Elther.get()}           {self.I_Elthr}.0     ')
                if self.Senether.get()!=0:
                        self.txtarea.insert(END,f'\n     Senether             {self.Senether.get()}           {self.I_Sene}.0     ')
                if self.Ethenex.get()!=0:
                        self.txtarea.insert(END,f'\n     Ethenex              {self.Ethenex.get()}           {self.I_Ethen}.0     ')
                if self.Bether.get()!=0:
                        self.txtarea.insert(END,f'\n     Bether               {self.Bether.get()}           {self.I_Bethe}.0     ')
                if self.Ceftef.get()!=0:
                        self.txtarea.insert(END,f'\n     Ceftef               {self.Ceftef.get()}           {self.I_Ceft}.0     ')
                if self.Arther.get()!=0:
                        self.txtarea.insert(END,f'\n     Arther               {self.Arther.get()}           {self.I_Arth}.0     ')
                if self.Ether.get()!=0: 
                        self.txtarea.insert(END,f'\n     Ether                {self.Ether.get()}           {  self.I_Ether}.0     ')
                if self.Insoether.get()!=0:
                        self.txtarea.insert(END,f'\n     Insoether            {self.Insoether.get()}           {self.I_Insoet}.0     ')
                if self.Artihuk.get()!=0:
                        self.txtarea.insert(END,f'\n     Artihuk              {self.Artihuk.get()}           {self.I_Artih}.0     ')
                if self.Articare.get()!=0:
                        self.txtarea.insert(END,f'\n     Articare             {self.Articare.get()}           {self.I_Artica}.0     ')
                if self.Dexa_M_X.get()!=0:
                        self.txtarea.insert(END,f'\n     Dexa-M-X             {self.Dexa_M_X.get()}           {self.I_Dexa}.0     ')
        # ===================| Equipments Bill Setting |===================
                if self.S_Gloves.get()!=0:
                        self.txtarea.insert(END,f'\n     S.Gloves             {self.S_Gloves.get()}           {self.E_SG}.0     ')
                if self.Sanitizer.get()!=0:
                        self.txtarea.insert(END,f'\n     Sanitizer            {self.Sanitizer.get()}           {self.E_Sanit}.0     ')
                if self.Dettol.get()!=0:
                        self.txtarea.insert(END,f'\n     Dettol               {self.Dettol.get()}           {self.E_Dett}.0     ')
                if self.S_Mask.get()!=0:
                        self.txtarea.insert(END,f'\n     S_Mask               {self.S_Mask.get()}           {self.E_SM}.0     ')
                if self.I_V_Set.get()!=0:
                        self.txtarea.insert(END,f'\n     IV.Set               {self.I_V_Set.get()}           {self.E_IV}.0     ')
                if self.Syring.get()!=0:
                        self.txtarea.insert(END,f'\n     Syring               {self.Syring.get()}           {self.E_Syr}.0     ')
                if self.Tape.get()!=0:
                        self.txtarea.insert(END,f'\n     Tape                 {self.Tape.get()}           {self.E_Tap}.0     ')
                if self.S_Cap.get()!=0:
                        self.txtarea.insert(END,f'\n     S.Cap                {self.S_Cap.get()}           {self.E_SC}.0     ')
                if self.Knee_Brace.get()!=0:
                        self.txtarea.insert(END,f'\n     Knee Brace           {self.Knee_Brace.get()}           {self.E_KB}.0     ')
                if self.Ankle_Brace.get()!=0:
                        self.txtarea.insert(END,f'\n     Ankle Brace          {self.Ankle_Brace.get()}           {self.E_AB}.0     ')
                if self.Heal_Brace.get()!=0: 
                        self.txtarea.insert(END,f'\n     Heal Brace           {self.Heal_Brace.get()}           {self.E_HB}.0     ')
                if self.Elastic_Crepe.get()!=0:
                        self.txtarea.insert(END,f'\n     Elastic Crepe        {self.Elastic_Crepe.get()}           {self.E_EC}.0     ')
                if self.Whool.get()!=0:
                        self.txtarea.insert(END,f'\n     Whool                {self.Whool.get()}           {self.E_Wool}.0     ')
                if self.Saniplast.get()!=0:
                        self.txtarea.insert(END,f'\n     Saniplast            {self.Saniplast.get()}           {self.E_Sanip}.0     ')
                if self.Thermometer.get()!=0:
                        self.txtarea.insert(END,f'\n     Thermometer          {self.Thermometer.get()}           {self.E_Therm}.0     ')
# ===================| Total Ammount Setting |===================
                # self.txtarea.insert(END,f'\n\n``````````````````````````````````````````````')
                self.txtarea.insert(END,f'\n\n----------------------------------------------------')
                self.txtarea.insert(END,f'\n      Total  -----------------------  {self.Total_Tablet_Price+self.Total_Syrup_Price+self.Total_Injection_Price+self.Total_Equipment_Price}/-')
                self.Save_bill()
# ===================| Saving Bill Option |===================
    def Save_bill(self):
        self.op  = messagebox.askyesno('Save Bill','Do you want to Save Bill ?')
        if self.op>0:
                self.bill_data = self.txtarea.get('1.0',END)
                f1 = open('Bills/'+str(self.Bill_id.get())+'.txt','w')
                f1.write(self.bill_data)
                f1.close()   
                messagebox.showinfo('Saved',f'Bill No : {self.Bill_id.get()} Saved Succesfully ')     
        else:
                return
# ===================| Search Button Setting |===================
    def Find_bill(self):
        Present = 'No'
        for i in os.listdir('Bills/'):
            if i.split('.')[0]==self.Bill_id.get():
                f1 = open(f'Bills/{i}','r')
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                Present = 'Yes'
        if Present=='No':
            messagebox.showerror('Error','Invalid Bill Number !')
# ===================| Clear Button Setting |===================
    def Clear_Data(self):
        op  = messagebox.askyesno('Clear Bill','Do you want to Clear Bill ?')
        if op >0:
                self.Panadol .set(0)
                self.Ponistan .set(0)
                self.Atenolol .set(0)
                self.Baclofen .set(0)
                self.Brofen .set(0)
                self.Cefaclor .set(0)
                self.Etoposide .set(0)
                self.Morphin .set(0)
                self.Oxicodon .set(0)
                self.Advil .set(0)
                self.Emoxil .set(0)
                self.Disprin .set(0)
                self.Avil .set(0)
                self.Septran .set(0)
                self.Regix .set(0)
                # |----------------| Syrup Variables |----------------|
                self.Panadol_S .set(0)
                self.Esticof .set(0)
                self.Hydrolin .set(0)
                self.Ascoril .set(0)
                self.Brofen_S .set(0)
                self.Cofcol .set(0)
                self.Lazoran .set(0)
                self.Morphin_S .set(0)
                self.Payodin .set(0)
                self.Advil_S .set(0)
                self.Emoxil_S .set(0)
                self.Coftin .set(0)
                self.Coscopin .set(0)
                self.Cofride_T .set(0)
                self.Calcium_P .set(0)
                # |----------------| Injections Variables |----------------|
                self.Calcium_C .set(0)
                self.Neorobion .set(0)
                self.Decadron .set(0)
                self.Avil_I .set(0)
                self.Elther .set(0)
                self.Senether .set(0)
                self.Ethenex .set(0)
                self.Bether .set(0)
                self.Ceftef .set(0)
                self.Arther .set(0)
                self.Ether .set(0)
                self.Insoether .set(0)
                self.Artihuk .set(0)
                self.Articare .set(0)
                self.Dexa_M_X .set(0)
                # |----------------| Equipments Variables |----------------|
                self.S_Gloves .set(0)
                self.Sanitizer .set(0)
                self.Dettol .set(0)
                self.S_Mask .set(0)
                self.I_V_Set .set(0)
                self.Syring .set(0)
                self.Tape .set(0)
                self.S_Cap .set(0)
                self.Knee_Brace .set(0)
                self.Ankle_Brace .set(0)
                self.Heal_Brace .set(0)
                self.Elastic_Crepe .set(0)
                self.Whool .set(0)
                self.Saniplast .set(0)
                self.Thermometer .set(0)
                # |----------------| Total Bill Variables |----------------|
                self.Tablets_price .set('')
                self.Syrups_price .set('')
                self.Injections_price .set('')
                self.Equipments_price .set('')
                self.Grand_Total_price .set('')
                # |----------------| Customer Vriables |----------------|
                self.Bill_id .set('')
                x=random.randint(1111111,9999999)
                self.Bill_id .set(str(x))
                self.Search_bill .set('')
                self.Name .set('')
                self.Contact .set('')
                # |----------------| Welcome Calling Point |----------------|
                self.Welcome()
                self.Print_Bill
        else:
                return
# |----------------| Exit Functionality |----------------|
    def Exit_Win(self):
        op = messagebox.askyesno('Exit','Are you Sure ? ')
        if op>0:
                root.destroy()
        else:
                return
        
# |----------------| Print Functionality |----------------|
    def Print_Bill(self):
        if ((self.Name.get() =='' or self.Contact.get() == '') or (self.Grand_Total_price.get() == '') or (self.Grand_Total_price.get() == 'Rs. 0.00/-')): 
                messagebox.showerror('Hint','Please Generate & Save the Receipt\n \n\t   Thanks!')  
        elif self.op>0:
                op_  = messagebox.askyesno('Print Bill','Do you want to Print Bill ?')
                if op_>0:
                        print_bill = self.txtarea.get('1.0',END)
                        file_name = tempfile.mktemp('.txt')
                        open(file_name,'w').write(print_bill)
                        os.startfile(file_name,'Print')
                else : 
                       return
        else:
                return   messagebox.showerror('Hint','Please Generate & Save the Receipt\n \n\t   Thanks!')  
                
                       
                        
 

# |----------------| Details Menu Frame |----------------|

# |----------------| Time Dsiplay |----------------|
    def Time_dis(self):
        Time = Label(self.Frame_1,font=('DS-Digital',22,'bold'),bg=self.bg_color,fg='red')
        Time.grid(row=0,column=7,padx=5,pady=0)
        self.display_time = strftime(' %H:%M:%S %p  ')
        Time.config(text = self.display_time)
        Time.after(1000,self.Time_dis)

# |----------------| Date Dsiplay |----------------|
    def Date_Day_dis(self):
        Date = Label(self.Frame_1,font=('DS-Digital',22,'bold'),bg=self.bg_color,fg='red')
        Date.grid(row=0,column=8,padx=3,pady=0)
        self.display_date = strftime('%d/%b/%Y')
        Date.config(text = self.display_date)


# |----------------| Price List Button |----------------|
    def Price_lst(self):
        win = Tk()
        win.geometry('500x504+570+200')
        win.resizable(False,False)
        win.title ('Price List')
        win.iconbitmap('Icon.ico')

        price_box = Label(win,bg='#FFCBA4',height=6,bd=7,relief=GROOVE)
        price_box.config(bg='#FFCBA4',padx=10,pady=2)
        price_box.pack(fill=X)
        Head = Label(win,text='Price List',font=('Monotype corsiva',35,'bold'),bg='#FFCBA4').place(x=157,y=22)
        # Head = Label(win,text='Pharmacy Managment System \nproject by\nMOHSIN',font=('Monotype corsiva',12),bg='#FFCBA4').place(x=160,y=38)

# ===============| Items Price |================

        # ===============| Tablets Price |================
        F_1_clr = '#EDEDEB'
        Frame_1 = LabelFrame(win,bd=3,text='Tablets',font=('times new roman',12,'bold'),fg='black',bg=F_1_clr,width=126,height=400)
        Frame_1.place(x=2,y=105)
        PR = Label(Frame_1,text=' Item\t Rs/-',font=('Consolas',10),bg=F_1_clr,bd=4,relief=GROOVE).place(x=10,y=4)
        DSH = Label(Frame_1,text='  -------------',font=('Consolas',10),bg=F_1_clr).place(x=1,y=26)
        Panadol = Label(Frame_1,text='Panadol\t  30',font=('Consolas',10),bg=F_1_clr).place(x=4,y=47)
        Ponistan = Label(Frame_1,text='Ponistan  30',font=('Consolas',10),bg=F_1_clr).place(x=4,y=68)
        Atenolol = Label(Frame_1,text='Atenolol  40',font=('Consolas',10),bg=F_1_clr).place(x=4,y=89)
        Baclofen = Label(Frame_1,text='Baclofen  125',font=('Consolas',10),bg=F_1_clr).place(x=4,y=110)
        Brofen = Label(Frame_1,text='Brofen    60',font=('Consolas',10),bg=F_1_clr).place(x=4,y=131)
        Cefaclor = Label(Frame_1,text='Cefaclor  800',font=('Consolas',10),bg=F_1_clr).place(x=4,y=152)
        Etoposide = Label(Frame_1,text='Etoposide 470',font=('Consolas',10),bg=F_1_clr).place(x=4,y=173)
        Morphin = Label(Frame_1,text='Morphin   340',font=('Consolas',10),bg=F_1_clr).place(x=4,y=194)
        Oxicodon = Label(Frame_1,text='Oxicodon  300',font=('Consolas',10),bg=F_1_clr).place(x=4,y=215)
        Advil = Label(Frame_1,text='Advil     15',font=('Consolas',10),bg=F_1_clr).place(x=4,y=236)
        Emoxil = Label(Frame_1,text='Emoxil    15',font=('Consolas',10),bg=F_1_clr).place(x=4,y=257)
        Disprin = Label(Frame_1,text='Disprin   23',font=('Consolas',10),bg=F_1_clr).place(x=4,y=278)
        Avil = Label(Frame_1,text='Avil      8',font=('Consolas',10),bg=F_1_clr).place(x=4,y=299)
        Septran = Label(Frame_1,text='Septran   40',font=('Consolas',10),bg=F_1_clr).place(x=4,y=320)
        Regix = Label(Frame_1,text='Regix     27',font=('Consolas',10),bg=F_1_clr).place(x=4,y=341)

        # ===============| Syrups Price |================
        F_1_clr = '#EDEDEB'
        Frame_1 = LabelFrame(win,bd=2,text='Syrup',font=('times new roman',12,'bold'),fg='black',bg=F_1_clr,width=127,height=400)
        Frame_1.place(x=125,y=105)
        PR = Label(Frame_1,text=' Item\t Rs/-',font=('Consolas',10),bg=F_1_clr,bd=4,relief=GROOVE).place(x=10,y=4)
        DSH = Label(Frame_1,text='  -------------',font=('Consolas',10),bg=F_1_clr).place(x=1,y=26)
        Panadol = Label(Frame_1,text='Panadol\t   98',font=('Consolas',10),bg=F_1_clr).place(x=4,y=47)
        Esticof = Label(Frame_1,text='Esticof    60',font=('Consolas',10),bg=F_1_clr).place(x=4,y=68)
        Hydrolin = Label(Frame_1,text='Hydrolin   70',font=('Consolas',10),bg=F_1_clr).place(x=4,y=89)
        Ascoril = Label(Frame_1,text='Ascoril    120',font=('Consolas',10),bg=F_1_clr).place(x=4,y=110)
        Brofen = Label(Frame_1,text='Brofen     100',font=('Consolas',10),bg=F_1_clr).place(x=4,y=131)
        Cofcol = Label(Frame_1,text='Cofcol     95',font=('Consolas',10),bg=F_1_clr).place(x=4,y=152)
        Lazoran = Label(Frame_1,text='Lazoran    115',font=('Consolas',10),bg=F_1_clr).place(x=4,y=173)
        Morphin_s = Label(Frame_1,text='Morphin-S  1800',font=('Consolas',10),bg=F_1_clr).place(x=4,y=194)
        Payodin = Label(Frame_1,text='Payodin    60',font=('Consolas',10),bg=F_1_clr).place(x=4,y=215)
        Advil = Label(Frame_1,text='Advil      75',font=('Consolas',10),bg=F_1_clr).place(x=4,y=236)
        Emoxil = Label(Frame_1,text='Emoxil     110',font=('Consolas',10),bg=F_1_clr).place(x=4,y=257)
        Coftin = Label(Frame_1,text='Coftin     45',font=('Consolas',10),bg=F_1_clr).place(x=4,y=278)
        Coscopin = Label(Frame_1,text='Coscopin   112',font=('Consolas',10),bg=F_1_clr).place(x=4,y=299)
        Cofride_T = Label(Frame_1,text='Cofride_T  212',font=('Consolas',10),bg=F_1_clr).place(x=4,y=320)
        Calcium_P = Label(Frame_1,text='Calcium_P  85',font=('Consolas',10),bg=F_1_clr).place(x=4,y=341)
        # ===============| Injections Price |================
        F_1_clr='#EDEDEB'
        Frame_1 = LabelFrame(win,bd=2,text='Injections',font=('times new roman',12,'bold'),fg='black',bg=F_1_clr,width=125,height=400)
        Frame_1.place(x=250,y=105)
        PR = Label(Frame_1,text=' Item\t Rs/-',font=('Consolas',10),bg=F_1_clr,bd=4,relief=GROOVE).place(x=10,y=4)
        DSH = Label(Frame_1,text='  -------------',font=('Consolas',10),bg=F_1_clr).place(x=1,y=26)
        Calcium_C = Label(Frame_1,text='Calcium_C  300',font=('Consolas',10),bg=F_1_clr).place(x=4,y=47)
        Neorobion = Label(Frame_1,text='Neorobion  28',font=('Consolas',10),bg=F_1_clr).place(x=4,y=68)
        Decadron = Label(Frame_1,text='Decadron   28',font=('Consolas',10),bg=F_1_clr).place(x=4,y=89)
        Avil = Label(Frame_1,text='Avil       12',font=('Consolas',10),bg=F_1_clr).place(x=4,y=110)
        Elther= Label(Frame_1,text='Elther     160',font=('Consolas',10),bg=F_1_clr).place(x=4,y=131)
        Senether = Label(Frame_1,text='Senether   12',font=('Consolas',10),bg=F_1_clr).place(x=4,y=152)
        Ethenex = Label(Frame_1,text='Ethenex    600',font=('Consolas',10),bg=F_1_clr).place(x=4,y=173)
        Bether = Label(Frame_1,text='Bether     250',font=('Consolas',10),bg=F_1_clr).place(x=4,y=194)
        Ceftef = Label(Frame_1,text='Ceftef     140',font=('Consolas',10),bg=F_1_clr).place(x=4,y=215)
        Arther = Label(Frame_1,text='Arther     215',font=('Consolas',10),bg=F_1_clr).place(x=4,y=236)
        Ether = Label(Frame_1,text='Ether      57',font=('Consolas',10),bg=F_1_clr).place(x=4,y=257)
        Insoether = Label(Frame_1,text='Insoether  22',font=('Consolas',10),bg=F_1_clr).place(x=4,y=278)
        Artihuk = Label(Frame_1,text='Artihuk    325',font=('Consolas',10),bg=F_1_clr).place(x=4,y=299)
        Articare = Label(Frame_1,text='Articare   26',font=('Consolas',10),bg=F_1_clr).place(x=4,y=320)
        Dexa_M_X= Label(Frame_1,text='Dexa_M_X   25',font=('Consolas',10),bg=F_1_clr).place(x=4,y=341)
        # ===============| Equipments Price |================
        F_1_clr = '#EDEDEB'
        Frame_1 = LabelFrame(win,bd=3,text='Equipments',font=('times new roman',12,'bold'),fg='black',bg=F_1_clr,width=127,height=400)
        Frame_1.place(x=372,y=105)
        PR = Label(Frame_1,text=' Item\t Rs/-',font=('Consolas',10),bg=F_1_clr,bd=4,relief=GROOVE).place(x=10,y=4)
        DSH = Label(Frame_1,text='  -------------',font=('Consolas',10),bg=F_1_clr).place(x=1,y=26)
        S_Gloves = Label(Frame_1,text='S_Gloves    50',font=('Consolas',10),bg=F_1_clr).place(x=4,y=47)
        Sanitizer = Label(Frame_1,text='Sanitizer   70',font=('Consolas',10),bg=F_1_clr).place(x=4,y=68)
        Dettol = Label(Frame_1,text='Dettol      125',font=('Consolas',10),bg=F_1_clr).place(x=4,y=89)
        S_Mask = Label(Frame_1,text='S_Mask      15',font=('Consolas',10),bg=F_1_clr).place(x=4,y=110)
        I_V_Set = Label(Frame_1,text='I_V_Set     30',font=('Consolas',10),bg=F_1_clr).place(x=4,y=131)
        Syring = Label(Frame_1,text='Syring      15',font=('Consolas',10),bg=F_1_clr).place(x=4,y=152)
        Tape = Label(Frame_1,text='Tape        35',font=('Consolas',10),bg=F_1_clr).place(x=4,y=173)
        S_Cap = Label(Frame_1,text='S_Cap       50',font=('Consolas',10),bg=F_1_clr).place(x=4,y=194)
        Knee_Brace = Label(Frame_1,text='Knee_Brace  150',font=('Consolas',10),bg=F_1_clr).place(x=4,y=215)
        Advil = Label(Frame_1,text='Ankle_Brace 150',font=('Consolas',10),bg=F_1_clr).place(x=4,y=236)
        Emoxil = Label(Frame_1,text='Heal_Brace  150',font=('Consolas',10),bg=F_1_clr).place(x=4,y=257)
        Disprin = Label(Frame_1,text='E_Crepe     180',font=('Consolas',10),bg=F_1_clr).place(x=4,y=278)
        Avil = Label(Frame_1,text='Whool       80',font=('Consolas',10),bg=F_1_clr).place(x=4,y=299)
        Septran = Label(Frame_1,text='Saniplast   5',font=('Consolas',10),bg=F_1_clr).place(x=4,y=320)
        Regix = Label(Frame_1,text='Thermometer 100',font=('Consolas',10),bg=F_1_clr).place(x=4,y=341)
        win.mainloop()

        
# |----------------| Calling Point |----------------|
root = Tk()
obj = Bill_App()
root.mainloop()
