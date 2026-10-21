# theme_form_required_marker()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 4331–4339 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L4331-L4339)
- **Topics:** [form_api](../../topics/form_api.md), [themeable](../../topics/themeable.md)

## Signature

```php
function theme_form_required_marker($variables)
```

## Documentation

```text
Returns HTML for a marker for required form elements.

@param $variables
  An associative array containing:
  - element: An associative array containing the properties of the element.

@ingroup themeable
```

## Code

```php
function theme_form_required_marker($variables) {
  // This is also used in the installer, pre-database setup.
  $t = get_t();
  $attributes = array(
    'class' => 'form-required',
    'title' => $t('This field is required.'),
  );
  return '<span' . drupal_attributes($attributes) . '>*</span>';
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
