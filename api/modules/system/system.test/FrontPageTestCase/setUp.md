# FrontPageTestCase::setUp()

- **Type:** Method
- **File:** [`modules/system/system.test`](../_file.md), lines 1703–1713 · [local source](../../../../../source/modules/system/system.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test#L1703-L1713)
- **Class:** [FrontPageTestCase](../FrontPageTestCase.md)
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

    // Create admin user, log in admin user, and create one node.
    $this->admin_user = $this->drupalCreateUser(array('access content', 'administer site configuration'));
    $this->drupalLogin($this->admin_user);
    $this->node_path = "node/" . $this->drupalCreateNode(array('promote' => 1))->nid;

    // Enable front page logging in system_test.module.
    variable_set('front_page_output', 1);
  }
```

---
_Drupal 7.103 · [modules/system/system.test](https://github.com/drupal/drupal/blob/7.103/modules/system/system.test) · Licensed GPL-2.0-or-later (see LICENSE)._
