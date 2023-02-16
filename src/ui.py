from tkinter import *
from src.ema import GetEma
from src.kccontrol import KCT, KCM
from threading import Thread
from time import sleep
from datetime import datetime
import sys, os


class Run():
    def __init__(self, frame):
        self.parent = frame
        self.status = False
        self.Run()
        self.parent.mainloop()
    def Run(self):
        self.parent.title("Kucoin Trade")
        self.parent.wm_iconbitmap('./images/icon.ico')
        self.parent.resizable(0, 0)
        self.parent.call('tk', 'scaling')
        self.frame1 = LabelFrame(self.parent, text="Account:")
        self.frame1.grid(row=0, column=0, sticky="nsew")

        self.apiKeyLabel = Label(self.frame1, text="API Key:", anchor='w', width=20)
        self.apiKeyLabel.grid(row=0, column=0, columnspan=2, padx = 5, pady = 5, sticky="nsew")
        self.apiKey = StringVar(value='')
        self.inputApiKey= Entry(self.frame1, width=50,textvariable=self.apiKey)
        self.inputApiKey.grid(row=0, column=2, columnspan=4, padx = 5, pady = 5, sticky="nsew")

        self.apiSecretLabel = Label(self.frame1, text="API Secret:", anchor='w', width=20)
        self.apiSecretLabel.grid(row=1, column=0, columnspan=2, padx = 5, pady = 5, sticky="nsew")
        self.apiSecret = StringVar(value='')
        self.inputApiSecret= Entry(self.frame1, width=50,textvariable=self.apiSecret)
        self.inputApiSecret.grid(row=1, column=2, columnspan=4, padx = 5, pady = 5, sticky="nsew")

        self.apiPassLabel = Label(self.frame1, text="API Passphrase:", anchor='w', width=20)
        self.apiPassLabel.grid(row=2, column=0, columnspan=2, padx = 5, pady = 5, sticky="nsew")
        self.apiPass = StringVar(value='')
        self.inputApiPass= Entry(self.frame1, width=50,textvariable=self.apiPass)
        self.inputApiPass.grid(row=2, column=2, columnspan=4, padx = 5, pady = 5, sticky="nsew")

        self.frame2 = LabelFrame(self.parent, text="Trade:")
        self.frame2.grid(row=1, column=0, sticky="nsew")

        self.pairsLabel = Label(self.frame2, text="Pair:", anchor='w', width=10)
        self.pairsLabel.grid(row=0, column=0, columnspan=2, padx = 5, pady = 5, sticky="nsew")
        self.pairs= StringVar(value="XBTUSDTM")
        self.inputPairs= Entry(self.frame2,textvariable=self.pairs, width=10)
        self.inputPairs.grid(row=0, column=2, columnspan=2, padx = 5, pady = 5, sticky="nsew")

        self.amountLabel = Label(self.frame2, text="Select Amount:", anchor='w', width=20)
        self.amountLabel.grid(row=0, column=4, columnspan=2, padx = 5, pady = 5, sticky="nsew")
        self.amount = StringVar(value="10")
        self.inputAmount= Entry(self.frame2,textvariable=self.amount, width=10)
        self.inputAmount.grid(row=0, column=6, columnspan=2, padx = 5, pady = 5, sticky="nsew")

        self.leverageLabel = Label(self.frame2, text="Leverage:", anchor='w', width=10)
        self.leverageLabel.grid(row=1, column=0, columnspan=2, padx = 5, pady = 5, sticky="nsew")
        self.leverage = StringVar(value="100")
        self.inputLeverage= Entry(self.frame2,textvariable=self.leverage, width=10)
        self.inputLeverage.grid(row=1, column=2, columnspan=2, padx = 5, pady = 5, sticky="nsew")

        self.intervalLabel = Label(self.frame2, text="Interval (minutes):", anchor='w', width=10)
        self.intervalLabel.grid(row=1, column=4, columnspan=2, padx = 5, pady = 5, sticky="nsew")
        self.interval = IntVar(value=1)
        self.inputInterval= Entry(self.frame2,textvariable=self.interval, width=10)
        self.inputInterval.grid(row=1, column=6, columnspan=2, padx = 5, pady = 5, sticky="nsew")

        self.lengthLabel = Label(self.frame2, text="Length Ema (Max 200):", anchor='w', width=20)
        self.lengthLabel.grid(row=2, column=0, columnspan=2, padx = 5, pady = 5, sticky="nsew")
        self.length = IntVar(value=200)
        self.inputLength= Entry(self.frame2,textvariable=self.length, width=10)
        self.inputLength.grid(row=2, column=2, columnspan=2, padx = 5, pady = 5, sticky="nsew")

        self.tpLabel = Label(self.frame2, text="Take Profit (%):", anchor='w', width=20)
        self.tpLabel.grid(row=3, column=0, columnspan=2, padx = 5, pady = 5, sticky="nsew")
        self.tp = IntVar(value=10)
        self.inputTp= Entry(self.frame2,textvariable=self.tp, width=10)
        self.inputTp.grid(row=3, column=2, columnspan=2, padx = 5, pady = 5, sticky="nsew")

        self.slLabel = Label(self.frame2, text="Stop Loss (%):", anchor='w', width=20)
        self.slLabel.grid(row=3, column=4, columnspan=2, padx = 5, pady = 5, sticky="nsew")
        self.sl = IntVar(value=10)
        self.inputSl= Entry(self.frame2,textvariable=self.sl, width=10)
        self.inputSl.grid(row=3, column=6, columnspan=2, padx = 5, pady = 5, sticky="nsew")

        self.frame4 = LabelFrame(self.parent, text="Detail:")
        self.frame4.grid(row=2, column=0, sticky="nsew")

        self.highLabel = Label(self.frame4, text="Ema High:", anchor='w', width=20)
        self.highLabel.grid(row=0, column=0, columnspan=2, padx = 5, pady = 5, sticky="nsew")
        self.emaHigh = Label(self.frame4, text="0", anchor='w', width=10)
        self.emaHigh.grid(row=0, column=2, columnspan=2, padx = 5, pady = 5, sticky="nsew")

        self.lowLabel = Label(self.frame4, text="Ema Low:", anchor='w', width=20)
        self.lowLabel.grid(row=0, column=4, columnspan=2, padx = 5, pady = 5, sticky="nsew")
        self.emaLow = Label(self.frame4, text="0", anchor='w', width=10)
        self.emaLow.grid(row=0, column=6, columnspan=2, padx = 5, pady = 5, sticky="nsew")

        self.pricerLabel = Label(self.frame4, text="Current:", anchor='w', width=20)
        self.pricerLabel.grid(row=1, column=0, columnspan=2, padx = 5, pady = 5, sticky="nsew")
        self.currentPrice = Label(self.frame4, text="0", anchor='w', width=10)
        self.currentPrice.grid(row=1, column=2, columnspan=2, padx = 5, pady = 5, sticky="nsew")

        self.statusLabel = Label(self.frame4, text="Status:", anchor='w', width=20)
        self.statusLabel.grid(row=1, column=4, columnspan=2, padx = 5, pady = 5, sticky="nsew")
        self.statusText = Label(self.frame4, text="Relax", anchor='w', width=10)
        self.statusText.grid(row=1, column=6, columnspan=2, padx = 5, pady = 5, sticky="nsew")
        

        self.frame3 = Frame(self.parent, relief=RAISED)
        self.frame3.grid(row=3, column=0, sticky="nsew")

        self.stopButton = Button(self.frame3, text="Stop", bg='#ff3131', width=15, command=self.Stop)
        self.stopButton.grid(row=0, column=0, padx = (235,5), pady = 5, sticky="nsew")

        self.startButton = Button(self.frame3, text="Start", bg='#5bc810', width=15, command=self.Start)
        self.startButton.grid(row=0, column=1, padx = 5, pady = 5, sticky="nsew")

        self.frame_5 = LabelFrame(self.parent, text="Log:")
        self.frame_5.grid(row=4, column=0, columnspan=3, sticky="nsew")

        self.textarea = Text(self.frame_5, width=57, height=10)
        #self.textarea.grid(side=LEFT, padx=10, pady=10)
        self.textarea.grid(row=0, column=0, columnspan=3, sticky="nsew", padx=5, pady=5)
        self.textarea.tag_config('n', foreground="black")
        self.textarea.tag_config('r', foreground="red")
        self.textarea.tag_config('g', foreground="green")
        self.textarea.tag_config('p', foreground="purple")

        scrollbar = Scrollbar(self.frame_5,command=self.textarea.yview)
        scrollbar.grid(row=0, column=3, sticky='nsew')
        self.textarea['yscrollcommand'] = scrollbar.set


    def CheckFail(self):
        excType, excObj, excTb = sys.exc_info()
        fname = os.path.split(excTb.tb_frame.f_code.co_filename)[1]
        err = str(excType) + "---" + str(fname) + "---" +str(excTb.tb_lineno)
        status = str(err)
        print(status)

    def Log(self, message, type="n"):
        time = datetime.now().strftime("%H:%M:%S")
        message = time + ": " + message
        self.textarea.insert(END, message, type)
        self.textarea.see(END)

    def Trade(self):
        apiKey = self.apiKey.get()
        apiSecret = self.apiSecret.get()
        apiPass = self.apiPass.get()
        pair = self.pairs.get()
        amount = self.amount.get()
        leverage = self.leverage.get()
        interval = self.interval.get()
        emaLength = self.length.get()
        tp = self.tp.get()
        sl = self.sl.get()
        listOrderId = []
        kct = KCT(apiKey, apiSecret, apiPass)
        kcm = KCM()
        hiPoint = 0
        loPoint = 0
        tickSize = KCM().GetTickSize(pair)
        while self.status:
            try:
                if len(listOrderId) < 1:
                    df = kcm.GetKlineData(pair, interval)
                    hiPoint, loPoint = GetEma(df, emaLength)
                    self.emaHigh["text"] = hiPoint
                    self.emaLow["text"] = loPoint
                    currentPrice = kcm.GetCurrentPrice(pair)
                    self.currentPrice["text"] = currentPrice
                    checkOrder = False
                    if currentPrice > hiPoint:
                        placePoint = hiPoint - hiPoint%tickSize
                        orderId = kct.CreateLimit(pair, "sell", leverage, amount, placePoint)
                        type = 0
                        tp = hiPoint*90/100
                        sl = hiPoint*110/100
                        self.Log(f"Place {orderId} sell order at {placePoint}, tp: {tp}, sl: {sl}", "g")
                        checkOrder = True
                    elif currentPrice < loPoint:
                        placePoint = hiPoint - hiPoint%tickSize
                        orderId = kct.CreateLimit(pair, "buy", leverage, amount, placePoint)
                        type = 1
                        tp = loPoint*110/100
                        sl = loPoint*90/100
                        self.Log(f"Place {orderId} buy order at {placePoint}, tp: {tp}, sl: {sl}", "g")
                        checkOrder = True
                    if checkOrder:
                        listOrderId = [orderId,type,tp,sl]
                else:
                    currentPrice = kcm.GetCurrentPrice(pair)
                    self.currentPrice["text"] = currentPrice
                    if type == 1:
                        if currentPrice >= tp:
                            kct.CancelOrderByID(listOrderId[0])
                            self.Log(f"TP {listOrderId[0]} at {listOrderId[2]}", "g")
                        elif currentPrice <= sl:
                            kct.CancelOrderByID(listOrderId[0])
                            self.Log(f"SL {listOrderId[0]} at {listOrderId[3]}", "r")
                    elif type==0:
                        if currentPrice <= tp:
                            kct.CancelOrderByID(listOrderId[0])
                            self.Log(f"TP {listOrderId[0]} at {listOrderId[2]}", "g")
                        elif currentPrice >= sl:
                            kct.CancelOrderByID(listOrderId[0])
                            self.Log(f"SL {listOrderId[0]} at {listOrderId[3]}", "r")
            except Exception as e:
                self.Log(str(e), "r")
                self.statusText["text"] = "Stop"
                break
            sleep(3)
        self.statusText["text"] = "Stop"



    def Start(self):
        self.status = True
        self.statusText["text"] = "Running"
        Thread(target=self.Trade, daemon = True).start()


    def Stop(self):
        self.status = False