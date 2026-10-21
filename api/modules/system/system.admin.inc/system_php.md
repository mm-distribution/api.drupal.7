# system_php()

- **Type:** Function
- **File:** [`modules/system/system.admin.inc`](_file.md), lines 2393–2397 · [local source](../../../../source/modules/system/system.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc#L2393-L2397)
- **Module/theme:** system

## Signature

```php
function system_php()
```

## Documentation

```text
Menu callback: return information about PHP.
```

## Code

```php
function system_php() {
  $phpinfo_flags = variable_get('sa_core_2023_004_phpinfo_flags', ~(INFO_VARIABLES | INFO_ENVIRONMENT));
  phpinfo($phpinfo_flags);
  drupal_exit();
}
```

---
_Drupal 7.103 · [modules/system/system.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/system/system.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
