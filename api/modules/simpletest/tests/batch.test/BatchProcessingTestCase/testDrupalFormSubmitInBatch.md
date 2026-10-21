# BatchProcessingTestCase::testDrupalFormSubmitInBatch()

- **Type:** Method
- **File:** [`modules/simpletest/tests/batch.test`](../_file.md), lines 132–138 · [local source](../../../../../../source/modules/simpletest/tests/batch.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test#L132-L138)
- **Class:** [BatchProcessingTestCase](../BatchProcessingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalFormSubmitInBatch()
```

## Documentation

```text
Test that drupal_form_submit() can run within a batch operation.
```

## Code

```php
  function testDrupalFormSubmitInBatch() {
    // Displaying the page triggers a batch that programmatically submits a
    // form.
    $value = rand(0, 255);
    $this->drupalGet('batch-test/nested-programmatic/' . $value);
    $this->assertEqual(batch_test_stack(), array('mock form submitted with value = ' . $value), t('drupal_form_submit() ran successfully within a batch operation.'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test) · Licensed GPL-2.0-or-later (see LICENSE)._
