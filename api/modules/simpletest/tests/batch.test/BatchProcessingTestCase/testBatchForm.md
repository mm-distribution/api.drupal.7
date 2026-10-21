# BatchProcessingTestCase::testBatchForm()

- **Type:** Method
- **File:** [`modules/simpletest/tests/batch.test`](../_file.md), lines 38–72 · [local source](../../../../../../source/modules/simpletest/tests/batch.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test#L38-L72)
- **Class:** [BatchProcessingTestCase](../BatchProcessingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testBatchForm()
```

## Documentation

```text
Test batches defined in a form submit handler.
```

## Code

```php
  function testBatchForm() {
    // Batch 0: no operation.
    $edit = array('batch' => 'batch_0');
    $this->drupalPost('batch-test/simple', $edit, 'Submit');
    $this->assertBatchMessages($this->_resultMessages('batch_0'), t('Batch with no operation performed successfully.'));
    $this->assertText('Redirection successful.', t('Redirection after batch execution is correct.'));

    // Batch 1: several simple operations.
    $edit = array('batch' => 'batch_1');
    $this->drupalPost('batch-test/simple', $edit, 'Submit');
    $this->assertBatchMessages($this->_resultMessages('batch_1'), t('Batch with simple operations performed successfully.'));
    $this->assertEqual(batch_test_stack(), $this->_resultStack('batch_1'), t('Execution order was correct.'));
    $this->assertText('Redirection successful.', t('Redirection after batch execution is correct.'));

    // Batch 2: one multistep operation.
    $edit = array('batch' => 'batch_2');
    $this->drupalPost('batch-test/simple', $edit, 'Submit');
    $this->assertBatchMessages($this->_resultMessages('batch_2'), t('Batch with multistep operation performed successfully.'));
    $this->assertEqual(batch_test_stack(), $this->_resultStack('batch_2'), t('Execution order was correct.'));
    $this->assertText('Redirection successful.', t('Redirection after batch execution is correct.'));

    // Batch 3: simple + multistep combined.
    $edit = array('batch' => 'batch_3');
    $this->drupalPost('batch-test/simple', $edit, 'Submit');
    $this->assertBatchMessages($this->_resultMessages('batch_3'), t('Batch with simple and multistep operations performed successfully.'));
    $this->assertEqual(batch_test_stack(), $this->_resultStack('batch_3'), t('Execution order was correct.'));
    $this->assertText('Redirection successful.', t('Redirection after batch execution is correct.'));

    // Batch 4: nested batch.
    $edit = array('batch' => 'batch_4');
    $this->drupalPost('batch-test/simple', $edit, 'Submit');
    $this->assertBatchMessages($this->_resultMessages('batch_4'), t('Nested batch performed successfully.'));
    $this->assertEqual(batch_test_stack(), $this->_resultStack('batch_4'), t('Execution order was correct.'));
    $this->assertText('Redirection successful.', t('Redirection after batch execution is correct.'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test) · Licensed GPL-2.0-or-later (see LICENSE)._
