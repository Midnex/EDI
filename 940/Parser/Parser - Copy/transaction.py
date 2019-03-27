class Transaction():

    def __init__(self, id, dcNum,
                 storeNum, addressPrimary,
                 addressSecondary,
                 city, state, zip, carrier,
                 service, scac, units,
                 upc, sku):
        self.id = id
        self.dcNum = dcNum
        self.storeNum = storeNum
        self.addressPrimary = addressPrimary
        self.addressSecondary = addressSecondary
        self.city = city
        self.state = state
        self.zip = zip
        self.carrier = carrier
        self.service = service
        self.scac = scac
        self.units = units
        self.upc = upc
        self.sku = sku