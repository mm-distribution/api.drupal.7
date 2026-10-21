# BatchProcessingTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/batch.test`](_file.md), lines 11–275 · [local source](../../../../../source/modules/simpletest/tests/batch.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test#L11-L275)
- **Module/theme:** batch_test

## Signature

```php
class BatchProcessingTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests for the Batch API.
```

## Methods (derived index)

- [getInfo()](BatchProcessingTestCase/getInfo.md)
- [setUp()](BatchProcessingTestCase/setUp.md)
- [testBatchNoForm()](BatchProcessingTestCase/testBatchNoForm.md) — Test batches triggered outside of form submission.
- [testBatchForm()](BatchProcessingTestCase/testBatchForm.md) — Test batches defined in a form submit handler.
- [testBatchFormMultistep()](BatchProcessingTestCase/testBatchFormMultistep.md) — Test batches defined in a multistep form.
- [testBatchFormMultipleBatches()](BatchProcessingTestCase/testBatchFormMultipleBatches.md) — Test batches defined in different submit handlers on the same form.
- [testBatchFormProgrammatic()](BatchProcessingTestCase/testBatchFormProgrammatic.md) — Test batches defined in a programmatically submitted form.
- [testDrupalFormSubmitInBatch()](BatchProcessingTestCase/testDrupalFormSubmitInBatch.md) — Test that drupal_form_submit() can run within a batch operation.
- [testBatchLargePercentage()](BatchProcessingTestCase/testBatchLargePercentage.md) — Test batches that return $context['finished'] > 1 do in fact complete. See http://drupal.org/node/600836
- [assertBatchMessages()](BatchProcessingTestCase/assertBatchMessages.md) — Will trigger a pass if the texts were found in order in the raw content.
- [_resultStack()](BatchProcessingTestCase/_resultStack.md) — Helper function: return expected execution stacks for the test batches.
- [_resultMessages()](BatchProcessingTestCase/_resultMessages.md) — Helper function: return expected result messages for the test batches.

---
_Drupal 7.103 · [modules/simpletest/tests/batch.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test) · Licensed GPL-2.0-or-later (see LICENSE)._
