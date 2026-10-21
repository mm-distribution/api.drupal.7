# taxonomy_vocabulary_confirm_reset_alphabetical_submit()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.admin.inc`](_file.md), lines 974–982 · [local source](../../../../source/modules/taxonomy/taxonomy.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc#L974-L982)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_vocabulary_confirm_reset_alphabetical_submit($form, &$form_state)
```

## Documentation

```text
Submit handler to reset a vocabulary to alphabetical order after confirmation.

@see taxonomy_vocabulary_confirm_reset_alphabetical()
```

## Code

```php
function taxonomy_vocabulary_confirm_reset_alphabetical_submit($form, &$form_state) {
  db_update('taxonomy_term_data')
    ->fields(array('weight' => 0))
    ->condition('vid', $form_state['values']['vid'])
    ->execute();
  drupal_set_message(t('Reset vocabulary %name to alphabetical order.', array('%name' => $form_state['values']['name'])));
  watchdog('taxonomy', 'Reset vocabulary %name to alphabetical order.', array('%name' => $form_state['values']['name']), WATCHDOG_NOTICE);
  $form_state['redirect'] = 'admin/structure/taxonomy/' . $form_state['values']['machine_name'];
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
