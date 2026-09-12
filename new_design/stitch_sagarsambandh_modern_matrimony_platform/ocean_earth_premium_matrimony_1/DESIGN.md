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
  on-surface-variant: '#41484d'
  inverse-surface: '#30312e'
  inverse-on-surface: '#f2f1ec'
  outline: '#71787e'
  outline-variant: '#c1c7ce'
  surface-tint: '#2d6482'
  primary: '#2d6482'
  on-primary: '#ffffff'
  primary-container: '#7fb3d5'
  on-primary-container: '#004562'
  inverse-primary: '#99cdf0'
  secondary: '#9d4311'
  on-secondary: '#ffffff'
  secondary-container: '#fe8d56'
  on-secondary-container: '#702900'
  tertiary: '#21648a'
  on-tertiary: '#ffffff'
  tertiary-container: '#78b3dd'
  on-tertiary-container: '#004565'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#c6e7ff'
  primary-fixed-dim: '#99cdf0'
  on-primary-fixed: '#001e2d'
  on-primary-fixed-variant: '#0a4c69'
  secondary-fixed: '#ffdbcc'
  secondary-fixed-dim: '#ffb595'
  on-secondary-fixed: '#351000'
  on-secondary-fixed-variant: '#7c2e00'
  tertiary-fixed: '#c9e6ff'
  tertiary-fixed-dim: '#92cdf9'
  on-tertiary-fixed: '#001e2f'
  on-tertiary-fixed-variant: '#004c6e'
  background: '#fbf9f4'
  on-background: '#1b1c19'
  surface-variant: '#e4e2dd'
  premium-blue: '#7FB3D5'
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
The design system embodies the philosophy of "Serene Sophistication," pivoting from deep teals to a lighter, more ethereal blue palette. It targets a discerning audience looking for lifelong partnership, evoking an emotional response of clarity, peace, and premium reliability.

The visual style is **Corporate Modern with a Soft Minimalist influence**. It relies on high-end editorial layouts, generous whitespace, and a refined "Air and Earth" color story. The transition to light blue shifts the brand from a heavy, traditional feel to a modern, aspirational matrimonial experience that feels fresh and trustworthy.

## Colors
The palette transition replaces the previous teal with **Premium Light Blue (#7FB3D5)** as the primary brand anchor. This color is used for high-level UI elements and primary call-to-actions, providing a breathable and sophisticated atmosphere. **Earth Warmth (#CC6633)** remains the secondary accent, reserved for "human-centric" highlights like interest indicators and heart icons to provide a grounding contrast to the airy blues.

The background uses **Cream Base (#F9F7F2)** to maintain an artisanal, paper-like quality. Surface containers utilize **Soft Sky (#DCEBF2)** and **Horizon Blue (#145C82)** for tiered cooling effects, ensuring the interface feels layered and intentional rather than flat.

## Typography
The system utilizes a high-contrast pairing of **Playfair Display** and **Inter**. The serif typeface (Playfair) is strictly for display and headline levels to signal heritage and elegance. Inter handles all functional UI, body text, and labeling to ensure maximum legibility within profile data and messaging.

For a structured, formal appearance, use `label-sm` in all-caps for secondary headers. Avoid using the serif face for any text block smaller than 20px to preserve visual clarity on digital screens.

## Layout & Spacing
The design system employs a **Fixed Grid** model for desktop, centered at 1200px, to mimic the feel of a high-end editorial magazine. On mobile, it transitions to a fluid 4-column system. 

The spacing rhythm is governed by an 8px base unit, but emphasizes large `section-gap` units of 80px to prevent the content from feeling crowded. Profiles and content modules should use wide 24px gutters to reinforce the premium, unhurried user experience.

## Elevation & Depth
Depth is created through **Tonal Layers** and light-tinted **Ambient Shadows**. Instead of neutral grays, shadows are tinted with the primary light blue to maintain a cohesive color temperature across the UI.

- **Level 0 (Background):** Cream Base (#F9F7F2).
- **Level 1 (Cards):** White (#FFFFFF) with a soft shadow (0px 4px 20px, 6% opacity of #7FB3D5).
- **Level 2 (Overlays):** White with a defined shadow (0px 10px 30px, 10% opacity of #7FB3D5).

Use 1px "Ghost Borders" in `Soft Sky` (#DCEBF2) to define secondary containers without adding unnecessary visual weight.

## Shapes
The shape language is **Rounded**, using a 0.5rem (8px) base for most components. This creates a gentle, approachable feeling that aligns with the brand's fluid "Ocean" motif. 

Major containers and profile cards scale up to **1.5rem (24px)**, creating distinct "soft rectangles" that frame photography elegantly. Functional elements like inputs and buttons use a slightly sharper **0.75rem (12px)** to indicate interactivity and precision.

## Components
- **Buttons:** Primary buttons feature the Premium Light Blue with white text. Use Earth Warmth (#CC6633) exclusively for "emotional conversion" points like "Connect" or "Send Interest."
- **Cards:** Profile cards are the central component, featuring white backgrounds, 24px padding, and 24px corner radii. Use a subtle Horizon Blue for secondary text within cards.
- **Input Fields:** Fields are styled with a 1px Soft Sky border. On focus, the border shifts to the Primary Blue with a soft 2px outer glow at 10% opacity.
- **Chips/Badges:** All tags (interests, traits) use pill-shaped containers with a Soft Sky background and Horizon Blue text for a low-contrast, organized look.
- **Lists:** High-density lists must use 16px vertical padding and subtle Soft Sky dividers to maintain the feeling of whitespace even when data is plentiful.