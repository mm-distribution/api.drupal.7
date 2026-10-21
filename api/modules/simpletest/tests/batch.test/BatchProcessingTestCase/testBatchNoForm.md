# BatchProcessingTestCase::testBatchNoForm()

- **Type:** Method
- **File:** [`modules/simpletest/tests/batch.test`](../_file.md), lines 27–33 · [local source](../../../../../../source/modules/simpletest/tests/batch.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test#L27-L33)
- **Class:** [BatchProcessingTestCase](../BatchProcessingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testBatchNoForm()
```

## Documentation

```text
Test batches triggered outside of form submission.
```

## Code

```php
  function testBatchNoForm() {
    // Displaying the page triggers batch 1.
    $this->drupalGet('batch-test/no-form');
    $this->assertBatchMessages($this->_resultMessages(1), t('Batch for step 2 performed successfully.'));
    $this->assertEqual(batch_test_stack(), $this->_resultStack('batch_1'), t('Execution order was correct.'));
    $this->assertText('Redirection successful.', t('Redirection after batch execution is correct.'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test) · Licensed GPL-2.0-or-later (see LICENSE)._
