# SimpleTestMissingDependentModuleUnitTest::testFail()

- **Type:** Method
- **File:** [`modules/simpletest/simpletest.test`](../_file.md), lines 572–574 · [local source](../../../../../source/modules/simpletest/simpletest.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test#L572-L574)
- **Class:** [SimpleTestMissingDependentModuleUnitTest](../SimpleTestMissingDependentModuleUnitTest.md)
- **Module/theme:** simpletest

## Signature

```php
function testFail()
```

## Documentation

```text
Ensure that this test will not be loaded despite its dependency.
```

## Code

```php
  function testFail() {
    $this->fail(t('Running test with missing required module.'));
  }
```

---
_Drupal 7.103 · [modules/simpletest/simpletest.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/simpletest.test) · Licensed GPL-2.0-or-later (see LICENSE)._
