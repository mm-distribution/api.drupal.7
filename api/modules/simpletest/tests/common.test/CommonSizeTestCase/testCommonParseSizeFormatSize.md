# CommonSizeTestCase::testCommonParseSizeFormatSize()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 677–685 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L677-L685)
- **Class:** [CommonSizeTestCase](../CommonSizeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testCommonParseSizeFormatSize()
```

## Documentation

```text
Cross-test parse_size() and format_size().
```

## Code

```php
  function testCommonParseSizeFormatSize() {
    foreach ($this->exact_test_cases as $size) {
      $this->assertEqual(
        $size,
        ($parsed_size = parse_size($string = format_size($size, NULL))),
        $size . ' == ' . $parsed_size . ' (' . $string . ')'
      );
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
