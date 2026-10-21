# node_unpublish_by_keyword_action_submit()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 4086–4088 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L4086-L4088)
- **Module/theme:** node

## Signature

```php
function node_unpublish_by_keyword_action_submit($form, $form_state)
```

## Documentation

```text
Saves settings form for node_unpublish_by_keyword_action().
```

## Code

```php
function node_unpublish_by_keyword_action_submit($form, $form_state) {
  return array('keywords' => drupal_explode_tags($form_state['values']['keywords']));
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
