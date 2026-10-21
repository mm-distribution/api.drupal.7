# hook_url_inbound_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/system/system.api.php`](_file.md), lines 4328–4334 · [local source](../../../../source/modules/system/system.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php#L4328-L4334)
- **Module/theme:** system
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_url_inbound_alter(&$path, $original_path, $path_language)
```

## Documentation

```text
Alters inbound URL requests.

@param $path
  The path being constructed, which, if a path alias, has been resolved to a
  Drupal path by the database, and which also may have been altered by other
  modules before this one.
@param $original_path
  The original path, before being checked for path aliases or altered by any
  modules.
@param $path_language
  The language of the path.

@see drupal_get_normal_path()
```

## Code

```php
function hook_url_inbound_alter(&$path, $original_path, $path_language) {
  // Create the path user/me/edit, which allows a user to edit their account.
  if (preg_match('|^user/me/edit(/.*)?|', $path, $matches)) {
    global $user;
    $path = 'user/' . $user->uid . '/edit' . $matches[1];
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_url_inbound_alter()".

- [url_alter_test_url_inbound_alter()](../../simpletest/tests/url_alter_test.module/url_alter_test_url_inbound_alter.md) — `modules/simpletest/tests/url_alter_test.module`

---
_Drupal 7.103 · [modules/system/system.api.php](https://github.com/drupal/drupal/blob/7.103/modules/system/system.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
