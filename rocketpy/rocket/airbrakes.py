import numpy as np

from ..mathutils.function import Function


class Airbrakes:

    def __init__(
        self,
        name,
        n,
        area, # per singolo petalo al 100% in m^2
        cd_table, # per singolo petalo
        lookup_table
    ):
        """Initializes Airbrakes class."""

        self.name = name
        self.n = n
        self.area = area
        self.cd_table = Function(
            cd_table,
            "Mach",
            "Velocità",
            "Estensione percentuale"
            "Cd singolo petalo"
            "linear",
            "constant",
            )
        self.lookup_table = Function(
            lookup_table,
            "Altitudine attuale",
            "Velocità attuale",
            "Estensione aerofreno"
            "Altitudine raggiunta con estensione aerofreno"
            "linear",
            "constant",
            )

    def airbrakes_trigger(self, current_velocity, current_altitude, target_altitude): # da rivedere

        """
        Returns the airbrakes total cd given velocity and altitude of the rocket
        """

        cd = 0.5 # test, poi va preso dalla lookup table
        current_airbrakes_cd = 3*cd # ho messo 3 perchè self.n da "'Airbrakes' has no attribute 'n'"

        return current_airbrakes_cd

    def __str__(self):
        """Returns a string representation of the Airbrakes class.

        Returns
        -------
        string
            String representation of Airbrakes class. It is human readable.
        """
        return "Airbrakes {} with a cd of {:.4f}".format(
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
