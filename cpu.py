try:
    import psutil
except ImportError:
    exit("This library requires the psutil module\nInstall with: sudo pip install psutil")

from dot3k.menu import MenuOption

class GraphCPU(MenuOption):
    """
    A simple "plug-in" example, this gets the CPU load
    and draws it to the LCD when active
    """

    def __init__(self, backlight=None):
        self.backlight = backlight
        self.cpu_samples = [0, 0, 0, 0, 0]
        self.cpu_avg = 0
        self.last = self.millis()
        MenuOption.__init__(self)

    def redraw(self, menu):
        now = self.millis()
        if now - self.last < 1000:
            return false

        self.cpu_samples.append(psutil.cpu_percent())
        self.cpu_samples.pop(0)
        self.cpu_avg = sum(self.cpu_samples) / len(self.cpu_samples)

        self.cpu_avg = round(self.cpu_avg * 100.0) / 100.0

        menu.write_row(0, 'Mem: ' + str(psutil.virtual_memory().percent))
        menu.write_row(1, 'CPU: ' + str(self.cpu_avg) + '%')
        menu.write_row(2, '#' * int(16 * (self.cpu_avg / 100.0)))

        if self.backlight is not None:
            self.backlight.set_graph(self.cpu_avg / 100.0)

    def left(self):
        if self.backlight is not None:
            self.backlight.set_graph(0)
        return False
