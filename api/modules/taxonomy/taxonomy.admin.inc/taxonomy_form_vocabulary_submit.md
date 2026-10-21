# taxonomy_form_vocabulary_submit()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.admin.inc`](_file.md), lines 211–237 · [local source](../../../../source/modules/taxonomy/taxonomy.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc#L211-L237)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_form_vocabulary_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for taxonomy_form_vocabulary().

@see taxonomy_form_vocabulary()
@see taxonomy_form_vocabulary_validate()
```

## Code

```php
function taxonomy_form_vocabulary_submit($form, &$form_state) {
  if ($form_state['triggering_element']['#value'] == t('Delete')) {
    // Rebuild the form to confirm vocabulary deletion.
    $form_state['rebuild'] = TRUE;
    $form_state['confirm_delete'] = TRUE;
    return;
  }

  $vocabulary = $form_state['vocabulary'];
  entity_form_submit_build_entity('taxonomy_vocabulary', $vocabulary, $form, $form_state);

  switch (taxonomy_vocabulary_save($vocabulary)) {
    case SAVED_NEW:
      drupal_set_message(t('Created new vocabulary %name.', array('%name' => $vocabulary->name)));
      watchdog('taxonomy', 'Created new vocabulary %name.', array('%name' => $vocabulary->name), WATCHDOG_NOTICE, l(t('edit'), 'admin/structure/taxonomy/' . $vocabulary->machine_name . '/edit'));
      break;

    case SAVED_UPDATED:
      drupal_set_message(t('Updated vocabulary %name.', array('%name' => $vocabulary->name)));
      watchdog('taxonomy', 'Updated vocabulary %name.', array('%name' => $vocabulary->name), WATCHDOG_NOTICE, l(t('edit'), 'admin/structure/taxonomy/' . $vocabulary->machine_name . '/edit'));
      break;
  }

  $form_state['values']['vid'] = $vocabulary->vid;
  $form_state['vid'] = $vocabulary->vid;
  $form_state['redirect'] = 'admin/structure/taxonomy';
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
