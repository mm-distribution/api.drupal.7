# CommonXssUnitTest::testEscaping()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 529–534 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L529-L534)
- **Class:** [CommonXssUnitTest](../CommonXssUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testEscaping()
```

## Documentation

```text
Check that special characters are escaped.
```

## Code

```php
  function testEscaping() {
     $text = check_plain("<script>");
     $this->assertEqual($text, '&lt;script&gt;', 'check_plain() escapes &lt;script&gt;');
     $text = check_plain('<>&"\'');
     $this->assertEqual($text, '&lt;&gt;&amp;&quot;&#039;', 'check_plain() escapes reserved HTML characters.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
