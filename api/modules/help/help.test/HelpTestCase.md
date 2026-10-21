# HelpTestCase

- **Type:** Class
- **File:** [`modules/help/help.test`](_file.md), lines 11–108 · [local source](../../../../source/modules/help/help.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/help/help.test#L11-L108)
- **Module/theme:** help

## Signature

```php
class HelpTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests help display and user access for all modules implementing help.
```

## Properties

### $big_user

```php
protected $big_user;
```

```text
The admin user that will be created.
```

### $any_user

```php
protected $any_user;
```

```text
The anonymous user that will be created.
```

### $modules

```php
protected $modules;
```

```text
The list of modules.
```

## Methods (derived index)

- [getInfo()](HelpTestCase/getInfo.md)
- [setUp()](HelpTestCase/setUp.md)
- [testHelp()](HelpTestCase/testHelp.md) — Logs in users, creates dblog events, and tests dblog functionality.
- [verifyHelp()](HelpTestCase/verifyHelp.md) — Verifies the logged in user has access to the various help nodes.
- [getModuleList()](HelpTestCase/getModuleList.md) — Gets the list of enabled modules that implement hook_help().

---
_Drupal 7.103 · [modules/help/help.test](https://github.com/drupal/drupal/blob/7.103/modules/help/help.test) · Licensed GPL-2.0-or-later (see LICENSE)._
