# taxonomy_term_confirm_delete()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.admin.inc`](_file.md), lines 873–891 · [local source](../../../../source/modules/taxonomy/taxonomy.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc#L873-L891)
- **Module/theme:** taxonomy
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function taxonomy_term_confirm_delete($form, &$form_state, $tid)
```

## Documentation

```text
Form builder for the term delete form.

@ingroup forms
@see taxonomy_term_confirm_delete_submit()
```

## Code

```php
function taxonomy_term_confirm_delete($form, &$form_state, $tid) {
  $term = taxonomy_term_load($tid);

  // Always provide entity id in the same form key as in the entity edit form.
  $form['tid'] = array('#type' => 'value', '#value' => $tid);

  $form['#term'] = $term;
  $form['type'] = array('#type' => 'value', '#value' => 'term');
  $form['name'] = array('#type' => 'value', '#value' => $term->name);
  $form['vocabulary_machine_name'] = array('#type' => 'value', '#value' => $term->vocabulary_machine_name);
  $form['delete'] = array('#type' => 'value', '#value' => TRUE);
  return confirm_form($form,
    t('Are you sure you want to delete the term %title?',
    array('%title' => $term->name)),
    'admin/structure/taxonomy',
    t('Deleting a term will delete all its children if there are any. This action cannot be undone.'),
    t('Delete'),
    t('Cancel'));
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
