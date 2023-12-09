
from rocketpy import Environment, SolidMotor, Rocket, Flight

env = Environment(latitude=32.990254, longitude=-106.974998, elevation=1400)

import datetime

tomorrow = datetime.date.today() + datetime.timedelta(days=1)

env.set_date(
    (tomorrow.year, tomorrow.month, tomorrow.day, 12)
)  # Hour given in UTC time

env.set_atmospheric_model(type="Forecast", file="GFS")

env.info()

L2375 = SolidMotor(
    thrust_source="data/motors/Cesaroni_4864L2375-P.eng",
    dry_mass=1.839,
    dry_inertia=(0.125, 0.125, 0.002), #incognita 
    nozzle_radius= 33 / 1000, #incognita
    grain_number=4,     #I
    grain_density=1815,   
    grain_outer_radius=27 / 1000,
    grain_initial_inner_radius=15 / 1000,
    grain_initial_height=320 / 1000,
    grain_separation=5 / 1000,      #I
    grains_center_of_mass_position=0.397,  #incognita
    center_of_dry_mass_position=0.317,    #incognita
    nozzle_position=0,  #incognita
    burn_time=1.9,
    throat_radius=11 / 1000,
    coordinate_system_orientation="nozzle_to_combustion_chamber",
)

L2375.info()

power_off_drag_completo = "data/calisto/powerOffDragCurve.csv"

Minerva = Rocket(
    radius=102 / 2000, #OR
    mass=7.718,    #OR
    inertia=(5.138, 5.138, 0.022),  #OR
    power_off_drag=power_off_drag_completo,
    power_on_drag="data/calisto/powerOnDragCurve.csv",
    center_of_mass_without_motor=0,  #OR
    coordinate_system_orientation="tail_to_nose",
)
Minerva.power_off_drag()

Minerva.add_motor(L2375, position=2.22795 )

#da chiedere 
rail_buttons = Minerva.set_rail_buttons(
    upper_button_position=0.0818,
    lower_button_position=-0.6182,
    angular_position=45,
)

nose_cone = Minerva.add_nose(
    length=0.38, kind="lvhaack", position=1.465  #OR
)

fin_set = Minerva.add_trapezoidal_fins(
    n=4,
    root_chord=0.36,    #OR
    tip_chord=0.070,    #OR
    span=0.120,     #OR
    position=-0.53,     #OR
    cant_angle=0.5,
    #airfoil=("data/calisto/NACA0012-radians.csv","radians"),
)

tail = Minerva.add_tail(
    top_radius=0.0102, bottom_radius=0.008, length=0.0436, position=-1.0825
)       #OR

main = Minerva.add_parachute(
    name="main",
    cd_s=1.4,   #OR
    trigger=800,      # ejection altitude in meters  
    sampling_rate= 105,
    lag=1.5,
    noise=(0, 8.3, 0.5),
)

drogue = Minerva.add_parachute(
    name="drogue",
    cd_s=0.80,   #OR
    trigger="apogee",  # ejection at apogee
    sampling_rate=105,
    lag=1.5,
    noise=(0, 8.3, 0.5),
)

Minerva.plots.static_margin()

test_flight = Flight(
    rocket=Minerva, environment=env, rail_length=5.2, inclination=85, heading=0
    )

test_flight.speed.plot(0, test_flight.apogee_time)

test_flight.speed.source

#test_flight.all_info()