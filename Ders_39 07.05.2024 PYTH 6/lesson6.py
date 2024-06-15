
# class Penguen():
#     # Class atribut:
#     sinif = "Quş"



#     # Instance atribut:
#     #     kralPinqivin, Kral Pinqivin 
#     def _init_(self, ad, yas, reng, ):
#         self.ad = ad
#         self.yas = yas
#         self.reng = reng
       


#     def uze_bilme(self):
#         return f"{self.ad} uze bilir"
    

#     def mahni_oxuya_bilme(self, mahni_oxuya_bilme = False):
#         if mahni_oxuya_bilme == True:
#             return f"{self.ad} mahni oxuya bilir"
#         else:
#             return f"{self.ad} mahni oxuya bilmir"
         

#     def reqs_ede_bilme(self, reqs_ede_bilme = False):
#         if reqs_ede_bilme == True:
#             return f"{self.ad} reqs ede bilir"
#         else:
#             return f"{self.ad} reqs ede bilmir"
        
  
    
    

    

# # Obyetkler:  
# kralPinqivin = Penguen("Kral Pinqivin", 4, "Qara")
# sariPinqivin = Penguen("Sari Pinqivin", 2, "Sari")
# neseliAyaklar = Penguen("Neşeli ayaklar", 5, "Ağ")



class Masin() :
    sinif = "Sedan"


    # Mercedes , BMW  , Audi , Kia , Hyundai

    def _init_(self, ad, il, reng, motor, ölke , suretler_qutusu):
        self.ad = ad
        self.il = il
        self.reng = reng
        self.motor = motor
        self.ölke = ölke
        self.suretler_qutusu = suretler_qutusu




    def sedandir (self):
        return f"{self.ad} sedandir"
    

    def alman_istehsalı(self, alman_istehsalı = False):
        if alman_istehsalı == True:
            return f"{self.ad} Almanya istehsalıdır"
        else:
            return f"{self.ad} Koreya istehsalıdır"
         

    def cip (self, cip = False):
        if cip == True:
            return f"{self.ad} 4x4 dür"
        else:
            return f"{self.ad} 4x4 deyil"



# Obyetkler:  

BMW = Masin("BMW", "2001", "Qara", "2.5" , "Almaniya", "Avtomat")
Mercedes = Masin("Mercedes", "2000", "Qara", "3.0" , "Almaniya", "Avtomat")
Audi = Masin("Audi", "2020", "Boz", "4.4" , "Almaniya", "Avtomat")
Kia = Masin("Kia", "2022", "Qara", "2.0" , "Koreya", "Avtomat")
Hyundai = Masin("Hyundai", "2024", "Qara", "2.5" , "Koreya", "Avtomat")


