# user_block_view()

- **Type:** Function
- **File:** [`modules/user/user.module`](_file.md), lines 1448–1497 · [local source](../../../../source/modules/user/user.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module#L1448-L1497)
- **Module/theme:** user
- **Implements:** [hook_block_view()](../../block/block.api.php/hook_block_view.md)

## Signature

```php
function user_block_view($delta = '')
```

## Documentation

```text
Implements hook_block_view().
```

## Code

```php
function user_block_view($delta = '') {
  global $user;

  $block = array();

  switch ($delta) {
    case 'login':
      // For usability's sake, avoid showing two login forms on one page.
      if (!$user->uid && !(arg(0) == 'user' && !is_numeric(arg(1)))) {

        $block['subject'] = t('User login');
        $block['content'] = drupal_get_form('user_login_block');
      }
      return $block;

    case 'new':
      if (user_access('access content')) {
        // Retrieve a list of new users who have subsequently accessed the site successfully.
        $items = db_query_range('SELECT uid, name FROM {users} WHERE status <> 0 AND access <> 0 ORDER BY created DESC', 0, variable_get('user_block_whois_new_count', 5))->fetchAll();
        $output = theme('user_list', array('users' => $items));

        $block['subject'] = t('Who\'s new');
        $block['content'] = $output;
      }
      return $block;

    case 'online':
      if (user_access('access content')) {
        // Count users active within the defined period.
        $interval = REQUEST_TIME - variable_get('user_block_seconds_online', 900);

        // Perform database queries to gather online user lists. We use s.timestamp
        // rather than u.access because it is much faster.
        $authenticated_count = db_query("SELECT COUNT(DISTINCT s.uid) FROM {sessions} s WHERE s.timestamp >= :timestamp AND s.uid > 0", array(':timestamp' => $interval))->fetchField();

        $output = '<p>' . format_plural($authenticated_count, 'There is currently 1 user online.', 'There are currently @count users online.') . '</p>';

        // Display a list of currently online users.
        $max_users = variable_get('user_block_max_list_count', 10);
        if ($authenticated_count && $max_users) {
          $items = db_query_range('SELECT u.uid, u.name, MAX(s.timestamp) AS max_timestamp FROM {users} u INNER JOIN {sessions} s ON u.uid = s.uid WHERE s.timestamp >= :interval AND s.uid > 0 GROUP BY u.uid, u.name ORDER BY max_timestamp DESC', 0, $max_users, array(':interval' => $interval))->fetchAll();
          $output .= theme('user_list', array('users' => $items));
        }

        $block['subject'] = t('Who\'s online');
        $block['content'] = $output;
      }
      return $block;
  }
}
```

---
_Drupal 7.103 · [modules/user/user.module](https://github.com/drupal/drupal/blob/7.103/modules/user/user.module) · Licensed GPL-2.0-or-later (see LICENSE)._
