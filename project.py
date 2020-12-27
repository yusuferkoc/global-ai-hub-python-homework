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
    counter=1
    while counter < 4:
        ad =input("adınızı girin:")
        soyad= input("soydınızı girin:")
        if (ad != adb and soyad!= soyadb ):
            print("hata tekrar deneyin")
            counter+=1
        elif (ad == adb and soyad!= soyadb):
            print("hata tekrar deneyin")
            counter+=1
        elif (ad != adb and soyad== soyadb):
            print("hata tekrar deneyin")
            counter+=1
        else: 
            print("Welcome ", ad)
            counter=5
            A=1
        if counter==4 :
            print("daha sonra tekrar dene")
            A=0
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
    giris()
    ders_liste()
    ders_al()
    notlandirma()
     
    

if __name__ == "__main__":
    main()