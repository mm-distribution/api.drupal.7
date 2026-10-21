# system_permission()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 219–256 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L219-L256)
- **Module/theme:** system
- **Implements:** [hook_permission()](../system.api.php/hook_permission.md)

## Signature

```php
function system_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function system_permission() {
  return array(
    'administer modules' => array(
      'title' => t('Administer modules'),
    ),
    'administer site configuration' => array(
      'title' => t('Administer site configuration'),
      'restrict access' => TRUE,
    ),
    'administer themes' => array(
      'title' => t('Administer themes'),
    ),
    'administer software updates' => array(
      'title' => t('Administer software updates'),
      'restrict access' => TRUE,
    ),
    'administer actions' => array(
      'title' => t('Administer actions'),
    ),
    'access administration pages' => array(
      'title' => t('Use the administration pages and help'),
    ),
    'access site in maintenance mode' => array(
      'title' => t('Use the site in maintenance mode'),
    ),
    'view the administration theme' => array(
      'title' => t('View the administration theme'),
      'description' => variable_get('admin_theme') ? '' : t('This is only used when the site is configured to use a separate administration theme on the <a href="@appearance-url">Appearance</a> page.', array('@appearance-url' => url('admin/appearance'))),
    ),
    'access site reports' => array(
      'title' => t('View site reports'),
      'restrict access' => TRUE,
    ),
    'block IP addresses' => array(
      'title' => t('Block IP addresses'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
