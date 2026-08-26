# Millie UI — Visual Style Catalog

This is a vocabulary and implementation guide, not a list of mandatory trends.

For each project choose one primary style and at most one supporting influence unless the product
is explicitly experiential.

---

## 1. Refined Minimal

**Look**
- disciplined whitespace
- quiet surfaces
- precise typography
- hairline borders
- little decoration
- one controlled accent
- fine alignment

**Best for**
- premium SaaS
- professional services
- architecture
- finance
- portfolios
- modern corporate

**Palette**
- warm/cool off-white or near-black neutral base
- low-chroma tinted grays
- one distinctive accent

**Implementation**
- strong grid
- minimal card wrappers
- large content measures only where useful
- typography does most hierarchy work
- borders/elevation nearly invisible

**Motion**
- opacity + 4–12px translation
- precise shared-layout transitions
- subtle underline/clip reveals

**Avoid**
- making "minimal" mean empty
- 100px gaps between every section
- huge type without content reason

---

## 2. Luxury Minimal

**Look**
- restraint
- material quality
- editorial scale
- carefully cropped photography
- refined serif/sans pairing or exceptional single family
- muted accent

**Best for**
- luxury
- hospitality
- fashion
- beauty
- automotive
- premium property
- boutique studio

**Palette**
- ivory/bone/stone/charcoal/espresso/ink
- jewel or metallic-inspired accent used sparingly

**Implementation**
- strong image art direction
- low UI chrome
- generous but controlled vertical rhythm
- thin rules
- elegant type tracking

**Motion**
- slower, eased reveals
- image masks
- subtle parallax
- light reflection

**Avoid**
- fake gold gradients
- excessive cursive type
- low contrast beige-on-beige

---

## 3. Swiss / International

**Look**
- rational grid
- asymmetry
- clean sans typography
- bold scale contrasts
- strong alignment
- disciplined color

**Best for**
- studios
- architecture
- cultural institutions
- editorial products
- portfolios
- information-heavy marketing

**Implementation**
- visible grid logic
- flush alignments
- modular columns
- deliberate negative space
- rules and labels

**Motion**
- crisp directional transitions
- grid-aware reveals
- minimal springiness

**Avoid**
- turning it into generic corporate minimalism

---

## 4. Editorial / Magazine

**Look**
- typography-led
- image/text pacing
- magazine grid
- captions
- pull quotes
- varied scale
- occasional deliberate grid breaks

**Best for**
- publications
- fashion
- portfolios
- content sites
- brand storytelling
- reports

**Implementation**
- baseline rhythm
- constrained body measure
- serif/sans or display/body pair
- art-directed image ratios
- caption system
- multi-column layouts where content supports them

**Motion**
- mask reveal
- image crop shift
- line-by-line headline appearance
- restrained sticky media

**Avoid**
- animating every paragraph
- unreadable oversized display type

---

## 5. Monochrome Precision

**Look**
- black/white/graphite
- one optional accent
- strong typography
- dense clear hierarchy

**Best for**
- tools
- productivity
- docs
- developer products
- premium portfolios
- B2B

**Implementation**
- hierarchy through value, weight, size, border
- accent reserved for action/state
- excellent focus design

**Motion**
- fast, low-distance
- state interpolation

---

## 6. Industrial / Utilitarian

**Look**
- functional structure
- exposed grid
- condensed/technical type
- strong borders
- labels
- minimal ornament

**Best for**
- logistics
- manufacturing
- infrastructure
- devtools
- operations
- internal systems

**Palette**
- neutral base + safety/status colors

**Motion**
- immediate
- mechanical
- status driven

**Avoid**
- decorative "factory" textures that hurt clarity

---

## 7. Data-Dense Precision

**Look**
- compact
- sharp hierarchy
- low decoration
- information-rich tables/charts
- tuned numeric typography

**Best for**
- security
- NOC/SOC
- analytics
- finance
- operations
- monitoring

**Implementation**
- compact spacing
- tabular numerals
- high signal-to-noise
- semantic status color
- persistent filters where useful
- resizable/sortable data surfaces as appropriate

**Motion**
- small state transition only
- no slow decorative entrances

---

## 8. Glassmorphism

**Look**
- frosted translucent panels
- backdrop blur
- subtle edge highlight
- layered depth

**Best for**
- overlays
- media apps
- premium dashboards
- creative product marketing
- navigation/control layers

**Implementation**
```css
.glass {
  background: color-mix(in oklab, white 10%, transparent);
  border: 1px solid color-mix(in oklab, white 22%, transparent);
  backdrop-filter: blur(14px) saturate(120%);
}
```

Treat values as examples.

**Motion**
- subtle luminosity shift
- reflection follow
- restrained depth transition

**Avoid**
- blur on every component
- unpredictable background under text
- many nested backdrop roots
- low-end device GPU overload

---

## 9. Liquid-Glass-Inspired

**Look**
- fluid translucent foreground controls
- adaptive light/color pickup
- morphing capsules
- spatial separation between content and controls

**Best for**
- current Apple-platform native UI
- premium media controls
- navigation layers
- carefully selected web interpretations

**Implementation**
Native Apple:
- prefer system Liquid Glass materials/components

Web interpretation:
- backdrop blur
- layered highlight/refraction illusion
- dynamic light response
- controlled morphing
- fallback opaque surface

**Motion**
- touch/pointer-responsive material deformation
- shape morph
- highlight response

**Avoid**
- covering content layer in glass
- cloning Apple's exact visual identity
- glass on every card

---

## 10. Neumorphism / Soft UI

**Look**
- same-color surfaces
- light + dark opposing shadows
- extruded/inset controls
- soft molded feeling

**Best for**
- limited control clusters
- calm wellness
- audio controls
- playful settings
- hero demos

**Implementation**
- use hybrid boundaries
- visible label/icon contrast
- visible focus
- accent selected/active states
- inset active/pressed state

**Motion**
- shadow interpolation
- 1–2px press
- subtle spring

**Avoid**
- whole dense apps
- low contrast
- shadow-only affordance

---

## 11. Claymorphism

**Look**
- puffy forms
- oversized radius
- pastel/bright surfaces
- outer soft shadow
- inner highlight
- friendly 3D illustration

**Best for**
- education
- kids/family
- onboarding
- consumer tools
- playful fintech
- creative apps

**Motion**
- soft spring
- squash/press
- gentle floating accent objects

**Avoid**
- enterprise SOC console
- legal/medical critical workflow in full clay style

---

## 12. Modern Skeuomorphism

**Look**
- selective physical metaphor
- realistic material/lighting
- tactile controls
- knobs/sliders/dials where semantics support them

**Best for**
- music
- audio
- camera
- automotive
- creative tools
- simulations
- hobby products

**Implementation**
- use realism only where physical metaphor helps discoverability
- combine with modern flat information hierarchy
- avoid literal decoration unrelated to function

**Motion**
- inertia
- tactile press
- dial/slider physics
- material response

---

## 13. Paper / Crafted

**Look**
- paper fibers/noise
- ink-like type
- torn/cut edges sparingly
- print-inspired layers
- stamped details

**Best for**
- editorial
- food
- craft
- culture
- heritage
- portfolios

**Implementation**
- subtle texture overlays
- print-like rules
- tactile layering
- avoid making text itself noisy

**Motion**
- page/clip reveal
- paper slide
- stamp appearance

---

## 14. Chrome / Holographic

**Look**
- spectral reflection
- metallic/chrome surfaces
- iridescent gradient
- controlled glow

**Best for**
- fashion
- music
- gaming
- futuristic brand
- creative portfolio
- launch campaign

**Implementation**
- conic/radial gradients
- mask
- blend modes carefully
- pointer-aware highlight on limited elements
- WebGL shader for high-end hero only when justified

**Motion**
- reflection sweep
- angle-dependent hue shift
- shimmer on rare focal object

**Avoid**
- shimmering every control
- text readability over spectral surfaces

---

## 15. Neobrutalism

**Look**
- strong borders
- hard offset shadows
- saturated blocks
- chunky typography
- visible structure
- playful rawness

**Best for**
- creative products
- youth brands
- education
- startup campaigns
- tools with playful identity

**Implementation**
```css
.neo {
  border: 2px solid currentColor;
  box-shadow: 6px 6px 0 currentColor;
}
.neo:active {
  transform: translate(3px, 3px);
  box-shadow: 3px 3px 0 currentColor;
}
```

**Motion**
- snappy
- hard translation
- graphic wipes

**Avoid**
- luxury/legal/trust-heavy contexts unless brand explicitly calls for it

---

## 16. Raw Brutalism

**Look**
- exposed HTML-like structure
- utilitarian type
- stark contrast
- unexpected hierarchy
- deliberate roughness

**Best for**
- art
- experimental studio
- cultural/editorial
- concept portfolios

**Implementation**
- meaningful rawness, not broken CSS
- retain semantic interaction
- clear focus and navigation despite aesthetic

---

## 17. Bauhaus / Geometric

**Look**
- primary/simple geometry
- circles/rectangles
- strong grid
- bold color blocks
- typographic geometry

**Best for**
- education
- culture
- design/architecture
- creative brands
- events

**Motion**
- geometric translation/rotation
- masked wipes
- shape assembly

---

## 18. Art Deco / Geometric Luxury

**Look**
- symmetry
- elegant lines
- geometric framing
- rich dark/light contrast
- restrained metallic accents

**Best for**
- hospitality
- events
- luxury services
- heritage/fashion

**Implementation**
- border ornaments with restraint
- serif/display type
- symmetrical composition
- do not fake metallic text with cheap gradients

---

## 19. Maximalist

**Look**
- multiple scales
- saturated color
- strong imagery
- layered composition
- expressive type

**Best for**
- music
- fashion
- campaigns
- entertainment
- creative studios

**Rules**
- hierarchy must remain obvious
- complexity must be choreographed
- reserve calm zones

**Motion**
- kinetic typography
- collage movement
- layered parallax
- strong scene transitions

---

## 20. Anti-Grid / Expressive Type

**Look**
- intentional asymmetry
- overlaps
- off-axis composition
- type as image
- grid breaks

**Best for**
- portfolio
- studio
- fashion
- launch
- editorial campaign

**Implementation**
- underlying hidden grid still required
- mobile version must be recomposed, not merely stacked

---

## 21. Organic / Natural

**Look**
- soft asymmetry
- earthy palette
- botanical/natural imagery
- fluid shapes
- humanist typography

**Best for**
- wellness
- food
- sustainability
- travel
- lifestyle
- community

**Motion**
- gentle drift
- organic mask
- soft spring
- slow parallax

**Avoid**
- generic green gradient as shorthand for sustainability

---

## 22. Soft Pastel

**Look**
- low/moderate chroma pastels
- warm friendly type
- soft geometry
- bright neutral surfaces

**Best for**
- consumer
- wellness
- education
- creator tools
- social

**Rules**
- keep text contrast strong
- avoid making all semantic states pastel and indistinguishable

---

## 23. Dark Cinematic

**Look**
- near-black tinted surfaces
- image/video focus
- dramatic type
- controlled spotlight color
- depth

**Best for**
- entertainment
- gaming
- automotive
- luxury
- portfolio
- media

**Motion**
- cinematic reveal
- slow camera-like transitions
- light sweeps
- depth movement

**Avoid**
- pure black + neon cyan/purple by reflex

---

## 24. Retro-Futurist

**Look**
- historical future imagery
- chrome/plastic/CRT influences
- bold display type
- unusual grid
- glow used selectively

**Best for**
- tech campaigns
- music
- portfolio
- creative brands
- entertainment

**Motion**
- scan/reveal
- shader distortion
- spatial objects
- kinetic type

---

## 25. Y2K / Cyber-Pop

**Look**
- glossy shapes
- saturated accents
- metallic/iridescent details
- playful web nostalgia
- compact type/graphics

**Best for**
- music
- youth fashion
- creator brand
- gaming
- campaigns

**Avoid**
- critical enterprise UI unless only used for brand/marketing layer

---

## 26. Retro Pixel / Game

**Look**
- pixel type/graphics
- fixed-step animation
- game HUD cues
- limited palettes

**Best for**
- games
- creative portfolio
- fan/community
- event microsites

**Rules**
- normal readable body type may coexist
- preserve target sizes/accessibility

---

## 27. Heritage / Neo-Classic

**Look**
- archival/print references
- serif typography
- muted material palette
- careful ornament
- historic image treatment

**Best for**
- institutions
- premium food/drink
- museums
- craft
- property
- hospitality

**Motion**
- restrained
- page/print transitions
- slow image reveal

---

## 28. Gradient Mesh / Aurora

**Look**
- spatial color fields
- layered soft gradients
- atmospheric depth

**Best for**
- abstract digital products
- creative tools
- marketing backgrounds
- music/media

**Implementation**
- CSS gradients/canvas
- color interpolation in perceptual spaces where possible
- texture/noise to prevent sterile look

**Avoid**
- default blue/purple aurora
- gradient behind every section

---

## 29. Layered Spatial UI

**Look**
- foreground/midground/background
- depth-aware panels
- perspective
- controlled floating objects

**Best for**
- media
- product showcase
- spatial concepts
- dashboards needing layer hierarchy

**Implementation**
- CSS transforms first
- pointer tilt only on non-critical surfaces
- no text at unreadable perspective

---

## 30. 3D Product Showcase

**Look**
- real-time or pre-rendered product object
- camera-led storytelling
- product color/configuration interaction

**Best for**
- devices
- automotive
- furniture
- physical goods
- industrial products

**Motion**
- scroll rotation
- exploded view
- camera dolly
- hotspot transitions

**Performance**
- compressed models
- adaptive DPR
- lazy load
- static fallback

---

## 31. WebGL Narrative

**Look**
- website behaves as scenes/environment
- DOM text + GPU visuals
- scroll/input controls camera/objects

**Best for**
- portfolio
- campaign
- entertainment
- culture
- experimental brand

**Implementation**
- DOM owns semantic text and controls when possible
- WebGL owns visual atmosphere/spatial media
- one scroll/input source
- mobile simplified scene

---

## 32. Fashion / Editorial Luxe

**Look**
- dramatic photography
- type-led editorial composition
- stark layout shifts
- limited controls
- runway/catalog pacing

**Best for**
- fashion
- beauty
- art direction
- photographer portfolio

**Motion**
- image crop reveals
- page transitions
- type choreography

---

# Style Decision Shortcut

If trust is critical:
- refined minimal
- Swiss
- editorial
- monochrome precision
- data precision

If friendliness is critical:
- organic
- soft pastel
- claymorphism
- selective skeuomorphism

If distinctiveness is critical:
- neobrutalism
- maximalist
- anti-grid
- retro-futurist
- WebGL narrative

If luxury is critical:
- luxury minimal
- fashion/editorial luxe
- dark cinematic
- heritage
- Art Deco influence

If spatial/product demonstration is critical:
- layered spatial
- 3D showcase
- mixed DOM + WebGL

Never use this shortcut without product-context checks.
