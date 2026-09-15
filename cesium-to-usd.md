# Integrating Cesium into NVIDIA Omniverse

This guide walks you through installing the **Cesium for Omniverse** extension, connecting it to **Cesium ion**, capturing images from your scene, and placing objects on the globe.

---

# Overview

Cesium for Omniverse brings real-world geospatial data into NVIDIA Omniverse by streaming global terrain, imagery, photogrammetry, and 3D buildings. It enables you to create digital twins and large-scale simulations using real-world geographic data.

---

# Prerequisites

Before beginning, ensure you have:

- NVIDIA Omniverse USD Composer
- A Cesium ion account

For the official installation guide, refer to:

- [Cesium for Omniverse Quickstart](https://cesium.com/learn/omniverse/omniverse-quickstart/)

---

# Step 1: Add the Community Extension Registry

If the Cesium extensions do not appear in the Extension Manager, you will first need to add the Community Extension Registry.

1. Open **Developer** → **Extensions**.
2. Click **Options**.
3. Select **Settings**.
4. Navigate to **Extension Registry**.
5. Click the **green (+)** button.
6. Add the following registry URL:

```text
https://dw290v42wisod.cloudfront.net/exts/kit/community
```

7. Save the settings and restart Omniverse if prompted.

> **Note:** This registry hosts community-developed Omniverse extensions, including Cesium for Omniverse.

---

# Step 2: Install Cesium for Omniverse

After adding the registry:

1. Open **Developer** → **Extensions**.
2. Search for **Cesium**.
3. Install the following extensions:
   - **Cesium for Omniverse USD Plugins**
   - **Cesium for Omniverse**
4. Enable **Autoload** for **Cesium for Omniverse**.
5. Restart Omniverse.
6. When prompted, enable **Omniverse Fabric Scene Delegate**.

After restarting, you should see a **Cesium** tab on the right side of the application.

---

# Step 3: Connect to Cesium ion

1. Open the **Cesium** panel.
2. Click **Connect to Cesium ion**.
3. Log in to your Cesium ion account.
4. Authorize Omniverse to access your account.
5. Configure your **Default Token** as the project token.

Once connected, you can stream terrain, imagery, photogrammetry, and 3D buildings directly into your Omniverse scene.

---

# Step 4: Create Your First Geospatial Scene

Using the Cesium panel:

- Add **Cesium World Terrain + Bing Maps Aerial Imagery**
- Add **Cesium OSM Buildings**

Explore the scene by navigating around the globe and adjusting the camera settings as needed.

---

# Capturing Images and Videos

Once your scene is ready, you can capture high-quality screenshots and videos directly from Omniverse.

Follow the official tutorial:

- [Capturing Images and Video](https://cesium.com/learn/omniverse/omniverse-capturing-images/)

---

# Placing Objects on the Globe

Cesium allows you to place Omniverse assets such as trees, vehicles, buildings, and other 3D models on real-world terrain.

Follow the official tutorial:

- [Placing Objects on the Globe](https://cesium.com/learn/omniverse/omniverse-placing-objects/)

This tutorial covers:

- Adding Omniverse assets to a Cesium scene
- Positioning assets using latitude and longitude
- Using the **Cesium Globe Anchor** component
- Keeping objects georeferenced when the globe origin changes

---

  # Additional Resources

- [Aerometrex dataset](https://ion.cesium.com/assetdepot/1415196)
- [Add more functionalities from Cesium to Omniverse](https://cesium.com/learn/omniverse/)

---

