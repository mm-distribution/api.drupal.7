# url_alter_test_url_inbound_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/url_alter_test.module`](_file.md), lines 32–53 · [local source](../../../../../source/modules/simpletest/tests/url_alter_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/url_alter_test.module#L32-L53)
- **Module/theme:** batch_test
- **Implements:** [hook_url_inbound_alter()](../../../system/system.api.php/hook_url_inbound_alter.md)

## Signature

```php
function url_alter_test_url_inbound_alter(&$path, $original_path, $path_language)
```

## Documentation

```text
Implements hook_url_inbound_alter().
```

## Code

```php
function url_alter_test_url_inbound_alter(&$path, $original_path, $path_language) {
  if (!request_path() && !empty($_GET['q'])) {
    drupal_set_message("\$_GET['q'] is non-empty with an empty request path.");
  }

  // Rewrite user/username to user/uid.
  if (preg_match('!^user/([^/]+)(/.*)?!', $path, $matches)) {
    if ($account = user_load_by_name($matches[1])) {
      $matches += array(2 => '');
      $path = 'user/' . $account->uid . $matches[2];
    }
  }

  // Rewrite community/ to forum/.
  if ($path == 'community' || strpos($path, 'community/') === 0) {
    $path = 'forum' . substr($path, 9);
  }

  if ($path == 'url-alter-test/bar') {
    $path = 'url-alter-test/foo';
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/url_alter_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/url_alter_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
