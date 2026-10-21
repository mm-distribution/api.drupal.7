# batch_test_nested_drupal_form_submit()

- **Type:** Function
- **File:** [`modules/simpletest/tests/batch_test.module`](_file.md), lines 270–277 · [local source](../../../../../source/modules/simpletest/tests/batch_test.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module#L270-L277)
- **Module/theme:** batch_test

## Signature

```php
function batch_test_nested_drupal_form_submit($value = 1)
```

## Documentation

```text
Menu callback: programmatically submits a form within a batch.
```

## Code

```php
function batch_test_nested_drupal_form_submit($value = 1) {
  // Set the batch and process it.
  $batch['operations'] = array(
    array('_batch_test_nested_drupal_form_submit_callback', array($value)),
  );
  batch_set($batch);
  batch_process('batch-test/redirect');
}
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch_test.module](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch_test.module) · Licensed GPL-2.0-or-later (see LICENSE)._
