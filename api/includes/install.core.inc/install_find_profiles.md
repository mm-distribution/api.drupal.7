# install_find_profiles()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 1035–1037 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L1035-L1037)

## Signature

```php
function install_find_profiles()
```

## Documentation

```text
Finds all .profile files.
```

## Code

```php
function install_find_profiles() {
  return file_scan_directory('./profiles', '/\.profile$/', array('key' => 'name'));
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
