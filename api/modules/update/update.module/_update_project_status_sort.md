# _update_project_status_sort()

- **Type:** Function
- **File:** [`modules/update/update.module`](_file.md), lines 636–644 · [local source](../../../../source/modules/update/update.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module#L636-L644)
- **Module/theme:** update

## Signature

```php
function _update_project_status_sort($a, $b)
```

## Documentation

```text
Orders projects based on their status.

Callback for uasort() within update_requirements().
```

## Code

```php
function _update_project_status_sort($a, $b) {
  // The status constants are numerically in the right order, so we can
  // usually subtract the two to compare in the order we want. However,
  // negative status values should be treated as if they are huge, since we
  // always want them at the bottom of the list.
  $a_status = $a['status'] > 0 ? $a['status'] : (-10 * $a['status']);
  $b_status = $b['status'] > 0 ? $b['status'] : (-10 * $b['status']);
  return $a_status - $b_status;
}
```

---
_Drupal 7.103 · [modules/update/update.module](https://github.com/drupal/drupal/blob/7.103/modules/update/update.module) · Licensed GPL-2.0-or-later (see LICENSE)._
