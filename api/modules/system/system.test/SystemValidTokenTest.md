# SystemValidTokenTest

- **Type:** Class
- **File:** [`modules/system/system.test`](_file.md), lines 3079–3131 · [local source](../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L3079-L3131)
- **Module/theme:** system

## Signature

```php
class SystemValidTokenTest extends DrupalUnitTestCase
```

## Documentation

```text
Test case for drupal_valid_token().
```

## Properties

### $assertErrors

```php
protected $assertErrors = TRUE;
```

```text
Flag to indicate whether PHP error reportings should be asserted.

@var bool
```

## Methods (derived index)

- [getInfo()](SystemValidTokenTest/getInfo.md)
- [testTokenValidation()](SystemValidTokenTest/testTokenValidation.md) — Tests invalid invocations of drupal_valid_token() that must return FALSE.
- [errorHandler()](SystemValidTokenTest/errorHandler.md) — Overrides DrupalTestCase::errorHandler().

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
