# comment_permalink()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 479–494 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L479-L494)
- **Module/theme:** comment

## Signature

```php
function comment_permalink($cid)
```

## Documentation

```text
Redirects comment links to the correct page depending on comment settings.

Since comments are paged there is no way to guarantee which page a comment
appears on. Comment paging and threading settings may be changed at any time.
With threaded comments, an individual comment may move between pages as
comments can be added either before or after it in the overall discussion.
Therefore we use a central routing function for comment links, which
calculates the page number based on current comment settings and returns
the full comment view with the pager set dynamically.

@param $cid
  A comment identifier.
@return
  The comment listing set to the page on which the comment appears.
```

## Code

```php
function comment_permalink($cid) {
  if (($comment = comment_load($cid)) && ($node = node_load($comment->nid))) {

    // Find the current display page for this comment.
    $page = comment_get_display_page($comment->cid, $node->type);

    // Set $_GET['q'] and $_GET['page'] ourselves so that the node callback
    // behaves as it would when visiting the page directly.
    $_GET['q'] = 'node/' . $node->nid;
    $_GET['page'] = $page;

    // Return the node view, this will show the correct comment in context.
    return menu_execute_active_handler('node/' . $node->nid, FALSE);
  }
  return MENU_NOT_FOUND;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
