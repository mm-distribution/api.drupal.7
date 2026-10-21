# comment_node_view()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 615–714 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L615-L714)
- **Module/theme:** comment
- **Implements:** [hook_node_view()](../../node/node.api.php/hook_node_view.md)

## Signature

```php
function comment_node_view($node, $view_mode)
```

## Documentation

```text
Implements hook_node_view().
```

## Code

```php
function comment_node_view($node, $view_mode) {
  $links = array();

  if ($node->comment != COMMENT_NODE_HIDDEN) {
    if ($view_mode == 'rss') {
      // Add a comments RSS element which is a URL to the comments of this node.
      $node->rss_elements[] = array(
        'key' => 'comments',
        'value' => url('node/' . $node->nid, array('fragment' => 'comments', 'absolute' => TRUE))
      );
    }
    elseif ($view_mode == 'teaser') {
      // Teaser view: display the number of comments that have been posted,
      // or a link to add new comments if the user has permission, the node
      // is open to new comments, and there currently are none.
      if (user_access('access comments')) {
        if (!empty($node->comment_count)) {
          $links['comment-comments'] = array(
            'title' => format_plural($node->comment_count, '1 comment', '@count comments'),
            'href' => "node/$node->nid",
            'attributes' => array('title' => t('Jump to the first comment of this posting.')),
            'fragment' => 'comments',
            'html' => TRUE,
          );
          // Show a link to the first new comment.
          if ($new = comment_num_new($node->nid)) {
            $links['comment-new-comments'] = array(
              'title' => format_plural($new, '1 new comment', '@count new comments'),
              'href' => "node/$node->nid",
              'query' => comment_new_page_count($node->comment_count, $new, $node),
              'attributes' => array('title' => t('Jump to the first new comment of this posting.')),
              'fragment' => 'new',
              'html' => TRUE,
            );
          }
        }
      }
      if ($node->comment == COMMENT_NODE_OPEN) {
        if (user_access('post comments')) {
          $links['comment-add'] = array(
            'title' => t('Add new comment'),
            'href' => "comment/reply/$node->nid",
            'attributes' => array('title' => t('Add a new comment to this page.')),
            'fragment' => 'comment-form',
          );
        }
        else {
          $links['comment_forbidden'] = array(
            'title' => theme('comment_post_forbidden', array('node' => $node)),
            'html' => TRUE,
          );
        }
      }
    }
    elseif ($view_mode != 'search_index' && $view_mode != 'search_result') {
      // Node in other view modes: add a "post comment" link if the user is
      // allowed to post comments and if this node is allowing new comments.
      // But we don't want this link if we're building the node for search
      // indexing or constructing a search result excerpt.
      if ($node->comment == COMMENT_NODE_OPEN) {
        $comment_form_location = variable_get('comment_form_location_' . $node->type, COMMENT_FORM_BELOW);
        if (user_access('post comments')) {
          // Show the "post comment" link if the form is on another page, or
          // if there are existing comments that the link will skip past.
          if ($comment_form_location == COMMENT_FORM_SEPARATE_PAGE || (!empty($node->comment_count) && user_access('access comments'))) {
            $links['comment-add'] = array(
              'title' => t('Add new comment'),
              'attributes' => array('title' => t('Share your thoughts and opinions related to this posting.')),
              'href' => "node/$node->nid",
              'fragment' => 'comment-form',
            );
            if ($comment_form_location == COMMENT_FORM_SEPARATE_PAGE) {
              $links['comment-add']['href'] = "comment/reply/$node->nid";
            }
          }
        }
        else {
          $links['comment_forbidden'] = array(
            'title' => theme('comment_post_forbidden', array('node' => $node)),
            'html' => TRUE,
          );
        }
      }
    }

    $node->content['links']['comment'] = array(
      '#theme' => 'links__node__comment',
      '#links' => $links,
      '#attributes' => array('class' => array('links', 'inline')),
    );

    // Only append comments when we are building a node on its own node detail
    // page. We compare $node and $page_node to ensure that comments are not
    // appended to other nodes shown on the page, for example a node_reference
    // displayed in 'full' view mode within another node.
    if ($node->comment && $view_mode == 'full' && node_is_page($node) && empty($node->in_preview)) {
      $node->content['comments'] = comment_node_page_additions($node);
    }
  }
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
