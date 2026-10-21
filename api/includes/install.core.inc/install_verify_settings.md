# install_verify_settings()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 849–863 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L849-L863)

## Signature

```php
function install_verify_settings()
```

## Documentation

```text
Verifies the existing settings in settings.php.
```

## Code

```php
function install_verify_settings() {
  global $databases;

  // Verify existing settings (if any).
  if (!empty($databases) && install_verify_pdo()) {
    $database = $databases['default']['default'];
    drupal_static_reset('conf_path');
    $settings_file = './' . conf_path(FALSE) . '/settings.php';
    $errors = install_database_errors($database, $settings_file);
    if (empty($errors)) {
      return TRUE;
    }
  }
  return FALSE;
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
