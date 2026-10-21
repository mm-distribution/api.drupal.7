# _element_validate_integer_positive()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 1218–1220 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L1218-L1220)
- **Module/theme:** field

## Signature

```php
function _element_validate_integer_positive($element, &$form_state)
```

## Documentation

```text
DEPRECATED: Helper form element validator: integer > 0.

Use element_validate_integer_positive() instead.

@deprecated
@see element_validate_integer_positive()
```

## Code

```php
function _element_validate_integer_positive($element, &$form_state) {
  element_validate_integer_positive($element, $form_state);
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
