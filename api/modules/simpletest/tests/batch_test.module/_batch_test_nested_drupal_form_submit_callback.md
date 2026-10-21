# _batch_test_nested_drupal_form_submit_callback()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 282–285 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L282-L285)
- **Module/theme:** batch_test

## Signature

```php
function _batch_test_nested_drupal_form_submit_callback($value)
```

## Documentation

```text
Batch operation: submits form_test_mock_form using drupal_form_submit().
```

## Code

```php
function _batch_test_nested_drupal_form_submit_callback($value) {
  $state['values']['test_value'] = $value;
  drupal_form_submit('batch_test_mock_form', $state);
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
