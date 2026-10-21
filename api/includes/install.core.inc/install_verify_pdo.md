# install_verify_pdo()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 868–875 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L868-L875)

## Signature

```php
function install_verify_pdo()
```

## Documentation

```text
Verifies the PDO library.
```

## Code

```php
function install_verify_pdo() {
  // PDO was moved to PHP core in 5.2.0, but the old extension (targeting 5.0
  // and 5.1) is still available from PECL, and can still be built without
  // errors. To verify that the correct version is in use, we check the
  // PDO::ATTR_DEFAULT_FETCH_MODE constant, which is not available in the
  // PECL extension.
  return extension_loaded('pdo') && defined('PDO::ATTR_DEFAULT_FETCH_MODE');
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
