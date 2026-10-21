# UpdateTestUploadCase::setUp()

- **Type:** Method
- **File:** [`modules/update/update.test`](../_file.md), lines 708–713 · [local source](../../../../../source/modules/update/update.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test#L708-L713)
- **Class:** [UpdateTestUploadCase](../UpdateTestUploadCase.md)
- **Module/theme:** update

## Signature

```php
public function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  public function setUp() {
    parent::setUp('update', 'update_test');
    variable_set('allow_authorize_operations', TRUE);
    $admin_user = $this->drupalCreateUser(array('administer software updates', 'administer site configuration'));
    $this->drupalLogin($admin_user);
  }
```

---
_Drupal 7.103 · [modules/update/update.test](https://github.com/drupal/drupal/blob/7.103/modules/update/update.test) · Licensed GPL-2.0-or-later (see LICENSE)._
