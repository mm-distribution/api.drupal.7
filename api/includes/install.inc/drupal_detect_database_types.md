# drupal_detect_database_types()

- **Type:** Function
- **File:** [`includes/install.inc`](_file.md), lines 237–245 · [local source](../../../source/includes/install.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.inc#L237-L245)

## Signature

```php
function drupal_detect_database_types()
```

## Documentation

```text
Detects all supported databases that are compiled into PHP.

@return
 An array of database types compiled into PHP.
```

## Code

```php
function drupal_detect_database_types() {
  $databases = drupal_get_database_types();

  foreach ($databases as $driver => $installer) {
    $databases[$driver] = $installer->name();
  }

  return $databases;
}
```

---
_Drupal 7.103 · [includes/install.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
