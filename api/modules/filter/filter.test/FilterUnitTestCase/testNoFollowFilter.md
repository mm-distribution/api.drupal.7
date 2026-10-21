# FilterUnitTestCase::testNoFollowFilter()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 1231–1257 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L1231-L1257)
- **Class:** [FilterUnitTestCase](../FilterUnitTestCase.md)
- **Module/theme:** filter

## Signature

```php
function testNoFollowFilter()
```

## Documentation

```text
Tests the spam deterrent.
```

## Code

```php
  function testNoFollowFilter() {
    // Setup dummy filter object.
    $filter = new stdClass();
    $filter->settings = array(
      'allowed_html' => '<a>',
      'filter_html_help' => 1,
      'filter_html_nofollow' => 1,
    );

    // Test if the rel="nofollow" attribute is added, even if we try to prevent
    // it.
    $f = _filter_html('<a href="http://www.example.com/">text</a>', $filter);
    $this->assertNormalized($f, 'rel="nofollow"', 'Spam deterrent -- no evasion.');

    $f = _filter_html('<A href="http://www.example.com/">text</a>', $filter);
    $this->assertNormalized($f, 'rel="nofollow"', 'Spam deterrent evasion -- capital A.');

    $f = _filter_html("<a/href=\"http://www.example.com/\">text</a>", $filter);
    $this->assertNormalized($f, 'rel="nofollow"', 'Spam deterrent evasion -- non whitespace character after tag name.');

    $f = _filter_html("<\0a\0 href=\"http://www.example.com/\">text</a>", $filter);
    $this->assertNormalized($f, 'rel="nofollow"', 'Spam deterrent evasion -- some nulls.');

    $f = _filter_html('<a href="http://www.example.com/" rel="follow">text</a>', $filter);
    $this->assertNoNormalized($f, 'rel="follow"', 'Spam deterrent evasion -- with rel set - rel="follow" removed.');
    $this->assertNormalized($f, 'rel="nofollow"', 'Spam deterrent evasion -- with rel set - rel="nofollow" added.');
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
