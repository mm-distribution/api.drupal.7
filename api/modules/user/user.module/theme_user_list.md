# theme_user_list()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1559–1570 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1559-L1570)
- **Module/theme:** user
- **Topics:** [themeable](../../../topics/themeable.md)

## Signature

```php
function theme_user_list($variables)
```

## Documentation

```text
Returns HTML for a list of users.

@param $variables
  An associative array containing:
  - users: An array with user objects. Should contain at least the name and
    uid.
  - title: (optional) Title to pass on to theme_item_list().

@ingroup themeable
```

## Code

```php
function theme_user_list($variables) {
  $users = $variables['users'];
  $title = $variables['title'];
  $items = array();

  if (!empty($users)) {
    foreach ($users as $user) {
      $items[] = theme('username', array('account' => $user));
    }
  }
  return theme('item_list', array('items' => $items, 'title' => $title));
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
