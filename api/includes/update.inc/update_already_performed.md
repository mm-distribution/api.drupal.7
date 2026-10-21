# update_already_performed()

- **Type:** Function
- **File:** [`includes/update.inc`](_file.md), lines 1419–1421 · [local source](../../../source/includes/update.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/update.inc#L1419-L1421)

## Signature

```php
function update_already_performed($module, $number)
```

## Documentation

```text
Determines if a module update has already been performed.

@param $module
  The name of the module.
@param $number
  The number of the update within that module.

@return
  TRUE if the database schema indicates that the update has already been
  performed; FALSE otherwise.
```

## Code

```php
function update_already_performed($module, $number) {
  return $number <= drupal_get_installed_schema_version($module);
}
```

---
_Drupal 7.103 · [includes/update.inc](https://github.com/drupal/drupal/blob/7.103/includes/update.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
