# template_preprocess_comment_wrapper()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 2421–2427 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L2421-L2427)
- **Module/theme:** comment

## Signature

```php
function template_preprocess_comment_wrapper(&$variables)
```

## Documentation

```text
Process variables for comment-wrapper.tpl.php.

@see comment-wrapper.tpl.php
```

## Code

```php
function template_preprocess_comment_wrapper(&$variables) {
  // Provide contextual information.
  $variables['node'] = $variables['content']['#node'];
  $variables['display_mode'] = variable_get('comment_default_mode_' . $variables['node']->type, COMMENT_MODE_THREADED);
  // The comment form is optional and may not exist.
  $variables['content'] += array('comment_form' => array());
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
