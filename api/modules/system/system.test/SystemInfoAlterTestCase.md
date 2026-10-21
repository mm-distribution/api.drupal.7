# SystemInfoAlterTestCase

- **Type:** Class
- **File:** [`modules/system/system.test`](_file.md), lines 2440–2502 · [local source](../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2440-L2502)
- **Module/theme:** system

## Signature

```php
class SystemInfoAlterTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests the effectiveness of hook_system_info_alter().
```

## Methods (derived index)

- [getInfo()](SystemInfoAlterTestCase/getInfo.md)
- [testSystemInfoAlter()](SystemInfoAlterTestCase/testSystemInfoAlter.md) — Tests that {system}.info is rebuilt after a module that implements hook_system_info_alter() is enabled. Also tests if core *_list() functions return freshly altered info.
- [getSystemInfo()](SystemInfoAlterTestCase/getSystemInfo.md) — Returns the info array as it is stored in {system}.

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
