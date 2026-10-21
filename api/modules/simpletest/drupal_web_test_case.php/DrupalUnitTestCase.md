# DrupalUnitTestCase

- **Type:** Class
- **File:** [`modules/simpletest/drupal_web_test_case.php`](_file.md), lines 755–844 · [local source](../../../../source/modules/simpletest/drupal_web_test_case.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php#L755-L844)
- **Module/theme:** simpletest

## Signature

```php
class DrupalUnitTestCase extends DrupalTestCase
```

## Documentation

```text
Test case for Drupal unit tests.

These tests can not access the database nor files. Calling any Drupal
function that needs the database will throw exceptions. These include
watchdog(), module_implements(), module_invoke_all() etc.
```

## Methods (derived index)

- [__construct()](DrupalUnitTestCase/__construct.md) — Constructor for DrupalUnitTestCase.
- [setUp()](DrupalUnitTestCase/setUp.md) — Sets up unit test environment.
- [tearDown()](DrupalUnitTestCase/tearDown.md)

---
_Drupal 7.103 · [modules/simpletest/drupal_web_test_case.php](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/drupal_web_test_case.php) · Licensed GPL-2.0-or-later (see LICENSE)._
