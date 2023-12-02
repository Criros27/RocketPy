import numpy as np

from ..mathutils.function import Function
from ..prints.parachute_prints import _ParachutePrints
"possiamo adattare il prints anche agli aerofreni, facciamogliela prima implementare a loro"

class Airbrakes:
    
    def __init__(
        self,
        airbrakes_cd,
        airbrakes_area,
        lookup_table,
        n,
        noise=(0, 0, 0)
    ):
        """Initializes Airbreakes class.

        Parameters
        ----------
        
        cd_a : float
            Drag coefficient as a function of Mach and aerofreni's percentage of estraction.
        trigger : callable, float, str
            This parameter defines the trigger condition for the aerofreni
            ejection system.

        #da vedere

        sampling_rate : float
            Sampling rate in which the parachute trigger will be checked at.
            It is used to simulate the refresh rate of onboard sensors such
            as barometers. Default value is 100. Value must be given in hertz.

        noise : tuple, list, optional
            List in the format (mean, standard deviation, time-correlation).
            The values are used to add noise to the pressure signal which is
            passed to the trigger function. Default value is (0, 0, 0). Units
            are in pascal.
        Returns
        -------
        None
        """
        self.name = "Airbreakes"
        self.airbrakes_cd = airbrakes_cd
        self.airbrakes_area = airbrakes_area
        self.n = n
        self.lookup_table = "lookuptable" #da implementare path


        ### ATTENZIONE ###
        """
        # noise del paracadute, vediamo se alla fine di tutto dopo aver implementato
        # gli aerofreni riusciamo anche a far passare qualceh piccolo disturbo nel
        # calcolo del metodo.
        # VERIFICARE PRIMA che il disturbo non sia già stato implementato GLOBALMENTE
        # sul cd totale del razzo
        """
        self.noise_signal = [[-1e-6, np.random.normal(noise[0], noise[1])]]
        self.noisy_pressure_signal = []
        self.clean_pressure_signal = []
        self.noise_bias = noise[0]
        self.noise_deviation = noise[1]
        self.noise_corr = (noise[2], (1 - noise[2] ** 2) ** 0.5)
        self.clean_pressure_signal_function = Function(0)
        self.noisy_pressure_signal_function = Function(0)
        self.noise_signal_function = Function(0)

        alpha, beta = self.noise_corr
        self.noise_function = lambda: alpha * self.noise_signal[-1][
            1
        ] + beta * np.random.normal(noise[0], noise[1])
        "sta definendo una funzione anonima lambda"
        self.prints = _ParachutePrints(self)

        # evaluate the trigger
        trigger = True #per far runnare
        if callable(trigger):
            self.triggerfunc = trigger
        """
        elif isinstance(trigger, (int,float)):
            def triggerfunc(p, h, y):
                # p = pressure considering parachute noise signal
                # h = height above ground level considering parachute noise signal
                # y = [x, y, z, vx, vy, vz, e0, e1, e2, e3, w1, w2, w3]
                return True if y[5] < 0 and h < trigger else False

            self.triggerfunc = triggerfunc
        """
        """
        qui sta dicendo che se il trigger è chiamabile lo definisce, altrimenti se
        non è chiamabile (trigger non rilevato) verifica le condizioni di emergenza
        del trigger, come ad esempio l'altezza o la velocità segnate
        e se sono verificate, forza il trigger
        
        
        """
        
        return None
        

    def __str__(self):
        """Returns a string representation of the Airbreakes class.

        Returns
        -------
        string
            String representation of Airbreakes class. It is human readable.
        """
        return "Airbreakes {} with a cd_a of {:.4f} m2".format(
            self.name.title(),
            self.airbrakes_cd,
        )

    def info(self):
        """Prints information about the Airbreakes class."""
        self.prints.all()

        return None

    def all_info(self):
        """Prints all information about the Airbreakes class."""
        self.info()
        # self.plots.all() # Airbreakes still doesn't have plots

        return None
    
    def airbrakes_area_update():
        pass
    def airbrakes_cd_update():
        pass
