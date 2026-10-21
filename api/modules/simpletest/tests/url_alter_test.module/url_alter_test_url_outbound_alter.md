# url_alter_test_url_outbound_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/url_alter_test.module`](_file.md), lines 58–71 · [local source](../../../../../source/modules/simpletest/tests/url_alter_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/url_alter_test.module#L58-L71)
- **Module/theme:** batch_test
- **Implements:** [hook_url_outbound_alter()](../../../system/system.api.php/hook_url_outbound_alter.md)

## Signature

```php
function url_alter_test_url_outbound_alter(&$path, &$options, $original_path)
```

## Documentation

```text
Implements hook_url_outbound_alter().
```

## Code

```php
function url_alter_test_url_outbound_alter(&$path, &$options, $original_path) {
  // Rewrite user/uid to user/username.
  if (preg_match('!^user/([0-9]+)(/.*)?!', (string) $path, $matches)) {
    if ($account = user_load($matches[1])) {
      $matches += array(2 => '');
      $path = 'user/' . $account->name . $matches[2];
    }
  }

  // Rewrite forum/ to community/.
  if ($path == 'forum' || strpos((string) $path, 'forum/') === 0) {
    $path = 'community' . substr($path, 5);
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/url_alter_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/url_alter_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
