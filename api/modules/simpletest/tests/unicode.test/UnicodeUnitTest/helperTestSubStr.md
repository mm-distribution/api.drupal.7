# UnicodeUnitTest::helperTestSubStr()

- **Type:** Method
- **File:** [`modules/simpletest/tests/unicode.test`](../_file.md), lines 130–188 · [local source](../../../../../../source/modules/simpletest/tests/unicode.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test#L130-L188)
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
  function helperTestSubStr() {
    $testcase = array(
      //     012345678901234567890123
      array('frànçAIS is über-åwesome', 0, 0,
            ''),
      array('frànçAIS is über-åwesome', 0, 1,
            'f'),
      array('frànçAIS is über-åwesome', 0, 8,
            'frànçAIS'),
      array('frànçAIS is über-åwesome', 0, 23,
            'frànçAIS is über-åwesom'),
      array('frànçAIS is über-åwesome', 0, 24,
            'frànçAIS is über-åwesome'),
      array('frànçAIS is über-åwesome', 0, 25,
            'frànçAIS is über-åwesome'),
      array('frànçAIS is über-åwesome', 0, 100,
            'frànçAIS is über-åwesome'),
      array('frànçAIS is über-åwesome', 4, 4,
                'çAIS'),
      array('frànçAIS is über-åwesome', 1, 0,
            ''),
      array('frànçAIS is über-åwesome', 100, 0,
            ''),
      array('frànçAIS is über-åwesome', -4, 2,
                                'so'),
      array('frànçAIS is über-åwesome', -4, 3,
                                'som'),
      array('frànçAIS is über-åwesome', -4, 4,
                                'some'),
      array('frànçAIS is über-åwesome', -4, 5,
                                'some'),
      array('frànçAIS is über-åwesome', -7, 10,
                             'åwesome'),
      array('frànçAIS is über-åwesome', 5, -10,
                 'AIS is üb'),
      array('frànçAIS is über-åwesome', 0, -10,
            'frànçAIS is üb'),
      array('frànçAIS is über-åwesome', 0, -1,
        'frànçAIS is über-åwesom'),
      array('frànçAIS is über-åwesome', -7, -2,
                             'åweso'),
      array('frànçAIS is über-åwesome', -7, -6,
                             'å'),
      array('frànçAIS is über-åwesome', -7, -7,
                             ''),
      array('frànçAIS is über-åwesome', -7, -8,
                             ''),
      array('...', 0, 2, '..'),
      array('以呂波耳・ほへとち。リヌルヲ。', 1, 3,
              '呂波耳'),

    );

    foreach ($testcase as $test) {
      list($input, $start, $length, $output) = $test;
      $result = drupal_substr($input, $start, $length);
      $this->assertEqual($result, $output, format_string('%input substring at offset %offset for %length characters is %output (got %result)', array('%input' => $input, '%offset' => $start, '%length' => $length, '%output' => $output, '%result' => $result)));
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/unicode.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test) · Licensed GPL-2.0-or-later (see LICENSE)._
