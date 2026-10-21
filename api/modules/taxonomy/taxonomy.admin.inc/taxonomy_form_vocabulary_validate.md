# taxonomy_form_vocabulary_validate()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.admin.inc`](_file.md), lines 193–203 · [local source](../../../../source/modules/taxonomy/taxonomy.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc#L193-L203)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_form_vocabulary_validate($form, &$form_state)
```

## Documentation

```text
Form validation handler for taxonomy_form_vocabulary().

Makes sure that the machine name of the vocabulary is not in the
disallowed list (names that conflict with menu items, such as 'list'
and 'add').

@see taxonomy_form_vocabulary()
@see taxonomy_form_vocabulary_submit()
```

## Code

```php
function taxonomy_form_vocabulary_validate($form, &$form_state) {
  // During the deletion there is no 'machine_name' key
  if (isset($form_state['values']['machine_name'])) {
    // Do not allow machine names to conflict with taxonomy path arguments.
    $machine_name = $form_state['values']['machine_name'];
    $disallowed = array('add', 'list');
    if (in_array($machine_name, $disallowed)) {
      form_set_error('machine_name', t('The machine-readable name cannot be "add" or "list".'));
    }
  }
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
