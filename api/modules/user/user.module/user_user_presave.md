# user_user_presave()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1317–1340 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1317-L1340)
- **Module/theme:** user
- **Implements:** [hook_user_presave()](../user.api.php/hook_user_presave.md)

## Signature

```php
function user_user_presave(&$edit, $account, $category)
```

## Documentation

```text
Implements hook_user_presave().
```

## Code

```php
function user_user_presave(&$edit, $account, $category) {
  if ($category == 'account' || $category == 'register') {
    if (!empty($edit['picture_upload'])) {
      $edit['picture'] = $edit['picture_upload'];
    }
    // Delete picture if requested, and if no replacement picture was given.
    elseif (!empty($edit['picture_delete'])) {
      $edit['picture'] = NULL;
    }
  }

  // Filter out roles with empty values to avoid granting extra roles when
  // processing custom form submissions.
  if (isset($edit['roles'])) {
    $edit['roles'] = array_filter($edit['roles']);
  }

  // Move account cancellation information into $user->data.
  foreach (array('user_cancel_method', 'user_cancel_notify') as $key) {
    if (isset($edit[$key])) {
      $edit['data'][$key] = $edit[$key];
    }
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
