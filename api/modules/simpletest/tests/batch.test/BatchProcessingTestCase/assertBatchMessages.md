# BatchProcessingTestCase::assertBatchMessages()

- **Type:** Method
- **File:** [`modules/simpletest/tests/batch.test`](../_file.md), lines 163–166 · [local source](../../../../../../source/modules/simpletest/tests/batch.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test#L163-L166)
- **Class:** [BatchProcessingTestCase](../BatchProcessingTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function assertBatchMessages($texts, $message)
```

## Documentation

```text
Will trigger a pass if the texts were found in order in the raw content.

@param $texts
  Array of raw strings to look for .
@param $message
  Message to display.
@return
  TRUE on pass, FALSE on fail.
```

## Code

```php
  function assertBatchMessages($texts, $message) {
    $pattern = '|' . implode('.*', $texts) .'|s';
    return $this->assertPattern($pattern, $message);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test) · Licensed GPL-2.0-or-later (see LICENSE)._
