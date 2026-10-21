# ModuleDependencyTestCase::testProjectNamespaceForDependencies()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 395–402 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L395-L402)
- **Class:** [ModuleDependencyTestCase](../ModuleDependencyTestCase.md)
- **Module/theme:** system

## Signature

```php
function testProjectNamespaceForDependencies()
```

## Documentation

```text
Checks functionality of project namespaces for dependencies.
```

## Code

```php
  function testProjectNamespaceForDependencies() {
    // Enable module with project namespace to ensure nothing breaks.
    $edit = array(
      'modules[Testing][system_project_namespace_test][enable]' => TRUE,
    );
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->assertModules(array('system_project_namespace_test'), TRUE);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
