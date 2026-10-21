# node_submit()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 1052–1068 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L1052-L1068)
- **Module/theme:** node

## Signature

```php
function node_submit($node)
```

## Documentation

```text
Prepares node for saving by populating author and creation date.

@param $node
  A node object.

@return
  An updated node object.
```

## Code

```php
function node_submit($node) {
  // A user might assign the node author by entering a user name in the node
  // form, which we then need to translate to a user ID.
  if (isset($node->name)) {
    if ($account = user_load_by_name($node->name)) {
      $node->uid = $account->uid;
    }
    else {
      $node->uid = 0;
    }
  }

  $node->created = !empty($node->date) ? strtotime($node->date) : REQUEST_TIME;
  $node->validated = TRUE;

  return $node;
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
