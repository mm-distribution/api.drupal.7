# UpdateCoreTestCase::setUp()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 73–77 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L73-L77)
- **Class:** [UpdateCoreTestCase](../UpdateCoreTestCase.md)
- **Module/theme:** update

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('update_test', 'update');
    $admin_user = $this->drupalCreateUser(array('administer site configuration', 'administer modules'));
    $this->drupalLogin($admin_user);
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
