# FieldUITestCase::setUp()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 15–36 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L15-L36)
- **Class:** [FieldUITestCase](../FieldUITestCase.md)
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
    // Since this is a base class for many test cases, support the same
    // flexibility that DrupalWebTestCase::setUp() has for the modules to be
    // passed in as either an array or a variable number of string arguments.
    $modules = func_get_args();
    if (isset($modules[0]) && is_array($modules[0])) {
      $modules = $modules[0];
    }
    $modules[] = 'field_test';
    parent::setUp($modules);

    // Create test user.
    $admin_user = $this->drupalCreateUser(array('access content', 'administer content types', 'administer taxonomy', 'administer fields'));
    $this->drupalLogin($admin_user);

    // Create content type, with underscores.
    $type_name = strtolower($this->randomName(8)) . '_test';
    $type = $this->drupalCreateContentType(array('name' => $type_name, 'type' => $type_name));
    $this->type = $type->type;
    // Store a valid URL name, with hyphens instead of underscores.
    $this->hyphen_type = str_replace('_', '-', $this->type);
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
