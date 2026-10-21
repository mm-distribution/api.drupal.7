# SystemAdminTestCase::setUp()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 2827–2840 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L2827-L2840)
- **Class:** [SystemAdminTestCase](../SystemAdminTestCase.md)
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
    // testAdminPages() requires Locale module.
    parent::setUp(array('locale'));

    // Create an administrator with all permissions, as well as a regular user
    // who can only access administration pages and perform some Locale module
    // administrative tasks, but not all of them.
    $this->admin_user = $this->drupalCreateUser(array_keys(module_invoke_all('permission')));
    $this->web_user = $this->drupalCreateUser(array(
      'access administration pages',
      'translate interface',
    ));
    $this->drupalLogin($this->admin_user);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
