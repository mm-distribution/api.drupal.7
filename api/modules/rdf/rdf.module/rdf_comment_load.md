# rdf_comment_load()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 419–430 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L419-L430)
- **Module/theme:** rdf
- **Implements:** [hook_comment_load()](../../comment/comment.api.php/hook_comment_load.md)

## Signature

```php
function rdf_comment_load($comments)
```

## Documentation

```text
Implements hook_comment_load().
```

## Code

```php
function rdf_comment_load($comments) {
  foreach ($comments as $comment) {
    // Pages with many comments can show poor performance. This information
    // isn't needed until rdf_preprocess_comment() is called, but set it here
    // to optimize performance for websites that implement an entity cache.
    $comment->rdf_data['date'] = rdf_rdfa_attributes($comment->rdf_mapping['created'], $comment->created);
    $comment->rdf_data['nid_uri'] = url('node/' . $comment->nid);
    if ($comment->pid) {
      $comment->rdf_data['pid_uri'] = url('comment/' . $comment->pid, array('fragment' => 'comment-' . $comment->pid));
    }
  }
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
