# _color_hsl2rgb()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 764–776 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L764-L776)
- **Module/theme:** color

## Signature

```php
function _color_hsl2rgb($hsl)
```

## Documentation

```text
Converts an HSL triplet into RGB.
```

## Code

```php
function _color_hsl2rgb($hsl) {
  $h = $hsl[0];
  $s = $hsl[1];
  $l = $hsl[2];
  $m2 = ($l <= 0.5) ? $l * ($s + 1) : $l + $s - $l*$s;
  $m1 = $l * 2 - $m2;

  return array(
    _color_hue2rgb($m1, $m2, $h + 0.33333),
    _color_hue2rgb($m1, $m2, $h),
    _color_hue2rgb($m1, $m2, $h - 0.33333),
  );
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
