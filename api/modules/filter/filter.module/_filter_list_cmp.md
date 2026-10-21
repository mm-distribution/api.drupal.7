# _filter_list_cmp()

- **Type:** Function
- **File:** [`modules/filter/filter.module`](_file.md), lines 632–634 · [local source](../../../../source/modules/filter/filter.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module#L632-L634)
- **Module/theme:** filter

## Signature

```php
function _filter_list_cmp($a, $b)
```

## Documentation

```text
Sorts an array of filters by filter name.

Callback for uasort() within filter_get_filters().
```

## Code

```php
function _filter_list_cmp($a, $b) {
  return strcmp($a['title'], $b['title']);
}
```

---
_Drupal 7.103 · [modules/filter/filter.module](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.module) · Licensed GPL-2.0-or-later (see LICENSE)._
