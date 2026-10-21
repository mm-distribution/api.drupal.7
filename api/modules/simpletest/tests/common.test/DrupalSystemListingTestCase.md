# DrupalSystemListingTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/common.test`](_file.md), lines 2856–2911 · [local source](../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L2856-L2911)
- **Module/theme:** batch_test

## Signature

```php
class DrupalSystemListingTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests for the drupal_system_listing() function.
```

## Properties

### $profile

```php
protected $profile = 'testing';
```

```text
Use the testing profile; this is needed for testDirectoryPrecedence().
```

## Methods (derived index)

- [getInfo()](DrupalSystemListingTestCase/getInfo.md)
- [testDirectoryPrecedence()](DrupalSystemListingTestCase/testDirectoryPrecedence.md) — Test that files in different directories take precedence as expected.

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
