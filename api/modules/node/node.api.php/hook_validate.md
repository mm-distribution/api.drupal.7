# hook_validate()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 1272–1278 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L1272-L1278)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_validate($node, $form, &$form_state)
```

## Documentation

```text
Perform node validation before a node is created or updated.

This is a node-type-specific hook, which is invoked only for the node type
being affected. See
@link node_api_hooks Node API hooks @endlink for more information.

Use hook_node_validate() to respond to node validation of all node types.

This hook is invoked from node_validate(), after a user has finished
editing the node and is previewing or submitting it. It is invoked at the end
of all the standard validation steps, and before hook_node_validate() is
invoked.

To indicate a validation error, use form_set_error().

Note: Changes made to the $node object within your hook implementation will
have no effect.  The preferred method to change a node's content is to use
hook_node_presave() instead.

@param $node
  The node being validated.
@param $form
  The form being used to edit the node.
@param $form_state
  The form state array.

@ingroup node_api_hooks
```

## Code

```php
function hook_validate($node, $form, &$form_state) {
  if (isset($node->end) && isset($node->start)) {
    if ($node->start > $node->end) {
      form_set_error('time', t('An event may not end before it starts.'));
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_validate()".

- [node_validate()](../node.module/node_validate.md) — `modules/node/node.module`
- [poll_validate()](../../poll/poll.module/poll_validate.md) — `modules/poll/poll.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
