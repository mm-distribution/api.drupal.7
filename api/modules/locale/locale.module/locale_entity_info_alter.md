# locale_entity_info_alter()

- **Type:** Function
- **File:** [`modules/locale/locale.module`](_file.md), lines 525–530 · [local source](../../../../source/modules/locale/locale.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module#L525-L530)
- **Module/theme:** locale
- **Implements:** [hook_entity_info_alter()](../../system/system.api.php/hook_entity_info_alter.md)

## Signature

```php
function locale_entity_info_alter(&$entity_info)
```

## Documentation

```text
Implements hook_entity_info_alter().
```

## Code

```php
function locale_entity_info_alter(&$entity_info) {
  $entity_info['node']['translation']['locale'] = TRUE;
  if (isset($entity_info['comment'])) {
    $entity_info['comment']['translation']['locale'] = TRUE;
  }
}
```

---
_Drupal 7.103 · [modules/locale/locale.module](https://github.com/drupal/drupal/blob/7.103/modules/locale/locale.module) · Licensed GPL-2.0-or-later (see LICENSE)._
