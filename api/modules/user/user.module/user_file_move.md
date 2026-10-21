# user_file_move()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 923–934 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L923-L934)
- **Module/theme:** user
- **Implements:** [hook_file_move()](../../system/system.api.php/hook_file_move.md)

## Signature

```php
function user_file_move($file, $source)
```

## Documentation

```text
Implements hook_file_move().
```

## Code

```php
function user_file_move($file, $source) {
  // If a user's picture is replaced with a new one, update the record in
  // the users table.
  if (isset($file->fid) && isset($source->fid) && $file->fid != $source->fid) {
    db_update('users')
      ->fields(array(
        'picture' => $file->fid,
      ))
      ->condition('picture', $source->fid)
      ->execute();
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
