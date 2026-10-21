# user_search_execute()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 966–1007 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L966-L1007)
- **Module/theme:** user
- **Implements:** [hook_search_execute()](../../search/search.api.php/hook_search_execute.md)

## Signature

```php
function user_search_execute($keys = NULL, $conditions = NULL)
```

## Documentation

```text
Implements hook_search_execute().
```

## Code

```php
function user_search_execute($keys = NULL, $conditions = NULL) {
  $find = array();
  // Escape for LIKE matching.
  $keys = db_like($keys);
  // Replace wildcards with MySQL/PostgreSQL wildcards.
  $keys = preg_replace('!\*+!', '%', $keys);
  $query = db_select('users')->extend('PagerDefault');
  $query->fields('users', array('uid'));
  if (user_access('administer users')) {
    // Administrators can also search in the otherwise private email field,
    // and they don't need to be restricted to only active users.
    $query->fields('users', array('mail'));
    $query->condition(db_or()->
      condition('name', '%' . $keys . '%', 'LIKE')->
      condition('mail', '%' . $keys . '%', 'LIKE'));
  }
  else {
    // Regular users can only search via usernames, and we do not show them
    // blocked accounts.
    $query->condition('name', '%' . $keys . '%', 'LIKE')
      ->condition('status', 1);
  }
  $uids = $query
    ->limit(15)
    ->execute()
    ->fetchCol();
  $accounts = user_load_multiple($uids);

  $results = array();
  foreach ($accounts as $account) {
    $result = array(
      'title' => format_username($account),
      'link' => url('user/' . $account->uid, array('absolute' => TRUE)),
    );
    if (user_access('administer users')) {
      $result['title'] .= ' (' . $account->mail . ')';
    }
    $results[] = $result;
  }

  return $results;
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
