# file_test_file_move()

- **Type:** Function
- **File:** [`modules/simpletest/tests/file_test.module`](_file.md), lines 309–311 · [local source](../../../../../source/modules/simpletest/tests/file_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module#L309-L311)
- **Module/theme:** batch_test
- **Implements:** [hook_file_move()](../../../system/system.api.php/hook_file_move.md)

## Signature

```php
function file_test_file_move($file, $source)
```

## Documentation

```text
Implements hook_file_move().
```

## Code

```php
function file_test_file_move($file, $source) {
  _file_test_log_call('move', array($file, $source));
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/file_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/file_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
