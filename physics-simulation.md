# Physics Simulation in NVIDIA Omniverse

This guide introduces the fundamentals of physics simulation in NVIDIA Omniverse. You will learn how to enable physics, create rigid body simulations, convert solid objects into liquid using particle systems, build a conveyor belt, and create a simple falling leaves animation using physics.

---

# Prerequisites

Before starting this tutorial, ensure that you have:

- NVIDIA Omniverse USD Composer installed
- Basic knowledge of creating and manipulating objects in Omniverse

---

# Enable Physics

Physics functionality is provided through the **omni.physx.bundle** extension.

## Step 1: Enable the Physics Extension

1. Open **Developer → Extensions**.
2. Search for:

```
omni.physx.bundle
```

3. Enable the extension.

---

# Creating a Basic Physics Simulation

This example demonstrates rigid body physics and gravity.

## Step 1: Create the Ground

1. Create a mesh that will act as the ground plane.
2. Select the mesh.
3. Click the **Eye** icon in the viewport.
4. Select:

```
Show By Type
    → Physics
        → Colliders
            → Selected
```

You should now see the collider represented by **pink outlines** around the mesh.

---

## Step 2: Add a Falling Object

1. Create another mesh (for example, a cube or sphere).
2. Position it above the ground.
3. Select the object.
4. Add a **Dynamic Collider**.

Press **Play** on the timeline.

The object should fall onto the ground due to gravity.

---

# Solid to Liquid Simulation

Omniverse allows rigid meshes to be converted into particle-based liquids.

## Step 1: Convert a Mesh into Particles

1. Select the mesh.
2. Right-click the mesh.
3. Choose:

```
Add
    → Particle Sampler
```

This converts the mesh into particles.

---

## Step 2: Enable Particle Isosurface

1. Select the **Particle System**.
2. Click:

```
Add
    → Physics
        → Particle Isosurface
```

---

## Step 3: Create a Particle Material

1. Navigate to:

```
Create
    → Physics
        → Material
```

2. Create a **PBD Particle Material**.

---

## Step 4: Modify Material Properties

Select the newly created particle material and change:

- **Friction:** `0.1`

---

## Step 5: Assign the Material

1. Select the **Particle System**.
2. Assign the newly created **PBD Particle Material**.

---

## Step 6: Simulate

Press **Play**.

The particles now behave like a liquid.

To better visualize the liquid:

- Hide the original mesh.
- Hide the particle set.
- Leave the particle isosurface visible.

---

# Creating a Conveyor Belt

This example demonstrates surface velocity for moving objects.

## Step 1: Create the Belt

1. Add a conveyor belt model or create a cube that will act as the belt.
2. Place several objects on top of the belt.

---

## Step 2: Add Physics

Select the belt mesh.

On the **Property** panel:

```
+ Add
    → Physics
        → Rigid Body with Colliders Preset
```

---

## Step 3: Configure the Rigid Body

Under the **Physics** section, change:

- **Kinematic Enabled:** On
- **Velocities in Local Space:** On

---

## Step 4: Add Surface Velocity

With the belt still selected:

```
+ Add
    → Physics
        → Surface Velocity
```

---

## Step 5: Configure Surface Velocity

Set:

- **Surface Linear Velocity**
  - **Y:** `20`

Save the scene.

Press **Play**.

The conveyor belt will move backward, causing the objects to fall off.

---

## Step 6: Reverse the Belt Direction

Change:

- **Surface Linear Velocity**
  - **Y:** `-20`

Save the scene.

Press **Play** again.

The objects now move correctly along the conveyor belt.

You can repeat these steps for additional conveyor belt sections.

---

# Falling Leaves Simulation

This example demonstrates a simple physics-based falling leaves animation.

## Step 1: Add the Tree

1. Import the **Maple Tree** asset from the NVIDIA Asset Library.
2. Add several leaf meshes to the scene.

---

## Step 2: Enable Physics

Assign each leaf as a dynamic rigid body.

Press **Play**.

The leaves will fall and bounce on the ground.

---

## Step 3: Adjust Damping

For a more natural falling motion, change the following values:

- **Linear Damping:** `5`
- **Angular Damping:** `3`

---

## Step 4: Position the Leaves

Move the leaves onto the tree branches.

Press **Play**.

The leaves will naturally fall from the branches.

You can duplicate additional leaves to create a richer autumn effect.

---

## Step 5: Sequential Falling (Optional)

To make the animation more realistic:

- Create an **Action Graph**.
- Add delays so that each leaf begins falling at a different time.
- This creates a natural effect where leaves fall one after another instead of simultaneously.

---

# Reference Videos

## Basic Physics

https://www.youtube.com/watch?v=iurSCfTyoB4

---

## Particle Fluids (Solid to Liquid)

https://www.youtube.com/watch?v=eMyroevX1nA

---
