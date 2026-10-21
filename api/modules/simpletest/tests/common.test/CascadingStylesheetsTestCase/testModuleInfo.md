# CascadingStylesheetsTestCase::testModuleInfo()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 773–789 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L773-L789)
- **Class:** [CascadingStylesheetsTestCase](../CascadingStylesheetsTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testModuleInfo()
```

## Documentation

```text
Test that stylesheets in module .info files are loaded.
```

## Code

```php
  function testModuleInfo() {
    $this->drupalGet('');

    // Verify common_test.css in a STYLE media="all" tag.
    $elements = $this->xpath('//style[@media=:media and contains(text(), :filename)]', array(
      ':media' => 'all',
      ':filename' => 'tests/common_test.css',
    ));
    $this->assertTrue(count($elements), "Stylesheet with media 'all' in module .info file found.");

    // Verify common_test.print.css in a STYLE media="print" tag.
    $elements = $this->xpath('//style[@media=:media and contains(text(), :filename)]', array(
      ':media' => 'print',
      ':filename' => 'tests/common_test.print.css',
    ));
    $this->assertTrue(count($elements), "Stylesheet with media 'print' in module .info file found.");
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
