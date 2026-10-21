# theme_hidden()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 4009–4014 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L4009-L4014)
- **Topics:** [form_api](../../topics/form_api.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_hidden($variables)
```

## Documentation

```text
Returns HTML for a hidden form element.

@param $variables
  An associative array containing:
  - element: An associative array containing the properties of the element.
    Properties used: #name, #value, #attributes.

@ingroup themeable
```

## Code

```php
function theme_hidden($variables) {
  $element = $variables['element'];
  $element['#attributes']['type'] = 'hidden';
  element_set_attributes($element, array('name', 'value'));
  return '<input' . drupal_attributes($element['#attributes']) . " />\n";
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
