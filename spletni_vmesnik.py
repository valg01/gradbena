import bottle
from model import Hisa, Prostor, Delo

IME_DATOTEKE = "stanje.json"
try:
    moj_model = Hisa.preberi_iz_dat(IME_DATOTEKE)
except:
    moj_model = Hisa("")

@bottle.get("/")
def osnovna_stran():
    return bottle.template("osnovna_stran.tpl", neopravljena=moj_model.skupno_stevilo_neopravljenih(), zamujena=moj_model.skupno_stevilo_zamujenih())

bottle.run(reloder=True, debug=True)
