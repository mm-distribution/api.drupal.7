# FieldUIAlterTestCase::setUp()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 700–706 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L700-L706)
- **Class:** [FieldUIAlterTestCase](../FieldUIAlterTestCase.md)
- **Module/theme:** field_ui

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp(array('field_test'));

    // Create test user.
    $admin_user = $this->drupalCreateUser(array('access content', 'administer content types', 'administer users', 'administer fields'));
    $this->drupalLogin($admin_user);
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
