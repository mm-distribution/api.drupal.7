# translation_permission()

- **Type:** Function
- **File:** [`modules/translation/translation.module`](_file.md), lines 108–114 · [local source](../../../../source/modules/translation/translation.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module#L108-L114)
- **Module/theme:** translation
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function translation_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function translation_permission() {
  return array(
    'translate content' => array(
      'title' => t('Translate content'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/translation/translation.module](https://github.com/drupal/drupal/blob/7.103/modules/translation/translation.module) · Licensed GPL-2.0-or-later (see LICENSE)._
