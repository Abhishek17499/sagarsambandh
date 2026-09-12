---
name: Serene Radiance
colors:
  surface: '#fff8f5'
  surface-dim: '#e9d6cc'
  surface-bright: '#fff8f5'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#fff1ea'
  surface-container: '#feeadf'
  surface-container-high: '#f8e4da'
  surface-container-highest: '#f2dfd4'
  on-surface: '#231a13'
  on-surface-variant: '#564337'
  inverse-surface: '#392e27'
  inverse-on-surface: '#ffede4'
  outline: '#897365'
  outline-variant: '#dcc1b1'
  surface-tint: '#944a00'
  primary: '#944a00'
  on-primary: '#ffffff'
  primary-container: '#e67e22'
  on-primary-container: '#502600'
  inverse-primary: '#ffb783'
  secondary: '#2d6482'
  on-secondary: '#ffffff'
  secondary-container: '#a7dbfe'
  on-secondary-container: '#29617f'
  tertiary: '#00658f'
  on-tertiary: '#ffffff'
  tertiary-container: '#00a3e4'
  on-tertiary-container: '#00354d'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#ffdcc5'
  primary-fixed-dim: '#ffb783'
  on-primary-fixed: '#301400'
  on-primary-fixed-variant: '#713700'
  secondary-fixed: '#c6e7ff'
  secondary-fixed-dim: '#99cdf0'
  on-secondary-fixed: '#001e2d'
  on-secondary-fixed-variant: '#0a4c69'
  tertiary-fixed: '#c7e7ff'
  tertiary-fixed-dim: '#86cfff'
  on-tertiary-fixed: '#001e2e'
  on-tertiary-fixed-variant: '#004c6d'
  background: '#fff8f5'
  on-background: '#231a13'
  surface-variant: '#f2dfd4'
  ocean-deep: '#0C2A46'
  horizon-blue: '#145C82'
  soft-sky: '#DCEBF2'
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
  gutter: 24px
  margin-mobile: 20px
  margin-desktop: 64px
  section-gap: 80px
  container-max: 1200px
---

## Brand & Style
The design system evolves into "Serene Radiance," a visual narrative that balances the calming influence of coastal horizons with the vibrant energy of new beginnings. It targets a premium demographic seeking meaningful matrimonial connections, evoking an emotional response of optimism, warmth, and high-end reliability.

The design style is **Corporate Modern with a Warm Minimalist influence**. It prioritizes clarity and breathability, utilizing expansive whitespace and high-quality editorial layouts. By introducing a vibrant orange as the primary driver for action, the brand shifts from purely tranquil to proactive and inviting, ensuring the "premium" feel is maintained through structured typography and sophisticated color layering rather than visual clutter.

## Colors
The color strategy centers on the interplay between **Vibrant Orange (#E67E22)** and **Premium Light Blue (#7FB3D5)**. Orange is the primary action color, used for buttons, key calls-to-action, and critical navigation points to signify energy and warmth. The Light Blue serves as the primary brand anchor, providing a serene backdrop that ensures the vibrant orange feels intentional and sophisticated rather than overwhelming.

The background remains grounded in **Cream Base (#F9F7F2)** to provide a tactile, artisanal texture. **Ocean Deep (#0C2A46)** is reserved for high-contrast typography and essential structural elements, while **Soft Sky (#DCEBF2)** acts as a subtle container color to differentiate content zones without introducing heavy borders.

## Typography
The typography system relies on a classical-modernist pairing. **Playfair Display** is the expressive voice of the brand, used for all display and headline levels to convey heritage, elegance, and the "premium" nature of the service. 

**Inter** provides the functional foundation, used for body text, data points, and labels. This pairing ensures that while the brand feels high-fashion and editorial, the actual user experience of reading profiles and communicating remains effortless and legible. Use all-caps with `label-sm` for category headers to create a rhythmic hierarchy that feels organized and professional.

## Layout & Spacing
This design system utilizes a **Fixed Grid** model for desktop experiences, centered at 1200px, to maintain an editorial and controlled aesthetic. On mobile devices, the layout transitions to a fluid 4-column grid with 20px side margins.

The spacing philosophy is defined by "Luxurious Breathability." A generous 80px `section-gap` is used to separate major content blocks, preventing the interface from feeling crowded. Inside components, a 24px gutter provides ample room for photography and data to coexist without friction. All spacing is derived from an 8px base unit to ensure mathematical harmony.

## Elevation & Depth
Hierarchy is established through **Tonal Layers** and tinted **Ambient Shadows**, avoiding sterile grays in favor of a cohesive color temperature.

- **Level 0 (Foundation):** Cream Base (#F9F7F2) provides the primary canvas.
- **Level 1 (Interaction):** White (#FFFFFF) cards feature a soft shadow (0px 4px 20px, 6% opacity) tinted with Horizon Blue.
- **Level 2 (Navigation/Modals):** Elements that sit above the main content use a more defined shadow (0px 10px 30px, 10% opacity) also tinted with the brand's blue tones.

Use 1px "Ghost Borders" in `Soft Sky` (#DCEBF2) to define the boundaries of secondary elements, maintaining a light and airy feel.

## Shapes
The shape language is **Rounded**, utilizing a 0.5rem (8px) base to ensure the UI feels approachable and gentle. 

To reinforce the premium editorial feel, larger content containers and profile cards utilize `rounded-xl` (1.5rem/24px) to frame imagery elegantly. Interactive elements like input fields and primary buttons use a slightly more disciplined `rounded-md` (0.75rem/12px), striking a balance between the soft brand motif and the precision required for functional components.

## Components
- **Buttons:** Primary buttons are the focal point, utilizing the Vibrant Orange (#E67E22) with white text. Secondary buttons should use a ghost style with a Light Blue border.
- **Cards:** Profile and content cards feature a white background with a 24px corner radius. Padding within cards should be a minimum of 24px to preserve the high-end feel.
- **Input Fields:** Styled with a 1px `Soft Sky` border and a `Cream Base` fill. On focus, the border transitions to Vibrant Orange with a subtle outer glow.
- **Chips & Badges:** Tags for interests or traits should be pill-shaped with a `Soft Sky` background and `Horizon Blue` text for high legibility and low visual noise.
- **Lists:** Data-heavy lists must use 16px vertical padding and 1px `Soft Sky` dividers to ensure the information remains scannable and premium.
- **Key Actions:** Any "emotional" actions (e.g., Send Interest, Connect) must use the primary orange to ensure they are the most prominent elements on the screen.