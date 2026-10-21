# theme_image_button()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3980–3997 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3980-L3997)
- **Topics:** [form_api](../../topics/form_api.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_image_button($variables)
```

## Documentation

```text
Returns HTML for an image button form element.

@param $variables
  An associative array containing:
  - element: An associative array containing the properties of the element.
    Properties used: #attributes, #button_type, #name, #value, #title, #src.

@ingroup themeable
```

## Code

```php
function theme_image_button($variables) {
  $element = $variables['element'];
  $element['#attributes']['type'] = 'image';
  element_set_attributes($element, array('id', 'name', 'value'));

  $element['#attributes']['src'] = file_create_url($element['#src']);
  if (!empty($element['#title'])) {
    $element['#attributes']['alt'] = $element['#title'];
    $element['#attributes']['title'] = $element['#title'];
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
