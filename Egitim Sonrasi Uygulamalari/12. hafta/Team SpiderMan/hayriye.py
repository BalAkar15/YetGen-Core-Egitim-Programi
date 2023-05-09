import pygame
# pygame modullerini kullanabilmek icin init() fonksiyonunu yazdik.
pygame.init()
# pencere boyutu
genislik = 1000
yukseklik = 600
screen = pygame.display.set_mode((genislik, yukseklik))
# pencere ismi
pygame.display.set_caption("Team Spiderman Games")
#######RENKLER#######
siyah = (0, 0, 0)
beyaz = (255, 255, 255)
kirmizi = (255, 0, 0)
yesil = (0, 255, 0)
mavi = (0, 0, 255)
sari = (255, 255, 0)
turuncu = (255, 165, 0)
mor = (128, 0, 128)
pembe = (255, 192, 203)
koyu_portakal = (255, 140, 0)
koyu_turkuaz = (0, 206, 209)
lavanta = (230, 230, 250)
sari_yesil = (173, 255, 47)
sarisin = (255, 255, 240)
orta_mor = (147, 112, 219)
acik_deniz_yesili = (32, 178, 170)
kahverengi = (240, 230, 140)
koyu_portakal_kirmizi = (220, 20, 60)
altin = (255, 215, 0)
acik_yesil = (144, 238, 144)
koyu_zeytin_yesili = (85, 107, 47)
gumus = (192, 192, 192)
orta_deniz_yesili = (60, 179, 113)
koyu_mavi = (0, 0, 139)

##BUTON SINIFI##
class Button:
    # butonumuz icin x ekseni, y ekseni, yukseklik, genislik, renk ve yazi 
    # parametrelerini sinifimiza dahil ettik
    def __init__(self, x, y, width, height, color, text):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
    # butonumuzu cizecek ve ana pencereye ekleyecek fonksiyonu yazdik. Burada surface degiskeni ile 
    # butonun cizilecegi pencereyi belirtecegiz.
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.Font(None, 64)
        text = font.render(self.text, True, siyah,gumus)
        text_rect = text.get_rect(center=self.rect.center)
        surface.blit(text, text_rect)
# ana ekranda oyuna baslayacagimiz play butonunu olusturduk
play_button = Button(250, 250, 500, 100, lavanta, "PLAY GAME")
#replay butonu
replay_button = Button(250, 350, 500, 100, gumus, "REPLAY GAME")
#########OYUNCU SINIFI####
class Oyuncu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('asker.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = 520
        self.rect.centerx = 350
        self.hiz = 10
        self.jump = False
        self.jumpC = 10  
    def update(self):
        tus = pygame.key.get_pressed()
        if tus[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.hiz
        elif tus[pygame.K_RIGHT] and self.rect.right < 1000:
            self.rect.x += self.hiz
        elif tus[pygame.K_UP] and self.rect.bottom > 400:
            self.rect.y -= self.hiz
        elif tus[pygame.K_DOWN] and self.rect.bottom < 600:
            self.rect.y += self.hiz
        if self.jump == False:
            if tus[pygame.K_SPACE]:
                self.jump = True
        else:
            if self.jumpC >= -10:
                self.rect.y -= (self.jumpC * abs(self.jumpC)) * 0.5
                self.jumpC -= 1
            else:
                self.jump = False
                self.jumpC = 10
                self.rect.bottom = 520
#kopek hareketi icin
kopekYon = 'left'
#puanlari saymasi icin bir puan degiskeni olusturduk.
point = 0
#oyuncu sinifimizdan bir karakter olusturduk
oyuncu = Oyuncu()
oyuncu_grup = pygame.sprite.Group()
oyuncu_grup.add(oyuncu)
fps = 60
saat = pygame.time.Clock()

############### ANA OYUN DONGUMUZ ###############
running = True
while running:
    # bu kod sayesinde eger oyun kapatilirsa dongu sonlanacak ve oyundan cikilacaktir.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # her dongude arka plan pembeye boyanacak.
    screen.fill(lavanta)
    # play butonunu cizdirdik
    play_button.draw(screen)
    #mouse pozisyonunu ve mouse basilip basilmadigi bilgilerini aldik
    mouse_pos = pygame.mouse.get_pos()
    mouse_pressed = pygame.mouse.get_pressed()
    # eger mouse play butonunun uzerindeyse ve mousenin sol tusuna iki kere basildiysa bu kod calisacak.
    # Amacimiz bu kod blogu calistiginda oyunun ilk penceresi calissin.

    if mouse_pressed[0] and play_button.rect.collidepoint(mouse_pos):
####### 1. PENCERE ##########
        kopek = pygame.image.load('dog.png')
        kopekC = kopek.get_rect()
        money = pygame.image.load('money.png')
        moneyC = money.get_rect()
        moneyC.bottom = 520
        moneyC.centerx = 650 
        kopekC.bottom = 520
        kopekC.centerx = 550 
        pencere1 = pygame.display.set_mode((genislik,yukseklik))
        arka_plan1 = pygame.image.load('pencere1.jpeg')
        
        running1 = True
        while running1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    running1 = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            pencere1.fill(siyah)
            pencere1.blit(arka_plan1,(0,0))
#kopek hareketi
            if kopekYon == 'right' and kopekC.x < 650:
                kopekC.x += 1
                if kopekC.x == 650:
                    kopekYon = 'left'
                    kopek = pygame.image.load('dog.png')
            elif kopekYon == 'left' and kopekC.x > 400:
                kopekC.x-= 1
                if kopekC.x == 400:
                    kopekYon = 'right'
                    kopek = pygame.image.load('dog2.png')
#Oyuncu kopege temas ederse
            if oyuncu.rect.colliderect(kopekC):
                font = pygame.font.SysFont("calibri", 64, True)
                yazi = font.render('GAME OVER!', True, siyah)
                yaziCd = yazi.get_rect()
                yaziCd.center = (genislik/2, yukseklik/2)
                
                pencere_go = pygame.display.set_mode((genislik,yukseklik))
                running_kopek = True
                while running_kopek:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            running1 = False
                            running_kopek = False
                    pencere_go.fill(kirmizi)
                    replay_button.draw(pencere_go)
                    mouse_pos = pygame.mouse.get_pos()
                    mouse_pressed = pygame.mouse.get_pressed()
                    pencere_go.blit(yazi,yaziCd)
                    if mouse_pressed[0] and replay_button.rect.collidepoint(mouse_pos):
                        oyuncu.rect.bottom = 520
                        oyuncu.rect.centerx = 350 
                        running1 = False
                        running_kopek = False
                    pygame.display.update()
#oyuncu paraya temas ederse    
            if oyuncu.rect.colliderect(moneyC):
                point += 1
                moneyC.topleft = (1100,700)
#skor yazisi    
            font = pygame.font.SysFont("calibri", 32, True)
            skor = font.render(f'SKOR : {point}', True, siyah,beyaz)
            SKORc = skor.get_rect()
            SKORc.topleft = (0,0)
            pencere1.blit(skor,SKORc)
            pencere1.blit(money,moneyC)
            pencere1.blit(kopek, kopekC)
            oyuncu_grup.draw(pencere1)
            oyuncu_grup.update()
            pygame.display.update()
            saat.tick(fps)
            if oyuncu.rect.x > 700:
############2. PENCERE KODLARI #######
                oyuncu.rect.bottom = 520
                oyuncu.rect.centerx = 100
                pencere2 = pygame.display.set_mode((genislik,yukseklik))
                arka_plan2 = pygame.image.load('pencere2.jpeg')
        
                running2 = True
                while running2:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            running1 = False
                            running2 = False

                    mouse_pos = pygame.mouse.get_pos()
                    mouse_pressed = pygame.mouse.get_pressed()
                    pencere2.fill(siyah)
                    pencere2.blit(arka_plan2,(0,0))

                    pencere2.blit(skor,SKORc)
                    oyuncu_grup.draw(pencere2)
                    oyuncu_grup.update()
                    pygame.display.update()
                    saat.tick(fps)
                    if oyuncu.rect.x > 900:
############ 3. PENCERE KODLARI #######
                        oyuncu.rect.bottom = 520
                        oyuncu.rect.centerx = 100
                        pencere3 = pygame.display.set_mode((genislik,yukseklik))
                        arka_plan3 = pygame.image.load('pencere3.jpeg')
        
                        running3 = True
                        while running3:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    running = False
                                    running1 = False
                                    running2 = False
                                    running3 = False

                            mouse_pos = pygame.mouse.get_pos()
                            mouse_pressed = pygame.mouse.get_pressed()
                            pencere3.fill(siyah)
                            pencere3.blit(arka_plan3,(0,0))

                            pencere3.blit(skor,SKORc)
                            oyuncu_grup.draw(pencere3)
                            oyuncu_grup.update()
                            pygame.display.update()
                            saat.tick(fps)
                            if oyuncu.rect.x > 900:
############4. PENCERE KODLARI ##########
                                oyuncu.rect.bottom = 520
                                oyuncu.rect.centerx = 100
                                pencere4 = pygame.display.set_mode((genislik,yukseklik))
                                arka_plan4 = pygame.image.load('pencere4.jpeg')
        
                                running4 = True
                                while running4:
                                    for event in pygame.event.get():
                                        if event.type == pygame.QUIT:
                                            running = False
                                            running1 = False
                                            running2 = False
                                            running3 = False
                                            running4 = False
                                    mouse_pos = pygame.mouse.get_pos()
                                    mouse_pressed = pygame.mouse.get_pressed()
                                    pencere4.fill(siyah)
                                    pencere4.blit(arka_plan4,(0,0))
                                    pencere4.blit(skor,SKORc)
                                    oyuncu_grup.draw(pencere4)
                                    oyuncu_grup.update()
                                    pygame.display.update()
                                    saat.tick(fps)
    pygame.display.update()

pygame.quit()