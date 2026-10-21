# ModuleDependencyTestCase::testUninstallDependents()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 541–570 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L541-L570)
- **Class:** [ModuleDependencyTestCase](../ModuleDependencyTestCase.md)
- **Module/theme:** system

## Signature

```php
function testUninstallDependents()
```

## Documentation

```text
Tests attempting to uninstall a module that has installed dependents.
```

## Code

```php
  function testUninstallDependents() {
    // Enable the forum module.
    $edit = array('modules[Core][forum][enable]' => 'forum');
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->assertModules(array('forum'), TRUE);

    // Disable forum and comment. Both should now be installed but disabled.
    $edit = array('modules[Core][forum][enable]' => FALSE);
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->assertModules(array('forum'), FALSE);
    $edit = array('modules[Core][comment][enable]' => FALSE);
    $this->drupalPost('admin/modules', $edit, t('Save configuration'));
    $this->assertModules(array('comment'), FALSE);

    // Check that the taxonomy module cannot be uninstalled.
    $this->drupalGet('admin/modules/uninstall');
    $checkbox = $this->xpath('//input[@type="checkbox" and @disabled="disabled" and @name="uninstall[comment]"]');
    $this->assert(count($checkbox) == 1, 'Checkbox for uninstalling the comment module is disabled.');

    // Uninstall the forum module, and check that taxonomy now can also be
    // uninstalled.
    $edit = array('uninstall[forum]' => 'forum');
    $this->drupalPost('admin/modules/uninstall', $edit, t('Uninstall'));
    $this->drupalPost(NULL, NULL, t('Uninstall'));
    $this->assertText(t('The selected modules have been uninstalled.'), 'Modules status has been updated.');
    $edit = array('uninstall[comment]' => 'comment');
    $this->drupalPost('admin/modules/uninstall', $edit, t('Uninstall'));
    $this->drupalPost(NULL, NULL, t('Uninstall'));
    $this->assertText(t('The selected modules have been uninstalled.'), 'Modules status has been updated.');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
