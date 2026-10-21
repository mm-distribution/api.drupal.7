# _color_unpack()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 736–747 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L736-L747)
- **Module/theme:** color

## Signature

```php
function _color_unpack($hex, $normalize = FALSE)
```

## Documentation

```text
Converts a hex color into an RGB triplet.
```

## Code

```php
function _color_unpack($hex, $normalize = FALSE) {
  $hex = substr($hex, 1);
  if (strlen($hex) == 3) {
    $hex = $hex[0] . $hex[0] . $hex[1] . $hex[1] . $hex[2] . $hex[2];
  }
  $c = hexdec($hex);
  for ($i = 16; $i >= 0; $i -= 8) {
    $out[] = (($c >> $i) & 0xFF) / ($normalize ? 255 : 1);
  }

  return $out;
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
