from pyPS4Controller.controller import Controller


class PSController(Controller):


    def __init__(self, device, guest, **kwargs):
        Controller.__init__(self, interface=device, **kwargs)
        self._guest = guest
        self._guest.start()


    def shutdown(self):
        self._guest.shutdown()


    def on_up_arrow_press(self):
        self._guest.moveForward()


    def on_down_arrow_press(self):
        self._guest.moveBackward()


    def on_up_down_arrow_release(self):
        self._guest.stop()


    def on_right_arrow_press(self):
        self._guest.strafeRight()


    def on_left_arrow_press(self):
        self._guest.strafeLeft()


    def on_left_right_arrow_release(self):
        self._guest.stop()


    def on_R2_press(self, value):
        self._guest.rotateRight()


    def on_R2_release(self):
        self._guest.stop()


    def on_L2_press(self, value):
        self._guest.rotateLeft()

    
    def on_L2_release(self):
        self._guest.stop()
