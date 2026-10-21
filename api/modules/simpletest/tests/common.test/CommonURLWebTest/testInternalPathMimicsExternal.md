# CommonURLWebTest::testInternalPathMimicsExternal()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 414–424 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L414-L424)
- **Class:** [CommonURLWebTest](../CommonURLWebTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testInternalPathMimicsExternal()
```

## Documentation

```text
Tests the url() function on internal paths which mimic external URLs.
```

## Code

```php
  function testInternalPathMimicsExternal() {
    // Ensure that calling url(current_path()) on "/http://example.com" (an
    // internal path which mimics an external URL) always links to the internal
    // path, not the external URL. This helps protect against external URL link
    // injection vulnerabilities.
    variable_set('common_test_link_to_current_path', TRUE);
    $this->drupalGet('/http://example.com');
    $this->clickLink('link which should point to the current path');
    $this->assertUrl('/http://example.com');
    $this->assertText('link which should point to the current path');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
