# _install_profile_modules_finished()

- **Type:** Function
- **File:** [`includes/install.core.inc`](_file.md), lines 1630–1634 · [local source](../../../source/includes/install.core.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc#L1630-L1634)

## Signature

```php
function _install_profile_modules_finished($success, $results, $operations)
```

## Documentation

```text
Implements callback_batch_finished().

'Finished' callback for module installation batch.
```

## Code

```php
function _install_profile_modules_finished($success, $results, $operations) {
  // Flush all caches to complete the module installation process. Subsequent
  // installation tasks will now have full access to the profile's modules.
  drupal_flush_all_caches();
}
```

---
_Drupal 7.103 · [includes/install.core.inc](https://github.com/drupal/drupal/blob/7.103/includes/install.core.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
