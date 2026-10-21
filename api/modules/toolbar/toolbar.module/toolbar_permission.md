# toolbar_permission()

- **Type:** Function
- **File:** [`modules/toolbar/toolbar.module`](_file.md), lines 28–34 · [local source](../../../../source/modules/toolbar/toolbar.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module#L28-L34)
- **Module/theme:** toolbar
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function toolbar_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function toolbar_permission() {
  return array(
    'access toolbar' => array(
      'title' => t('Use the administration toolbar'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/toolbar/toolbar.module](https://github.com/drupal/drupal/blob/7.103/modules/toolbar/toolbar.module) · Licensed GPL-2.0-or-later (see LICENSE)._
