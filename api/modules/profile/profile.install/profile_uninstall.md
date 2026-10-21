# profile_uninstall()

- **Type:** Function
- **File:** [`modules/profile/profile.install`](_file.md), lines 11–13 · [local source](../../../../source/modules/profile/profile.install) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.install#L11-L13)
- **Module/theme:** profile
- **Implements:** [hook_uninstall()](../../system/system.api.php/hook_uninstall.md)

## Signature

```php
function profile_uninstall()
```

## Documentation

```text
Implements hook_uninstall().
```

## Code

```php
function profile_uninstall() {
  variable_del('profile_block_author_fields');
}
```

---
_Drupal 7.103 · [modules/profile/profile.install](https://github.com/drupal/drupal/blob/7.103/modules/profile/profile.install) · Licensed GPL-2.0-or-later (see LICENSE)._
