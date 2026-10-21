# DrupalAddHtmlHeadLinkTest::testDrupalAddHtmlHeadLink()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 3414–3429 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L3414-L3429)
- **Class:** [DrupalAddHtmlHeadLinkTest](../DrupalAddHtmlHeadLinkTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testDrupalAddHtmlHeadLink()
```

## Documentation

```text
Tests drupal_add_html_head_link().
```

## Code

```php
  function testDrupalAddHtmlHeadLink() {
    $this->drupalGet('common-test/html_head_link');
    $expected_link_header = implode(',', array(
      '</foo?bar=baz>; rel="alternate"',
      '</foo/bar>; hreflang="nl"; rel="alternate"',
      '</foo/bar>; hreflang="de"; rel="alternate"',
      '</foo?bar=baz&baz=false>; hreflang="en"; rel="alternate"',
    ));
    $this->assertEqual($this->drupalGetHeader('Link'), $expected_link_header);

    // Check that duplicate alternate URLs with different hreflangs are allowed.
    $test_link = $this->xpath('//head/link[@rel="alternate"][@href="/foo/bar"]');
    $this->assertEqual(count($test_link), 2, 'Duplicate alternate URLs are allowed.');
    // Check that link element attributes are HTML-encoded.
    $this->assertRaw('<link href="/foo?bar=baz&amp;baz=false" hreflang="en" rel="alternate" />');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
