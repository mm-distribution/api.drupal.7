# theme_radios()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 2999–3013 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L2999-L3013)
- **Topics:** [form_api](../../topics/form_api.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_radios($variables)
```

## Documentation

```text
Returns HTML for a set of radio button form elements.

@param $variables
  An associative array containing:
  - element: An associative array containing the properties of the element.
    Properties used: #title, #value, #options, #description, #required,
    #attributes, #children.

@ingroup themeable
```

## Code

```php
function theme_radios($variables) {
  $element = $variables['element'];
  $attributes = array();
  if (isset($element['#id'])) {
    $attributes['id'] = $element['#id'];
  }
  $attributes['class'] = 'form-radios';
  if (!empty($element['#attributes']['class'])) {
    $attributes['class'] .= ' ' . implode(' ', $element['#attributes']['class']);
  }
  if (isset($element['#attributes']['title'])) {
    $attributes['title'] = $element['#attributes']['title'];
  }
  return '<div' . drupal_attributes($attributes) . '>' . (!empty($element['#children']) ? $element['#children'] : '') . '</div>';
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
