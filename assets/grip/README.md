# Coherent envelope grip

Created with the built-in imagegen tool. The composition was generated as one physical scene, then edited to extract a registered clean envelope and complete hands. WebP assets preserve transparency; their shared SVG coordinate space is 1536 × 1024.

Files: `composition.webp`, `envelope.webp`, `left-hand.webp`, `right-hand.webp`.

Native mask geometry and markup are maintained in `scripts/build_grip.py`; motion is defined in `grip.css`. Finger masks, envelope edges and contact shadows all use the same camera registration.

## Prompts

### composition

Use case: product-mockup. Create ONE coherent photorealistic product photograph, not separate floating hands. Use ONLY the top envelope vignette in the LEFT column of the reference for hand positioning. A thick closed deep emerald green (#124C3C) wedding envelope is ACTUALLY HELD by two ivory satin opera-gloved hands: the hand entering from the left holds the UPPER LEFT corner, with its thumb visibly pressing the front and the other fingers wrapped behind the top edge. The hand entering from the right supports the LOWER RIGHT corner, thumb on the front near the corner and other fingers curled UNDER the lower paper edge. The paper edge must pass BETWEEN fingers. Show believable physical contact, compression/creases of satin at contact, narrow contact shadows, no gap between fingertips and paper. Both hands and envelope share the same soft upper-left light and camera. Camera straight-on/orthographic, envelope level and flat, no tilt or perspective skew. Wide 3:2 canvas. Envelope rectangle occupies exactly x=25% to 75%, y=27% to 71% of the canvas; all remaining space is transparent. Left wrist enters from the left edge around y=26%; right wrist enters from right edge around y=69%. Hands visible around corners, not covering the center. Envelope has a triangular closed flap, subtle linen paper grain, fine folds and thin paper edges, gently rounded lower corners. Plain emerald paper only, NO seal, NO monogram, NO text, NO floral decorations: these will be added in HTML. Do not render a website, table, background fabric, or any background; genuine transparent cutout. Anatomically correct elegant hands with five fingers, full physical grip instead of hovering. Preserve a realistic refined wedding-stationery look.

### envelope

Precise object edit: remove BOTH white gloved hands and their contact shadows from this image, leaving ONLY the same emerald envelope on a genuinely transparent background. Preserve the original 1536x1024 canvas and EXACT position, size, color, paper grain, folds, camera and lighting of the envelope. Envelope straight rectangular bounds approximately x=326..1174, y=230..783. Reconstruct the hidden paper under the two thumbs and the hidden top-left/lower-right corners, using matching emerald paper. Keep the triangular flap exactly as it is, its point around x=756,y=614. No seal, no text, no added objects. Do NOT recenter, crop, zoom, tilt or resize anything. This is a registered clean plate for animation, all originally visible envelope edges must remain in the identical pixel locations.

### left

Background extraction / precise object edit. Extract ONLY the upper LEFT white satin gloved hand and wrist from this composition; remove the envelope and the right hand. Reconstruct the portions of the fingers that were hidden BEHIND the envelope as anatomically natural curled fingers holding a thin sheet. Keep the visible thumb, hand, wrist folds, pose, lighting, scale and EXACT LOCATION unchanged. Output on the SAME 1536x1024 transparent canvas: left wrist is cropped by the LEFT image edge, visible hand occupies roughly x=0..655,y=100..410. Visible thumb presses down around x=370..530,y=260..370. Do NOT center the hand, do NOT zoom, do NOT change the pinch/grip pose. Keep the hand at the FAR LEFT in exactly the original registered coordinates, with the rest of the canvas transparent. No envelope, no paper, no green color artifacts, no shadows from an absent envelope, no right hand, no text. Preserve ivory satin texture and natural five-finger anatomy.

### right

Background extraction / precise object edit. Extract ONLY the lower RIGHT white satin gloved hand and wrist from this composition; remove the envelope and the left hand. Reconstruct portions of fingers hidden BEHIND the paper as naturally curled supporting fingers. Keep all visible parts, especially the thumb pressing against the paper and the cupped fingers beneath it, in exactly the same pose, lighting, scale, texture and LOCATION. Output the SAME 1536x1024 transparent canvas: right wrist cropped at the RIGHT image edge, hand occupies roughly x=700..1536,y=655..950. Thumb points toward the LEFT and sits at x=885..1130,y=655..785. Do NOT center, crop, zoom, tilt or move the hand, do NOT change the grip. All other space is genuinely transparent. No paper, envelope, green artifacts, cast shadows from an absent envelope, left hand, text, or other objects. Preserve anatomically correct ivory satin gloves.

