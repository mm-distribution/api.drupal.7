# comment_prepare_thread()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 875–908 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L875-L908)
- **Module/theme:** comment

## Signature

```php
function comment_prepare_thread(&$comments)
```

## Documentation

```text
Loop over comment thread, noting indentation level.

@param array $comments
  An array of comment objects, keyed by cid.
@return
  The $comments argument is altered by reference with indentation information.
```

## Code

```php
function comment_prepare_thread(&$comments) {
  // A flag stating if we are still searching for first new comment on the thread.
  $first_new = TRUE;

  // A counter that helps track how indented we are.
  $divs = 0;

  foreach ($comments as $key => $comment) {
    if ($first_new && $comment->new != MARK_READ) {
      // Assign the anchor only for the first new comment. This avoids duplicate
      // id attributes on a page.
      $first_new = FALSE;
      $comment->first_new = TRUE;
    }

    // The $divs element instructs #prefix whether to add an indent div or
    // close existing divs (a negative value).
    $comment->depth = count(explode('.', $comment->thread)) - 1;
    if ($comment->depth > $divs) {
      $comment->divs = 1;
      $divs++;
    }
    else {
      $comment->divs = $comment->depth - $divs;
      while ($comment->depth < $divs) {
        $divs--;
      }
    }
    $comments[$key] = $comment;
  }

  // The final comment must close up some hanging divs
  $comments[$key]->divs_final = $divs;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
