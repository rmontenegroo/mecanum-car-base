from pyPS4Controller.controller import Controller

class PSController(Controller):

    def __init__(self, device, guest, **kwargs):
        Controller.__init__(self, interface=device, **kwargs)
        self._guest = guest
        self._guest.start()


    def shutdown(self):
        self._guest.stop()

