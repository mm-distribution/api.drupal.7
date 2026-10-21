# DateTimeFunctionalTest::setUp()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1332–1338 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1332-L1338)
- **Class:** [DateTimeFunctionalTest](../DateTimeFunctionalTest.md)
- **Module/theme:** system

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp(array('locale'));

    // Create admin user and log in admin user.
    $this->admin_user = $this->drupalCreateUser(array('administer site configuration'));
    $this->drupalLogin($this->admin_user);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
