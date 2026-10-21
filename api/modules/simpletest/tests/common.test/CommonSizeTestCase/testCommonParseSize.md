# CommonSizeTestCase::testCommonParseSize()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 644–672 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L644-L672)
- **Class:** [CommonSizeTestCase](../CommonSizeTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testCommonParseSize()
```

## Documentation

```text
Check that parse_size() returns the proper byte sizes.
```

## Code

```php
  function testCommonParseSize() {
    foreach ($this->exact_test_cases as $string => $size) {
      $this->assertEqual(
        $parsed_size = parse_size($string),
        $size,
        $size . ' == ' . $parsed_size . ' (' . $string . ')'
      );
    }

    // Some custom parsing tests
    $string = '23476892 bytes';
    $this->assertEqual(
      ($parsed_size = parse_size($string)),
      $size = 23476892,
      $string . ' == ' . $parsed_size . ' bytes'
    );
    $string = '76MRandomStringThatShouldBeIgnoredByParseSize.'; // 76 MB
    $this->assertEqual(
      $parsed_size = parse_size($string),
      $size = 79691776,
      $string . ' == ' . $parsed_size . ' bytes'
    );
    $string = '76.24 Giggabyte'; // Misspeld text -> 76.24 GB
    $this->assertEqual(
      $parsed_size = parse_size($string),
      $size = 81862076662,
      $string . ' == ' . $parsed_size . ' bytes'
    );
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
