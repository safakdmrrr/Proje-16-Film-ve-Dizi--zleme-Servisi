import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QLabel, QListWidget, QMessageBox
class Film:
    def __init__(self, adı, yönetmeni, türü):
        self.adı = adı
        self.yönetmeni = yönetmeni
        self.türü = türü

class Kullanıcı:
    def __init__(self, kullanıcı_adı, şifre):
        self.kullanıcı_adı = kullanıcı_adı
        self.şifre = şifre
        self.izleme_geçmişi = []

    def izleme_geçmişi_ekle(self, film):
        self.izleme_geçmişi.append(film)

class İçerik:
    def __init__(self, adı, süresi, türü):
        self.adı = adı
        self.süresi = süresi
        self.türü = türü

class İzlemeServisi:
    def __init__(self):
        self.filmler = []
        self.kullanıcılar = []

    def film_ekle(self, film):
        self.filmler.append(film)

    def kullanıcı_ekle(self, kullanıcı):
        self.kullanıcılar.append(kullanıcı)

class FilmEklePencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Film Ekle")
        self.setGeometry(200, 200, 300, 250)

        layout = QVBoxLayout()

        self.label_film_adı = QLabel("Film Adı:", self)
        layout.addWidget(self.label_film_adı)

        self.edit_film_adı = QLineEdit(self)
        layout.addWidget(self.edit_film_adı)

        self.label_yönetmen = QLabel("Yönetmen:", self)
        layout.addWidget(self.label_yönetmen)

        self.edit_yönetmen = QLineEdit(self)
        layout.addWidget(self.edit_yönetmen)

        self.label_tür = QLabel("Tür:", self)
        layout.addWidget(self.label_tür)

        self.edit_tür = QLineEdit(self)
        layout.addWidget(self.edit_tür)

        film_ekle_button = QPushButton("Film Ekle", self)
        film_ekle_button.clicked.connect(self.film_ekle)
        layout.addWidget(film_ekle_button)

        self.setLayout(layout)

    def film_ekle(self):
        film_adı = self.edit_film_adı.text()
        yönetmen = self.edit_yönetmen.text()
        tür = self.edit_tür.text()

        # Burada film eklenmesi işlemleri gerçekleştirilebilir
        print("Film Eklendi:", film_adı, yönetmen, tür)
        self.edit_film_adı.clear()
        self.edit_yönetmen.clear()
        self.edit_tür.clear()

class AnaPencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.eklenen_filmler = []

    def init_ui(self):
        self.setWindowTitle("Film ve Dizi İzleme Servisi")
        self.setGeometry(100, 100, 400, 400)

        layout = QVBoxLayout()

        film_ekle_button = QPushButton("Film Ekle", self)
        film_ekle_button.clicked.connect(self.film_ekle_pencere_ac)
        layout.addWidget(film_ekle_button)

        listele_button = QPushButton("Filmleri Listele", self)
        listele_button.clicked.connect(self.filmleri_listele)
        layout.addWidget(listele_button)

        self.liste_widget = QListWidget(self)
        layout.addWidget(self.liste_widget)

        izle_button = QPushButton("İçerik İzle", self)
        izle_button.clicked.connect(self.icerik_izle)
        layout.addWidget(izle_button)

        self.setLayout(layout)

    def film_ekle_pencere_ac(self):
        self.film_ekle_pencere = FilmEklePencere()
        self.film_ekle_pencere.show()

    def filmleri_listele(self):
        self.liste_widget.clear()
        for film in self.eklenen_filmler:
            self.liste_widget.addItem(f"{film.adı} - {film.yönetmeni} - {film.türü}")

    def icerik_izle(self):
        secilen_filmler = self.liste_widget.selectedItems()
        if not secilen_filmler:
            QMessageBox.warning(self, "Uyarı", "İzlemek için bir film seçiniz.")
        else:
            secilen_film = secilen_filmler[0].text()
            QMessageBox.information(self, "İzleme Başladı", f"{secilen_film} izleniyor...")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pencere = AnaPencere()
    pencere.show()
    sys.exit(app.exec_())
