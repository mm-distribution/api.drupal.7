# UnicodeUnitTest::helperTestStrLen()

- **Type:** Method
- **File:** [`modules/simpletest/tests/unicode.test`](../_file.md), lines 117–128 · [local source](../../../../../../source/modules/simpletest/tests/unicode.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test#L117-L128)
- **Class:** [UnicodeUnitTest](../UnicodeUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
}
```

## Documentation

_No docblock in source._

## Code

```php
  function helperTestStrLen() {
    $testcase = array(
      'tHe QUIcK bRoWn' => 15,
      'ÜBER-åwesome' => 12,
      'NULL' => 0,
    );

    foreach ($testcase as $input => $output) {
      $tested_value = ($input === 'NULL' ? NULL : $input);
      $this->assertEqual(drupal_strlen($tested_value), $output, format_string('%input length is %output', array('%input' => $input, '%output' => $output)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/unicode.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test) · Licensed GPL-2.0-or-later (see LICENSE)._
