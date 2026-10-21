# BatchPercentagesUnitTestCase::testBatchPercentages()

- **Type:** Method
- **File:** [`modules/simpletest/tests/batch.test`](../_file.md), lines 387–402 · [local source](../../../../../../source/modules/simpletest/tests/batch.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test#L387-L402)
- **Class:** [BatchPercentagesUnitTestCase](../BatchPercentagesUnitTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testBatchPercentages()
```

## Documentation

```text
Test the _batch_api_percentage() function.
```

## Code

```php
  function testBatchPercentages() {
    foreach ($this->testCases as $expected_result => $arguments) {
      // PHP sometimes casts numeric strings that are array keys to integers,
      // cast them back here.
      $expected_result = (string) $expected_result;
      $total = $arguments['total'];
      $current = $arguments['current'];
      $actual_result = _batch_api_percentage($total, $current);
      if ($actual_result === $expected_result) {
        $this->pass(t('Expected the batch api percentage at the state @numerator/@denominator to be @expected%, and got @actual%.', array('@numerator' => $current, '@denominator' => $total, '@expected' => $expected_result, '@actual' => $actual_result)));
      }
      else {
        $this->fail(t('Expected the batch api percentage at the state @numerator/@denominator to be @expected%, but got @actual%.', array('@numerator' => $current, '@denominator' => $total, '@expected' => $expected_result, '@actual' => $actual_result)));
      }
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/batch.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/batch.test) · Licensed GPL-2.0-or-later (see LICENSE)._
