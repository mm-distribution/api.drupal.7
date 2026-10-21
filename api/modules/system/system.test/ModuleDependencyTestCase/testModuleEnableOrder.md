# ModuleDependencyTestCase::testModuleEnableOrder()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 513–536 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L513-L536)
- **Class:** [ModuleDependencyTestCase](../ModuleDependencyTestCase.md)
- **Module/theme:** system

## Signature

```php
function testModuleEnableOrder()
```

## Documentation

```text
Tests that module dependencies are enabled in the correct order via the
UI. Dependencies should be enabled before their dependents.
```

## Code

```php
  function testModuleEnableOrder() {
    module_enable(array('module_test'), FALSE);
    $this->resetAll();
    $this->assertModules(array('module_test'), TRUE);
    variable_set('dependency_test', 'dependency');
    // module_test creates a dependency chain: forum depends on poll, which
    // depends on php. The correct enable order is, php, poll, forum.
    $expected_order = array('php', 'poll', 'forum');

    // Enable the modules through the UI, verifying that the dependency chain
    // is correct.
    $edit = array();
    $edit['modules[Core][forum][enable]'] = 'forum';
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->assertModules(array('forum'), FALSE);
    $this->assertText(t('You must enable the Poll, PHP filter modules to install Forum.'), t('Dependency chain created.'));
    $edit['modules[Core][poll][enable]'] = 'poll';
    $edit['modules[Core][php][enable]'] = 'php';
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->assertModules(array('forum', 'poll', 'php'), TRUE);

    // Check the actual order which is saved by module_test_modules_enabled().
    $this->assertIdentical(variable_get('test_module_enable_order', FALSE), $expected_order, t('Modules enabled in the correct order.'));
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
