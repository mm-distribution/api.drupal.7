# locale_permission()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 249–259 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L249-L259)
- **Module/theme:** locale
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function locale_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function locale_permission() {
  return array(
    'administer languages' => array(
      'title' => t('Administer languages'),
    ),
    'translate interface' => array(
      'title' => t('Translate interface texts'),
      'restrict access' => TRUE,
    ),
  );
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
