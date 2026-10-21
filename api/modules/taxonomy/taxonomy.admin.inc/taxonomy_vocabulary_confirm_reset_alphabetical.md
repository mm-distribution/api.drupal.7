# taxonomy_vocabulary_confirm_reset_alphabetical()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.admin.inc`](_file.md), lines 952–967 · [local source](../../../../source/modules/taxonomy/taxonomy.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc#L952-L967)
- **Module/theme:** taxonomy
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function taxonomy_vocabulary_confirm_reset_alphabetical($form, &$form_state, $vid)
```

## Documentation

```text
Form builder to confirm resetting a vocabulary to alphabetical order.

@ingroup forms
@see taxonomy_vocabulary_confirm_reset_alphabetical_submit()
```

## Code

```php
function taxonomy_vocabulary_confirm_reset_alphabetical($form, &$form_state, $vid) {
  $vocabulary = taxonomy_vocabulary_load($vid);

  $form['type'] = array('#type' => 'value', '#value' => 'vocabulary');
  $form['vid'] = array('#type' => 'value', '#value' => $vid);
  $form['machine_name'] = array('#type' => 'value', '#value' => $vocabulary->machine_name);
  $form['name'] = array('#type' => 'value', '#value' => $vocabulary->name);
  $form['reset_alphabetical'] = array('#type' => 'value', '#value' => TRUE);
  return confirm_form($form,
                  t('Are you sure you want to reset the vocabulary %title to alphabetical order?',
                  array('%title' => $vocabulary->name)),
                  'admin/structure/taxonomy/' . $vocabulary->machine_name,
                  t('Resetting a vocabulary will discard all custom ordering and sort items alphabetically.'),
                  t('Reset to alphabetical'),
                  t('Cancel'));
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
