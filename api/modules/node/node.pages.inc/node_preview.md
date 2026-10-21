# node_preview()

- **Type:** Function
- **File:** [`modules/node/node.pages.inc`](_file.md), lines 373–410 · [local source](../../../../source/modules/node/node.pages.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc#L373-L410)
- **Module/theme:** node

## Signature

```php
function node_preview($node)
```

## Documentation

```text
Generates a node preview.

@param $node
  The node to preview.

@return
  An HTML-formatted string of a node preview.

@see node_form_build_preview()
```

## Code

```php
function node_preview($node) {
  // Clone the node before previewing it to prevent the node itself from being
  // modified.
  $cloned_node = clone $node;
  if (node_access('create', $cloned_node) || node_access('update', $cloned_node)) {
    _field_invoke_multiple('load', 'node', array($cloned_node->nid => $cloned_node));
    // Load the user's name when needed.
    if (isset($cloned_node->name)) {
      // The use of isset() is mandatory in the context of user IDs, because
      // user ID 0 denotes the anonymous user.
      if ($user = user_load_by_name($cloned_node->name)) {
        $cloned_node->uid = $user->uid;
        $cloned_node->picture = $user->picture;
      }
      else {
        $cloned_node->uid = 0; // anonymous user
      }
    }
    elseif ($cloned_node->uid) {
      $user = user_load($cloned_node->uid);
      $cloned_node->name = $user->name;
      $cloned_node->picture = $user->picture;
    }

    $cloned_node->changed = REQUEST_TIME;
    $nodes = array($cloned_node->nid => $cloned_node);

    // Display a preview of the node.
    if (!form_get_errors()) {
      $cloned_node->in_preview = TRUE;
      $output = theme('node_preview', array('node' => $cloned_node));
      unset($cloned_node->in_preview);
    }
    drupal_set_title(t('Preview'), PASS_THROUGH);

    return $output;
  }
}
```

---
_Drupal 7.103 · [modules/node/node.pages.inc](https://github.com/drupal/drupal/blob/7.103/modules/node/node.pages.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
