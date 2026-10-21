# FilterUnitTestCase::testHtmlFilter()

- **Type:** Method
- **File:** [`modules/filter/filter.test`](../_file.md), lines 1182–1226 · [local source](../../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L1182-L1226)
- **Class:** [FilterUnitTestCase](../FilterUnitTestCase.md)
- **Module/theme:** filter

## Signature

```php
function testHtmlFilter()
```

## Documentation

```text
Tests filter settings, defaults, access restrictions and similar.

@todo This is for functions like filter_filter and check_markup, whose
  functionality is not completely focused on filtering. Some ideas:
  restricting formats according to user permissions, proper cache
  handling, defaults -- allowed tags/attributes/protocols.

@todo It is possible to add script, iframe etc. to allowed tags, but this
  makes HTML filter completely ineffective.

@todo Class, id, name and xmlns should be added to disallowed attributes,
  or better a whitelist approach should be used for that too.
```

## Code

```php
  function testHtmlFilter() {
    // Setup dummy filter object.
    $filter = new stdClass();
    $filter->settings = array(
      'allowed_html' => '<a> <em> <strong> <cite> <blockquote> <code> <ul> <ol> <li> <dl> <dt> <dd> <test-element>',
      'filter_html_help' => 1,
      'filter_html_nofollow' => 0,
    );

    // HTML filter is not able to secure some tags, these should never be
    // allowed.
    $f = _filter_html('<script />', $filter);
    $this->assertNoNormalized($f, 'script', 'HTML filter should always remove script tags.');

    $f = _filter_html('<iframe />', $filter);
    $this->assertNoNormalized($f, 'iframe', 'HTML filter should always remove iframe tags.');

    $f = _filter_html('<object />', $filter);
    $this->assertNoNormalized($f, 'object', 'HTML filter should always remove object tags.');

    $f = _filter_html('<style />', $filter);
    $this->assertNoNormalized($f, 'style', 'HTML filter should always remove style tags.');

    // Some tags make CSRF attacks easier, let the user take the risk herself.
    $f = _filter_html('<img />', $filter);
    $this->assertNoNormalized($f, 'img', 'HTML filter should remove img tags on default.');

    $f = _filter_html('<input />', $filter);
    $this->assertNoNormalized($f, 'img', 'HTML filter should remove input tags on default.');

    // Filtering content of some attributes is infeasible, these shouldn't be
    // allowed too.
    $f = _filter_html('<p style="display: none;" />', $filter);
    $this->assertNoNormalized($f, 'style', 'HTML filter should remove style attribute on default.');

    $f = _filter_html('<p onerror="alert(0);" />', $filter);
    $this->assertNoNormalized($f, 'onerror', 'HTML filter should remove on* attributes on default.');

    $f = _filter_html('<code onerror>&nbsp;</code>', $filter);
    $this->assertNoNormalized($f, 'onerror', 'HTML filter should remove empty on* attributes on default.');

    // Custom tags are supported and should be allowed through.
    $f = _filter_html('<test-element></test-element>', $filter);
    $this->assertNormalized($f, 'test-element', 'HTML filter should allow custom elements.');
  }
```

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
