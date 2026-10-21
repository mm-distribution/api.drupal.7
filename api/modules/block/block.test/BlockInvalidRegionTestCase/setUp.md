# BlockInvalidRegionTestCase::setUp()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 850–855 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L850-L855)
- **Class:** [BlockInvalidRegionTestCase](../BlockInvalidRegionTestCase.md)
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
    parent::setUp(array('block', 'block_test'));
    // Create an admin user.
    $admin_user = $this->drupalCreateUser(array('administer site configuration', 'access administration pages'));
    $this->drupalLogin($admin_user);
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
