# UpdateScriptFunctionalTest

- **Type:** Class
- **File:** [`modules/system/system.test`](_file.md), lines 2507–2691 · [local source](../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2507-L2691)
- **Module/theme:** system

## Signature

```php
class UpdateScriptFunctionalTest extends DrupalWebTestCase
```

## Documentation

```text
Tests for the update system functionality.
```

## Properties

### $update_url

```php
private $update_url;
```

### $update_user

```php
private $update_user;
```

## Methods (derived index)

- [getInfo()](UpdateScriptFunctionalTest/getInfo.md)
- [setUp()](UpdateScriptFunctionalTest/setUp.md)
- [testNoPendingUpdates()](UpdateScriptFunctionalTest/testNoPendingUpdates.md) — Tests that there are no pending updates for the first test method.
- [testUpdateAccess()](UpdateScriptFunctionalTest/testUpdateAccess.md) — Tests access to the update script.
- [testRequirements()](UpdateScriptFunctionalTest/testRequirements.md) — Tests that requirements warnings and errors are correctly displayed.
- [testThemeSystem()](UpdateScriptFunctionalTest/testThemeSystem.md) — Tests the effect of using the update script on the theme system.
- [testNoUpdateFunctionality()](UpdateScriptFunctionalTest/testNoUpdateFunctionality.md) — Tests update.php when there are no updates to apply.
- [testSuccessfulUpdateFunctionality()](UpdateScriptFunctionalTest/testSuccessfulUpdateFunctionality.md) — Tests update.php after performing a successful update.

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
