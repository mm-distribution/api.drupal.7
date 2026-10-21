# CommonXssUnitTest::testFormatStringAndT()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 539–550 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L539-L550)
- **Class:** [CommonXssUnitTest](../CommonXssUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testFormatStringAndT()
```

## Documentation

```text
Test t() and format_string() replacement functionality.
```

## Code

```php
  function testFormatStringAndT() {
    foreach (array('format_string', 't') as $function) {
      $text = $function('Simple text');
      $this->assertEqual($text, 'Simple text', $function . ' leaves simple text alone.');
      $text = $function('Escaped text: @value', array('@value' => '<script>'));
      $this->assertEqual($text, 'Escaped text: &lt;script&gt;', $function . ' replaces and escapes string.');
      $text = $function('Placeholder text: %value', array('%value' => '<script>'));
      $this->assertEqual($text, 'Placeholder text: <em class="placeholder">&lt;script&gt;</em>', $function . ' replaces, escapes and themes string.');
      $text = $function('Verbatim text: !value', array('!value' => '<script>'));
      $this->assertEqual($text, 'Verbatim text: <script>', $function . ' replaces verbatim string as-is.');
    }
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
