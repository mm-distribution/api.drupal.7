# shortcut_block_info()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 189–195 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L189-L195)
- **Module/theme:** shortcut
- **Implements:** [hook_block_info()](../../block/block.api.php/hook_block_info.md)

## Signature

```php
function shortcut_block_info()
```

## Documentation

```text
Implements hook_block_info().
```

## Code

```php
function shortcut_block_info() {
  $blocks['shortcuts']['info'] = t('Shortcuts');
  // Shortcut blocks can't be cached because each menu item can have a custom
  // access callback. menu.inc manages its own caching.
  $blocks['shortcuts']['cache'] = DRUPAL_NO_CACHE;
  return $blocks;
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
