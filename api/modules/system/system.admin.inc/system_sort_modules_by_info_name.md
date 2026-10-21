# system_sort_modules_by_info_name()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 959–961 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L959-L961)
- **Module/theme:** system

## Signature

```php
function system_sort_modules_by_info_name($a, $b)
```

## Documentation

```text
Array sorting callback; sorts modules or themes by their name.
```

## Code

```php
function system_sort_modules_by_info_name($a, $b) {
  return strcasecmp($a->info['name'], $b->info['name']);
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
