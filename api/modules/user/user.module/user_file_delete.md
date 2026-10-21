# user_file_delete()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 939–945 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L939-L945)
- **Module/theme:** user
- **Implements:** [hook_file_delete()](../../system/system.api.php/hook_file_delete.md)

## Signature

```php
function user_file_delete($file)
```

## Documentation

```text
Implements hook_file_delete().
```

## Code

```php
function user_file_delete($file) {
  // Remove any references to the file.
  db_update('users')
    ->fields(array('picture' => 0))
    ->condition('picture', $file->fid)
    ->execute();
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
