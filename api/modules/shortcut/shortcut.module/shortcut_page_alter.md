# shortcut_page_alter()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 701–707 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L701-L707)
- **Module/theme:** shortcut
- **Implements:** [hook_page_alter()](../../system/system.api.php/hook_page_alter.md)

## Signature

```php
function shortcut_page_alter(&$page)
```

## Documentation

```text
Implements hook_page_alter().
```

## Code

```php
function shortcut_page_alter(&$page) {
  if (isset($page['page_top']['toolbar'])) {
    // If the toolbar is available, add a pre-render function to display the
    // current shortcuts in the toolbar drawer.
    $page['page_top']['toolbar']['#pre_render'][] = 'shortcut_toolbar_pre_render';
  }
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
