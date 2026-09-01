# Working with Gaussian Splats in NVIDIA Omniverse

This guide explains how to convert a Gaussian Splat model from a `.ply` file to a `.usd` file so that it can be loaded and visualized in NVIDIA Omniverse.

---

# Reference Documentation

For more information about Gaussian Splats and Particle Fields in Omniverse, refer to the official NVIDIA documentation:

- [NVIDIA Omniverse Particle Fields Documentation](https://docs.omniverse.nvidia.com/materials-and-rendering/latest/particle-fields.html)

---

# Required Resources

Download all required resources from the shared Google Drive folder:

- [Gaussian Splats Resources](https://drive.google.com/drive/folders/1tYSxp_NKSJc28f25OMY3OITorigCVOaz?usp=drive_link)

The folder contains:

- A sample Gaussian Splat model (`flowers_1.ply`)
- `py3dgsPlyToUsd.py`, a Python script that converts a `.ply` file into a `.usd` file

---

# Converting a `.ply` File to `.usd`

After downloading the resources, place the `.ply` file and the conversion script in the same directory.

Open a terminal in that directory and execute:

```bash
python py3dgsPlyToUsd.py --input flowers_1.ply --output flowers_1.usd
```

This command:

- Reads the Gaussian Splat model (`flowers_1.ply`)
- Converts it into a USD file
- Creates a new file named `flowers_1.usd`

If the conversion is successful, you can import the generated `.usd` file into NVIDIA Omniverse.

---

# Importing into Omniverse

After the conversion is complete:

1. Launch **USD Composer** or another Omniverse Kit application.
2. Open the generated `flowers_1.usd` file.
3. Verify that the Gaussian Splat appears correctly in the viewport.

---

# Troubleshooting

## Error: `ModuleNotFoundError: No module named 'pxr'`

If you encounter the following error:

```text
ModuleNotFoundError: No module named 'pxr'
```

follow the steps below.

### Step 1: Verify Your Python Installation

Run the following commands:

```bash
where python
```

```bash
python --version
```

```bash
python -m pip --version
```

Verify that all commands point to the same Python installation.

---

### Step 2: Install the USD Python Package

Install the required package by running:

```bash
python -m pip install usd-core
```

---

### Step 3: Verify the Installation

Run the following command:

```bash
python -c "from pxr import Usd, UsdGeom, Vt, Gf, UsdVol; print('USD OK')"
```

If the installation was successful, you should see:

```text
USD OK
```

---

### Step 4: Convert the Gaussian Splat Again

Once the installation has been verified, run the conversion command again:

```bash
python py3dgsPlyToUsd.py --input flowers_1.ply --output flowers_1.usd
```

---

# Expected Output

After completing the conversion successfully, your directory should contain files similar to the following:

```text
flowers_1.ply
flowers_1.usd
py3dgsPlyToUsd.py
```

You can now open `flowers_1.usd` in NVIDIA Omniverse for visualization and further editing.
