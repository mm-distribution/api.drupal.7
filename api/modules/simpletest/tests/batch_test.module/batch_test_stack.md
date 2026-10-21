# batch_test_stack()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 503–513 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L503-L513)
- **Module/theme:** batch_test

## Signature

```php
function batch_test_stack($data = NULL, $reset = FALSE)
```

## Documentation

```text
Helper function: store or retrieve traced execution data.
```

## Code

```php
function batch_test_stack($data = NULL, $reset = FALSE) {
  if ($reset) {
    variable_del('batch_test_stack');
  }
  if (!isset($data)) {
    return variable_get('batch_test_stack', array());
  }
  $stack = variable_get('batch_test_stack', array());
  $stack[] = $data;
  variable_set('batch_test_stack', $stack);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
