# hook_node_operations()

- **Type:** Hook (documentation function)
- **File:** [`modules/node/node.api.php`](_file.md), lines 422–460 · [local source](../../../../source/modules/node/node.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php#L422-L460)
- **Module/theme:** node
- **Topics:** [hooks](../../../topics/hooks.md)

## Signature

```php
function hook_node_operations()
```

## Documentation

```text
Add mass node operations.

This hook enables modules to inject custom operations into the mass
operations dropdown found at admin/content, by associating a callback
function with the operation, which is called when the form is submitted. The
callback function receives one initial argument, which is an array of the
checked nodes.

@return
  An array of operations. Each operation is an associative array that may
  contain the following key-value pairs:
  - label: (required) The label for the operation, displayed in the dropdown
    menu.
  - callback: (required) The function to call for the operation.
  - callback arguments: (optional) An array of additional arguments to pass
    to the callback function.
```

## Code

```php
function hook_node_operations() {
  $operations = array(
    'publish' => array(
      'label' => t('Publish selected content'),
      'callback' => 'node_mass_update',
      'callback arguments' => array('updates' => array('status' => NODE_PUBLISHED)),
    ),
    'unpublish' => array(
      'label' => t('Unpublish selected content'),
      'callback' => 'node_mass_update',
      'callback arguments' => array('updates' => array('status' => NODE_NOT_PUBLISHED)),
    ),
    'promote' => array(
      'label' => t('Promote selected content to front page'),
      'callback' => 'node_mass_update',
      'callback arguments' => array('updates' => array('status' => NODE_PUBLISHED, 'promote' => NODE_PROMOTED)),
    ),
    'demote' => array(
      'label' => t('Demote selected content from front page'),
      'callback' => 'node_mass_update',
      'callback arguments' => array('updates' => array('promote' => NODE_NOT_PROMOTED)),
    ),
    'sticky' => array(
      'label' => t('Make selected content sticky'),
      'callback' => 'node_mass_update',
      'callback arguments' => array('updates' => array('status' => NODE_PUBLISHED, 'sticky' => NODE_STICKY)),
    ),
    'unsticky' => array(
      'label' => t('Make selected content not sticky'),
      'callback' => 'node_mass_update',
      'callback arguments' => array('updates' => array('sticky' => NODE_NOT_STICKY)),
    ),
    'delete' => array(
      'label' => t('Delete selected content'),
      'callback' => NULL,
    ),
  );
  return $operations;
}
```

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_node_operations()".

- [node_node_operations()](../node.admin.inc/node_node_operations.md) — `modules/node/node.admin.inc`

---
_Drupal 7.103 · [modules/node/node.api.php](https://github.com/drupal/drupal/blob/7.103/modules/node/node.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
