# node_object_prepare()

- **Type:** Function
- **File:** [`modules/node/node.module`](_file.md), lines 979–1004 · [local source](../../../../source/modules/node/node.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module#L979-L1004)
- **Module/theme:** node

## Signature

```php
function node_object_prepare($node)
```

## Documentation

```text
Prepares a node object for editing.

Fills in a few default values, and then invokes hook_prepare() on the node
type module, and hook_node_prepare() on all modules.

@param $node
  A node object.
```

## Code

```php
function node_object_prepare($node) {
  // Set up default values, if required.
  $node_options = variable_get('node_options_' . $node->type, array('status', 'promote'));
  // If this is a new node, fill in the default values.
  if (!isset($node->nid) || isset($node->is_new)) {
    foreach (array('status', 'promote', 'sticky') as $key) {
      // Multistep node forms might have filled in something already.
      if (!isset($node->$key)) {
        $node->$key = (int) in_array($key, $node_options);
      }
    }
    global $user;
    $node->uid = $user->uid;
    $node->created = REQUEST_TIME;
  }
  else {
    $node->date = format_date($node->created, 'custom', 'Y-m-d H:i:s O');
    // Remove the log message from the original node object.
    $node->log = NULL;
  }
  // Always use the default revision setting.
  $node->revision = in_array('revision', $node_options);

  node_invoke($node, 'prepare');
  module_invoke_all('node_prepare', $node);
}
```

---
_Drupal 7.103 · [modules/node/node.module](https://github.com/drupal/drupal/blob/7.103/modules/node/node.module) · Licensed GPL-2.0-or-later (see LICENSE)._
