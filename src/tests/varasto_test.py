import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.epakelpo_varasto = Varasto(-1)
        self.varasto2 = Varasto(10, -1)
        self.varasto3 = Varasto(10, 11)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_tekee_nollatun_varaston_kun_tilavuus_negatiivinen(self):
        self.assertAlmostEqual(self.epakelpo_varasto.tilavuus, 0) #testi korjattu taas toimivaksi

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_varastolla_oikea_saldo_kun_annettu_saldo_negatiivinen(self):
        self.assertAlmostEqual(self.varasto2.saldo, 0)

    def test_varastolla_oikea_saldo_kun_annettu_saldo_yli_kapasiteetin(self):
        self.assertAlmostEqual(self.varasto3.saldo, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_liikaa_saldoa(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_negatiivinen_luku(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.lisaa_varastoon(-2)
        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_otetaan_yli_saldon(self):
        self.varasto.lisaa_varastoon(5)
        maara = self.varasto.ota_varastosta(7)
        self.assertAlmostEqual(maara, 5)

    def test_otetaan_negatiivinen_maara(self):
        self.varasto.lisaa_varastoon(5)
        maara = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(maara, 0)

    def test_oikea_tulostus(self):
        self.varasto.lisaa_varastoon(5)
        mj = "saldo = 5, vielä tilaa 5"
        self.assertAlmostEqual(mj, str(self.varasto))

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
