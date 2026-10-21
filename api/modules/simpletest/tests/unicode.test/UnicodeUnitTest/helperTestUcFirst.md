# UnicodeUnitTest::helperTestUcFirst()

- **Type:** Method
- **File:** [`modules/simpletest/tests/unicode.test`](../_file.md), lines 101–115 · [local source](../../../../../../source/modules/simpletest/tests/unicode.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test#L101-L115)
- **Class:** [UnicodeUnitTest](../UnicodeUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php

```

## Documentation

_No docblock in source._

## Code

```php
  function helperTestUcFirst() {
    $testcase = array(
      'tHe QUIcK bRoWn' => 'THe QUIcK bRoWn',
      'françAIS' => 'FrançAIS',
      'über' => 'Über',
      'åwesome' => 'Åwesome'
    );
    if ($this->extendedMode) {
      $testcase['σion'] = 'Σion';
    }

    foreach ($testcase as $input => $output) {
      $this->assertEqual(drupal_ucfirst($input), $output, format_string('%input is ucfirst-ed as %output', array('%input' => $input, '%output' => $output)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/unicode.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test) · Licensed GPL-2.0-or-later (see LICENSE)._
