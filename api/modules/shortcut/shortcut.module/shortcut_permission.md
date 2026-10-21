# shortcut_permission()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 50–64 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L50-L64)
- **Module/theme:** shortcut
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function shortcut_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function shortcut_permission() {
  return array(
    'administer shortcuts' => array(
      'title' => t('Administer shortcuts'),
    ),
    'customize shortcut links' => array(
      'title' => t('Edit current shortcut set'),
      'description' => t('Editing the current shortcut set will affect other users if that set has been assigned to or selected by other users. Granting "Select any shortcut set" permission along with this permission will grant permission to edit any shortcut set.'),
    ),
    'switch shortcut sets' => array(
      'title' => t('Select any shortcut set'),
      'description' => t('From all shortcut sets, select one to be own active set. Without this permission, an administrator selects shortcut sets for users.'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
