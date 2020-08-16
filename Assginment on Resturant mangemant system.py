from tkinter import*
from tkinter import ttk
import random
from datetime import datetime
import time;
from tkinter import messagebox

#===============================creating class===================================================================================================================================================

class Customer:
    def __init__(self,root):
        self.t = t
        self.t.title("Resturant Managment system")
        self.t.geometry("1350x750+0+0")
        
        #========================================constructing Frames==================================================================
        Tops= Frame(self.t,width = 1350, height=100, bd=6, relief="raise")
        Tops.grid(row=0,column=0, columnspan=4,sticky=W)

        BottomMainFrame= Frame(self.t,width=1350,height=650, bd=6, relief="raise")
        BottomMainFrame.grid()
        
        F1= Frame(BottomMainFrame,width = 444, height=642, bd=2, relief="raise")
        F1.grid(row=1,column=0, sticky=W)
        F2= Frame(BottomMainFrame,width = 444, height=642,bd=2, relief="raise")
        F2.grid(row=1,column=1, sticky=W)
        F3= Frame(BottomMainFrame,width = 444, height=642,bd=2,relief="raise")
        F3.grid(row=1,column=2,sticky=W)
        F2TOP= Frame(F2,width = 444, height=346,bd=1, relief="raise")
        F2TOP.grid(row=0,column=0, columnspan=4,sticky=W)
        F2BOTTOM= Frame(F2,width = 444, height=296,bd=0, relief="raise")
        F2BOTTOM.grid(row=1,column=0, columnspan=4,sticky=W)
        
        Date = StringVar()
        Time = StringVar()
        Date.set(time.strftime("%d/%m/%Y"))
        Time.set(time.strftime(" %H/%M/%S  "))
        
        self.lblTitle = Label(Tops, font = ('arial', 20, 'bold'), textvariable=Date, fg="crimson", pady=9, bd=5).grid(row = 0, column= 0)
        self.lblTitle = Label(Tops, font = ('arial', 50, 'bold'), text = "       Resturant billing system        ").grid(row = 0, column= 1)
        self.lblTitle = Label(Tops, font = ('arial', 20, 'bold'), textvariable=Time,fg="crimson", pady=9, bd=5).grid(row = 0, column= 2)
        
#=======================================initializing variable==================================================================================================================================
                
        var1 =IntVar()
        var2 =IntVar()
        var3 =IntVar()
        var4 =IntVar()
        var5 =IntVar()
        var6 =IntVar()
        var7 =IntVar()
        var8 =IntVar()
        var9 =IntVar()
        var10 =IntVar()
        var11 =IntVar()
        var12 =IntVar()
        var13 =IntVar()
        var14 =IntVar()
        var15 =IntVar()
        var16 =IntVar()
        var17 =IntVar()
        var18 =IntVar()
        var19 =IntVar()
        var20 =IntVar()
        var21 =IntVar()
        var22 =StringVar()
        var23 =IntVar()

        var1.set(0)
        var2.set(0)
        var3.set(0)
        var4.set(0)
        var5.set(0)
        var6.set(0)
        var7.set(0)
        var8.set(0)
        var9.set(0)
        var10.set(0)
        var11.set(0)
        var12.set(0)
        var13.set(0)
        var14.set(0)
        var15.set(0)
        var16.set(0)
        var17.set(0)
        var18.set(0)
        var19.set(0)
        var20.set(0)
        var21.set(0)
        var22.set("")
        var23.set(0)

        varThukpa =StringVar()
        varvegmomo =StringVar()
        varchickenmomo =StringVar()
        varVchowmein  =StringVar()
        varCchowmein =StringVar()
        varBlackforest =StringVar()
        varwhiteforest =StringVar()
        varchoCoffeete =StringVar()

        varFryrice = StringVar()
        varPasta = StringVar()
        varSamosa = StringVar()
        varSalad = StringVar()
        varOmlet = StringVar()

        varTea = StringVar()
        varCoffee = StringVar()
        varSprit = StringVar()
        varfanta = StringVar()
        varBottleWater = StringVar()

        varVanillaCone = StringVar()
        varVanillaShake = StringVar()
        varStrawberryShake = StringVar()


        varChange = StringVar()
        varSubTotal = StringVar()
        varTotal = StringVar()
        varVAT = StringVar()
        varServiceCharge = StringVar()
        varPayment = IntVar()

        varThukpa.set('0')
        varvegmomo.set('0')
        varchickenmomo.set('0')
        varVchowmein .set('0')
        varCchowmein.set('0')
        varBlackforest.set('0')
        varwhiteforest.set('0')
        varchoCoffeete.set('0')
        varTotal.set('0')

        varFryrice.set('0')
        varPasta.set('0')
        varSamosa.set('0')
        varSalad.set('0')
        varOmlet.set('0')

        varTea.set('0') 
        varCoffee.set('0') 
        varSprit.set('0')
        varfanta.set('0')
        varBottleWater.set('0')

        varVanillaCone.set('0')
        varVanillaShake.set('0')
        varStrawberryShake.set('0')

        varVAT.set("")
        varServiceCharge.set("0")
        varTotal.set("0")
        varChange.set("0")
        varSubTotal.set("0")

#=============================Exit===========================================================================================================================================================
        def iExit():
            qExit= messagebox.askyesno("Resturant Managment system", "Do you want to quit?")
            if qExit >0:
                root.destroy()
            else:
                try:
                    qExit ("no")
                except:
                     qExit= messagebox.askyesno("Resturant Managment system", "Do you want to stay?")
                     if qExit <1:
                        root.destroy()
                        return

#===============================Reset========================================================================================================================================================
                
        def Reset():
            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set(0)
            var12.set(0)
            var13.set(0)
            var14.set(0)
            var15.set(0)
            var16.set(0)
            var17.set(0)
            var18.set(0)
            var19.set(0)
            var20.set(0)
            var21.set(0)
            var23.set(0)

            varThukpa.set('0')
            varvegmomo.set('0')
            varchickenmomo.set('0')
            varVchowmein .set('0')
            varCchowmein.set('0')
            varBlackforest.set('0')
            varwhiteforest.set('0')
            varchoCoffeete.set('0')
            varTotal.set('0')

            varFryrice.set('0')
            varPasta.set('0')
            varSamosa.set('0')
            varSalad.set('0')
            varOmlet.set('0')

            varTea.set('0') 
            varCoffee.set('0') 
            varSprit.set('0')
            varfanta.set('0')
            varBottleWater.set('0')

            varVanillaCone.set('0')
            varVanillaShake.set('0')
            varStrawberryShake.set('0')

            varVAT.set("")
            varServiceCharge.set("0")
            varTotal.set("0")
            varChange.set("0")
            varSubTotal.set("0")
            varPayment.set("0")
            
            self.txtThukpa.configure(state = DISABLED)
            self.txtvegmomo.configure(state = DISABLED)
            self.txtchickenmomo.configure(state = DISABLED)
            self.txtVchowmein .configure(state = DISABLED)
            self.txtCchowmein.configure(state = DISABLED)
            self.txtBlackforest.configure(state = DISABLED)
            self.txtwhiteforest.configure(state = DISABLED)
            self.txtchoCoffeete.configure(state = DISABLED)
            self.txtFryrice.configure(state = DISABLED)
            self.txtPasta.configure(state = DISABLED)
            self.txtSamosa.configure(state = DISABLED)
            self.txtSalad.configure(state = DISABLED)
            self.txtOmlet.configure(state = DISABLED)
            self.txtTea.configure(state = DISABLED)
            self.txtCoffee.configure(state = DISABLED)
            self.txtSprit.configure(state = DISABLED)
            self.txtfanta.configure(state = DISABLED)
            self.txtBottleWater.configure(state = DISABLED)
            self.txtVanillaCone.configure(state = DISABLED)
            self.txtVanillaShake.configure(state = DISABLED)
            self.txtStrawberryShake.configure(state = DISABLED)
            self.txtChange.configure(state = DISABLED)
            self.txtServiceCharge.configure(state = DISABLED)
            self.txtSubTotal.configure(state = DISABLED)
            self.txtTotal.configure(state = DISABLED)
            var8.get() == 0

        def chkThukpa():
            if (var1.get() == 1):
                self.txtThukpa.configure(state = NORMAL)
                varThukpa.set("")
            elif(var1.get() ==0):
                self.txtThukpa.configure(state = DISABLED)
                varThukpa.set("0")

        def chkvegmomo():
            if (var2.get() == 1):
                self.txtvegmomo.configure(state = NORMAL)
                varvegmomo.set("")
            elif(var2.get() ==0):
                self.txtvegmomo.configure(state = DISABLED)
                varvegmomo.set("0")

        def chkchickenmomo():
            if (var3.get() == 1):
                self.txtchickenmomo.configure(state = NORMAL)
                varchickenmomo.set("")
            elif(var3.get() ==0):
                self.txtchickenmomo.configure(state = DISABLED)
                varchickenmomo.set("0")


        def chkVchowmein ():
            if (var4.get() == 1):
                self.txtVchowmein .configure(state = NORMAL)
                varVchowmein .set("")
            elif(var4.get() ==0):
                self.txtVchowmein .configure(state = DISABLED)
                varVchowmein .set("0")

        def chkCchowmein():
            if (var5.get() == 1):
                self.txtCchowmein.configure(state = NORMAL)
                varCchowmein.set("")
            elif(var5.get() ==0):
                self.txtCchowmein.configure(state = DISABLED)
                varCchowmein.set("0")

        def chkBlackforest():
            if (var6.get() == 1):
                self.txtBlackforest.configure(state = NORMAL)
                varBlackforest.set("")
            elif(var6.get() ==0):
                self.txtBlackforest.configure(state = DISABLED)
                varBlackforest.set("0")


        def chkwhiteforest():
            if (var7.get() == 1):
                self.txtwhiteforest.configure(state = NORMAL)
                varwhiteforest.set("")
            elif(var7.get() ==0):
                self.txtwhiteforest.configure(state = DISABLED)
                varwhiteforest.set("0")

        def chkchoCoffeete():
            if (var8.get() == 1):
                self.txtchoCoffeete.configure(state = NORMAL)
                varchoCoffeete.set("")
            elif(var8.get() ==0):
                self.txtchoCoffeete.configure(state = DISABLED)
                varchoCoffeete.set("0")

        def chkFryrice():
            if (var9.get() == 1):
                self.txtFryrice.configure(state = NORMAL)
                varFryrice.set("")
            elif(var9.get() ==0):
                self.txtFryrice.configure(state = DISABLED)
                varFryrice.set("0")


        def chkPasta():
            if (var10.get() == 1):
                self.txtPasta.configure(state = NORMAL)
                varPasta.set("")
            elif(var10.get() ==0):
                self.txtPasta.configure(state = DISABLED)
                varPasta.set("0")

        def chkSamosa():
            if (var11.get() == 1):
                self.txtSamosa.configure(state = NORMAL)
                varSamosa.set("")
            elif(var11.get() ==0):
                self.txtSamosa.configure(state = DISABLED)
                varSamosa.set("0")

        def chkSalad():
            if (var12.get() == 1):
                self.txtSalad.configure(state = NORMAL)
                varSalad.set("")
            elif(var12.get() ==0):
                self.txtSalad.configure(state = DISABLED)
                varSalad.set("0")


        def chkOmlet():
            if (var13.get() == 1):
                self.txtOmlet.configure(state = NORMAL)
                varOmlet.set("")
            elif(var13.get() ==0):
                self.txtOmlet.configure(state = DISABLED)
                varOmlet.set("0")

        def chkTea():
            if (var14.get() == 1):
                self.txtTea.configure(state = NORMAL)
                varTea.set("")
            elif(var14.get() ==0):
                self.txtTea.configure(state = DISABLED)
                varTea.set("0")

        def chkCoffee():
            if (var15.get() == 1):
                self.txtCoffee.configure(state = NORMAL)
                varCoffee.set("")
            elif(var15.get() ==0):
                self.txtCoffee.configure(state = DISABLED)
                varCoffee.set("0")


        def chkSprit():
            if (var16.get() == 1):
                self.txtSprit.configure(state = NORMAL)
                varSprit.set("")
            elif(var16.get() ==0):
                self.txtSprit.configure(state = DISABLED)
                varSprit.set("0")

        def chkfanta():
            if (var17.get() == 1):
                self.txtfanta.configure(state = NORMAL)
                varfanta.set("")
            elif(var17.get() ==0):
                self.txtfanta.configure(state = DISABLED)
                varfanta.set("0")

        def chkBottleWater():
            if (var18.get() == 1):
                self.txtBottleWater.configure(state = NORMAL)
                varBottleWater.set("")
            elif(var18.get() ==0):
                self.txtBottleWater.configure(state = DISABLED)
                varBottleWater.set("0")


        def chkVanillaCone():
            if (var19.get() == 1):
                self.txtVanillaCone.configure(state = NORMAL)
                varVanillaCone.set("")
            elif(var19.get() ==0):
                self.txtVanillaCone.configure(state = DISABLED)
                varVanillaCone.set("0")


        def chkVanillaShake():
            if (var20.get() == 1):
                self.txtVanillaShake.configure(state = NORMAL)
                varVanillaShake.set("")
            elif(var20.get() ==0):
                self.txtVanillaShake.configure(state = DISABLED)
                varVanillaShake.set("0")

        def chkStrawberryShake():
            if (var21.get() == 1):
                self.txtStrawberryShake.configure(state = NORMAL)
                varStrawberryShake.set("")
            elif(var21.get() ==0):
                self.txtStrawberryShake.configure(state = DISABLED)
                varStrawberryShake.set("0")
                
#=======================================Total================================================================================================================================================
        def Costofmeal():
            meal1 = float(varThukpa.get())
            meal2 = float(varvegmomo.get())
            meal3 = float(varchickenmomo.get())
            meal4 = float(varVchowmein .get())
            meal5 = float(varCchowmein.get())
            meal6 = float(varBlackforest.get())
            meal7 = float(varwhiteforest.get())
            meal8 = float(varchoCoffeete.get())
            meal9 = float(varFryrice.get())
            meal10 = float(varPasta.get())
            meal11 = float(varSamosa.get())
            meal12 = float(varSalad.get())
            meal13 = float(varOmlet.get())
            meal14 = float(varTea.get()) 
            meal15 = float(varCoffee.get()) 
            meal16 = float(varSprit.get())
            meal17 = float(varfanta.get())
            meal18 = float(varBottleWater.get())
            meal19= float(varVanillaCone.get())
            meal20= float(varVanillaShake.get())
            meal21= float(varStrawberryShake.get())


            iTotal1= ((meal1 * 50) + (meal2 * 60) + (meal3 * 80) + (meal4 * 60))
            iTotal2= ((meal5 * 80) + (meal6 * 60) + (meal7 * 70) + (meal8 * 50))
            iTotal3= ((meal9 * 80) + (meal10 * 70) + (meal11 * 60) + (meal12 * 50))
            iTotal4= ((meal13 * 25) + (meal14 * 20) + (meal15 * 30) + (meal16 * 50))
            iTotal5= ((meal17 * 50) + (meal18 * 25) + (meal19 * 80) + (meal20 * 80) + (meal21 * 80))

           
            if (var22.get() == "Cash"):
                iChange = float(varPayment.get())
                iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5)
                iServiceCharge = 10
                iServiceChargeq = str('%.2f'%(iServiceCharge))
                varServiceCharge.set(iServiceChargeq)

                iCostq =str('%.2f'%(iCost))
                varSubTotal.set(iCostq)
                iTotalq =str('%.2f'%(iCost + iServiceCharge))
                varTotal.set(iTotalq)
                cChange = (iChange - (iCost + iServiceCharge))
                cChangeq =str('%.2f'%(cChange))
                varChange.set(cChangeq)

            elif (var22.get() == 'Master Card' or 'Visa Card'or 'Debit Card'):
                varPayment.set("")
                iCost = (iTotal1 + iTotal2 + iTotal3 + iTotal4 + iTotal5)
                iServiceCharge = 10
                iServiceChargeq = str('%.2f'%(iServiceCharge))
                varServiceCharge.set(iServiceChargeq)
                iCostq =str('%.2f'%(iCost))
                varSubTotal.set(iCostq)
                iTotalq =str('%.2f'%(iCost + iServiceCharge))
                varTotal.set(iTotalq)
                varChange.set("")

#========================Frame 1 ============================================================================================================================================================

        self.lblMeal = Label(F1, font = ('arial', 18, 'bold'), text = " Fast Lunch veg. and nonveg.\n")
        self.lblMeal.grid(row = 0, column= 0)

        self.Thukpa = Checkbutton(F1, text="Thukpa\t\tRs.50",command=chkThukpa, variable=var1, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=1, column=0, sticky=W)
        self.txtThukpa = Entry(F1, font=('arial', 18,'bold'), textvariable = varThukpa, width=6, justify='right', state = DISABLED)
        self.txtThukpa.grid(row=1, column=1)

        self.vegmomo = Checkbutton(F1, text="Veg.momo\tRs.60",command=chkvegmomo, variable=var2, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=2, column=0, sticky=W)
        self.txtvegmomo = Entry(F1, font=('arial', 18,'bold'), textvariable = varvegmomo, width=6, justify='right', state = DISABLED)
        self.txtvegmomo.grid(row=2, column=1)

        self.chickenmomo = Checkbutton(F1, text="C.momo\t\tRs.80",command=chkchickenmomo, variable=var3, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=3, column=0, sticky=W)
        self.txtchickenmomo = Entry(F1, font=('arial', 18,'bold'), textvariable = varchickenmomo, width=6, justify='right', state = DISABLED)
        self.txtchickenmomo.grid(row=3, column=1)

        self.Vchowmein  = Checkbutton(F1, text="Veg.chowmein \tRs.60",command=chkVchowmein , variable=var4, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=4, column=0, sticky=W)
        self.txtVchowmein  = Entry(F1, font=('arial', 18,'bold'), textvariable = varVchowmein , width=6, justify='right', state = DISABLED)
        self.txtVchowmein .grid(row=4, column=1)

        self.Cchowmein = Checkbutton(F1, text="C.chowmein\tRs.80",command=chkCchowmein, variable=var5, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=5, column=0, sticky=W)
        self.txtCchowmein = Entry(F1, font=('arial', 18,'bold'), textvariable = varCchowmein, width=6, justify='right', state = DISABLED)
        self.txtCchowmein.grid(row=5, column=1)

        self.lblSandwich = Label(F1, font = ('arial', 20, 'bold'), text = "\nPastery\n")
        self.lblSandwich.grid(row = 6, column= 0)

        self.Blackforest = Checkbutton(F1, text="Black forest\tRs.60",command=chkBlackforest, variable=var6, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=7, column=0, sticky=W)
        self.txtBlackforest = Entry(F1, font=('arial', 18,'bold'), textvariable = varBlackforest, width=6, justify='right', state = DISABLED)
        self.txtBlackforest.grid(row=7, column=1)

        self.whiteforest = Checkbutton(F1, text="White forest\tRs.70",command=chkwhiteforest, variable=var7, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=8, column=0, sticky=W)
        self.txtwhiteforest = Entry(F1, font=('arial', 18,'bold'), textvariable = varwhiteforest, width=6, justify='right', state = DISABLED)
        self.txtwhiteforest.grid(row=8, column=1)

        self.choCoffeete = Checkbutton(F1, text="Chocolate\tRs.50",command=chkchoCoffeete, variable=var8, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=9, column=0, sticky=W)
        self.txtchoCoffeete = Entry(F1, font=('arial', 18,'bold'), textvariable = varchoCoffeete, width=6, justify='right', state = DISABLED)
        self.txtchoCoffeete.grid(row=9, column=1)

        self.lblspace  = Label(F1, text='\n\n\n\n\n\n\n')
        self.lblspace.grid(row= 10, column=0)

                        

#==================================Frame 2==================================================================================================================================================

        self.lblMeal = Label(F2TOP, font = ('arial', 18, 'bold'),bd = 6, text = "Fast Foods\n")
        self.lblMeal.grid(row = 0, column= 0)

        self.Fryrice = Checkbutton(F2TOP, text="Fry rice\t\t\tRs.80",command=chkFryrice, variable=var9, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=1, column=0, sticky=W)
        self.txtFryrice = Entry(F2TOP, font=('arial', 18,'bold'), textvariable = varFryrice, width=6, justify='right', state = DISABLED)
        self.txtFryrice.grid(row=1, column=1)

        self.Pasta = Checkbutton(F2TOP, text="Pasta\t\t\tRs.70",command=chkPasta, variable=var10, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=2, column=0, sticky=W)
        self.txtPasta = Entry(F2TOP, font=('arial', 18,'bold'), textvariable = varPasta, width=6, justify='right', state = DISABLED)
        self.txtPasta.grid(row=2, column=1)

        self.Samosa = Checkbutton(F2TOP, text="Samosa\t\t\tRs.60",command=chkSamosa, variable=var11, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=3, column=0, sticky=W)
        self.txtSamosa = Entry(F2TOP, font=('arial', 18,'bold'), textvariable = varSamosa, width=6, justify='right', state = DISABLED)
        self.txtSamosa.grid(row=3, column=1)

        self.Salad = Checkbutton(F2TOP, text="Salad\t\t\tRs.50",command=chkSalad, variable=var12, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=4, column=0, sticky=W)
        self.txtSalad = Entry(F2TOP, font=('arial', 18,'bold'), textvariable = varSalad, width=6, justify='right', state = DISABLED)
        self.txtSalad.grid(row=4, column=1)

        self.Omlet = Checkbutton(F2TOP, text="Omlet\t\t\tRs.25",command=chkOmlet, variable=var13, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=5, column=0, sticky=W)
        self.txtOmlet = Entry(F2TOP, font=('arial', 18,'bold'), textvariable = varOmlet, width=6, justify='right', state = DISABLED)
        self.txtOmlet.grid(row=5, column=1)

#=================================Frame 3====================================================================================================================================================



        self.lblMeal = Label(F3, font = ('arial', 18, 'bold'), text = "Drinks\n")
        self.lblMeal.grid(row = 0, column= 0)

        self.Tea = Checkbutton(F3, text="Tea\t     Rs.20",command=chkTea, variable=var14, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=1, column=0, sticky=W)
        self.txtTea = Entry(F3, font=('arial', 18,'bold'), textvariable = varTea, width=6, justify='right', state = DISABLED)
        self.txtTea.grid(row=1, column=1)

        self.Coffee = Checkbutton(F3, text="Coffee\t     Rs.30",command=chkCoffee, variable=var15, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=2, column=0, sticky=W)
        self.txtCoffee = Entry(F3, font=('arial', 18,'bold'), textvariable = varCoffee, width=6, justify='right', state = DISABLED)
        self.txtCoffee.grid(row=2, column=1)

        self.Sprit = Checkbutton(F3, text="Sprit\t     Rs.50",command=chkSprit, variable=var16, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=3, column=0, sticky=W)
        self.txtSprit = Entry(F3, font=('arial', 18,'bold'), textvariable = varSprit, width=6, justify='right', state = DISABLED)
        self.txtSprit.grid(row=3, column=1)

        self.fanta = Checkbutton(F3, text="fanta\t     Rs.50",command=chkfanta, variable=var17, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=4, column=0, sticky=W)
        self.txtfanta = Entry(F3, font=('arial', 18,'bold'), textvariable = varfanta, width=6, justify='right', state = DISABLED)
        self.txtfanta.grid(row=4, column=1)

        self.BottleWater = Checkbutton(F3, text="BottleWater Rs.25",command=chkBottleWater, variable=var18, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=5, column=0, sticky=W)
        self.txtBottleWater = Entry(F3, font=('arial', 18,'bold'), textvariable = varBottleWater, width=6, justify='right', state = DISABLED)
        self.txtBottleWater.grid(row=5, column=1)


        self.lblShakes= Label(F3, font=('arial', 20, 'bold'), text="\nShakes\n")
        self.lblShakes.grid(row=6, column=0)

        self.VanillaCone = Checkbutton(F3, text="Vanilla Cone\tRs.80",command=chkVanillaCone, variable=var19, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=7, column=0, sticky=W)
        self.txtVanillaCone = Entry(F3, font=('arial', 18,'bold'), textvariable = varVanillaCone, width=6, justify='right', state = DISABLED)
        self.txtVanillaCone.grid(row=7, column=1)

        self.VanillaShake = Checkbutton(F3, text="Vanilla Shake\tRs.80",command=chkVanillaShake, variable=var20, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=8, column=0, sticky=W)
        self.txtVanillaShake = Entry(F3, font=('arial', 18,'bold'), textvariable = varVanillaShake, width=6, justify='right', state = DISABLED)
        self.txtVanillaShake.grid(row=8, column=1)

        self.StrawberryShake = Checkbutton(F3, text="Strawberry Shake\tRs.80",command=chkStrawberryShake, variable=var21, onvalue=1, offvalue=0,font=('arial', 18,'bold')).grid(row=9, column=0, sticky=W)
        self.txtStrawberryShake = Entry(F3, font=('arial', 18,'bold'), textvariable = varStrawberryShake, width=6, justify='right', state = DISABLED)
        self.txtStrawberryShake.grid(row=9, column=1)

        self.lblspace=Label(F3, text="\n\n\n\n\n\n\n")

        self.lblspace.grid(row =10, column =0)

#===================================================F2BOTTOM=================================================================================================================================

        self.lblPaymentMethod= Label(F2BOTTOM, font=('arial', 14, 'bold'), text="Payment Method", bd=10,width=22 , anchor='w')
        self.lblPaymentMethod.grid(row=0, column=0)


        self.lblChange = Label(F2BOTTOM, font=('arial', 14, 'bold'), text="Change", bd=10, anchor="w")
        self.lblChange.grid(row=0, column=1)
        self.txtChange = Entry(F2BOTTOM,  font=('arial', 18, 'bold'), textvariable = varChange,justify='right', width=6, state= DISABLED)
        self.txtChange.grid(row=0, column=2)

        self.cmbPaymentMethod = ttk.Combobox(F2BOTTOM, textvariable = var22, state='readonly', font=('arial', 10, 'bold'), width=20)
        self.cmbPaymentMethod['value'] = ('Cash', 'Master Card', 'Visa Card', 'Debit Card')
        self.cmbPaymentMethod.current(0)
        self.cmbPaymentMethod.grid(row=1, column=0)


        self.lblServiceCharge = Label(F2BOTTOM, font=('arial', 14, 'bold'), text="S.charge", bd=10, anchor="w")
        self.lblServiceCharge.grid(row=1, column=1)
        self.txtServiceCharge = Entry(F2BOTTOM,  font=('arial', 18, 'bold'), textvariable = varServiceCharge, width=6,justify='right', state= DISABLED)
        self.txtServiceCharge.grid(row=1, column=2)

        self.txtPayment = Entry(F2BOTTOM, font=('arial', 14, 'bold'), textvariable = varPayment, width=6,justify='right')
        self.txtPayment.grid(row=2, column=0)




        self.lblSubTotal = Label(F2BOTTOM, font=('arial', 14, 'bold'), text="Sub Total", bd=10,width=8, anchor="w")
        self.lblSubTotal.grid(row=2, column=1)
        self.txtSubTotal = Entry(F2BOTTOM,  font=('arial', 14, 'bold'), textvariable = varSubTotal, width=7, justify='right', state= DISABLED)
        self.txtSubTotal.grid(row=2, column=2)


        self.lblTotal = Label(F2BOTTOM, font=('arial', 14, 'bold'), text="Total", bd=10, width=6, anchor="w")
        self.lblTotal.grid(row=3, column=1)
        self.txtTotal = Entry(F2BOTTOM,  font=('arial', 14, 'bold'), textvariable = varTotal, width=6, justify='right', state= DISABLED)
        self.txtTotal.grid(row=3, column=2)


#=======================Frame 2 BUTTON========================================================================================================================================================

        self.btnTotal = Button(F2BOTTOM,command = Costofmeal, padx=16, pady=1, bd=4,fg='black', font=('arial', 16, 'bold'), text="Total", width=5).grid(row=4, column=0)

        self.btnReset = Button(F2BOTTOM, padx=16, pady=1, bd=4,fg='black', font=('arial', 16, 'bold'), text="Reset", width=5,command = Reset).grid(row=4, column=1)

        self.btnExit = Button(F2BOTTOM, padx=16, pady=1, bd=4, fg='black', font=('arial', 16, 'bold'), text="Exit", width=5, command = lambda:iExit()).grid(row=4, column=2)
                               

        self.lblspace  = Label(F2BOTTOM, text='     \n\n\n\n\n\n\n')
        self.lblspace.grid(row= 5, column=0)
        
       

if __name__=='__main__':
    t=Tk()
    application = Customer(t)
    t.mainloop()
