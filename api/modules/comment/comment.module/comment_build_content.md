# comment_build_content()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 993–1029 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L993-L1029)
- **Module/theme:** comment

## Signature

```php
function comment_build_content($comment, $node, $view_mode = 'full', $langcode = NULL)
```

## Documentation

```text
Builds a structured array representing the comment's content.

The content built for the comment (field values, comments, file attachments or
other comment components) will vary depending on the $view_mode parameter.

@param $comment
  A comment object.
@param $node
  The node the comment is attached to.
@param $view_mode
  View mode, e.g. 'full', 'teaser'...
@param $langcode
  (optional) A language code to use for rendering. Defaults to the global
  content language of the current request.
```

## Code

```php
function comment_build_content($comment, $node, $view_mode = 'full', $langcode = NULL) {
  if (!isset($langcode)) {
    $langcode = $GLOBALS['language_content']->language;
  }

  // Remove previously built content, if exists.
  $comment->content = array();

  // Allow modules to change the view mode.
  $view_mode = key(entity_view_mode_prepare('comment', array($comment->cid => $comment), $view_mode, $langcode));

  // Build fields content.
  field_attach_prepare_view('comment', array($comment->cid => $comment), $view_mode, $langcode);
  entity_prepare_view('comment', array($comment->cid => $comment), $langcode);
  $comment->content += field_attach_view('comment', $comment, $view_mode, $langcode);

  $comment->content['links'] = array(
    '#theme' => 'links__comment',
    '#pre_render' => array('drupal_pre_render_links'),
    '#attributes' => array('class' => array('links', 'inline')),
  );
  if (empty($comment->in_preview)) {
    $comment->content['links']['comment'] = array(
      '#theme' => 'links__comment__comment',
      '#links' => comment_links($comment, $node),
      '#attributes' => array('class' => array('links', 'inline')),
    );
  }

  // Allow modules to make their own additions to the comment.
  module_invoke_all('comment_view', $comment, $view_mode, $langcode);
  module_invoke_all('entity_view', $comment, 'comment', $view_mode, $langcode);

  // Make sure the current view mode is stored if no module has already
  // populated the related key.
  $comment->content += array('#view_mode' => $view_mode);
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
