# DrupalHtmlToTextTestCase::testFootnoteReferences()

- **Type:** Method
- **File:** [`modules/simpletest/tests/mail.test`](../_file.md), lines 464–483 · [local source](../../../../../../source/modules/simpletest/tests/mail.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test#L464-L483)
- **Class:** [DrupalHtmlToTextTestCase](../DrupalHtmlToTextTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testFootnoteReferences()
```

## Documentation

```text
Test that footnote references are properly generated.
```

## Code

```php
  function testFootnoteReferences() {
    global $base_path, $base_url;
    $source = '<a href="http://www.example.com/node/1">Host and path</a>'
      . '<br /><a href="http://www.example.com">Host, no path</a>'
      . '<br /><a href="' . $base_path . 'node/1">Path, no host</a>'
      . '<br /><a href="node/1">Relative path</a>';
    // @todo Footnote URLs should be absolute.
    $tt = "Host and path [1]"
      . "\nHost, no path [2]"
      // @todo The following two references should be combined.
      . "\nPath, no host [3]"
      . "\nRelative path [4]"
      . "\n"
      . "\n[1] http://www.example.com/node/1"
      . "\n[2] http://www.example.com"
      // @todo The following two references should be combined.
      . "\n[3] $base_url/node/1"
      . "\n[4] node/1\n";
    $this->assertHtmlToText($source, $tt, 'Footnotes');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/mail.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/mail.test) · Licensed GPL-2.0-or-later (see LICENSE)._
