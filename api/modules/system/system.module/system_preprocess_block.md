# system_preprocess_block()

- **Type:** Function
- **File:** [`modules/system/system.module`](_file.md), lines 2135–2140 · [local source](../../../../source/modules/system/system.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module#L2135-L2140)
- **Module/theme:** system

## Signature

```php
function system_preprocess_block(&$variables)
```

## Documentation

```text
Implements hook_preprocess_block().
```

## Code

```php
function system_preprocess_block(&$variables) {
  // System menu blocks should get the same class as menu module blocks.
  if ($variables['block']->module == 'system' && in_array($variables['block']->delta, array_keys(menu_list_system_menus()))) {
    $variables['classes_array'][] = 'block-menu';
  }
}
```

---
_Drupal 7.103 · [modules/system/system.module](https://github.com/drupal/drupal/blob/7.103/modules/system/system.module) · Licensed GPL-2.0-or-later (see LICENSE)._
