# block_user_role_delete()

- **Type:** Function
- **File:** [`modules/block/block.module`](_file.md), lines 1053–1057 · [local source](../../../../source/modules/block/block.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module#L1053-L1057)
- **Module/theme:** block
- **Implements:** [hook_user_role_delete()](../../user/user.api.php/hook_user_role_delete.md)

## Signature

```php
function block_user_role_delete($role)
```

## Documentation

```text
Implements hook_user_role_delete().

Removes deleted role from blocks that use it.
```

## Code

```php
function block_user_role_delete($role) {
  db_delete('block_role')
    ->condition('rid', $role->rid)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/block/block.module](https://github.com/drupal/drupal/blob/7.103/modules/block/block.module) · Licensed GPL-2.0-or-later (see LICENSE)._
