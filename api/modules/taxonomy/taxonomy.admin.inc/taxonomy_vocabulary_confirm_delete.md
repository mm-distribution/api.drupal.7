# taxonomy_vocabulary_confirm_delete()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.admin.inc`](_file.md), lines 913–931 · [local source](../../../../source/modules/taxonomy/taxonomy.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc#L913-L931)
- **Module/theme:** taxonomy
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function taxonomy_vocabulary_confirm_delete($form, &$form_state, $vid)
```

## Documentation

```text
Form builder for the vocabulary delete confirmation form.

@ingroup forms
@see taxonomy_vocabulary_confirm_delete_submit()
```

## Code

```php
function taxonomy_vocabulary_confirm_delete($form, &$form_state, $vid) {
  $vocabulary = taxonomy_vocabulary_load($vid);

  // Always provide entity id in the same form key as in the entity edit form.
  $form['vid'] = array('#type' => 'value', '#value' => $vid);

  $form['#vocabulary'] = $vocabulary;
  $form['#id'] = 'taxonomy_vocabulary_confirm_delete';
  $form['type'] = array('#type' => 'value', '#value' => 'vocabulary');
  $form['name'] = array('#type' => 'value', '#value' => $vocabulary->name);
  $form['#submit'] = array('taxonomy_vocabulary_confirm_delete_submit');
  return confirm_form($form,
    t('Are you sure you want to delete the vocabulary %title?',
    array('%title' => $vocabulary->name)),
    'admin/structure/taxonomy',
    t('Deleting a vocabulary will delete all the terms in it. This action cannot be undone.'),
    t('Delete'),
    t('Cancel'));
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
