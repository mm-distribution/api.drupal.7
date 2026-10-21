# UnicodeUnitTest::helperTestTruncate()

- **Type:** Method
- **File:** [`modules/simpletest/tests/unicode.test`](../_file.md), lines 227–286 · [local source](../../../../../../source/modules/simpletest/tests/unicode.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test#L227-L286)
- **Class:** [UnicodeUnitTest](../UnicodeUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
* Tests truncate_utf8().
```

## Documentation

```text
Tests truncate_utf8().
```

## Code

```php
  function helperTestTruncate() {
    // Each case is an array with input string, length to truncate to, and
    // expected return value.

    // Test non-wordsafe, non-ellipsis cases.
    $non_wordsafe_non_ellipsis_cases = array(
      array('frànçAIS is über-åwesome', 24, 'frànçAIS is über-åwesome'),
      array('frànçAIS is über-åwesome', 23, 'frànçAIS is über-åwesom'),
      array('frànçAIS is über-åwesome', 17, 'frànçAIS is über-'),
      array('以呂波耳・ほへとち。リヌルヲ。', 6, '以呂波耳・ほ'),
    );
    $this->runTruncateTests($non_wordsafe_non_ellipsis_cases, FALSE, FALSE);

    // Test non-wordsafe, ellipsis cases.
    $non_wordsafe_ellipsis_cases = array(
      array('frànçAIS is über-åwesome', 24, 'frànçAIS is über-åwesome'),
      array('frànçAIS is über-åwesome', 23, 'frànçAIS is über-åwe...'),
      array('frànçAIS is über-åwesome', 17, 'frànçAIS is üb...'),
    );
    $this->runTruncateTests($non_wordsafe_ellipsis_cases, FALSE, TRUE);

    // Test wordsafe, ellipsis cases.
    $wordsafe_ellipsis_cases = array(
      array('123', 1, '.'),
      array('123', 2, '..'),
      array('123', 3, '123'),
      array('1234', 3, '...'),
      array('1234567890', 10, '1234567890'),
      array('12345678901', 10, '1234567...'),
      array('12345678901', 11, '12345678901'),
      array('123456789012', 11, '12345678...'),
      array('12345 7890', 10, '12345 7890'),
      array('12345 7890', 9, '12345...'),
      array('123 567 90', 10, '123 567 90'),
      array('123 567 901', 10, '123 567...'),
      array('Stop. Hammertime.', 17, 'Stop. Hammertime.'),
      array('Stop. Hammertime.', 16, 'Stop....'),
      array('frànçAIS is über-åwesome', 24, 'frànçAIS is über-åwesome'),
      array('frànçAIS is über-åwesome', 23, 'frànçAIS is über...'),
      array('frànçAIS is über-åwesome', 17, 'frànçAIS is...'),
      array('¿Dónde está el niño?', 20, '¿Dónde está el niño?'),
      array('¿Dónde está el niño?', 19, '¿Dónde está el...'),
      array('¿Dónde está el niño?', 15, '¿Dónde está...'),
      array('¿Dónde está el niño?', 10, '¿Dónde...'),
      array('Help! Help! Help!', 17, 'Help! Help! Help!'),
      array('Help! Help! Help!', 16, 'Help! Help!...'),
      array('Help! Help! Help!', 15, 'Help! Help!...'),
      array('Help! Help! Help!', 14, 'Help! Help!...'),
      array('Help! Help! Help!', 13, 'Help! Help...'),
      array('Help! Help! Help!', 12, 'Help!...'),
      array('Help! Help! Help!', 11, 'Help!...'),
      array('Help! Help! Help!', 10, 'Help!...'),
      array('Help! Help! Help!', 9, 'Help!...'),
      array('Help! Help! Help!', 8, 'Help!...'),
      array('Help! Help! Help!', 7, 'Help...'),
      array('Help! Help! Help!', 6, 'Hel...'),
      array('Help! Help! Help!', 5, 'He...'),
    );
    $this->runTruncateTests($wordsafe_ellipsis_cases, TRUE, TRUE);
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/unicode.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test) · Licensed GPL-2.0-or-later (see LICENSE)._
