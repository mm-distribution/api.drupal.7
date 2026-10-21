# FilterUnitTestCase

- **Type:** Class
- **File:** [`modules/filter/filter.test`](_file.md), lines 890–1926 · [local source](../../../../source/modules/filter/filter.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test#L890-L1926)
- **Module/theme:** filter

## Signature

```php
class FilterUnitTestCase extends DrupalUnitTestCase
```

## Documentation

```text
Unit tests for core filters.
```

## Methods (derived index)

- [getInfo()](FilterUnitTestCase/getInfo.md)
- [testLineBreakFilter()](FilterUnitTestCase/testLineBreakFilter.md) — Tests the line break filter.
- [testFilterXSS()](FilterUnitTestCase/testFilterXSS.md) — Tests limiting allowed tags and XSS prevention.
- [testHtmlFilter()](FilterUnitTestCase/testHtmlFilter.md) — Tests filter settings, defaults, access restrictions and similar.
- [testNoFollowFilter()](FilterUnitTestCase/testNoFollowFilter.md) — Tests the spam deterrent.
- [testFilterXSSAdmin()](FilterUnitTestCase/testFilterXSSAdmin.md) — Tests the loose, admin HTML filter.
- [testHtmlEscapeFilter()](FilterUnitTestCase/testHtmlEscapeFilter.md) — Tests the HTML escaping filter.
- [testUrlFilter()](FilterUnitTestCase/testUrlFilter.md) — Tests the URL filter.
- [assertFilteredString()](FilterUnitTestCase/assertFilteredString.md) — Asserts multiple filter output expectations for multiple input strings.
- [testUrlFilterContent()](FilterUnitTestCase/testUrlFilterContent.md) — Tests URL filter on longer content.
- [testHtmlCorrectorFilter()](FilterUnitTestCase/testHtmlCorrectorFilter.md) — Tests the HTML corrector filter.
- [assertNormalized()](FilterUnitTestCase/assertNormalized.md) — Asserts that a text transformed to lowercase with HTML entities decoded does contains a given string.
- [assertNoNormalized()](FilterUnitTestCase/assertNoNormalized.md) — Asserts that text transformed to lowercase with HTML entities decoded does not contain a given string.
- [filterUrlWithPcreErrors()](FilterUnitTestCase/filterUrlWithPcreErrors.md) — Calls filter_url with pcre.backtrack_limit set to 1.

---
_Drupal 7.103 · [modules/filter/filter.test](https://github.com/drupal/drupal/blob/7.103/modules/filter/filter.test) · Licensed GPL-2.0-or-later (see LICENSE)._
