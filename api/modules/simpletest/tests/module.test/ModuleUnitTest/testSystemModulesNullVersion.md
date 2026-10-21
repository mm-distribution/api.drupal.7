# ModuleUnitTest::testSystemModulesNullVersion()

- **Type:** Method
- **File:** [`modules/simpletest/tests/module.test`](../_file.md), lines 132–139 · [local source](../../../../../../source/modules/simpletest/tests/module.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test#L132-L139)
- **Class:** [ModuleUnitTest](../ModuleUnitTest.md)
- **Module/theme:** batch_test

## Signature

```php
function testSystemModulesNullVersion()
```

## Documentation

```text
Test system_modules() with a module with a dependency with a null version.
```

## Code

```php
  function testSystemModulesNullVersion() {
    module_enable(array('system_requires_null_version_test'), FALSE);
    $this->resetAll();
    $admin = $this->drupalCreateUser(array('administer modules'));
    $this->drupalLogin($admin);
    $this->drupalGet('admin/modules');
    $this->assertText('System null version test', 'Module admin UI listed dependency with null version successfully.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/module.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/module.test) · Licensed GPL-2.0-or-later (see LICENSE)._
