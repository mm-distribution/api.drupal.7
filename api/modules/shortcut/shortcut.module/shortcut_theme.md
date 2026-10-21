# shortcut_theme()

- **Type:** Function
- **File:** [`modules/shortcut/shortcut.module`](_file.md), lines 177–184 · [local source](../../../../source/modules/shortcut/shortcut.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module#L177-L184)
- **Module/theme:** shortcut
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function shortcut_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function shortcut_theme() {
  return array(
    'shortcut_set_customize' => array(
      'render element' => 'form',
      'file' => 'shortcut.admin.inc',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/shortcut/shortcut.module](https://github.com/drupal/drupal/blob/7.103/modules/shortcut/shortcut.module) · Licensed GPL-2.0-or-later (see LICENSE)._
