# SimpleTestBrowserTestCase::testXPathEscaping()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 398–415 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L398-L415)
- **Class:** [SimpleTestBrowserTestCase](../SimpleTestBrowserTestCase.md)
- **Module/theme:** simpletest

## Signature

```php
function testXPathEscaping()
```

## Documentation

```text
Tests XPath escaping.
```

## Code

```php
  function testXPathEscaping() {
    $testpage = <<< EOF
<html>
<body>
<a href="link1">A "weird" link, just to bother the dumb "XPath 1.0"</a>
<a href="link2">A second "even more weird" link, in memory of George O'Malley</a>
</body>
</html>
EOF;
    $this->drupalSetContent($testpage);

    // Matches the first link.
    $urls = $this->xpath('//a[text()=:text]', array(':text' => 'A "weird" link, just to bother the dumb "XPath 1.0"'));
    $this->assertEqual($urls[0]['href'], 'link1', 'Match with quotes.');

    $urls = $this->xpath('//a[text()=:text]', array(':text' => 'A second "even more weird" link, in memory of George O\'Malley'));
    $this->assertEqual($urls[0]['href'], 'link2', 'Match with mixed single and double quotes.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
