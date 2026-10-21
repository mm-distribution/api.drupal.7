# PageNotFoundTestCase::setUp()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1150–1156 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1150-L1156)
- **Class:** [PageNotFoundTestCase](../PageNotFoundTestCase.md)
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

    // Create an administrative user.
    $this->admin_user = $this->drupalCreateUser(array('administer site configuration'));
    $this->drupalLogin($this->admin_user);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
