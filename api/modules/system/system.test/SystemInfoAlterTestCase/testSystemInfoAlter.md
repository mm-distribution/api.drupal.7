# SystemInfoAlterTestCase::testSystemInfoAlter()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2454–2485 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2454-L2485)
- **Class:** [SystemInfoAlterTestCase](../SystemInfoAlterTestCase.md)
- **Module/theme:** system

## Signature

```php
function testSystemInfoAlter()
```

## Documentation

```text
Tests that {system}.info is rebuilt after a module that implements
hook_system_info_alter() is enabled. Also tests if core *_list() functions
return freshly altered info.
```

## Code

```php
  function testSystemInfoAlter() {
    // Enable our test module. Flush all caches, which we assert is the only
    // thing necessary to use the rebuilt {system}.info.
    module_enable(array('module_test'), FALSE);
    drupal_flush_all_caches();
    $this->assertTrue(module_exists('module_test'), 'Test module is enabled.');

    $info = $this->getSystemInfo('seven', 'theme');
    $this->assertTrue(isset($info['regions']['test_region']), 'Altered theme info was added to {system}.info.');
    $seven_regions = system_region_list('seven');
    $this->assertTrue(isset($seven_regions['test_region']), 'Altered theme info was returned by system_region_list().');
    $system_list_themes = system_list('theme');
    $info = $system_list_themes['seven']->info;
    $this->assertTrue(isset($info['regions']['test_region']), 'Altered theme info was returned by system_list().');
    $list_themes = list_themes();
    $this->assertTrue(isset($list_themes['seven']->info['regions']['test_region']), 'Altered theme info was returned by list_themes().');

    // Disable the module and verify that {system}.info is rebuilt without it.
    module_disable(array('module_test'), FALSE);
    drupal_flush_all_caches();
    $this->assertFalse(module_exists('module_test'), 'Test module is disabled.');

    $info = $this->getSystemInfo('seven', 'theme');
    $this->assertFalse(isset($info['regions']['test_region']), 'Altered theme info was removed from {system}.info.');
    $seven_regions = system_region_list('seven');
    $this->assertFalse(isset($seven_regions['test_region']), 'Altered theme info was not returned by system_region_list().');
    $system_list_themes = system_list('theme');
    $info = $system_list_themes['seven']->info;
    $this->assertFalse(isset($info['regions']['test_region']), 'Altered theme info was not returned by system_list().');
    $list_themes = list_themes();
    $this->assertFalse(isset($list_themes['seven']->info['regions']['test_region']), 'Altered theme info was not returned by list_themes().');
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
