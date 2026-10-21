# theme_container()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3444–3460 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3444-L3460)
- **Topics:** [form_api](../../topics/form_api.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_container($variables)
```

## Documentation

```text
Returns HTML to wrap child elements in a container.

Used for grouped form items. Can also be used as a theme wrapper for any
renderable element, to surround it with a <div> and add attributes such as
classes or an HTML ID.

See the @link forms_api_reference.html Form API reference @endlink for more
information on the #theme_wrappers render array property.

@param $variables
  An associative array containing:
  - element: An associative array containing the properties of the element.
    Properties used: #id, #attributes, #children.

@ingroup themeable
```

## Code

```php
function theme_container($variables) {
  $element = $variables['element'];
  // Ensure #attributes is set.
  $element += array('#attributes' => array());

  // Special handling for form elements.
  if (isset($element['#array_parents'])) {
    // Assign an html ID.
    if (!isset($element['#attributes']['id'])) {
      $element['#attributes']['id'] = $element['#id'];
    }
    // Add the 'form-wrapper' class.
    $element['#attributes']['class'][] = 'form-wrapper';
  }

  return '<div' . drupal_attributes($element['#attributes']) . '>' . $element['#children'] . '</div>';
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
