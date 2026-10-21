# drupal_load_updates()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 81–87 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L81-L87)

## Signature

```php
function drupal_load_updates()
```

## Documentation

```text
Loads .install files for installed modules to initialize the update system.
```

## Code

```php
function drupal_load_updates() {
  foreach (drupal_get_installed_schema_version(NULL, FALSE, TRUE) as $module => $schema_version) {
    if ($schema_version > -1) {
      module_load_install($module);
    }
  }
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
