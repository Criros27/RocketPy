
from rocketpy import Environment, SolidMotor, Rocket, Flight

env = Environment(latitude=43.63871944444445, longitude=-116.2413513485235, elevation=1430)

import datetime

tomorrow = datetime.date.today() + datetime.timedelta(days=1)

env.set_date(
    (tomorrow.year, tomorrow.month, tomorrow.day, 12)
)  # Hour given in UTC time

env.set_atmospheric_model(type="Forecast", file="GFS")

env.info()

#L2375 = SolidMotor(
#    thrust_source="data/motors/Cesaroni_4864L2375-P.eng",
#    dry_mass=1.839,
#    dry_inertia=(0.125, 0.125, 0.002), #incognita 
#    nozzle_radius= 33 / 1000, #incognita
#    grain_number=3,     #I
#    grain_density=1815,   
#    grain_outer_radius=27 / 1000,
#    grain_initial_inner_radius=15 / 1000,
#    grain_initial_height=320 / 1000,
#    grain_separation=5 / 1000,      #I
#    grains_center_of_mass_position=0.397,  #incognita
#    center_of_dry_mass_position=0.317,    #incognita
#    nozzle_position=0,  #incognita
#    burn_time=1.9,
#    throat_radius=11 / 1000,
#    coordinate_system_orientation="nozzle_to_combustion_chamber",
#)

#L2375.info()

L1350 = SolidMotor(
    thrust_source="data/motors/Cesaroni_4263L1350-P.eng",
    dry_mass=1.546,
    dry_inertia=(0.125, 0.125, 0.002), #incognita 
    nozzle_radius= 33 / 1000, #incognita
    grain_number=3,     #I
    grain_density=1815,   
    grain_outer_radius=75 / 2000,
    grain_initial_inner_radius=15 / 2000,
    grain_initial_height=490 / 3000, #OR
    grain_separation=5 / 1000,      #Incognita
    grains_center_of_mass_position=0.397,  #OR
    center_of_dry_mass_position=0.317,    #OR
    nozzle_position=0,  #OR
    burn_time=3.28, #I
    throat_radius=11 / 1000,
    coordinate_system_orientation="nozzle_to_combustion_chamber",
)

L1350.info()

#power_on_drag = "data/calisto/powerOnDragCurve.csv"
#power_off_drag = "data/calisto/powerOffDragCurve.csv"
drag_minerva = "data/minerva/Mach_cd_Minerva.csv"

Minerva = Rocket(
    radius=102 / 2000, #OR
    mass=7.227,    #OR
    inertia=(4.078, 4.078, 0.015),  #OR
    power_off_drag=drag_minerva,
    power_on_drag=drag_minerva,
    center_of_mass_without_motor=0,  #OR
    coordinate_system_orientation="tail_to_nose",
)
Minerva.power_off_drag()

Minerva.add_motor(L1350, position=-1.02 )

#da chiedere 
rail_buttons = Minerva.set_rail_buttons(
    upper_button_position=0.0818,
    lower_button_position=-0.6182,
    angular_position=45,
)

nose_cone = Minerva.add_nose(
    length=0.38, kind="lvhaack", position=1.38  #OR
)

fin_set = Minerva.add_trapezoidal_fins(
    n=4,
    root_chord=0.18,    #OR
    tip_chord=0.0275,    #OR
    span=0.105,     #OR
    position=-0.79,     #OR
    cant_angle=0,
    #airfoil=("data/calisto/NACA0012-radians.csv","radians"),
)

tail = Minerva.add_tail(
    top_radius=0.0102, bottom_radius=0.008, length=0.0436, position=-0.9764
)       #OR

main = Minerva.add_parachute( # 8m/s
    name="main",
    cd_s=0.8*3.0643, # cd_s è cd*area    #OR
    trigger=400,      # ejection altitude in meters  
    sampling_rate= 105,
    lag=2,
    noise=(0, 8.3, 0.5),
)

drogue = Minerva.add_parachute( # 30m/s
    name="drogue",
    cd_s=0.8*0.2828,   #OR
    trigger="apogee",  # ejection at apogee
    sampling_rate=105,
    lag=2,
    noise=(0, 8.3, 0.5),
)

Minerva.plots.static_margin()

test_flight = Flight(
    rocket=Minerva, environment=env, rail_length=5, inclination=85, heading=0
    )

test_flight.speed.plot(0, test_flight.apogee_time)

test_flight.speed.source

test_flight.all_info()
test_flight.info()