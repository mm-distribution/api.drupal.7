# NoHelpTestCase

- **Type:** Class
- **File:** [`modules/help/help.test`](_file.md), lines 113–142 · [local source](../../../../source/modules/help/help.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/help/help.test#L113-L142)
- **Module/theme:** help

## Signature

```php
class NoHelpTestCase extends DrupalWebTestCase
```

## Documentation

```text
Tests a module without help to verify it is not listed in the help page.
```

## Properties

### $big_user

```php
protected $big_user;
```

```text
The user who will be created.
```

## Methods (derived index)

- [getInfo()](NoHelpTestCase/getInfo.md)
- [setUp()](NoHelpTestCase/setUp.md)
- [testMainPageNoHelp()](NoHelpTestCase/testMainPageNoHelp.md) — Ensures modules not implementing help do not appear on admin/help.

---
_Drupal 7.103 · [modules/help/help.test](https://github.com/drupal/drupal/blob/7.103/modules/help/help.test) · Licensed GPL-2.0-or-later (see LICENSE)._
