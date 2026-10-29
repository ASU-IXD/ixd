# A Room That Feels the Weather: Data-Driven Interior in Omniverse

In this tutorial you will build an interior room whose ceiling fan spins with the outdoor wind and whose lights change color with the outdoor temperature, using two datasets, two NVIDIA assets, one imported model and two short scripts written with the help of AI.

## Files in this folder

[Here](https://drive.google.com/drive/folders/1lAnIDaTni9AU_m00xp9uHZHKqEDYK7ey?usp=sharing) are the files

| File | What it is |
| --- | --- |
| connect_ceiling_fan.py | Connects a dataset to the ceiling fan's spin |
| connect_room_lights_temperature.py | Connects temperature to the color of every light in the room |
| DataSet/ | `wind_december.csv`, `temperature_december.csv`, and the June versions of both |
| Interior_Scene.usdz | External Asset |
| DemoOutput/ | An example of the output |

## What you'll build

Two objects in one room, each driven by one column of outdoor data. One hour of data plays as one second of animation, so a full day takes 24 seconds.

| Object | Dataset | Column | What changes |
| --- | --- | --- | --- |
| Ceiling fan (NVIDIA asset) | `wind_december.csv` | `speed_ms` | The blades spin faster when it's windier, and stop when the wind drops below 2.5 m/s |
| Room lights, including the floor lamp (NVIDIA asset) | `temperature_december.csv` | `temp_c` | The light color moves from blue (cold) through yellow and orange to red (super hot) |

The data is a typical December day in Phoenix, not real measurements. The same scripts work with any day that has the same columns, including the June files.

<img width="335" height="237" alt="image" src="https://github.com/user-attachments/assets/1c043b6e-7672-4109-921b-5771bd8fd9fb" />

<img width="1131" height="350" alt="image" src="https://github.com/user-attachments/assets/c16729e0-02fe-4c27-bc7a-834b05509b75" />

## How AI will help write the code

The working scripts were written with an AI assistant.

**What made the difference:**

- Say who the code is for ("students who don't code/ beginners") and what must stay in the interface.
- Ask for the smallest script, with everything you might change in one settings block at the top.
- Send screenshots of the Stage panel and the console when something breaks.
- Change one thing per round, run it, then report what happened.
- When an object keeps fighting the data, try a simpler object before writing more code.

## Part 1: Build the room
<img width="1920" height="1080" alt="Capture 0000" src="https://github.com/user-attachments/assets/97f3ca2b-4184-48b9-91a9-7f50123d9f8d" />


Build an interior in Omniverse as you normally would, then bring in two NVIDIA assets from the **NVIDIA Assets** tab of the Content browser: a **ceiling fan** and a **floor lamp**.

Check two things in the Stage panel, because the scripts depend on them:

1. **The fan's spinning part.** Expand `CeilingFan`. The blades live inside a mesh called `Hub`. Right-click it → *Copy Prim Path*, for example `/World/CeilingFan/Hub`.

<img width="610" height="128" alt="image" src="https://github.com/user-attachments/assets/f2165793-e612-484b-84f5-08cc26da3965" />

2. **The lights.** Expand the lamp. It contains a `SphereLight`. Any other lights in your room count too. Note the path of the group that holds them all, for example `/World/Interior_Scene`.

<img width="614" height="169" alt="image" src="https://github.com/user-attachments/assets/6c5a7c7d-6636-447f-ab46-78c0770f22b0" />

Lower or hide the dome light so the room is fairly dark; colored light shows much better that way.

## Part 2: The data

Put both files in `C:\omniverse\data_world\data\` and open them in Excel first, so you know the numbers before you see them in 3D. Each has one row per hour, 0 to 23.

| File | Columns | Example row (3 pm) |
| --- | --- | --- |
| `wind_december.csv` | `hour`, `speed_ms` (wind speed, m/s), `direction_deg` (not used here) | 15, 4.9, 235 |
| `temperature_december.csv` | `hour`, `temp_c` (°C) | 15, 19.0 |

Before running anything, predict: when will the fan start turning, and what color will the room be at 7 am?

## Part 3: Wind makes the fan spin

Set the timeline to 24 fps, frames 0 to 552. Open **Window → Script Editor**, paste in `connect_ceiling_fan.py`, check the settings block, and click **Run**.

```python
DATA_FILE = "wind_december.csv"        # which dataset drives the fan
COLUMN    = "speed_ms"                 # which column in that file
FAN       = "/World/CeilingFan/Hub"    # the part that spins (hub + blades)
SPIN_AXIS = "Z"                        # the axis it spins around: "X", "Y" or "Z"
START_AT  = 2.5                        # below this value the fan is off
SPEED     = 60                         # how fast it spins for each unit of data
```

## Part 4: Temperature colors the lights

Paste `connect_room_lights_temperature.py` into the Script Editor. Set `ROOM` to the group that holds your lights, then click **Run**.

```python
DATA_FILE = "temperature_december.csv"     # which day's temperatures
ROOM      = "/World/Interior_Scene"        # every light inside this will change color
```

The script finds every light inside `ROOM` by itself and prints each one it connected, so you can check none were missed. Each hour's temperature becomes a color on this scale, keyed on the light's **color**:

| Temperature | Color |
| --- | --- |
| 5 °C and below | Blue (cold) |
| 20 °C | Yellow (medium) |
| 32 °C | Orange (hotter) |
| 42 °C and above | Red (super hot) |

Between those temperatures the colors blend smoothly. The script also turns off each light's built-in color temperature setting, which would otherwise override the data color.

## Part 5: Play the day

Press **Play**. The room now behaves according to the weather outside: a cold, calm winter morning, a breezy afternoon, a cooling evening.

| Frame | Time | Outside | Fan | Lights |
| --- | --- | --- | --- | --- |
| 0 | Midnight | 11.8 °C, calm | Off | Blue-grey |
| 168 | 7 am | 7 °C, calm | Off | Blue, the coldest hour |
| 288 | Noon | 15 °C, wind 2.5 m/s | Starts turning slowly | Between blue and yellow |
| 360 | 3 pm | 19 °C, wind 4.9 m/s | Fastest | Yellow, the warmest hour |
| 456 | 7 pm | 17 °C, wind 1.7 m/s | Stops | Fading back toward blue |

[Here](https://drive.google.com/file/d/15EUBuBPHdqXZOBC6uY_H2-PKMxf-UQee/view?usp=sharing) is how the Demo looks like

Now switch seasons: change `DATA_FILE` to `wind_june.csv` and `temperature_june.csv` in the two scripts and run them again. The summer room glows orange to red all day, and the fan runs from late morning well into the evening.

<img width="1920" height="1080" alt="Capture 0062" src="https://github.com/user-attachments/assets/b4b9c671-1ca3-4a5b-9abd-4b58c2049a65" />
<img width="1920" height="1080" alt="Capture 0195" src="https://github.com/user-attachments/assets/7f5fa988-ff59-464c-bc69-a83c841ebfe2" />
<img width="1920" height="1080" alt="Capture 0375" src="https://github.com/user-attachments/assets/536b9205-e55a-4c24-bbc0-7002c4bc9640" />

## Connect your own object with AI

Pick one more object in your room and one column of data, and use an AI assistant to connect them. Ideas: curtains that sway with wind speed, a window glow that brightens with sunlight, a thermostat display that changes color with temperature.

Start with this prompt and fill in the blanks:

```text
I'm working in NVIDIA Omniverse and running Python in the Script Editor.
I don't code, so keep the script as short and readable as possible.

- Object: ________ at the path /World/________ (copied from the Stage panel)
- Property to change: ________ (for example rotation, color, scale, light intensity)
- Data: a CSV at C:\omniverse\data_world\data\________.csv with columns hour, ________

Set one keyframe per hour at frame hour × 24.
Put everything I might change in a settings block at the top.
Clear old keyframes before writing new ones.
Ask me questions first if anything is unclear.
```


## Troubleshooting

| Problem | Fix |
| --- | --- |
| Red console error mentioning `NoneType` or "invalid prim" | A path in the settings block doesn't match. Copy it again from the Stage panel |
| Fan blades tumble or flip | Change `SPIN_AXIS` to `"Y"` (or `"X"`) and run again |
| Fewer lights listed in the console than you expected | A light sits outside the `ROOM` group. Use a higher group, such as `/World` |
| Lights change color but look white | Raise the light's **Intensity** and darken the room |
| The bulb glass stays white | The bulb mesh has its own material; ask the AI to color it too, with a screenshot of the lamp's Looks folder |
| `KeyError` in the console | A CSV column name doesn't match exactly |
| File not found | Put the CSVs in `C:\omniverse\data_world\data\` or change `DATA` in the script |
| An imported model won't behave | It may have its own animation or skeleton. Try a simpler or NVIDIA asset first |
