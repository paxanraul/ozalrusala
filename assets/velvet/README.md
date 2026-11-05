# Emerald velvet assets

Created with the built-in **imagegen** tool for the November 2026 wedding invitation redesign. Final project assets are local WebP files with transparency preserved. Native SVG stationery variants are derived from this project's original SVGs.

| Asset | File | Use |
| --- | --- | --- |
| Velvet | `velvet.webp` | Emerald velvet background |
| Satin | `drapery.webp` | Transparent fabric section divider |
| Bouquet | `flowers.webp` | Transparent white flower arrangement |
| Gloves | `gloves-presentation.webp` | Upper-left and lower-right hands supporting the envelope from behind |

The source PNGs are retained in the local imagegen output directory. The website uses only the optimized files in this directory.

## Generation prompts

### Velvet

Use case: product-mockup. Asset type: background texture for an emerald and ivory luxury wedding invitation website. Create a photorealistic portrait 2:3 image entirely of rich, deep emerald green velvet fabric, color family #124C3C with dark green shadows. Quiet, elegant vertical folds, subtle soft sheen and visible fine velvet pile, gentle side lighting. Keep the center dark and visually calm for white text and an envelope overlay. Fill the full frame edge to edge. No objects, no people, no flowers, no borders, no text, no red, no logos. This is only a fabric background asset, not a website mockup.

### Drapery

Use case: product-mockup. Asset type: isolated horizontal decorative fabric divider for a luxury emerald wedding invitation website. Photorealistic deep emerald green satin drapery, matching #124C3C, with a gathered swag hanging low in the center and sweeping upward at both left and right edges. Wide 2:1 composition, continuous cloth fills lower half, upper silhouette is a dramatic U-shaped flowing fold, layered sumptuous folds and soft highlights. All outside the fabric must be genuinely transparent, no background, no floor, no white rectangle. No other objects, no gold, no text, no red, no logos. Elegant realistic material, photographed studio quality.

### Flowers

Use case: product-mockup. Asset type: isolated botanical decoration for an emerald and ivory luxury wedding invitation website. A compact sumptuous asymmetric horizontal arrangement of five creamy white garden roses, white ranunculus, two white orchid blossoms, small ivory buds, and dark emerald green leaves. Fine realistic petal detail, soft romantic studio lighting, antique wedding stationery styling. Horizontal 3:2 arrangement, all flowers and foliage entirely inside frame with generous transparent margin. Genuinely transparent background, no vase, no hands, no ground or backdrop, no text, no pink, no burgundy, no gold, no logos.

### Gloves — initial version (`gloves.webp`)

Use case: product-mockup. Asset type: transparent foreground layer for a luxury wedding invitation envelope animation. Photorealistic pair of elegant hands in ivory white satin opera gloves, cropped at the wrists entering from the far left and far right edges of a wide 3:2 image. Left hand reaches in slightly higher, lightly pinching the upper left corner of an INVISIBLE horizontal envelope; right hand comes in lower and cups its lower right corner. The invisible envelope is centered and occupies the central 60% of the width and middle 35% of height: leave this central space entirely transparent with NO envelope or paper visible. Only two anatomically correct gloved hands and wrists, very subtle satin folds and soft realistic lighting. Hands stay near left/right edges, do not touch or overlap center. Genuinely transparent background, no skin, no jewelry, no text, no objects, no floor, no logos.

### Gloves — final reference composition (`gloves-presentation.webp`)

Built-in imagegen edit using the user-supplied wedding reference and the initial glove asset. Final prompt:

Create an isolated transparent asset of TWO white satin opera-gloved hands. Image 1 is a composition reference: look ONLY at the envelope vignette at the top of the LEFTMOST column. Reproduce that asymmetrical hand positioning and natural extended-finger pose exactly: ONE hand enters horizontally from the LEFT, above the envelope's upper-left corner, fingers pointing right and gently resting over/behind its top edge; the OTHER hand enters horizontally from the RIGHT at the LOWER right corner, fingers pointing left and cradling the envelope from below. These hands must NOT be symmetrical or at the same height. Image 2 is only a material and lighting reference for ivory satin gloves. REPLACE its pinching/OK-circle pose with the relaxed elongated fingers from image 1. No fingers curled into a pinch, no thumb/index tip touching. This will be layered BEHIND an existing envelope in HTML, so render complete hands with palms/fingers extending inward enough to be occluded by the envelope. Wide 3:2 canvas. Invisible envelope target rectangle x=20%-80%, y=28%-73%. Upper LEFT wrist enters at x=0%, y=24%; upper hand extends to x=36%, y=32%, fingertips laid flat, thumb gently lower, no circular gap. Lower RIGHT wrist enters at x=100%, y=77%; lower hand extends to x=64%, y=74%, palm gently supporting, fingers relaxed and straight. Leave the full center empty. Render only two anatomically correct gloved hands/wrists on genuinely transparent background. NO envelope or card, NO flowers, NO text, NO website screenshot, NO burgundy background. Photorealistic ivory satin, fine fabric creases, soft studio light.
