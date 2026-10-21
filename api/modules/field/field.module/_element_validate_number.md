# _element_validate_number()

- **Type:** Function
- **File:** [`modules/field/field.module`](_file.md), lines 1230–1232 · [local source](../../../../source/modules/field/field.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module#L1230-L1232)
- **Module/theme:** field

## Signature

```php
function _element_validate_number($element, &$form_state)
```

## Documentation

```text
DEPRECATED: Helper form element validator: number.

Use element_validate_number() instead.

@deprecated
@see element_validate_number()
```

## Code

```php
function _element_validate_number($element, &$form_state) {
  element_validate_number($element, $form_state);
}
```

---
_Drupal 7.103 · [modules/field/field.module](https://github.com/drupal/drupal/blob/7.103/modules/field/field.module) · Licensed GPL-2.0-or-later (see LICENSE)._
