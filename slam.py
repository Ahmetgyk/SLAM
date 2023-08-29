from PIL import Image, ImageDraw

image_path = "beyaz_resim.png" 
image = Image.open(image_path)

width, height = 600, 600
red = (230, 30, 30)

image = Image.new("RGB", (width, height), "black")

image.putpixel((20, 25), red)

# İki noktanın koordinatları
start_point = (10, 20)  # İlk nokta (örnek olarak)
end_point = (500, 550)    # İkinci nokta (örnek olarak)

# Çizgi rengi
line_color = (255, 0, 0)  # Kırmızı (R: 255, G: 0, B: 0)

# Çizgiyi resimde çizme
draw = ImageDraw.Draw(image)
draw.line([start_point, end_point], fill=line_color, width=2)

# Çizginin geçtiği pikselleri ve noktaları renklendirme


image.putpixel(start_point, (255, 0, 0))  # İlk noktayı kırmızı yap
image.putpixel(end_point, (255, 0, 0))    # İkinci noktayı kırmızı yap

# Değiştirilmiş resmi görüntüleme veya kaydetme
image.show()

image.save("resim.png")