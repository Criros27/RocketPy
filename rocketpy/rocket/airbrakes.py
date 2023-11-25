import numpy as np

from ..mathutils.function import Function


class Airbrakes:

    def __init__(
        self,
        name,
        n,
        area,
        cd,
        lookup_table,
    ):
        """Initializes Airbrakes class."""

        self.name = name
        self.n = n
        self.area = area
        self.cd = cd
        self.lookup_table = Function(
            lookup_table,
            "Altitudine attuale",
            "Velocità attuale",
            "Estensione aerofreno"
            "Altitudine raggiunta con estensione aerofreno"
            "linear",
            "constant",
            )

        # evaluate the trigger
        if callable(trigger):
            self.triggerfunc = trigger
        elif isinstance(trigger, (int, float)):
            # trigger is the lookup table in csv format
            def triggerfunc(p, h, y):
                # p = pressure considering parachute noise signal
                # h = height above ground level considering parachute noise signal
                # y = [x, y, z, vx, vy, vz, e0, e1, e2, e3, w1, w2, w3
                if y[5] < 0 and h < trigger:
                    return self.area, self.cd

            self.triggerfunc = triggerfunc

        elif trigger == "apogee":
            # trigger for apogee
            def triggerfunc(p, h, y):
                # p = pressure considering parachute noise signal
                # h = height above ground level considering parachute noise signal
                # y = [x, y, z, vx, vy, vz, e0, e1, e2, e3, w1, w2, w3]
                return True if y[5] < 0 else False

            self.triggerfunc = triggerfunc

        return None

    def __str__(self):
        """Returns a string representation of the Airbrakes class.

        Returns
        -------
        string
            String representation of Airbrakes class. It is human readable.
        """
        return "Airbrakes {} with a cd of {:.4f} m2".format(
            self.name.title(),
            self.cd,
        )

    def info(self):
        """Prints information about the Airbrakes class."""
        self.prints.all()

        return None

    def all_info(self):
        """Prints all information about the Airbrakes class."""
        self.info()
        # self.plots.all() # Airbrakes still doesn't have plots

        return None
