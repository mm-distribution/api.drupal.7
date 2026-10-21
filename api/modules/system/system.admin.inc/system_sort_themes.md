# system_sort_themes()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 970–978 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L970-L978)
- **Module/theme:** system

## Signature

```php
function system_sort_themes($a, $b)
```

## Documentation

```text
Sorts themes by their names, with the default theme listed first.

Callback for uasort() within system_themes_page().

@see system_sort_modules_by_info_name().
```

## Code

```php
function system_sort_themes($a, $b) {
  if ($a->is_default) {
    return -1;
  }
  if ($b->is_default) {
    return 1;
  }
  return strcasecmp($a->info['name'], $b->info['name']);
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
