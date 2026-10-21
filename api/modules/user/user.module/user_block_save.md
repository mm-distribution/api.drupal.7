# user_block_save()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1430–1443 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1430-L1443)
- **Module/theme:** user
- **Implements:** [hook_block_save()](../../block/block.api.php/hook_block_save.md)

## Signature

```php
function user_block_save($delta = '', $edit = array())
```

## Documentation

```text
Implements hook_block_save().
```

## Code

```php
function user_block_save($delta = '', $edit = array()) {
  global $user;

  switch ($delta) {
    case 'new':
      variable_set('user_block_whois_new_count', $edit['user_block_whois_new_count']);
      break;

    case 'online':
      variable_set('user_block_seconds_online', $edit['user_block_seconds_online']);
      variable_set('user_block_max_list_count', $edit['user_block_max_list_count']);
      break;
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
