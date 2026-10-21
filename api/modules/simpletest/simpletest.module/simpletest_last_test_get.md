# simpletest_last_test_get()

- **Type:** Function
- **File:** [`modules/simpletest/simpletest.module`](_file.md), lines 240–244 · [local source](../../../../source/modules/simpletest/simpletest.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module#L240-L244)
- **Module/theme:** simpletest

## Signature

```php
function simpletest_last_test_get($test_id)
```

## Documentation

```text
Get information about the last test that ran given a test ID.

@param $test_id
  The test ID to get the last test from.
@return
  Array containing the last database prefix used and the last test class
  that ran.
```

## Code

```php
function simpletest_last_test_get($test_id) {
  $last_prefix = db_query_range('SELECT last_prefix FROM {simpletest_test_id} WHERE test_id = :test_id', 0, 1, array(':test_id' => $test_id))->fetchField();
  $last_test_class = db_query_range('SELECT test_class FROM {simpletest} WHERE test_id = :test_id ORDER BY message_id DESC', 0, 1, array(':test_id' => $test_id))->fetchField();
  return array($last_prefix, $last_test_class);
}
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.module) · Licensed GPL-2.0-or-later (see LICENSE)._
