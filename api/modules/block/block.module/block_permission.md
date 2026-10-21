# block_permission()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 95–101 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L95-L101)
- **Module/theme:** block
- **Implements:** [hook_permission()](../../system/system.api.php/hook_permission.md)

## Signature

```php
function block_permission()
```

## Documentation

```text
Implements hook_permission().
```

## Code

```php
function block_permission() {
  return array(
    'administer blocks' => array(
      'title' => t('Administer blocks'),
    ),
  );
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
