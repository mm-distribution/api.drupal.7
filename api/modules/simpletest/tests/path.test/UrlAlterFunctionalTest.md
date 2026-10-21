# UrlAlterFunctionalTest

- **Type:** Class
- **File:** [`modules/simpletest/tests/path.test`](_file.md), lines 132–245 · [local source](../../../../../source/modules/simpletest/tests/path.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test#L132-L245)
- **Module/theme:** batch_test

## Signature

```php
class UrlAlterFunctionalTest extends DrupalWebTestCase
```

## Documentation

```text
Tests hook_url_alter functions.
```

## Methods (derived index)

- [getInfo()](UrlAlterFunctionalTest/getInfo.md)
- [setUp()](UrlAlterFunctionalTest/setUp.md)
- [testUrlAlter()](UrlAlterFunctionalTest/testUrlAlter.md) — Test that URL altering works and that it occurs in the correct order.
- [testCurrentUrlRequestedPath()](UrlAlterFunctionalTest/testCurrentUrlRequestedPath.md) — Test current_path() and request_path().
- [testGetQInitialized()](UrlAlterFunctionalTest/testGetQInitialized.md) — Tests that $_GET['q'] is initialized when the request path is empty.
- [assertUrlOutboundAlter()](UrlAlterFunctionalTest/assertUrlOutboundAlter.md) — Assert that an outbound path is altered to an expected value.
- [assertUrlInboundAlter()](UrlAlterFunctionalTest/assertUrlInboundAlter.md) — Assert that a inbound path is altered to an expected value.

---
_Drupal 7.103 · [modules/simpletest/tests/path.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/path.test) · Licensed GPL-2.0-or-later (see LICENSE)._
