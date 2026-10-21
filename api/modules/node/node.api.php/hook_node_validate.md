# hook_node_validate()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 771–777 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L771-L777)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_api_hooks](../../../topics/node_api_hooks.md)

## Signature

```php
function hook_node_validate($node, $form, &$form_state)
```

## Documentation

```text
Perform node validation before a node is created or updated.

This hook is invoked from node_validate(), after a user has finished editing
the node and is previewing or submitting it. It is invoked at the end of all
the standard validation steps, and after the type-specific hook_validate() is
invoked.

To indicate a validation error, use form_set_error().

Note: Changes made to the $node object within your hook implementation will
have no effect.  The preferred method to change a node's content is to use
hook_node_presave() instead. If it is really necessary to change the node at
the validate stage, you can use form_set_value().

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
function hook_node_validate($node, $form, &$form_state) {
  if (isset($node->end) && isset($node->start)) {
    if ($node->start > $node->end) {
      form_set_error('time', t('An event may not end before it starts.'));
    }
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_validate()".

- [forum_node_validate()](../../forum/forum.module/forum_node_validate.md) — `modules/forum/forum.module`
- [translation_node_validate()](../../translation/translation.module/translation_node_validate.md) — `modules/translation/translation.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
