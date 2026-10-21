# contextual_permission()

- **Type:** Function
- **File:** [`modules/contextual/contextual.module`](_file.md), lines 29–36 · [local source](../../../../source/modules/contextual/contextual.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/contextual/contextual.module#L29-L36)
- **Module/theme:** contextual
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function contextual_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function contextual_permission() {
  return array(
    'access contextual links' => array(
      'title' => t('Use contextual links'),
      'description' => t('Use contextual links to perform actions related to elements on a page.'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/contextual/contextual.module](https://github.com/drupal/drupal/blob/7.103/modules/contextual/contextual.module) · Licensed GPL-2.0-or-later (see LICENSE)._
