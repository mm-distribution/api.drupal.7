# common_test_drupal_goto_redirect_advanced()

- **Type:** Function
- **File:** [`modules/simpletest/tests/common_test.module`](_file.md), lines 74–76 · [local source](../../../../../source/modules/simpletest/tests/common_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module#L74-L76)
- **Module/theme:** batch_test

## Signature

```php
function common_test_drupal_goto_redirect_advanced()
```

## Documentation

```text
Redirect using drupal_goto().
```

## Code

```php
function common_test_drupal_goto_redirect_advanced() {
  drupal_goto('common-test/drupal_goto', array('query' => array('foo' => '123')), 301);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/common_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
