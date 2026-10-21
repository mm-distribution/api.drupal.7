# CommentInterfaceTest::setEnvironment()

- **Type:** Method
- **File:** [`modules/comment/comment.test`](../_file.md), lines 741–847 · [local source](../../../../../source/modules/comment/comment.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test#L741-L847)
- **Class:** [CommentInterfaceTest](../CommentInterfaceTest.md)
- **Module/theme:** comment

## Signature

```php
function setEnvironment(array $info)
```

## Documentation

```text
Re-configures the environment, module settings, and user permissions.

@param $info
  An associative array describing the environment to setup:
  - Environment conditions:
    - authenticated: Boolean whether to test with $this->web_user or
      anonymous.
    - comment count: Boolean whether to test with a new/unread comment on
      $this->node or no comments.
  - Configuration settings:
    - form: COMMENT_FORM_BELOW or COMMENT_FORM_SEPARATE_PAGE.
    - user_register: USER_REGISTER_ADMINISTRATORS_ONLY or
      USER_REGISTER_VISITORS.
    - contact: COMMENT_ANONYMOUS_MAY_CONTACT or
      COMMENT_ANONYMOUS_MAYNOT_CONTACT.
    - comments: COMMENT_NODE_OPEN, COMMENT_NODE_CLOSED, or
      COMMENT_NODE_HIDDEN.
  - User permissions:
    These are granted or revoked for the user, according to the
    'authenticated' flag above. Pass 0 or 1 as parameter values. See
    user_role_change_permissions().
    - access comments
    - post comments
    - skip comment approval
    - edit own comments
```

## Code

```php
  function setEnvironment(array $info) {
    static $current;

    // Apply defaults to initial environment.
    if (!isset($current)) {
      $current = array(
        'authenticated' => FALSE,
        'comment count' => FALSE,
        'form' => COMMENT_FORM_BELOW,
        'user_register' => USER_REGISTER_VISITORS,
        'contact' => COMMENT_ANONYMOUS_MAY_CONTACT,
        'comments' => COMMENT_NODE_OPEN,
        'access comments' => 0,
        'post comments' => 0,
        // Enabled by default, because it's irrelevant for this test.
        'skip comment approval' => 1,
        'edit own comments' => 0,
      );
    }
    // Complete new environment with current environment.
    $info = array_merge($current, $info);

    // Change environment conditions.
    if ($current['authenticated'] != $info['authenticated']) {
      if ($this->loggedInUser) {
        $this->drupalLogout();
      }
      else {
        $this->drupalLogin($this->web_user);
      }
    }
    if ($current['comment count'] != $info['comment count']) {
      if ($info['comment count']) {
        // Create a comment via CRUD API functionality, since
        // $this->postComment() relies on actual user permissions.
        $comment = (object) array(
          'cid' => NULL,
          'nid' => $this->node->nid,
          'node_type' => $this->node->type,
          'pid' => 0,
          'uid' => 0,
          'status' => COMMENT_PUBLISHED,
          'subject' => $this->randomName(),
          'hostname' => ip_address(),
          'language' => LANGUAGE_NONE,
          'comment_body' => array(LANGUAGE_NONE => array($this->randomName())),
        );
        comment_save($comment);
        $this->comment = $comment;

        // comment_num_new() relies on node_last_viewed(), so ensure that no one
        // has seen the node of this comment.
        db_delete('history')->condition('nid', $this->node->nid)->execute();
      }
      else {
        $cids = db_query("SELECT cid FROM {comment}")->fetchCol();
        comment_delete_multiple($cids);
        unset($this->comment);
      }
    }

    // Change comment settings.
    variable_set('comment_form_location_' . $this->node->type, $info['form']);
    variable_set('comment_anonymous_' . $this->node->type, $info['contact']);
    if ($this->node->comment != $info['comments']) {
      $this->node->comment = $info['comments'];
      node_save($this->node);
    }

    // Change user settings.
    variable_set('user_register', $info['user_register']);

    // Change user permissions.
    $rid = ($this->loggedInUser ? DRUPAL_AUTHENTICATED_RID : DRUPAL_ANONYMOUS_RID);
    $perms = array_intersect_key($info, array('access comments' => 1, 'post comments' => 1, 'skip comment approval' => 1, 'edit own comments' => 1));
    user_role_change_permissions($rid, $perms);

    // Output verbose debugging information.
    // @see DrupalTestCase::error()
    $t_form = array(
      COMMENT_FORM_BELOW => 'below',
      COMMENT_FORM_SEPARATE_PAGE => 'separate page',
    );
    $t_contact = array(
      COMMENT_ANONYMOUS_MAY_CONTACT => 'optional',
      COMMENT_ANONYMOUS_MAYNOT_CONTACT => 'disabled',
      COMMENT_ANONYMOUS_MUST_CONTACT => 'required',
    );
    $t_comments = array(
      COMMENT_NODE_OPEN => 'open',
      COMMENT_NODE_CLOSED => 'closed',
      COMMENT_NODE_HIDDEN => 'hidden',
    );
    $verbose = $info;
    $verbose['form'] = $t_form[$info['form']];
    $verbose['contact'] = $t_contact[$info['contact']];
    $verbose['comments'] = $t_comments[$info['comments']];
    $message = t('Changed environment:<pre>@verbose</pre>', array(
      '@verbose' => var_export($verbose, TRUE),
    ));
    $this->assert('debug', $message, 'Debug');

    // Update current environment.
    $current = $info;

    return $info;
  }
```

---
_Drupal 7.103 · [modules/comment/comment.test](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.test) · Licensed GPL-2.0-or-later (see LICENSE)._
