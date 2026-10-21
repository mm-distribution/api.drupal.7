# _element_validate_integer()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 1206–1208 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L1206-L1208)
- **Module/theme:** field

## Signature

```php
function _element_validate_integer($element, &$form_state)
```

## Documentation

```text
DEPRECATED: Helper form element validator: integer.

Use element_validate_integer() instead.

@deprecated
@see element_validate_integer()
```

## Code

```php
function _element_validate_integer($element, &$form_state) {
  element_validate_integer($element, $form_state);
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
