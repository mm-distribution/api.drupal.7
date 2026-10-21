# block_theme()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 78–90 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L78-L90)
- **Module/theme:** block
- **Implements:** [hook_theme()](../../system/system.api.php/hook_theme.md)

## Signature

```php
function block_theme()
```

## Documentation

```text
Implements hook_theme().
```

## Code

```php
function block_theme() {
  return array(
    'block' => array(
      'render element' => 'elements',
      'template' => 'block',
    ),
    'block_admin_display_form' => array(
      'template' => 'block-admin-display-form',
      'file' => 'block.admin.inc',
      'render element' => 'form',
    ),
  );
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
