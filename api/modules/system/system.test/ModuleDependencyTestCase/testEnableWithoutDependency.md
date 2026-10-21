# ModuleDependencyTestCase::testEnableWithoutDependency()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 407–428 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L407-L428)
- **Class:** [ModuleDependencyTestCase](../ModuleDependencyTestCase.md)
- **Module/theme:** system

## Signature

```php
function testEnableWithoutDependency()
```

## Documentation

```text
Attempt to enable translation module without locale enabled.
```

## Code

```php
  function testEnableWithoutDependency() {
    // Attempt to enable content translation without locale enabled.
    $edit = array();
    $edit['modules[Core][translation][enable]'] = 'translation';
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->assertText(t('Some required modules must be enabled'), 'Dependency required.');

    $this->assertModules(array('translation', 'locale'), FALSE);

    // Assert that the locale tables weren't enabled.
    $this->assertTableCount('languages', FALSE);
    $this->assertTableCount('locale', FALSE);

    $this->drupalPost(NULL, NULL, t('Continue'));
    $this->assertText(t('The configuration options have been saved.'), 'Modules status has been updated.');

    $this->assertModules(array('translation', 'locale'), TRUE);

    // Assert that the locale tables were enabled.
    $this->assertTableCount('languages', TRUE);
    $this->assertTableCount('locale', TRUE);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
