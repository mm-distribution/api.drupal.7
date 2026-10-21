# _color_blend()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 722–731 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L722-L731)
- **Module/theme:** color

## Signature

```php
function _color_blend($img, $hex1, $hex2, $alpha)
```

## Documentation

```text
Blends two hex colors and returns the GD color.
```

## Code

```php
function _color_blend($img, $hex1, $hex2, $alpha) {
  $in1 = _color_unpack($hex1);
  $in2 = _color_unpack($hex2);
  $out = array($img);
  for ($i = 0; $i < 3; ++$i) {
    $out[] = (int) ($in1[$i] + ($in2[$i] - $in1[$i]) * $alpha);
  }

  return call_user_func_array('imagecolorallocate', $out);
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
