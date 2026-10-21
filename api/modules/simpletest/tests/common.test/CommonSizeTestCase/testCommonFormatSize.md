# CommonSizeTestCase::testCommonFormatSize()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 629–639 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L629-L639)
- **Class:** [CommonSizeTestCase](../CommonSizeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testCommonFormatSize()
```

## Documentation

```text
Check that format_size() returns the expected string.
```

## Code

```php
  function testCommonFormatSize() {
    foreach (array($this->exact_test_cases, $this->rounded_test_cases) as $test_cases) {
      foreach ($test_cases as $expected => $input) {
        $this->assertEqual(
          ($result = format_size($input, NULL)),
          $expected,
          $expected . ' == ' . $result . ' (' . $input . ' bytes)'
        );
      }
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
