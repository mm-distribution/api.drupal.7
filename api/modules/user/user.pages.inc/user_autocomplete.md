# user_autocomplete()

- **Type:** Function
- **File:** [`modules/user/user.pages.inc`](_file.md), lines 11–21 · [local source](../../../../source/modules/user/user.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc#L11-L21)
- **Module/theme:** user

## Signature

```php
function user_autocomplete($string = '')
```

## Documentation

```text
Menu callback; Retrieve a JSON object containing autocomplete suggestions for existing users.
```

## Code

```php
function user_autocomplete($string = '') {
  $matches = array();
  if ($string) {
    $result = db_select('users')->fields('users', array('name'))->condition('name', db_like($string) . '%', 'LIKE')->range(0, 10)->execute();
    foreach ($result as $user) {
      $matches[$user->name] = check_plain($user->name);
    }
  }

  drupal_json_output($matches);
}
```

---
_Drupal 7.103 · [modules/user/user.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/user/user.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
