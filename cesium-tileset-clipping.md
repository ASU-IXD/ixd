# Tileset Clipping in Cesium for Omniverse

This guide demonstrates how to clip portions of a Cesium tileset using **Cesium Cartographic Polygons** and **Polygon Raster Overlays**. Tileset clipping is useful for hiding parts of a streamed tileset so they can be replaced with custom 3D content or to focus on a specific area of interest.

---

# Prerequisites

Before starting this tutorial, make sure you have:

- NVIDIA Omniverse USD Composer installed
- Cesium for Omniverse installed and connected to your Cesium ion account
- Completed the **Cesium for Omniverse Quickstart** tutorial

Reference:

- [Cesium for Omniverse Quickstart](https://cesium.com/learn/omniverse/omniverse-quickstart/)
- [Official Tileset Clipping Tutorial](https://cesium.com/learn/omniverse/omniverse-tileset-clipping/)

---

# Tutorial

Follow the official Cesium tutorial step-by-step:

- [Tileset Clipping](https://cesium.com/learn/omniverse/omniverse-tileset-clipping/)

---

# Troubleshooting

## Step 2.3 – Unable to Edit the Polygon

If you cannot edit the polygon after creating it:

1. In the **Stage** panel, locate the **cartographic_polygon** object.
2. Right-click the object.
3. Select **Edit Control Vertices**.
4. The control points should now appear, allowing you to reshape the polygon.

---

## Step 3.1 – Unable to Find "Polygon Raster Overlay"

If **Polygon Raster Overlay** is not available when right-clicking the tileset:

1. Go to **Window → Cesium**.
2. Enable all four Cesium windows:
   - Cesium
   - Cesium Assets
   - Cesium Debugging
   - Cesium Settings
3. Return to your tileset.
4. Right-click the tileset and select:

```
Add
└── Cesium
    └── Polygon Raster Overlay
```

The Polygon Raster Overlay option should now be available.

---

# Note

> **Important:** Disable **Cesium World Terrain** while following this tutorial. Doing so makes it much easier to observe the clipping effect and verify that your changes are being applied correctly.
