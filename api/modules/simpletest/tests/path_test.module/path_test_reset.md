# path_test_reset()

- **Type:** Function
- **File:** [`modules/simpletest/tests/path_test.module`](_file.md), lines 11–13 · [local source](../../../../../source/modules/simpletest/tests/path_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path_test.module#L11-L13)
- **Module/theme:** batch_test

## Signature

```php
function path_test_reset()
```

## Documentation

```text
Resets the path test results.
```

## Code

```php
function path_test_reset() {
  variable_set('path_test_results', array());
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/path_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
