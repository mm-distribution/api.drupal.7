# BlockCacheTestCase::setUp()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 501–522 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L501-L522)
- **Class:** [BlockCacheTestCase](../BlockCacheTestCase.md)
- **Module/theme:** block

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('block_test');

    // Create an admin user, log in and enable test blocks.
    $this->admin_user = $this->drupalCreateUser(array('administer blocks', 'access administration pages'));
    $this->drupalLogin($this->admin_user);

    // Create additional users to test caching modes.
    $this->normal_user = $this->drupalCreateUser();
    $this->normal_user_alt = $this->drupalCreateUser();
    // Sync the roles, since drupalCreateUser() creates separate roles for
    // the same permission sets.
    user_save($this->normal_user_alt, array('roles' => $this->normal_user->roles));
    $this->normal_user_alt->roles = $this->normal_user->roles;

    // Enable block caching.
    variable_set('block_cache', TRUE);

    // Enable our test block.
    $edit['blocks[block_test_test_cache][region]'] = 'sidebar_first';
    $this->drupalPost('admin/structure/block', $edit, t('Save blocks'));
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
