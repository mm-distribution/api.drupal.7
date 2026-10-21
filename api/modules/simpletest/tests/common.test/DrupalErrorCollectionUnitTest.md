# DrupalErrorCollectionUnitTest

- **Type:** Class
- **File:** [`modules/simpletest/tests/common.test`](_file.md), lines 2742–2828 · [local source](../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2742-L2828)
- **Module/theme:** batch_test

## Signature

```php
class DrupalErrorCollectionUnitTest extends DrupalWebTestCase
```

## Documentation

```text
Tests Simpletest error and exception collector.
```

## Properties

### $collectedErrors

```php
protected $collectedErrors = array();
```

```text
Errors triggered during the test.

Errors are intercepted by the overriden implementation
of DrupalWebTestCase::error below.

@var Array
```

## Methods (derived index)

- [getInfo()](DrupalErrorCollectionUnitTest/getInfo.md)
- [setUp()](DrupalErrorCollectionUnitTest/setUp.md)
- [testErrorCollect()](DrupalErrorCollectionUnitTest/testErrorCollect.md) — Test that simpletest collects errors from the tested site.
- [error()](DrupalErrorCollectionUnitTest/error.md) — Error handler that collects errors in an array.
- [assertError()](DrupalErrorCollectionUnitTest/assertError.md) — Assert that a collected error matches what we are expecting.

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
