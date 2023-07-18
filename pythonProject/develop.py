import turtle
import time

# Turtle ekranını ayarla
wn = turtle.Screen()
wn.title("Sayac")
wn.bgcolor("white")
wn.setup(width=800, height=600)

# Turtle nesnesini oluştur
pen = turtle.Turtle()
pen.speed(1)  # Sayacın hızını ayarla

# Sayacı ekrana yazdır
for i in range(30, -1, -1):
    pen.clear()  # Önceki sayıyı temizle
    pen.write(i, align="center", font=("Courier", 24, "normal"))
    time.sleep(1)  # 1 saniye bekle

wn.mainloop()
