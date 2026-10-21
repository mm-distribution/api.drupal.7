# _color_rewrite_stylesheet()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 496–562 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L496-L562)
- **Module/theme:** color

## Signature

```php
function _color_rewrite_stylesheet($theme, &$info, &$paths, $palette, $style)
```

## Documentation

```text
Rewrites the stylesheet to match the colors in the palette.
```

## Code

```php
function _color_rewrite_stylesheet($theme, &$info, &$paths, $palette, $style) {
  $themes = list_themes();
  // Prepare color conversion table.
  $conversion = $palette;
  foreach ($conversion as $k => $v) {
    $conversion[$k] = drupal_strtolower($v);
  }
  $default = color_get_palette($theme, TRUE);

  // Split off the "Don't touch" section of the stylesheet.
  $split = "Color Module: Don't touch";
  if (strpos($style, $split) !== FALSE) {
    list($style, $fixed) = explode($split, $style);
  }

  // Find all colors in the stylesheet and the chunks in between.
  $style = preg_split('/(#[0-9a-f]{6}|#[0-9a-f]{3})/i', $style, -1, PREG_SPLIT_DELIM_CAPTURE);
  $is_color = FALSE;
  $output = '';
  $base = 'base';

  // Iterate over all the parts.
  foreach ($style as $chunk) {
    if ($is_color) {
      $chunk = drupal_strtolower($chunk);
      // Check if this is one of the colors in the default palette.
      if ($key = array_search($chunk, $default)) {
        $chunk = $conversion[$key];
      }
      // Not a pre-set color. Extrapolate from the base.
      else {
        $chunk = _color_shift($palette[$base], $default[$base], $chunk, $info['blend_target']);
      }
    }
    else {
      // Determine the most suitable base color for the next color.

      // 'a' declarations. Use link.
      if (preg_match('@[^a-z0-9_-](a)[^a-z0-9_-][^/{]*{[^{]+$@i', $chunk)) {
        $base = 'link';
      }
      // 'color:' styles. Use text.
      elseif (preg_match('/(?<!-)color[^{:]*:[^{#]*$/i', $chunk)) {
        $base = 'text';
      }
      // Reset back to base.
      else {
        $base = 'base';
      }
    }
    $output .= $chunk;
    $is_color = !$is_color;
  }
  // Append fixed colors segment.
  if (isset($fixed)) {
    $output .= $fixed;
  }

  // Replace paths to images.
  foreach ($paths['map'] as $before => $after) {
    $before = base_path() . $paths['source'] . $before;
    $before = preg_replace('`(^|/)(?!../)([^/]+)/../`', '$1', $before);
    $output = str_replace($before, $after, $output);
  }

  return $output;
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
