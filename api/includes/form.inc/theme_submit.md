# theme_submit()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3938–3940 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3938-L3940)
- **Topics:** [form_api](../../topics/form_api.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_submit($variables)
```

## Documentation

```text
Returns HTML for a submit button form element.

@param $variables
  An associative array containing:
  - element: An associative array containing the properties of the element.
    Properties used: #attributes, #button_type, #name, #value.

@ingroup themeable
```

## Code

```php
function theme_submit($variables) {
  return theme('button', $variables['element']);
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
