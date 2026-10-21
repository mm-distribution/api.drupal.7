# FieldUIAlterTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/field_ui/field_ui.test`](../_file.md), lines 692–698 · [local source](../../../../../source/modules/field_ui/field_ui.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test#L692-L698)
- **Class:** [FieldUIAlterTestCase](../FieldUIAlterTestCase.md)
- **Module/theme:** field_ui

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'Widget customization',
      'description' => 'Test custom field widget hooks and callbacks on field administration pages.',
      'group' => 'Field UI',
    );
  }
```

---
_Drupal 7.103 · [modules/field_ui/field_ui.test](https://github.com/drupal/drupal/blob/7.103/modules/field_ui/field_ui.test) · Licensed GPL-2.0-or-later (see LICENSE)._
