# UnicodeUnitTest::helperTestStrToUpper()

- **Type:** Method
- **File:** [`modules/simpletest/tests/unicode.test`](../_file.md), lines 87–99 · [local source](../../../../../../source/modules/simpletest/tests/unicode.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test#L87-L99)
- **Class:** [UnicodeUnitTest](../UnicodeUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function helperTestStrToUpper()
```

## Documentation

_No docblock in source._

## Code

```php
  function helperTestStrToUpper() {
    $testcase = array(
      'tHe QUIcK bRoWn' => 'THE QUICK BROWN',
      'FrançAIS is ÜBER-åwesome' => 'FRANÇAIS IS ÜBER-ÅWESOME',
    );
    if ($this->extendedMode) {
      $testcase['αβγδεζηθικλμνξοσὠ'] = 'ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΣὨ';
    }

    foreach ($testcase as $input => $output) {
      $this->assertEqual(drupal_strtoupper($input), $output, format_string('%input is uppercased as %output', array('%input' => $input, '%output' => $output)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/unicode.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test) · Licensed GPL-2.0-or-later (see LICENSE)._
