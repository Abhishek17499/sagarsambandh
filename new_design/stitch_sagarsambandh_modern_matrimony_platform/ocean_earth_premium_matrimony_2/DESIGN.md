---
name: Ocean-Earth Premium Matrimony
colors:
  surface: '#fbf9f4'
  surface-dim: '#dbdad5'
  surface-bright: '#fbf9f4'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f5f3ee'
  surface-container: '#f0eee9'
  surface-container-high: '#eae8e3'
  surface-container-highest: '#e4e2dd'
  on-surface: '#1b1c19'
  on-surface-variant: '#3f4948'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f1ec'
  outline: '#6f7979'
  outline-variant: '#bec9c8'
  surface-tint: '#096969'
  primary: '#004c4c'
  on-primary: '#ffffff'
  primary-container: '#006666'
  on-primary-container: '#93e1e0'
  inverse-primary: '#86d4d3'
  secondary: '#9d4311'
  on-secondary: '#ffffff'
  secondary-container: '#fe8d56'
  on-secondary-container: '#702900'
  tertiary: '#6a3516'
  on-tertiary: '#ffffff'
  tertiary-container: '#874c2b'
  on-tertiary-container: '#ffc8ad'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#a2f0ef'
  primary-fixed-dim: '#86d4d3'
  on-primary-fixed: '#002020'
  on-primary-fixed-variant: '#004f4f'
  secondary-fixed: '#ffdbcc'
  secondary-fixed-dim: '#ffb595'
  on-secondary-fixed: '#351000'
  on-secondary-fixed-variant: '#7c2e00'
  tertiary-fixed: '#ffdbcb'
  tertiary-fixed-dim: '#ffb690'
  on-tertiary-fixed: '#341100'
  on-tertiary-fixed-variant: '#6e3819'
  background: '#fbf9f4'
  on-background: '#1b1c19'
  surface-variant: '#e4e2dd'
  deep-ocean: '#0C2A46'
  horizon-blue: '#145C82'
  soft-sky: '#DCEBF2'
  earth-warmth: '#CC6633'
  cream-base: '#F9F7F2'
typography:
  display-lg:
    fontFamily: Playfair Display
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Playfair Display
    fontSize: 32px
    fontWeight: '600'
    lineHeight: 40px
  headline-lg-mobile:
    fontFamily: Playfair Display
    fontSize: 28px
    fontWeight: '600'
    lineHeight: 36px
  title-md:
    fontFamily: Playfair Display
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.05em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  base: 8px
  margin-mobile: 20px
  margin-desktop: 64px
  gutter: 24px
  section-gap: 80px
---

## Brand & Style

The design system is built on the philosophy of "Steadfast Elegance," merging the vastness of the ocean with the grounding nature of the earth. It targets a sophisticated audience seeking meaningful, long-term connections. The emotional response is one of calm assurance, reliability, and warmth, moving away from the frenetic energy of dating apps toward a dignified matrimonial experience.

The visual style is **Corporate Modern with a Soft Minimalist influence**. It prioritizes generous whitespace and a refined color story to create a premium atmosphere. A signature "Wave Motif" is used as a subtle, low-opacity background element or a custom divider to reinforce the brand's namesake without overwhelming the user interface.

## Colors

The palette follows an "Ocean-Earth" narrative. **Deep Ocean Teal (#006666)** serves as the primary brand anchor, used for key actions and structural identity. **Soft Terracotta (#CC6633)** is the secondary accent, strategically applied to "human" elements like profile matches, messaging indicators, and heart icons to provide warmth and contrast.

The background uses **Warm Cream (#F9F7F2)** instead of pure white to create a soft, paper-like feel that reduces eye strain and feels more artisanal. For data-heavy areas or secondary surfaces, we utilize the extracted **Horizon Blue (#145C82)** and **Soft Sky (#DCEBF2)** to provide cooling tonal variations that complement the teal.

## Typography

This design system employs a high-contrast typographic pairing to signal "Premium Tradition." **Playfair Display** is used for headlines, profile names, and editorial moments. Its elegant serifs convey a sense of heritage and trustworthiness.

**Inter** is the functional workhorse, used for all UI components, body text, and labels. It ensures maximum readability for profile bios and data fields. To maintain a clean look, avoid using Playfair Display for text smaller than 20px. Use the `label-sm` style in all-caps for minor category headers to add a touch of formal structure.

## Layout & Spacing

The layout follows a **Fixed Grid** approach for desktop (1200px max-width) to maintain an intimate, editorial feel, while utilizing a fluid 4-column system for mobile. 

Spacing is intentionally generous. We use an 8px base unit but prioritize larger gaps (`section-gap`) between profile modules to give the content "room to breathe." Margins on mobile are slightly wider than standard (20px) to enhance the premium, non-cramped aesthetic. Elements should be aligned to a 12-column grid on desktop, with profile cards typically spanning 3 or 4 columns.

## Elevation & Depth

Hierarchy is established through **Tonal Layers** and **Ambient Shadows**. Surfaces are tiered to create a natural flow:
- **Level 0 (Background):** Warm Cream (#F9F7F2).
- **Level 1 (Cards/Surface):** Pure White (#FFFFFF) with a very soft, diffused shadow (0px 4px 20px, 4% opacity of Deep Ocean Teal).
- **Level 2 (Modals/Popovers):** Pure White with a more defined shadow (0px 10px 30px, 8% opacity).

Avoid harsh black shadows; instead, tint shadows with the Primary Teal to maintain a cohesive color temperature. Use subtle 1px borders in `Soft Sky` (#DCEBF2) to define boundaries on white surfaces without adding visual weight.

## Shapes

The shape language is defined by **Rounded (0.5rem)** corners as a baseline, scaling up to **rounded-xl (1.5rem)** for major containers and profile cards. This soft geometry mimics the fluid nature of the brand's "Ocean" theme and feels more approachable than sharp corners.

Buttons and input fields should utilize a 12px (0.75rem) radius to bridge the gap between the soft cards and functional elements. Profile images should never be sharp-edged; always use a minimum of 16px radius or a soft-squircle shape.

## Components

- **Buttons:** Primary buttons use Deep Ocean Teal with white text and 12px rounded corners. Secondary buttons use a Ghost style with a Teal border. Use Soft Terracotta only for "High Emotion" actions like "Send Interest" or "Favorite."
- **Cards:** Profile cards are the hero component. They feature white backgrounds, 24px internal padding, and 16px corner radius. Include a subtle "Wave" divider at the bottom of the image container.
- **Input Fields:** Fields use a 1px border in #DCEBF2. On focus, the border transitions to Deep Ocean Teal with a 2px outer glow in the same color at 10% opacity.
- **Chips/Badges:** Used for profile tags (e.g., "Verified," "Vegetarian"). These should have a pill-shape (32px radius) and use low-saturation versions of the brand colors to avoid clutter.
- **Lists:** Use generous vertical padding (16px+) between list items. Use the Soft Terracotta for small iconography within lists to draw the eye to key personality traits.
- **Wave Motif:** A custom SVG wave should be used as a divider between major landing page sections or as a subtle watermark in the header area.