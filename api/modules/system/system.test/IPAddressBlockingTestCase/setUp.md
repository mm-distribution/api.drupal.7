# IPAddressBlockingTestCase::setUp()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 713–719 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L713-L719)
- **Class:** [IPAddressBlockingTestCase](../IPAddressBlockingTestCase.md)
- **Module/theme:** system

## Signature

```php
function setUp()
```

## Documentation

```text
Implement setUp().
```

## Code

```php
  function setUp() {
    parent::setUp();

    // Create user.
    $this->blocking_user = $this->drupalCreateUser(array('block IP addresses'));
    $this->drupalLogin($this->blocking_user);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
