# hook_node_access_records_alter()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 338–349 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L338-L349)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md), [node_access](../../../topics/node_access.md)

## Signature

```php
function hook_node_access_records_alter(&$grants, $node)
```

## Documentation

```text
Alter permissions for a node before it is written to the database.

Node access modules establish rules for user access to content. Node access
records are stored in the {node_access} table and define which permissions
are required to access a node. This hook is invoked after node access modules
returned their requirements via hook_node_access_records(); doing so allows
modules to modify the $grants array by reference before it is stored, so
custom or advanced business logic can be applied.

@see hook_node_access_records()

Upon viewing, editing or deleting a node, hook_node_grants() builds a
permissions array that is compared against the stored access records. The
user must have one or more matching permissions in order to complete the
requested operation.

A module may deny all access to a node by setting $grants to an empty array.

@see hook_node_grants()
@see hook_node_grants_alter()

@param $grants
  The $grants array returned by hook_node_access_records().
@param $node
  The node for which the grants were acquired.

The preferred use of this hook is in a module that bridges multiple node
access modules with a configurable behavior, as shown in the example with the
'is_preview' field.

@ingroup node_access
```

## Code

```php
function hook_node_access_records_alter(&$grants, $node) {
  // Our module allows editors to mark specific articles with the 'is_preview'
  // field. If the node being saved has a TRUE value for that field, then only
  // our grants are retained, and other grants are removed. Doing so ensures
  // that our rules are enforced no matter what priority other grants are given.
  if ($node->is_preview) {
    // Our module grants are set in $grants['example'].
    $temp = $grants['example'];
    // Now remove all module grants but our own.
    $grants = array('example' => $temp);
  }
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_access_records_alter()".

- [node_test_node_access_records_alter()](../tests/node_test.module/node_test_node_access_records_alter.md) — `modules/node/tests/node_test.module`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
