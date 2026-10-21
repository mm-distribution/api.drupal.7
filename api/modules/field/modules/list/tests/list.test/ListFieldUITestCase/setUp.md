# ListFieldUITestCase::setUp()

- **Type:** Method
- **File:** [`modules/field/modules/list/tests/list.test`](../_file.md), lines 226–239 · [local source](../../../../../../../../source/modules/field/modules/list/tests/list.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test#L226-L239)
- **Class:** [ListFieldUITestCase](../ListFieldUITestCase.md)
- **Module/theme:** list_test

## Signature

```php
function setUp()
```

## Documentation

_No docblock in source._

## Code

```php
  function setUp() {
    parent::setUp('field_test', 'field_ui');

    // Create test user.
    $admin_user = $this->drupalCreateUser(array('access content', 'administer content types', 'administer taxonomy', 'administer fields'));
    $this->drupalLogin($admin_user);

    // Create content type, with underscores.
    $type_name = 'test_' . strtolower($this->randomName());
    $type = $this->drupalCreateContentType(array('name' => $type_name, 'type' => $type_name));
    $this->type = $type->type;
    // Store a valid URL name, with hyphens instead of underscores.
    $this->hyphen_type = str_replace('_', '-', $this->type);
  }
```

---
_Drupal 7.103 · [modules/field/modules/list/tests/list.test](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/list/tests/list.test) · Licensed GPL-2.0-or-later (see LICENSE)._
