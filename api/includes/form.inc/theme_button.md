# theme_button()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3952–3968 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3952-L3968)
- **Topics:** [form_api](../../topics/form_api.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_button($variables)
```

## Documentation

```text
Returns HTML for a button form element.

@param $variables
  An associative array containing:
  - element: An associative array containing the properties of the element.
    Properties used: #attributes, #button_type, #name, #value.

@ingroup themeable
```

## Code

```php
function theme_button($variables) {
  $element = $variables['element'];
  $element['#attributes']['type'] = 'submit';
  element_set_attributes($element, array('id', 'name', 'value'));

  // Remove name attribute, if empty, for W3C compliance.
  if (isset($element['#attributes']['name']) && $element['#attributes']['name'] === '') {
    unset($element['#attributes']['name']);
  }

  $element['#attributes']['class'][] = 'form-' . $element['#button_type'];
  if (!empty($element['#attributes']['disabled'])) {
    $element['#attributes']['class'][] = 'form-button-disabled';
  }

  return '<input' . drupal_attributes($element['#attributes']) . ' />';
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
