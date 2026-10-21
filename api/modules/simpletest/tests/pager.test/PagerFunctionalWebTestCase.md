# PagerFunctionalWebTestCase

- **Type:** Class
- **File:** [`modules/simpletest/tests/pager.test`](_file.md), lines 11–175 · [local source](../../../../../source/modules/simpletest/tests/pager.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/pager.test#L11-L175)
- **Module/theme:** batch_test

## Signature

```php
class PagerFunctionalWebTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests pager functionality.
```

## Properties

### $profile

```php
protected $profile = 'testing';
```

### $admin_user

```php
protected $admin_user;
```

## Methods (derived index)

- [getInfo()](PagerFunctionalWebTestCase/getInfo.md)
- [setUp()](PagerFunctionalWebTestCase/setUp.md)
- [testActiveClass()](PagerFunctionalWebTestCase/testActiveClass.md) — Tests markup and CSS classes of pager links.
- [testThemePagerQuantityNotSet()](PagerFunctionalWebTestCase/testThemePagerQuantityNotSet.md) — Tests theme_pager() when an empty quantity is passed.
- [assertPagerItems()](PagerFunctionalWebTestCase/assertPagerItems.md) — Asserts pager items and links.
- [assertClass()](PagerFunctionalWebTestCase/assertClass.md) — Asserts that an element has a given class.
- [assertNoClass()](PagerFunctionalWebTestCase/assertNoClass.md) — Asserts that an element does not have a given class.

---
_Drupal 7.103 · [modules/simpletest/tests/pager.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/pager.test) · Licensed GPL-2.0-or-later (see LICENSE)._
