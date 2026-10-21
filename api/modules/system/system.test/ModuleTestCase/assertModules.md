# ModuleTestCase::assertModules()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 81–92 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L81-L92)
- **Class:** [ModuleTestCase](../ModuleTestCase.md)
- **Module/theme:** system

## Signature

```php
function assertModules(array $modules, $enabled)
```

## Documentation

```text
Assert the list of modules are enabled or disabled.

@param $modules
  Module list to check.
@param $enabled
  Expected module state.
```

## Code

```php
  function assertModules(array $modules, $enabled) {
    module_list(TRUE);
    foreach ($modules as $module) {
      if ($enabled) {
        $message = 'Module "@module" is enabled.';
      }
      else {
        $message = 'Module "@module" is not enabled.';
      }
      $this->assertEqual(module_exists($module), $enabled, format_string($message, array('@module' => $module)));
    }
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
