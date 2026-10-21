# color_valid_hexadecimal_string()

- **Type:** Function
- **File:** [`modules/color/color.module`](_file.md), lines 340–342 · [local source](../../../../source/modules/color/color.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module#L340-L342)
- **Module/theme:** color

## Signature

```php
function color_valid_hexadecimal_string($color)
```

## Documentation

```text
Determines if a hexadecimal CSS color string is valid.

@param $color
  The string to check.

@return
  TRUE if the string is a valid hexadecimal CSS color string, or FALSE if it
  isn't.
```

## Code

```php
function color_valid_hexadecimal_string($color) {
  return preg_match('/^#([a-f0-9]{3}){1,2}$/iD', $color);
}
```

---
_Drupal 7.103 · [modules/color/color.module](https://github.com/drupal/drupal/blob/7.103/modules/color/color.module) · Licensed GPL-2.0-or-later (see LICENSE)._
