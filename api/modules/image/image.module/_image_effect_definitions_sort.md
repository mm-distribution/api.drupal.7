# _image_effect_definitions_sort()

- **Type:** Function
- **File:** [`modules/image/image.module`](_file.md), lines 1492–1494 · [local source](../../../../source/modules/image/image.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module#L1492-L1494)
- **Module/theme:** image

## Signature

```php
function _image_effect_definitions_sort($a, $b)
```

## Documentation

```text
Internal function for sorting image effect definitions through uasort().

@see image_effect_definitions()
```

## Code

```php
function _image_effect_definitions_sort($a, $b) {
  return strcasecmp($a['name'], $b['name']);
}
```

---
_Drupal 7.103 · [modules/image/image.module](https://github.com/drupal/drupal/blob/7.103/modules/image/image.module) · Licensed GPL-2.0-or-later (see LICENSE)._
