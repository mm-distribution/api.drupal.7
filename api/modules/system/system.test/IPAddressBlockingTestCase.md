# IPAddressBlockingTestCase

- **Type:** Class
- **File:** [`modules/system/system.test`](_file.md), lines 696–792 · [local source](../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L696-L792)
- **Module/theme:** system

## Signature

```php
class IPAddressBlockingTestCase extends DrupalWebTestCase
```

## Documentation

_No docblock in source._

## Properties

### $blocking_user

```php
protected $blocking_user;
```

## Methods (derived index)

- [getInfo()](IPAddressBlockingTestCase/getInfo.md) — Implement getInfo().
- [setUp()](IPAddressBlockingTestCase/setUp.md) — Implement setUp().
- [testIPAddressValidation()](IPAddressBlockingTestCase/testIPAddressValidation.md) — Test a variety of user input to confirm correct validation and saving of data.
- [testDuplicateIpAddress()](IPAddressBlockingTestCase/testDuplicateIpAddress.md) — Test duplicate IP addresses are not present in the 'blocked_ips' table.

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
