import phone
import entertainment
import comm


class Smartphone(phone.Phone, entertainment.Entertainment, comm.Comm):
    def __init__(self, make, model, receiver, text, song):
        phone.Phone.__init__(self, make, model)
        comm.Comm.__init__(self, receiver, text)
        entertainment.Entertainment.__init__(self, song)
