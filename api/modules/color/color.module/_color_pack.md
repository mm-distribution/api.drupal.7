# _color_pack()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 752–759 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L752-L759)
- **Module/theme:** color

## Signature

```php
function _color_pack($rgb, $normalize = FALSE)
```

## Documentation

```text
Converts an RGB triplet to a hex color.
```

## Code

```php
function _color_pack($rgb, $normalize = FALSE) {
  $out = 0;
  foreach ($rgb as $k => $v) {
    $out |= (((int) ($v * ($normalize ? 255 : 1))) << (16 - $k * 8));
  }

  return '#' . str_pad(dechex($out), 6, 0, STR_PAD_LEFT);
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
