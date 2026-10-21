# SimpleTestBrokenSetUp

- **Type:** Class
- **File:** [`modules/simpletest/simpletest.test`](_file.md), lines 586–642 · [local source](../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L586-L642)
- **Module/theme:** simpletest

## Signature

```php
class SimpleTestBrokenSetUp extends DrupalWebTestCase
```

## Documentation

```text
Tests a test case that does not run parent::setUp() in its setUp() method.

If a test case does not call parent::setUp(), running
DrupalTestCase::tearDown() would destroy the main site's database tables.
Therefore, we ensure that tests which are not set up properly are skipped.

@see DrupalTestCase
```

## Methods (derived index)

- [getInfo()](SimpleTestBrokenSetUp/getInfo.md)
- [setUp()](SimpleTestBrokenSetUp/setUp.md)
- [tearDown()](SimpleTestBrokenSetUp/tearDown.md)
- [testBreakSetUp()](SimpleTestBrokenSetUp/testBreakSetUp.md) — Runs this test case from within the simpletest child site.

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
