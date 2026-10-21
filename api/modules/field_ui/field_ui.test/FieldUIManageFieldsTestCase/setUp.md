# FieldUIManageFieldsTestCase::setUp()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 151–158 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L151-L158)
- **Class:** [FieldUIManageFieldsTestCase](../FieldUIManageFieldsTestCase.md)
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
    parent::setUp();

    // Create random field name.
    $this->field_label = $this->randomName(8);
    $this->field_name_input =  strtolower($this->randomName(8));
    $this->field_name = 'field_'. $this->field_name_input;
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
