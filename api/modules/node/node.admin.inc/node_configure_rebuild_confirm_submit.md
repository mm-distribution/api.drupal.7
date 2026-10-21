# node_configure_rebuild_confirm_submit()

- **Type:** Function
- **File:** [`modules/node/node.admin.inc`](_file.md), lines 25–28 · [local source](../../../../source/modules/node/node.admin.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc#L25-L28)
- **Module/theme:** node

## Signature

```php
function node_configure_rebuild_confirm_submit($form, &$form_state)
```

## Documentation

```text
Handler for wipe confirmation

@see node_configure_rebuild_confirm()
```

## Code

```php
function node_configure_rebuild_confirm_submit($form, &$form_state) {
  node_access_rebuild(TRUE);
  $form_state['redirect'] = 'admin/reports/status';
}
```

---
_Drupal 7.103 · [modules/node/node.admin.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.admin.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
