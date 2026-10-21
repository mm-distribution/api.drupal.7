# ModuleUnitTest::assertModuleList()

- **Type:** Method
- **File:** [`modules/simpletest/tests/module.test`](../_file.md), lines 93–98 · [local source](../../../../../../source/modules/simpletest/tests/module.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test#L93-L98)
- **Class:** [ModuleUnitTest](../ModuleUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
protected function assertModuleList(Array $expected_values, $condition)
```

## Documentation

```text
Assert that module_list() return the expected values.

@param $expected_values
  The expected values, sorted by weight and module name.
```

## Code

```php
  protected function assertModuleList(Array $expected_values, $condition) {
    $expected_values = array_combine($expected_values, $expected_values);
    $this->assertEqual($expected_values, module_list(), format_string('@condition: module_list() returns correct results', array('@condition' => $condition)));
    ksort($expected_values);
    $this->assertIdentical($expected_values, module_list(FALSE, FALSE, TRUE), format_string('@condition: module_list() returns correctly sorted results', array('@condition' => $condition)));
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/module.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test) · Licensed GPL-2.0-or-later (see LICENSE)._
