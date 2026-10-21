# UnicodeUnitTest::testDecodeEntities()

- **Type:** Method
- **File:** [`modules/simpletest/tests/unicode.test`](../_file.md), lines 193–222 · [local source](../../../../../../source/modules/simpletest/tests/unicode.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test#L193-L222)
- **Class:** [UnicodeUnitTest](../UnicodeUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
* Test decode_entities().
```

## Documentation

```text
Test decode_entities().
```

## Code

```php
  function testDecodeEntities() {
    $testcase = array(
      'Drupal' => 'Drupal',
      '<script>' => '<script>',
      '&lt;script&gt;' => '<script>',
      '&#60;script&#62;' => '<script>',
      '&amp;lt;script&amp;gt;' => '&lt;script&gt;',
      '"' => '"',
      '&#34;' => '"',
      '&amp;#34;' => '&#34;',
      '&quot;' => '"',
      '&amp;quot;' => '&quot;',
      "'" => "'",
      '&#39;' => "'",
      '&amp;#39;' => '&#39;',
      '©' => '©',
      '&copy;' => '©',
      '&#169;' => '©',
      '→' => '→',
      '&#8594;' => '→',
      '➼' => '➼',
      '&#10172;' => '➼',
      '&euro;' => '€',
    );
    foreach ($testcase as $input => $output) {
      $this->assertEqual(decode_entities($input), $output, format_string('Make sure the decoded entity of @input is @output', array('@input' => $input, '@output' => $output)));
    }
    // Test NULL value.
    $this->assertEqual(decode_entities(NULL), '', format_string('Make sure the decoded entity of NULL is empty string'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/unicode.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/unicode.test) · Licensed GPL-2.0-or-later (see LICENSE)._
