# _color_rgb2hsl()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 793–816 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L793-L816)
- **Module/theme:** color

## Signature

```php
function _color_rgb2hsl($rgb)
```

## Documentation

```text
Converts an RGB triplet to HSL.
```

## Code

```php
function _color_rgb2hsl($rgb) {
  $r = $rgb[0];
  $g = $rgb[1];
  $b = $rgb[2];
  $min = min($r, min($g, $b));
  $max = max($r, max($g, $b));
  $delta = $max - $min;
  $l = ($min + $max) / 2;
  $s = 0;

  if ($l > 0 && $l < 1) {
    $s = $delta / ($l < 0.5 ? (2 * $l) : (2 - 2 * $l));
  }

  $h = 0;
  if ($delta > 0) {
    if ($max == $r && $max != $g) $h += ($g - $b) / $delta;
    if ($max == $g && $max != $b) $h += (2 + ($b - $r) / $delta);
    if ($max == $b && $max != $r) $h += (4 + ($r - $g) / $delta);
    $h /= 6;
  }

  return array($h, $s, $l);
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
