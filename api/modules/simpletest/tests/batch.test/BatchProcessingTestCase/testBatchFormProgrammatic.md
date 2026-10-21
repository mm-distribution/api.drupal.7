# BatchProcessingTestCase::testBatchFormProgrammatic()

- **Type:** Method
- **File:** [`modules/simpletest/tests/batch.test`](../_file.md), lines 116–127 · [local source](../../../../../../source/modules/simpletest/tests/batch.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test#L116-L127)
- **Class:** [BatchProcessingTestCase](../BatchProcessingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testBatchFormProgrammatic()
```

## Documentation

```text
Test batches defined in a programmatically submitted form.

Same as above, but the form is submitted through drupal_form_execute().
```

## Code

```php
  function testBatchFormProgrammatic() {
    // Batches 1, 2 and 3 are triggered in sequence by different submit
    // handlers. Each submit handler modify the submitted 'value'.
    $value = rand(0, 255);
    $this->drupalGet('batch-test/programmatic/' . $value);
    // Check that result messages are present and in the correct order.
    $this->assertBatchMessages($this->_resultMessages('chained'), t('Batches defined in separate submit handlers performed successfully.'));
    // The stack contains execution order of batch callbacks and submit
    // hanlders and logging of corresponding $form_state[{values'].
    $this->assertEqual(batch_test_stack(), $this->_resultStack('chained', $value), t('Execution order was correct, and $form_state is correctly persisted.'));
    $this->assertText('Got out of a programmatic batched form.', t('Page execution continues normally.'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test) · Licensed GPL-2.0-or-later (see LICENSE)._
