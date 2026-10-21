# comment_view_multiple()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1111–1133 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1111-L1133)
- **Module/theme:** comment

## Signature

```php
function comment_view_multiple($comments, $node, $view_mode = 'full', $weight = 0, $langcode = NULL)
```

## Documentation

```text
Construct a drupal_render() style array from an array of loaded comments.

@param $comments
  An array of comments as returned by comment_load_multiple().
@param $node
  The node the comments are attached to.
@param $view_mode
  View mode, e.g. 'full', 'teaser'...
@param $weight
  An integer representing the weight of the first comment in the list.
@param $langcode
  A string indicating the language field values are to be shown in. If no
  language is provided the current content language is used.

@return
  An array in the format expected by drupal_render().
```

## Code

```php
function comment_view_multiple($comments, $node, $view_mode = 'full', $weight = 0, $langcode = NULL) {
  $build = array();
  $entities_by_view_mode = entity_view_mode_prepare('comment', $comments, $view_mode, $langcode);
  foreach ($entities_by_view_mode as $entity_view_mode => $entities) {
    field_attach_prepare_view('comment', $entities, $entity_view_mode, $langcode);
    entity_prepare_view('comment', $entities, $langcode);

    foreach ($entities as $entity) {
      $build[$entity->cid] = comment_view($entity, $node, $entity_view_mode, $langcode);
    }
  }

  foreach ($comments as $comment) {
    $build[$comment->cid]['#weight'] = $weight;
    $weight++;
  }
  // Sort here, to preserve the input order of the entities that were passed to
  // this function.
  uasort($build, 'element_sort');
  $build['#sorted'] = TRUE;

  return $build;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
