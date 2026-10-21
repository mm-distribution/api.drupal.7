# CommonURLUnitTest

- **Type:** Class
- **File:** [`modules/simpletest/tests/common.test`](_file.md), lines 76–393 · [local source](../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L76-L393)
- **Module/theme:** batch_test

## Signature

```php
class CommonURLUnitTest extends DrupalWebTestCase
```

## Documentation

```text
Tests for URL generation functions.

url() calls module_implements(), which may issue a db query, which requires
inheriting from a web test case rather than a unit test case.
```

## Methods (derived index)

- [getInfo()](CommonURLUnitTest/getInfo.md)
- [testLXSS()](CommonURLUnitTest/testLXSS.md) — Confirm that invalid text given as $path is filtered.
- [testLActiveClass()](CommonURLUnitTest/testLActiveClass.md)
- [testLCustomClass()](CommonURLUnitTest/testLCustomClass.md) — Tests for custom class in l() function.
- [hasClass()](CommonURLUnitTest/hasClass.md)
- [testDrupalGetQueryParameters()](CommonURLUnitTest/testDrupalGetQueryParameters.md) — Test drupal_get_query_parameters().
- [testDrupalHttpBuildQuery()](CommonURLUnitTest/testDrupalHttpBuildQuery.md) — Test drupal_http_build_query().
- [testDrupalParseUrl()](CommonURLUnitTest/testDrupalParseUrl.md) — Test drupal_parse_url().
- [testUrl()](CommonURLUnitTest/testUrl.md) — Test url() with/without query, with/without fragment, absolute on/off and assert all that works when clean URLs are on and off.
- [testExternalUrls()](CommonURLUnitTest/testExternalUrls.md) — Test external URL handling.

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
