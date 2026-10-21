# _color_gd()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 714–717 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L714-L717)
- **Module/theme:** color

## Signature

```php
function _color_gd($img, $hex)
```

## Documentation

```text
Converts a hex triplet into a GD color.
```

## Code

```php
function _color_gd($img, $hex) {
  $c = array_merge(array($img), _color_unpack($hex));
  return call_user_func_array('imagecolorallocate', $c);
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
