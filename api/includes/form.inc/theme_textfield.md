# theme_textfield()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 4055–4078 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L4055-L4078)
- **Topics:** [form_api](../../topics/form_api.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_textfield($variables)
```

## Documentation

```text
Returns HTML for a textfield form element.

@param $variables
  An associative array containing:
  - element: An associative array containing the properties of the element.
    Properties used: #title, #value, #description, #size, #maxlength,
    #required, #attributes, #autocomplete_path.

@ingroup themeable
```

## Code

```php
function theme_textfield($variables) {
  $element = $variables['element'];
  $element['#attributes']['type'] = 'text';
  element_set_attributes($element, array('id', 'name', 'value', 'size', 'maxlength'));
  _form_set_class($element, array('form-text'));

  $extra = '';
  if ($element['#autocomplete_path'] && !empty($element['#autocomplete_input'])) {
    drupal_add_library('system', 'drupal.autocomplete');
    $element['#attributes']['class'][] = 'form-autocomplete';

    $attributes = array();
    $attributes['type'] = 'hidden';
    $attributes['id'] = $element['#autocomplete_input']['#id'];
    $attributes['value'] = $element['#autocomplete_input']['#url_value'];
    $attributes['disabled'] = 'disabled';
    $attributes['class'][] = 'autocomplete';
    $extra = '<input' . drupal_attributes($attributes) . ' />';
  }

  $output = '<input' . drupal_attributes($element['#attributes']) . ' />';

  return $output . $extra;
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
