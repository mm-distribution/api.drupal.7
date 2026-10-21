# theme_select()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 2798–2804 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L2798-L2804)
- **Topics:** [form_api](../../topics/form_api.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_select($variables)
```

## Documentation

```text
Returns HTML for a select form element.

It is possible to group options together; to do this, change the format of
$options to an associative array in which the keys are group labels, and the
values are associative arrays in the normal $options format.

@param $variables
  An associative array containing:
  - element: An associative array containing the properties of the element.
    Properties used: #title, #value, #options, #description, #extra,
    #multiple, #required, #name, #attributes, #size.

@ingroup themeable
```

## Code

```php
function theme_select($variables) {
  $element = $variables['element'];
  element_set_attributes($element, array('id', 'name', 'size'));
  _form_set_class($element, array('form-select'));

  return '<select' . drupal_attributes($element['#attributes']) . '>' . form_select_options($element) . '</select>';
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
