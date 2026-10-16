# 🛰️ Draft From Aerial

Select an area on the aerial map and CAD Auto drafts the **curb lines** and
**building footprints** inside it, then shows them in the CAD view and exports
them as a DXF.

## Steps

1. **🛰 Aerial**: pan/zoom to the site.
2. **▭** (left tools), then drag a box on the map. **⛶** uses the whole visible map
   instead. Press `Esc` to cancel.
3. In the side panel, pick the layers and where each comes from:
   - **Auto-trace from aerial image** (curbs, the default): CAD Auto reads
     the aerial photo itself and traces the curb lines. See below.
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

## Auto-trace from aerial image

How the curbs are found:

1. It downloads the Esri aerial for the box (about 1 ft/px; coarser for very
   large boxes). Tracing always uses Esri, because the Ramsey County server
   doesn't allow the browser to read its pixels.
2. It pulls the street centerlines from OpenStreetMap and samples the
   **pavement color** along them.
3. It grows the paved area outward from the centerlines: pixels close to that
   color and within **Max curb offset** of a centerline. Cars, manholes and
   lane paint (holes up to about 500 sq ft) are filled in.
4. It traces the edge of the paved area, simplifies it, and drops pieces
   shorter than 15 ft. The results are the `CURB` lines.

Settings:

- **Pavement tolerance** (0.5–2): raise it if the curb line cuts into
  the street (patched or faded asphalt, shadows); lower it if it spills
  into driveways, parking lots or sidewalks.
- **Max curb offset from centerline**: 45 ft by default. Raise it for wide
  arterials, lower it to stop the trace leaking into lots.
- **Show detected pavement**: tints the area it treated as street, so you
  can see why a line went where it did.

It produces a draft, not survey-grade linework. **Tree canopy and shadows over
the gutter** push the line inward, and gray sidewalks or lots that touch the
street with no visible edge can pull it outward. Review the result against
the aerial before you use it. Accuracy is about one pixel (~1 ft) where the
gutter is visible.

## Details

- Curb lines are clipped to the box. Buildings that touch the box are kept
  whole.
- ArcGIS layers are queried with JSONP (`callback=`), so the server does not
  need CORS. Results are paged when the server sets `exceededTransferLimit`.
- The **Aerial** dropdown switches between Esri World Imagery and Ramsey County
  2024 orthophotos. If the county server doesn't load, the app falls back to Esri.
- The coordinate transform is FBK Checker's calibrated Ramsey County Lambert
  Conformal Conic. It's only meaningful for sites in or near Ramsey County.
