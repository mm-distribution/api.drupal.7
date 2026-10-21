# SystemMainContentFallback::setUp()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1826–1841 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1826-L1841)
- **Class:** [SystemMainContentFallback](../SystemMainContentFallback.md)
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
    parent::setUp('system_test');

    // Create and login admin user.
    $this->admin_user = $this->drupalCreateUser(array(
      'access administration pages',
      'administer site configuration',
      'administer modules',
      'administer blocks',
      'administer nodes',
    ));
    $this->drupalLogin($this->admin_user);

    // Create a web user.
    $this->web_user = $this->drupalCreateUser(array('access user profiles', 'access content'));
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
