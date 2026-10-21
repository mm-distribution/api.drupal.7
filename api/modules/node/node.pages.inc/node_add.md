# node_add()

- **Type:** Function
- **File:** [`modules/node/node.pages.inc`](_file.md), lines 72–81 · [local source](../../../../source/modules/node/node.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc#L72-L81)
- **Module/theme:** node

## Signature

```php
function node_add($type)
```

## Documentation

```text
Returns a node submission form.

@param $type
  The node type for the submitted node.

@return
  The themed form.
```

## Code

```php
function node_add($type) {
  global $user;

  $types = node_type_get_types();
  $node = (object) array('uid' => $user->uid, 'name' => (isset($user->name) ? $user->name : ''), 'type' => $type, 'language' => LANGUAGE_NONE);
  drupal_set_title(t('Create @name', array('@name' => $types[$type]->name)), PASS_THROUGH);
  $output = drupal_get_form($type . '_node_form', $node);

  return $output;
}
```

---
_Drupal 7.103 · [modules/node/node.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
