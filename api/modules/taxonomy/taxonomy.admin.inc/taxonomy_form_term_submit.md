# taxonomy_form_term_submit()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.admin.inc`](_file.md), lines 801–851 · [local source](../../../../source/modules/taxonomy/taxonomy.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc#L801-L851)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_form_term_submit($form, &$form_state)
```

## Documentation

```text
Submit handler to insert or update a term.

@see taxonomy_form_term()
```

## Code

```php
function taxonomy_form_term_submit($form, &$form_state) {
  if ($form_state['triggering_element']['#value'] == t('Delete')) {
    // Execute the term deletion.
    if ($form_state['values']['delete'] === TRUE) {
      return taxonomy_term_confirm_delete_submit($form, $form_state);
    }
    // Rebuild the form to confirm term deletion.
    $form_state['rebuild'] = TRUE;
    $form_state['confirm_delete'] = TRUE;
    return;
  }

  $term = taxonomy_form_term_submit_build_taxonomy_term($form, $form_state);

  $status = taxonomy_term_save($term);
  switch ($status) {
    case SAVED_NEW:
      drupal_set_message(t('Created new term %term.', array('%term' => $term->name)));
      watchdog('taxonomy', 'Created new term %term.', array('%term' => $term->name), WATCHDOG_NOTICE, l(t('edit'), 'taxonomy/term/' . $term->tid . '/edit'));
      break;
    case SAVED_UPDATED:
      drupal_set_message(t('Updated term %term.', array('%term' => $term->name)));
      watchdog('taxonomy', 'Updated term %term.', array('%term' => $term->name), WATCHDOG_NOTICE, l(t('edit'), 'taxonomy/term/' . $term->tid . '/edit'));
      // Clear the page and block caches to avoid stale data.
      cache_clear_all();
      break;
  }

  $current_parent_count = empty($form_state['values']['parent']) ? 0 : count((array) $form_state['values']['parent']);
  $previous_parent_count = empty($form['#term']['parent']) ? 0 : count((array) $form['#term']['parent']);
  // Root doesn't count if it's the only parent.
  if ($current_parent_count == 1 && isset($form_state['values']['parent'][0])) {
    $current_parent_count = 0;
    $form_state['values']['parent'] = array();
  }

  // If the number of parents has been reduced to one or none, do a check on the
  // parents of every term in the vocabulary value.
  if ($current_parent_count < $previous_parent_count && $current_parent_count < 2) {
    taxonomy_check_vocabulary_hierarchy($form['#vocabulary'], $form_state['values']);
  }
  // If we've increased the number of parents and this is a single or flat
  // hierarchy, update the vocabulary immediately.
  elseif ($current_parent_count > $previous_parent_count && $form['#vocabulary']->hierarchy < 2) {
    $form['#vocabulary']->hierarchy = $current_parent_count == 1 ? 1 : 2;
    taxonomy_vocabulary_save($form['#vocabulary']);
  }

  $form_state['values']['tid'] = $term->tid;
  $form_state['tid'] = $term->tid;
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
