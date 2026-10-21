# common_test_drupal_goto_alter()

- **Type:** Function
- **File:** [`modules/simpletest/tests/common_test.module`](_file.md), lines 95–99 · [local source](../../../../../source/modules/simpletest/tests/common_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module#L95-L99)
- **Module/theme:** batch_test
- **Implements:** [hook_drupal_goto_alter()](../../../system/system.api.php/hook_drupal_goto_alter.md)

## Signature

```php
function common_test_drupal_goto_alter(&$path, &$options, &$http_response_code)
```

## Documentation

```text
Implements hook_drupal_goto_alter().
```

## Code

```php
function common_test_drupal_goto_alter(&$path, &$options, &$http_response_code) {
  if ($path == 'common-test/drupal_goto/fail') {
    $path = 'common-test/drupal_goto/redirect';
  }
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/common_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
