# modules/color/color.module

- **Source:** [local](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · 817 lines
- **Module/theme:** color

## File documentation

```text
@file
Allows users to change the color scheme of themes.
```

## Functions (derived index)

- [color_help()](color_help.md) — Implements hook_help().
- [color_theme()](color_theme.md) — Implements hook_theme().
- [color_form_system_theme_settings_alter()](color_form_system_theme_settings_alter.md) — Implements hook_form_FORM_ID_alter().
- [color_form_system_themes_alter()](color_form_system_themes_alter.md) — Implements hook_form_FORM_ID_alter().
- [_color_theme_select_form_alter()](_color_theme_select_form_alter.md) — Helper for hook_form_FORM_ID_alter() implementations.
- [_color_html_alter()](_color_html_alter.md) — Replaces style sheets with color-altered style sheets.
- [_color_page_alter()](_color_page_alter.md) — Replaces the logo with a color-altered logo.
- [color_get_info()](color_get_info.md) — Retrieves the Color module information for a particular theme.
- [color_get_palette()](color_get_palette.md) — Retrieves the color palette for a particular theme.
- [color_scheme_form()](color_scheme_form.md) — Form constructor for the color configuration form for a particular theme.
- [theme_color_scheme_form()](theme_color_scheme_form.md) — Returns HTML for a theme's color form.
- [color_palette_color_value()](color_palette_color_value.md) — Determines the value for a palette color field.
- [color_valid_hexadecimal_string()](color_valid_hexadecimal_string.md) — Determines if a hexadecimal CSS color string is valid.
- [color_scheme_form_validate()](color_scheme_form_validate.md) — Form validation handler for color_scheme_form().
- [color_scheme_form_submit()](color_scheme_form_submit.md) — Form submission handler for color_scheme_form().
- [_color_rewrite_stylesheet()](_color_rewrite_stylesheet.md) — Rewrites the stylesheet to match the colors in the palette.
- [_color_save_stylesheet()](_color_save_stylesheet.md) — Saves the rewritten stylesheet to disk.
- [_color_render_images()](_color_render_images.md) — Renders images that match a given palette.
- [_color_shift()](_color_shift.md) — Shifts a given color, using a reference pair and a target blend color.
- [_color_gd()](_color_gd.md) — Converts a hex triplet into a GD color.
- [_color_blend()](_color_blend.md) — Blends two hex colors and returns the GD color.
- [_color_unpack()](_color_unpack.md) — Converts a hex color into an RGB triplet.
- [_color_pack()](_color_pack.md) — Converts an RGB triplet to a hex color.
- [_color_hsl2rgb()](_color_hsl2rgb.md) — Converts an HSL triplet into RGB.
- [_color_hue2rgb()](_color_hue2rgb.md) — Helper function for _color_hsl2rgb().
- [_color_rgb2hsl()](_color_rgb2hsl.md) — Converts an RGB triplet to HSL.

---
_Drupal 7.103 · Licensed GPL-2.0-or-later (see LICENSE)._
