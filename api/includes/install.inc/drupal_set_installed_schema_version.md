# drupal_set_installed_schema_version()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 177–185 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L177-L185)

## Signature

```php
function drupal_set_installed_schema_version($module, $version)
```

## Documentation

```text
Update the installed version information for a module.

@param $module
  A module name.
@param $version
  The new schema version.
```

## Code

```php
function drupal_set_installed_schema_version($module, $version) {
  db_update('system')
    ->fields(array('schema_version' => $version))
    ->condition('name', $module)
    ->execute();

  // Reset the static cache of module schema versions.
  drupal_get_installed_schema_version(NULL, TRUE);
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
