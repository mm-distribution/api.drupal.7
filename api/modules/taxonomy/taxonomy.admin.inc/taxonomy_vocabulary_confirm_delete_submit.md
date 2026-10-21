# taxonomy_vocabulary_confirm_delete_submit()

- **Type:** Function
- **File:** [`modules/taxonomy/taxonomy.admin.inc`](_file.md), lines 938–944 · [local source](../../../../source/modules/taxonomy/taxonomy.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc#L938-L944)
- **Module/theme:** taxonomy

## Signature

```php
function taxonomy_vocabulary_confirm_delete_submit($form, &$form_state)
```

## Documentation

```text
Submit handler to delete a vocabulary after confirmation.

@see taxonomy_vocabulary_confirm_delete()
```

## Code

```php
function taxonomy_vocabulary_confirm_delete_submit($form, &$form_state) {
  $status = taxonomy_vocabulary_delete($form_state['values']['vid']);
  drupal_set_message(t('Deleted vocabulary %name.', array('%name' => $form_state['values']['name'])));
  watchdog('taxonomy', 'Deleted vocabulary %name.', array('%name' => $form_state['values']['name']), WATCHDOG_NOTICE);
  $form_state['redirect'] = 'admin/structure/taxonomy';
  cache_clear_all();
}
```

---
_Drupal 7.103 · [modules/taxonomy/taxonomy.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/taxonomy/taxonomy.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
