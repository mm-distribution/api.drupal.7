# _color_hue2rgb()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 781–788 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L781-L788)
- **Module/theme:** color

## Signature

```php
function _color_hue2rgb($m1, $m2, $h)
```

## Documentation

```text
Helper function for _color_hsl2rgb().
```

## Code

```php
function _color_hue2rgb($m1, $m2, $h) {
  $h = ($h < 0) ? $h + 1 : (($h > 1) ? $h - 1 : $h);
  if ($h * 6 < 1) return $m1 + ($m2 - $m1) * $h * 6;
  if ($h * 2 < 1) return $m2;
  if ($h * 3 < 2) return $m1 + ($m2 - $m1) * (0.66666 - $h) * 6;

  return $m1;
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
