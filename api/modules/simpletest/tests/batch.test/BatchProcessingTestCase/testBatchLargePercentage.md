# BatchProcessingTestCase::testBatchLargePercentage()

- **Type:** Method
- **File:** [`modules/simpletest/tests/batch.test`](../_file.md), lines 144–150 · [local source](../../../../../../source/modules/simpletest/tests/batch.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test#L144-L150)
- **Class:** [BatchProcessingTestCase](../BatchProcessingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testBatchLargePercentage()
```

## Documentation

```text
Test batches that return $context['finished'] > 1 do in fact complete.
See http://drupal.org/node/600836
```

## Code

```php
  function testBatchLargePercentage() {
    // Displaying the page triggers batch 5.
    $this->drupalGet('batch-test/large-percentage');
    $this->assertBatchMessages($this->_resultMessages(1), t('Batch for step 2 performed successfully.'));
    $this->assertEqual(batch_test_stack(), $this->_resultStack('batch_5'), t('Execution order was correct.'));
    $this->assertText('Redirection successful.', t('Redirection after batch execution is correct.'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test) · Licensed GPL-2.0-or-later (see LICENSE)._
