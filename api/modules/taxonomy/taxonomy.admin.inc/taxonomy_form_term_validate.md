# taxonomy_form_term_validate()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.admin.inc`](_file.md), lines 787–794 · [local source](../../../../source/modules/taxonomy/taxonomy.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc#L787-L794)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_form_term_validate($form, &$form_state)
```

## Documentation

```text
Validation handler for the term form.

@see taxonomy_form_term()
```

## Code

```php
function taxonomy_form_term_validate($form, &$form_state) {
  entity_form_field_validate('taxonomy_term', $form, $form_state);

  // Ensure numeric values.
  if (isset($form_state['values']['weight']) && !is_numeric($form_state['values']['weight'])) {
    form_set_error('weight', t('Weight value must be numeric.'));
  }
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
