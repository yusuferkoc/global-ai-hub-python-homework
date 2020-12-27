adb="globalai"
soyadb="hub" 
dersler=["JS","python","kubernetes","ML","ai"]
notlar={
    "midterm":50,
    "final":0,
    "project":0
}
secilen=[]
def giris():
    deneme=3
    while deneme > 0:
        ad=input()
        soyad=input()
        if adb != ad or soyadb != soyadb:
            print("yanlış tekrar deneyin")
            deneme-=1
        else:
            correct=True
            print("hoşgeldin",adb)
    print("daha sonra tekrar dene")

def ders_liste():
    i=0
   
    for ders in dersler:
        i+=1
        print(i,"-",ders)
        
def ders_al():
    ds=0
    while ds < 3:
        print("Kaç ders alacaksınız (en az 3)")
        ds=int(input())

    for ds in range(ds):
        print("ders numarası girin")
        sd=int(input())
        secilen.append(sd)
        ds-=1

    print("hangi dersten sınav oldunuz")
    yd=int(input())

def notlandirma():
    m=notlar["midterm"]
    f=notlar["final"]
    p=notlar["project"]
    res=m*30/100+f*50/100+p*20/100
    print("midterm:",m,"final:",f,"project:",p)
    print(res)

    if res >= 90:
        print("your grade:AA")
    elif res>=70 and res<90:
        print("your grade:BB")
    elif res>=50 and res<70:
        print("your grade:CC")
    elif res>=30 and res<50:
        print("your grade:DD")
    elif res<30:
        print("Fail")


def main():
    ders_liste()
    ders_al()
    notlandirma()
     
    

if __name__ == "__main__":
    main()