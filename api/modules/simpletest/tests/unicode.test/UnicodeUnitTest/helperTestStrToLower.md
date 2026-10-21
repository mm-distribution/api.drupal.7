# UnicodeUnitTest::helperTestStrToLower()

- **Type:** Method
- **File:** [`modules/simpletest/tests/unicode.test`](../_file.md), lines 73–85 · [local source](../../../../../../source/modules/simpletest/tests/unicode.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test#L73-L85)
- **Class:** [UnicodeUnitTest](../UnicodeUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function helperTestStrToLower()
```

## Documentation

_No docblock in source._

## Code

```php
  function helperTestStrToLower() {
    $testcase = array(
      'tHe QUIcK bRoWn' => 'the quick brown',
      'FrançAIS is ÜBER-åwesome' => 'français is über-åwesome',
    );
    if ($this->extendedMode) {
      $testcase['ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΣὨ'] = 'αβγδεζηθικλμνξοσὠ';
    }

    foreach ($testcase as $input => $output) {
      $this->assertEqual(drupal_strtolower($input), $output, format_string('%input is lowercased as %output', array('%input' => $input, '%output' => $output)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/unicode.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test) · Licensed GPL-2.0-or-later (see LICENSE)._
