

# Importing `.obj` file into NVIDIA Omniverse

This guide demonstrates how to import an external **`.obj`** model into NVIDIA Omniverse, convert it to the USD format, and apply textures to the imported asset.

---

# Overview

NVIDIA Omniverse uses **OpenUSD (Universal Scene Description)** as its native file format. While assets such as `.obj`, `.fbx`, and `.gltf` can be imported directly, converting them to USD allows for better compatibility and editing within Omniverse.

In this tutorial, you will:

- Import an `.obj` model.
- Convert it to a USD asset.
- Apply textures to the imported model.

---

# Importing an OBJ File

1. Open your Omniverse project.
2. Navigate to the location of your `.obj` model.
<img width="568" height="476" alt="image" src="https://github.com/user-attachments/assets/cef11845-0a81-407c-97e0-27ecdec40503" />

---

# Convert the OBJ File to USD

After importing the `.obj` file:

1. Right-click the imported object.
2. Select **Convert to USD**.
<img width="473" height="387" alt="image" src="https://github.com/user-attachments/assets/08abd0d4-c8ed-40d6-80d5-be468bd423c3" />

3. Keep the default conversion settings.
4. Enter a name for the new USD file.
5. Leave the remaining options as their default values.
6. Click **Convert**.
<img width="402" height="481" alt="image" src="https://github.com/user-attachments/assets/699e1173-23f6-411e-aa16-9676b3474eeb" />

Once the conversion is complete, the object will appear in your scene as a USD asset.

> **Note:** The imported model may appear without textures. This is expected because texture files are not always automatically assigned during the import process.
<img width="1875" height="766" alt="image" src="https://github.com/user-attachments/assets/9982a1e6-657e-4008-aa80-8fdcc3985a70" />

---

# Applying Textures

If the model appears without textures, you can manually assign them.

## Step 1: Locate the Material

1. Open the **Stage** panel.
2. Expand the imported object.
3. Locate the **Looks** folder.
4. Expand the **Looks** folder.

This folder contains the materials associated with the object.

---

## Step 2: Locate the Texture Files

Navigate to the folder containing your model files.

Most downloaded models include a **Materials** folder that contains:

- Diffuse (Albedo) textures
- Normal maps
- Roughness maps
- Metallic maps
- Other texture files

---

## Step 3: Assign the Albedo Texture

1. Select the material inside the **Looks** folder.
2. Open the **Properties** panel.
3. Locate the **Albedo Map** parameter.
4. Drag and drop the main texture image from the **Materials** folder into the **Albedo Map** placeholder.

Once assigned, the texture should immediately appear on the object in the viewport.

<img width="1838" height="917" alt="image" src="https://github.com/user-attachments/assets/e6b2047e-17f5-469b-969b-3f3e5919d33b" />

---

# Expected Result

After completing these steps, you should have:

- Successfully imported an external `.obj` model.
- Converted the model into the USD format.
- Applied the object's primary texture manually.
- Verified that the textured model appears correctly in the Omniverse viewport.

---

# Importing FBX Files

The same workflow can be used to import **`.fbx`** files into NVIDIA Omniverse.

1. Drag and drop the `.fbx` file into your Omniverse scene.
2. Right-click the imported object and select **Convert to USD**.
3. Keep the default conversion settings.
4. Enter a name for the USD file.
5. Click **Convert**.

Unlike `.obj` files, **`.fbx` files support animations**. If the imported model contains animation data, the animations will be preserved during the conversion to USD.

After the conversion is complete:

1. Select the imported USD object.
2. Click the **Play** button on the timeline.
3. Verify that the model's animations play correctly in the viewport.

> **Note:** If the model includes materials and textures, they may need to be assigned manually depending on how the original FBX file was exported.
