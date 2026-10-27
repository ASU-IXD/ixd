import csv, math, omni.usd
from pxr import Gf, Sdf, UsdGeom, UsdShade

stage = omni.usd.get_context().get_stage()
DATA = r"A:\PathToTheFolderWhichHasData"
SUN_DISTANCE = 1500


# =============================================================
#   CHANGE THESE 4 LINES FOR A DIFFERENT DAY
# =============================================================
SUN_FILE         = "sun_december.csv"            # sun data for the day
TEMPERATURE_FILE = "temperature_december.csv"    # temperature data for the day
# =============================================================


def read(file):
    return list(csv.DictReader(open(DATA + "\\" + file, encoding="utf-8-sig")))


# -------------------------------------------------------------
# SUN DATA  ->  sun sphere POSITION
# -------------------------------------------------------------
sun = stage.GetPrimAtPath("/World/Sun").GetAttribute("xformOp:translate")
sun.Clear()                                                 # remove any old keyframes first
points = []

for row in read(SUN_FILE):
    hour      = float(row["hour"])
    elevation = math.radians(float(row["elevation_deg"]))   # how high the sun is
    azimuth   = math.radians(float(row["azimuth_deg"]))     # which direction it is

    x =  math.cos(elevation) * math.sin(azimuth) * SUN_DISTANCE     # east / west
    y =  math.sin(elevation) * SUN_DISTANCE                         # up / down
    z = -math.cos(elevation) * math.cos(azimuth) * SUN_DISTANCE     # north / south

    sun.Set(Gf.Vec3d(x, y, z), hour * 24)                   # one keyframe per hour
    points.append(Gf.Vec3d(x, y, z))


# -------------------------------------------------------------
# TEMPERATURE DATA  ->  building material COLOR
# -------------------------------------------------------------
BLUE   = Gf.Vec3f(0.15, 0.40, 0.90)    # cold
YELLOW = Gf.Vec3f(0.95, 0.85, 0.25)    # medium
ORANGE = Gf.Vec3f(0.95, 0.50, 0.10)    # hotter
RED    = Gf.Vec3f(0.80, 0.08, 0.08)    # super hot

def mix(a, b, amount):
    return a + (b - a) * amount

def temperature_color(c):
    if c <= 5:  return BLUE
    if c <= 20: return mix(BLUE,   YELLOW, (c - 5)  / 15)   #  5 °C -> 20 °C
    if c <= 32: return mix(YELLOW, ORANGE, (c - 20) / 12)   # 20 °C -> 32 °C
    if c <= 42: return mix(ORANGE, RED,    (c - 32) / 10)   # 32 °C -> 42 °C
    return RED

color = UsdShade.Shader(stage.GetPrimAtPath("/World/Looks/BuildingMaterial/Shader")).CreateInput(
    "diffuseColor", Sdf.ValueTypeNames.Color3f)
color.GetAttr().Clear()                                     # remove any old keyframes first

for row in read(TEMPERATURE_FILE):
    hour = float(row["hour"])
    color.Set(temperature_color(float(row["temp_c"])), hour * 24)   # one keyframe per hour
