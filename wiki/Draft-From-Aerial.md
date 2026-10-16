# 🛰️ Draft From Aerial

Select an area on the aerial map and CAD Auto drafts the **curb lines** and
**building footprints** inside it, then shows them in the CAD view and exports
them as a DXF.

## Steps

1. **🛰 Aerial**: pan/zoom to the site.
2. **▭** (left tools), then drag a box on the map. **⛶** uses the whole visible map
   instead. Press `Esc` to cancel.
3. In the side panel, pick the layers and where each comes from:
   - **OpenStreetMap**: works out of the box. Buildings are well covered;
     curbs (`barrier=kerb`) are mapped in only some places.
   - **ArcGIS layer URL**: paste a GIS layer URL, e.g.
     `https://…/arcgis/rest/services/<Service>/MapServer/3`. This is the way to
     use the county or city curb and building layers. The URL is remembered.
4. Choose the output **Coordinates**:
   - **Ramsey County (US ft)**: the same county coordinates as FBK Checker
     and the survey data.
   - **Local (ft)**: the SW corner of the box is 0,0 (the panel shows its
     Ramsey coordinates).
5. **✏ Draft CAD lines**: the lines appear on the aerial (green = curb,
   blue = building) and in **📐 CAD**.
6. **↓ Export DXF**: an R12 DXF with layers `CURB` (green), `BLDG`
   (blue) and `AREA` (yellow box).

## Details

- Curb lines are clipped to the box. Buildings that touch the box are kept
  whole.
- ArcGIS layers are queried with JSONP (`callback=`), so the server does not
  need CORS. Results are paged when the server sets `exceededTransferLimit`.
- The **Aerial** dropdown switches between Esri World Imagery and Ramsey County
  2024 orthophotos. If the county server doesn't load, the app falls back to Esri.
- The coordinate transform is FBK Checker's calibrated Ramsey County Lambert
  Conformal Conic. It's only meaningful for sites in or near Ramsey County.
