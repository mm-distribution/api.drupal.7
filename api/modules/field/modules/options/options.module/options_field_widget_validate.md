# options_field_widget_validate()

- **Type:** Function
- **File:** [`modules/field/modules/options/options.module`](_file.md), lines 171–179 · [local source](../../../../../../source/modules/field/modules/options/options.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module#L171-L179)
- **Module/theme:** options

## Signature

```php
function options_field_widget_validate($element, &$form_state)
```

## Documentation

```text
Form element validation handler for options element.
```

## Code

```php
function options_field_widget_validate($element, &$form_state) {
  if ($element['#required'] && $element['#value'] == '_none') {
    form_error($element, t('!name field is required.', array('!name' => $element['#title'])));
  }
  // Transpose selections from field => delta to delta => field, turning
  // multiple selected options into multiple parent elements.
  $items = _options_form_to_storage($element);
  form_set_value($element, $items, $form_state);
}
```

---
_Drupal 7.103 · [modules/field/modules/options/options.module](https://github.com/drupal/drupal/blob/7.103/modules/field/modules/options/options.module) · Licensed GPL-2.0-or-later (see LICENSE)._
