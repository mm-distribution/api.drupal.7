# form_validate_machine_name()

- **Type:** Function
- **File:** [`includes/form.inc`](_file.md), lines 3732–3763 · [local source](../../../source/includes/form.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/form.inc#L3732-L3763)
- **Topics:** [form_api](../../topics/form_api.md)

## Signature

```php
function form_validate_machine_name(&$element, &$form_state)
```

## Documentation

```text
Form element validation handler for machine_name elements.

Note that #maxlength is validated by _form_validate() already.
```

## Code

```php
function form_validate_machine_name(&$element, &$form_state) {
  // Verify that the machine name not only consists of replacement tokens.
  if (preg_match('@^' . $element['#machine_name']['replace'] . '+$@', $element['#value'])) {
    form_error($element, t('The machine-readable name must contain unique characters.'));
  }

  // Verify that the machine name contains no disallowed characters.
  if (preg_match('@' . $element['#machine_name']['replace_pattern'] . '@', $element['#value'])) {
    if (!isset($element['#machine_name']['error'])) {
      // Since a hyphen is the most common alternative replacement character,
      // a corresponding validation error message is supported here.
      if ($element['#machine_name']['replace'] == '-') {
        form_error($element, t('The machine-readable name must contain only lowercase letters, numbers, and hyphens.'));
      }
      // Otherwise, we assume the default (underscore).
      else {
        form_error($element, t('The machine-readable name must contain only lowercase letters, numbers, and underscores.'));
      }
    }
    else {
      form_error($element, $element['#machine_name']['error']);
    }
  }

  // Verify that the machine name is unique.
  if ($element['#default_value'] !== $element['#value']) {
    $function = $element['#machine_name']['exists'];
    if ($function($element['#value'], $element, $form_state)) {
      form_error($element, t('The machine-readable name is already in use. It must be unique.'));
    }
  }
}
```

---
_Drupal 7.103 · [includes/form.inc](https://github.com/drupal/drupal/blob/7.103/includes/form.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
