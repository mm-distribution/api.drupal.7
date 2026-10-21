# comment_entity_info()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 94–141 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L94-L141)
- **Module/theme:** comment
- **Implements:** [hook_entity_info()](../../system/system.api.php/hook_entity_info.md)

## Signature

```php
function comment_entity_info()
```

## Documentation

```text
Implements hook_entity_info().
```

## Code

```php
function comment_entity_info() {
  $return = array(
    'comment' => array(
      'label' => t('Comment'),
      'base table' => 'comment',
      'uri callback' => 'comment_uri',
      'fieldable' => TRUE,
      'controller class' => 'CommentController',
      'entity keys' => array(
        'id' => 'cid',
        'bundle' => 'node_type',
        'label' => 'subject',
        'language' => 'language',
      ),
      'bundles' => array(),
      'view modes' => array(
        'full' => array(
          'label' => t('Full comment'),
          'custom settings' => FALSE,
        ),
      ),
      'static cache' => FALSE,
    ),
  );

  foreach (node_type_get_names() as $type => $name) {
    $return['comment']['bundles']['comment_node_' . $type] = array(
      'label' => t('@node_type comment', array('@node_type' => $name)),
      // Provide the node type/bundle name for other modules, so it does not
      // have to be extracted manually from the bundle name.
      'node bundle' => $type,
      'admin' => array(
        // Place the Field UI paths for comments one level below the
        // corresponding paths for nodes, so that they appear in the same set
        // of local tasks. Note that the paths use a different placeholder name
        // and thus a different menu loader callback, so that Field UI page
        // callbacks get a comment bundle name from the node type in the URL.
        // See comment_node_type_load() and comment_menu_alter().
        'path' => 'admin/structure/types/manage/%comment_node_type/comment',
        'bundle argument' => 4,
        'real path' => 'admin/structure/types/manage/' . str_replace('_', '-', $type) . '/comment',
        'access arguments' => array('administer content types'),
      ),
    );
  }

  return $return;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
