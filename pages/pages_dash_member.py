from pages.base_page import BasePage
import time

class DashBoard(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.notifikasi_bttn = self.get_by_role("navigation").get_by_role("link", name="icon-notification Notifikasi")
        self.home_bttn = self.get_by_role("link", name="logo_bl_2.png")
        self.transfer_bttn = self.get_by_role("link", name="icon-transfer Transfer Transfer")
        self.reward_bttn = self.get_by_role("navigation").get_by_role("link", name="icon-reward Hadiah")
        self.redeem_bttn = self.get_by_role("button", name="Redeem")
        self.yes_bttn = self.get_by_role("button", name="Ya, Lanjutkan")
        self.id_card = self.get_by_text("HaiAjazz KuvlarBersama Poin - SIT305.000 pts")
        self.promo_card = self.get_by_text("Info & Promo SpesialLihat")
        self.produk_card = self.get_by_text("Produk Menarik Untuk KamuLihat Semua")
        self.lihat_bttn_atas = self.get_by_role("button", name="Lihat Semua")
        self.lihat_bttn_bawah = self.get_by_role("button", name="Lihat Semua").nth(1)