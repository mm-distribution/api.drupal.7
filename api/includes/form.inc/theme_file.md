# theme_file()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 4205–4212 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L4205-L4212)
- **Topics:** [form_api](../../topics/form_api.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_file($variables)
```

## Documentation

```text
Returns HTML for a file upload form element.

For assistance with handling the uploaded file correctly, see the API
provided by file.inc.

@param $variables
  An associative array containing:
  - element: An associative array containing the properties of the element.
    Properties used: #title, #name, #size, #description, #required,
    #attributes.

@ingroup themeable
```

## Code

```php
function theme_file($variables) {
  $element = $variables['element'];
  $element['#attributes']['type'] = 'file';
  element_set_attributes($element, array('id', 'name', 'size'));
  _form_set_class($element, array('form-file'));

  return '<input' . drupal_attributes($element['#attributes']) . ' />';
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
