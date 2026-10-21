# node_type_delete_confirm_submit()

- **Type:** Function
- **File:** [`modules/node/content_types.inc`](_file.md), lines 439–452 · [local source](../../../../source/modules/node/content_types.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/content_types.inc#L439-L452)
- **Module/theme:** node

## Signature

```php
function node_type_delete_confirm_submit($form, &$form_state)
```

## Documentation

```text
Process content type delete confirm submissions.

@see node_type_delete_confirm()
```

## Code

```php
function node_type_delete_confirm_submit($form, &$form_state) {
  node_type_delete($form_state['values']['type']);

  variable_del('node_preview_' . $form_state['values']['type']);
  $t_args = array('%name' => $form_state['values']['name']);
  drupal_set_message(t('The content type %name has been deleted.', $t_args));
  watchdog('node', 'Deleted content type %name.', $t_args, WATCHDOG_NOTICE);

  node_types_rebuild();
  menu_rebuild();

  $form_state['redirect'] = 'admin/structure/types';
  return;
}
```

---
_Drupal 7.103 · [modules/node/content_types.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/content_types.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
