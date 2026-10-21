# UnicodeUnitTest::runTruncateTests()

- **Type:** Method
- **File:** [`modules/simpletest/tests/unicode.test`](../_file.md), lines 302–308 · [local source](../../../../../../source/modules/simpletest/tests/unicode.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test#L302-L308)
- **Class:** [UnicodeUnitTest](../UnicodeUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
*   TRUE to append ... if the input is truncated, FALSE to not append ....
```

## Documentation

```text
Runs test cases for helperTestTruncate().

Runs each test case through truncate_utf8() and compares the output
to the expected output.

@param $cases
  Cases array. Each case is an array with the input string, length to
  truncate to, and expected output.
@param $wordsafe
  TRUE to use word-safe truncation, FALSE to not use word-safe truncation.
@param $ellipsis
  TRUE to append ... if the input is truncated, FALSE to not append ....
```

## Code

```php
  function runTruncateTests($cases, $wordsafe, $ellipsis) {
    foreach ($cases as $case) {
      list($input, $max_length, $expected) = $case;
      $output = truncate_utf8($input, $max_length, $wordsafe, $ellipsis);
      $this->assertEqual($output, $expected, format_string('%input truncate to %length characters with %wordsafe, %ellipsis is %expected (got %output)', array('%input' => $input, '%length' => $max_length, '%output' => $output, '%expected' => $expected, '%wordsafe' => ($wordsafe ? 'word-safe' : 'not word-safe'), '%ellipsis' => ($ellipsis ? 'ellipsis' : 'not ellipsis'))));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/unicode.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test) · Licensed GPL-2.0-or-later (see LICENSE)._
