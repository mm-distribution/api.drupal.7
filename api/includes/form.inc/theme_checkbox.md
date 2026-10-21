# theme_checkbox()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3238–3250 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3238-L3250)
- **Topics:** [form_api](../../topics/form_api.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_checkbox($variables)
```

## Documentation

```text
Returns HTML for a checkbox form element.

@param $variables
  An associative array containing:
  - element: An associative array containing the properties of the element.
    Properties used: #id, #name, #attributes, #checked, #return_value.

@ingroup themeable
```

## Code

```php
function theme_checkbox($variables) {
  $element = $variables['element'];
  $element['#attributes']['type'] = 'checkbox';
  element_set_attributes($element, array('id', 'name', '#return_value' => 'value'));

  // Unchecked checkbox has #value of integer 0.
  if (!empty($element['#checked'])) {
    $element['#attributes']['checked'] = 'checked';
  }
  _form_set_class($element, array('form-checkbox'));

  return '<input' . drupal_attributes($element['#attributes']) . ' />';
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
