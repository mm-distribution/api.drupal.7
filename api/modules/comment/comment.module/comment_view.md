# comment_view()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 926–975 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L926-L975)
- **Module/theme:** comment

## Signature

```php
function comment_view($comment, $node, $view_mode = 'full', $langcode = NULL)
```

## Documentation

```text
Generate an array for rendering the given comment.

@param $comment
  A comment object.
@param $node
  The node the comment is attached to.
@param $view_mode
  View mode, e.g. 'full', 'teaser'...
@param $langcode
  (optional) A language code to use for rendering. Defaults to the global
  content language of the current request.

@return
  An array as expected by drupal_render().
```

## Code

```php
function comment_view($comment, $node, $view_mode = 'full', $langcode = NULL) {
  if (!isset($langcode)) {
    $langcode = $GLOBALS['language_content']->language;
  }

  // Populate $comment->content with a render() array.
  comment_build_content($comment, $node, $view_mode, $langcode);

  $build = $comment->content;
  // We don't need duplicate rendering info in comment->content.
  unset($comment->content);

  $build += array(
    '#theme' => 'comment__node_' . $node->type,
    '#comment' => $comment,
    '#node' => $node,
    '#view_mode' => $view_mode,
    '#language' => $langcode,
  );

  if (empty($comment->in_preview)) {
    $prefix = '';
    $is_threaded = isset($comment->divs) && variable_get('comment_default_mode_' . $node->type, COMMENT_MODE_THREADED) == COMMENT_MODE_THREADED;

    // Add 'new' anchor if needed.
    if (!empty($comment->first_new)) {
      $prefix .= "<a id=\"new\"></a>\n";
    }

    // Add indentation div or close open divs as needed.
    if ($is_threaded) {
      $prefix .= $comment->divs <= 0 ? str_repeat('</div>', abs($comment->divs)) : "\n" . '<div class="indented">';
    }

    // Add anchor for each comment.
    $prefix .= "<a id=\"comment-$comment->cid\"></a>\n";
    $build['#prefix'] = $prefix;

    // Close all open divs.
    if ($is_threaded && !empty($comment->divs_final)) {
      $build['#suffix'] = str_repeat('</div>', $comment->divs_final);
    }
  }

  // Allow modules to modify the structured comment.
  $type = 'comment';
  drupal_alter(array('comment_view', 'entity_view'), $build, $type);

  return $build;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
