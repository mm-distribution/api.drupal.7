# forum_confirm_delete_submit()

- **Type:** Function
- **File:** [`modules/forum/forum.admin.inc`](_file.md), lines 220–227 · [local source](../../../../source/modules/forum/forum.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.admin.inc#L220-L227)
- **Module/theme:** forum

## Signature

```php
function forum_confirm_delete_submit($form, &$form_state)
```

## Documentation

```text
Form submission handler for forum_confirm_delete().
```

## Code

```php
function forum_confirm_delete_submit($form, &$form_state) {
  taxonomy_term_delete($form_state['values']['tid']);
  drupal_set_message(t('The forum %term and all sub-forums have been deleted.', array('%term' => $form_state['values']['name'])));
  watchdog('content', 'forum: deleted %term and all its sub-forums.', array('%term' => $form_state['values']['name']));

  $form_state['redirect'] = 'admin/structure/forum';
  return;
}
```

---
_Drupal 7.103 · [modules/forum/forum.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/forum/forum.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
