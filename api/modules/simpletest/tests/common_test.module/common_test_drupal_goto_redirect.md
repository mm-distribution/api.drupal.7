# common_test_drupal_goto_redirect()

- **Type:** Function
- **File:** [`modules/simpletest/tests/common_test.module`](_file.md), lines 67–69 · [local source](../../../../../source/modules/simpletest/tests/common_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module#L67-L69)
- **Module/theme:** batch_test

## Signature

```php
function common_test_drupal_goto_redirect()
```

## Documentation

```text
Redirect using drupal_goto().
```

## Code

```php
function common_test_drupal_goto_redirect() {
  drupal_goto('common-test/drupal_goto');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/common_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
