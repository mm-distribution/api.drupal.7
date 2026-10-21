# php_permission()

- **Type:** Function
- **File:** [`modules/php/php.module`](_file.md), lines 29–36 · [local source](../../../../source/modules/php/php.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/php/php.module#L29-L36)
- **Module/theme:** php
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function php_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function php_permission() {
  return array(
    'use PHP for settings' => array(
      'title' => t('Use PHP for settings'),
      'restrict access' => TRUE,
    ),
  );
}
```

---
_Drupal 7.103 · [modules/php/php.module](https://github.com/drupal/drupal/blob/7.103/modules/php/php.module) · Licensed GPL-2.0-or-later (see LICENSE)._
