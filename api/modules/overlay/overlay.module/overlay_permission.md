# overlay_permission()

- **Type:** Function
- **File:** [`modules/overlay/overlay.module`](_file.md), lines 57–64 · [local source](../../../../source/modules/overlay/overlay.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module#L57-L64)
- **Module/theme:** overlay
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function overlay_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function overlay_permission() {
  return array(
    'access overlay' => array(
      'title' => t('Access the administrative overlay'),
      'description' => t('View administrative pages in the overlay.'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/overlay/overlay.module](https://github.com/drupal/drupal/blob/7.103/modules/overlay/overlay.module) · Licensed GPL-2.0-or-later (see LICENSE)._
