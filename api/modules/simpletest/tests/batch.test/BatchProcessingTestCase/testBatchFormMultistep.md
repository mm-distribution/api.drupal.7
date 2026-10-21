# BatchProcessingTestCase::testBatchFormMultistep()

- **Type:** Method
- **File:** [`modules/simpletest/tests/batch.test`](../_file.md), lines 77–92 · [local source](../../../../../../source/modules/simpletest/tests/batch.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test#L77-L92)
- **Class:** [BatchProcessingTestCase](../BatchProcessingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testBatchFormMultistep()
```

## Documentation

```text
Test batches defined in a multistep form.
```

## Code

```php
  function testBatchFormMultistep() {
    $this->drupalGet('batch-test/multistep');
    $this->assertText('step 1', t('Form is displayed in step 1.'));

    // First step triggers batch 1.
    $this->drupalPost(NULL, array(), 'Submit');
    $this->assertBatchMessages($this->_resultMessages('batch_1'), t('Batch for step 1 performed successfully.'));
    $this->assertEqual(batch_test_stack(), $this->_resultStack('batch_1'), t('Execution order was correct.'));
    $this->assertText('step 2', t('Form is displayed in step 2.'));

    // Second step triggers batch 2.
    $this->drupalPost(NULL, array(), 'Submit');
    $this->assertBatchMessages($this->_resultMessages('batch_2'), t('Batch for step 2 performed successfully.'));
    $this->assertEqual(batch_test_stack(), $this->_resultStack('batch_2'), t('Execution order was correct.'));
    $this->assertText('Redirection successful.', t('Redirection after batch execution is correct.'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test) · Licensed GPL-2.0-or-later (see LICENSE)._
