# comment_tokens()

- **Type:** Function
- **File:** [`modules/comment/comment.tokens.inc`](_file.md), lines 105–243 · [local source](../../../../source/modules/comment/comment.tokens.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.tokens.inc#L105-L243)
- **Module/theme:** comment
- **Implements:** [hook_tokens()](../../system/system.api.php/hook_tokens.md)

## Signature

```php
function comment_tokens($type, $tokens, array $data = array(), array $options = array())
```

## Documentation

```text
Implements hook_tokens().
```

## Code

```php
function comment_tokens($type, $tokens, array $data = array(), array $options = array()) {
  $url_options = array('absolute' => TRUE);
  if (isset($options['language'])) {
    $url_options['language'] = $options['language'];
    $language_code = $options['language']->language;
  }
  else {
    $language_code = NULL;
  }
  $sanitize = !empty($options['sanitize']);

  $replacements = array();

  if ($type == 'comment' && !empty($data['comment'])) {
    $comment = $data['comment'];

    foreach ($tokens as $name => $original) {
      switch ($name) {
        // Simple key values on the comment.
        case 'cid':
          $replacements[$original] = $comment->cid;
          break;

        // Poster identity information for comments
        case 'hostname':
          $replacements[$original] = $sanitize ? check_plain($comment->hostname) : $comment->hostname;
          break;

        case 'name':
          $name = ($comment->uid == 0) ? variable_get('anonymous', t('Anonymous')) : $comment->name;
          $replacements[$original] = $sanitize ? filter_xss($name) : $name;
          break;

        case 'mail':
          if ($comment->uid != 0) {
            $account = user_load($comment->uid);
            $mail = $account->mail;
          }
          else {
            $mail = $comment->mail;
          }
          $replacements[$original] = $sanitize ? check_plain($mail) : $mail;
          break;

        case 'homepage':
          $replacements[$original] = $sanitize ? check_url($comment->homepage) : $comment->homepage;
          break;

        case 'title':
          $replacements[$original] = $sanitize ? filter_xss($comment->subject) : $comment->subject;
          break;

        case 'body':
          if ($items = field_get_items('comment', $comment, 'comment_body', $language_code)) {
            $instance = field_info_instance('comment', 'body', 'comment_body');
            $field_langcode = field_language('comment', $comment, 'comment_body', $language_code);
            $replacements[$original] = $sanitize ? _text_sanitize($instance, $field_langcode, $items[0], 'value') : $items[0]['value'];
          }
          break;

        // Comment related URLs.
        case 'url':
          $url_options['fragment']  = 'comment-' . $comment->cid;
          $replacements[$original] = url('comment/' . $comment->cid, $url_options);
          break;

        case 'edit-url':
          $url_options['fragment'] = NULL;
          $replacements[$original] = url('comment/' . $comment->cid . '/edit', $url_options);
          break;

        // Default values for the chained tokens handled below.
        case 'author':
          $replacements[$original] = $sanitize ? filter_xss($comment->name) : $comment->name;
          break;

        case 'parent':
          if (!empty($comment->pid)) {
            $parent = comment_load($comment->pid);
            $replacements[$original] = $sanitize ? filter_xss($parent->subject) : $parent->subject;
          }
          break;

        case 'created':
          $replacements[$original] = format_date($comment->created, 'medium', '', NULL, $language_code);
          break;

        case 'changed':
          $replacements[$original] = format_date($comment->changed, 'medium', '', NULL, $language_code);
          break;

        case 'node':
          $node = node_load($comment->nid);
          $title = $node->title;
          $replacements[$original] = $sanitize ? filter_xss($title) : $title;
          break;
      }
    }

    // Chained token relationships.
    if ($node_tokens = token_find_with_prefix($tokens, 'node')) {
      $node = node_load($comment->nid);
      $replacements += token_generate('node', $node_tokens, array('node' => $node), $options);
    }

    if ($date_tokens = token_find_with_prefix($tokens, 'created')) {
      $replacements += token_generate('date', $date_tokens, array('date' => $comment->created), $options);
    }

    if ($date_tokens = token_find_with_prefix($tokens, 'changed')) {
      $replacements += token_generate('date', $date_tokens, array('date' => $comment->changed), $options);
    }

    if (($parent_tokens = token_find_with_prefix($tokens, 'parent')) && $parent = comment_load($comment->pid)) {
      $replacements += token_generate('comment', $parent_tokens, array('comment' => $parent), $options);
    }

    if (($author_tokens = token_find_with_prefix($tokens, 'author')) && $account = user_load($comment->uid)) {
      $replacements += token_generate('user', $author_tokens, array('user' => $account), $options);
    }
  }
  elseif ($type == 'node' & !empty($data['node'])) {
    $node = $data['node'];

    foreach ($tokens as $name => $original) {
      switch($name) {
        case 'comment-count':
          $replacements[$original] = $node->comment_count;
          break;

        case 'comment-count-new':
          $replacements[$original] = comment_num_new($node->nid);
          break;
      }
    }
  }

  return $replacements;
}
```

---
_Drupal 7.103 · [modules/comment/comment.tokens.inc](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.tokens.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
