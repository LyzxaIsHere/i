import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.spinner import Spinner
from kivy.uix.image import Image
layout = FloatLayout()
class BrawlHackApp(App):
	def build(self):
		bg = Image(source = 'background.png', allow_stretch = True, keep_ratio = True, size_hint = (1, 1), pos = (0, 0))
		layout.add_widget(bg)
# Counter Sözlüğü -------------------------------------------------------------------
		self.counters = {"None": "Yok", "8-Bit": "Penny", "Alli": "Bull", "Amber": "Byron", "Angelo": "Nani", "Ash": "Cordelius", "Barley": "Mortis", "Bea": "Charlie", "Belle": "Mandy", "Berry": "Stu", "Bibi": "Bull", "Bo": "Stu", "Bonnie": "R-T", "Brock": "Piper", "Bull": "Otis", "Buster": "Mina", "Buzz": "Mina", "Byron": "Mandy", "Carl": "Buzz", "Charlie": "Sandy", "Chester": "Amber", "Chuck": "Cordelius", "Clancy": "Charlie", "Colette": "Bea", "Colt": "Gus", "Cordelius": "Mina", "Crow": "Spike", "Darryl": "Shelly", "Doug": "Lumi", "Draco": "Lou", "Dynamike": "Mortis", "Edgar": "Bull", "El Primo": "Griff", "Emz": "Kaze", "Eve": "Janet", "Fang": "Chester", "Finx": "Gus", "Frank": "Colette", "Gale": "Janet", "Gene": "Charlie", "Gray": "Byron", "Griff": "Stu", "Grom": "Kenji", "Gus": "Mandy", "Hank": "Dynamike","Jacky": "Bull", "Jae-Yong": "Bonnie", "Janet": "Kenji", "Jessie": "Berry", "Juju": "Cordelius", "Kaze": "Tara", "Kenji": "Bull", "Kit": "Frank", "Larry & Lowrie": "Kenji", "Leon": "Mina", "Lily": "Bull", "Lola": "Carl", "Lou": "Gus", "Lumi": "Mortis", "Maisie": "Stu", "Mandy": "Max", "Max": "Stu", "Meeple": "Kenji", "Meg": "Charlie", "Melodie": "Crow", "Mico": "Bull", "Mina": "Bea", "Moe": "Stu", "Mortis": "Bull", "Mr. P": "Kenji", "Nani": "Gene", "Nita": "Larry & Lowrie", "Ollie": "Charlie", "Otis": "Stu", "Pam": "Lumi", "Pearl": "R-T", "Penny": "Larry & Lowrie", "Piper": "Max", "Poco": "Kenji", "R-T": "Gus", "Rico": "Juju", "Rosa": "Primo", "Ruffs": "Amber", "Sam": "Surge", "Sandy": "Nita", "Shade": "Bull", "Shelly": "Nita", "Spike": "Carl", "Sprout": "Kenji", "Squeak": "Kenji", "Stu": "Poco", "Surge": "Tara", "Tara": "Sandy", "Tick": "Kenji", "Trunk": "Bull", "Willow": "Juju", "Ziggy": "Kenji" }
# Counter Label Kısmı Burasıdır------------------------------------------------------
		self.label = Label(text= "Counter Burada Yazacak.", color = (1, 1, 1, 1), pos_hint = {'x': 0.2, 'y': 0.4}, font_size = "30sp")
# Spinner Kısmı Burasıdır------------------------------------------------------------
		spinner = Spinner(text = "Karakter Seç", values=list(self.counters.keys()), pos_hint = {'x': 0.01, 'y': 0.91}, size_hint = (0.25, 0.1))

#Layout, Bind Kısmı Burasıdır--------------------------------------------------------
		
		spinner.bind(text=self.secim_yapildi)
		layout.add_widget(self.label)
		layout.add_widget(spinner)
		return layout
#Seçim Definition'ı Burasıdır--------------------------------------------------------
	def secim_yapildi (self, spinner, secilen):
		counter = self.counters.get(secilen, "Bulunamadı")
		self.label.text = f"{counter}"
#Uygulamayı Başlatma Komudu Buradadır-------------------------------------------------
BrawlHackApp().run()