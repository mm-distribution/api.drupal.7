# _system_sort_requirements()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2862–2870 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2862-L2870)
- **Module/theme:** system

## Signature

```php
function _system_sort_requirements($a, $b)
```

## Documentation

```text
Helper function to sort requirements.
```

## Code

```php
function _system_sort_requirements($a, $b) {
  if (!isset($a['weight'])) {
    if (!isset($b['weight'])) {
      return strcasecmp($a['title'], $b['title']);
    }
    return -$b['weight'];
  }
  return isset($b['weight']) ? $a['weight'] - $b['weight'] : $a['weight'];
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
