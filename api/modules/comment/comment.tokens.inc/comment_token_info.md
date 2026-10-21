# comment_token_info()

- **Type:** Function
- **File:** [`modules/comment/comment.tokens.inc`](_file.md), lines 11–100 · [local source](../../../../source/modules/comment/comment.tokens.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.tokens.inc#L11-L100)
- **Module/theme:** comment
- **Implements:** [hook_token_info()](../../system/system.api.php/hook_token_info.md)

## Signature

```php
function comment_token_info()
```

## Documentation

```text
Implements hook_token_info().
```

## Code

```php
function comment_token_info() {
  $type = array(
    'name' => t('Comments'),
    'description' => t('Tokens for comments posted on the site.'),
    'needs-data' => 'comment',
  );

  // Comment-related tokens for nodes
  $node['comment-count'] = array(
    'name' => t("Comment count"),
    'description' => t("The number of comments posted on a node."),
  );
  $node['comment-count-new'] = array(
    'name' => t("New comment count"),
    'description' => t("The number of comments posted on a node since the reader last viewed it."),
  );

  // Core comment tokens
  $comment['cid'] = array(
    'name' => t("Comment ID"),
    'description' => t("The unique ID of the comment."),
  );
  $comment['hostname'] = array(
    'name' => t("IP Address"),
    'description' => t("The IP address of the computer the comment was posted from."),
  );
  $comment['name'] = array(
    'name' => t("Name"),
    'description' => t("The name left by the comment author."),
  );
  $comment['mail'] = array(
    'name' => t("Email address"),
    'description' => t("The email address left by the comment author."),
  );
  $comment['homepage'] = array(
    'name' => t("Home page"),
    'description' => t("The home page URL left by the comment author."),
  );
  $comment['title'] = array(
    'name' => t("Title"),
    'description' => t("The title of the comment."),
  );
  $comment['body'] = array(
    'name' => t("Content"),
    'description' => t("The formatted content of the comment itself."),
  );
  $comment['url'] = array(
    'name' => t("URL"),
    'description' => t("The URL of the comment."),
  );
  $comment['edit-url'] = array(
    'name' => t("Edit URL"),
    'description' => t("The URL of the comment's edit page."),
  );

  // Chained tokens for comments
  $comment['created'] = array(
    'name' => t("Date created"),
    'description' => t("The date the comment was posted."),
    'type' => 'date',
  );
  $comment['changed'] = array(
    'name' => t("Date changed"),
    'description' => t("The date the comment was most recently updated."),
    'type' => 'date',
  );
  $comment['parent'] = array(
    'name' => t("Parent"),
    'description' => t("The comment's parent, if comment threading is active."),
    'type' => 'comment',
  );
  $comment['node'] = array(
    'name' => t("Node"),
    'description' => t("The node the comment was posted to."),
    'type' => 'node',
  );
  $comment['author'] = array(
    'name' => t("Author"),
    'description' => t("The author of the comment, if they were logged in."),
    'type' => 'user',
  );

  return array(
    'types' => array('comment' => $type),
    'tokens' => array(
      'node' => $node,
      'comment' => $comment,
    ),
  );
}
```

---
_Drupal 7.103 · [modules/comment/comment.tokens.inc](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.tokens.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
