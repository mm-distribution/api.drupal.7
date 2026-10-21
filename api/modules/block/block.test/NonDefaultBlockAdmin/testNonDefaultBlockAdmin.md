# NonDefaultBlockAdmin::testNonDefaultBlockAdmin()

- **Type:** Method
- **File:** [`modules/block/block.test`](../_file.md), lines 395–400 · [local source](../../../../../source/modules/block/block.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test#L395-L400)
- **Class:** [NonDefaultBlockAdmin](../NonDefaultBlockAdmin.md)
- **Module/theme:** block

## Signature

```php
function testNonDefaultBlockAdmin()
```

## Documentation

```text
Test non-default theme admin.
```

## Code

```php
  function testNonDefaultBlockAdmin() {
    $admin_user = $this->drupalCreateUser(array('administer blocks', 'administer themes'));
    $this->drupalLogin($admin_user);
    theme_enable(array('stark'));
    $this->drupalGet('admin/structure/block/list/stark');
  }
```

---
_Drupal 7.103 · [modules/block/block.test](https://github.com/drupal/drupal/blob/7.103/modules/block/block.test) · Licensed GPL-2.0-or-later (see LICENSE)._
