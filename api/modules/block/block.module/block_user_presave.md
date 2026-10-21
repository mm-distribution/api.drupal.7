# block_user_presave()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 611–615 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L611-L615)
- **Module/theme:** block
- **Implements:** [hook_user_presave()](../../user/user.api.php/hook_user_presave.md)

## Signature

```php
function block_user_presave(&$edit, $account, $category)
```

## Documentation

```text
Implements hook_user_presave().
```

## Code

```php
function block_user_presave(&$edit, $account, $category) {
  if (isset($edit['block'])) {
    $edit['data']['block'] = $edit['block'];
  }
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
