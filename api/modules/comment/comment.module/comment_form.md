# comment_form()

- **Type:** Function
- **File:** [`modules/comment/comment.module`](_file.md), lines 1856–2066 · [local source](../../../../source/modules/comment/comment.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module#L1856-L2066)
- **Module/theme:** comment
- **Topics:** [forms](../../../topics/forms.md)

## Signature

```php
function comment_form($form, &$form_state, $comment)
```

## Documentation

```text
Generate the basic commenting form, for appending to a node or display on a separate page.

@see comment_form_validate()
@see comment_form_submit()

@ingroup forms
```

## Code

```php
function comment_form($form, &$form_state, $comment) {
  global $user;

  // During initial form build, add the comment entity to the form state for
  // use during form building and processing. During a rebuild, use what is in
  // the form state.
  if (!isset($form_state['comment'])) {
    $defaults = array(
      'name' => '',
      'mail' => '',
      'homepage' => '',
      'subject' => '',
      'comment' => '',
      'cid' => NULL,
      'pid' => NULL,
      'language' => LANGUAGE_NONE,
      'uid' => 0,
    );
    foreach ($defaults as $key => $value) {
      if (!isset($comment->$key)) {
        $comment->$key = $value;
      }
    }
    $form_state['comment'] = $comment;
  }
  else {
    $comment = $form_state['comment'];
  }

  $node = node_load($comment->nid);
  $form['#node'] = $node;

  // Use #comment-form as unique jump target, regardless of node type.
  $form['#id'] = drupal_html_id('comment_form');
  $form['#attributes']['class'][] = 'comment-form';
  $form['#theme'] = array('comment_form__node_' . $node->type, 'comment_form');

  $anonymous_contact = variable_get('comment_anonymous_' . $node->type, COMMENT_ANONYMOUS_MAYNOT_CONTACT);
  $is_admin = (!empty($comment->cid) && user_access('administer comments'));

  if (!$user->uid && $anonymous_contact != COMMENT_ANONYMOUS_MAYNOT_CONTACT) {
    $form['#attached']['library'][] = array('system', 'jquery.cookie');
    $form['#attributes']['class'][] = 'user-info-from-cookie';
  }

  // If not replying to a comment, use our dedicated page callback for new
  // comments on nodes.
  if (empty($comment->cid) && empty($comment->pid)) {
    $form['#action'] = url('comment/reply/' . $comment->nid);
  }

  if (isset($form_state['comment_preview'])) {
    $form += $form_state['comment_preview'];
  }

  // Display author information in a fieldset for comment moderators.
  if ($is_admin) {
    $form['author'] = array(
      '#type' => 'fieldset',
      '#title' => t('Administration'),
      '#collapsible' => TRUE,
      '#collapsed' => TRUE,
      '#weight' => -2,
    );
  }
  else {
    // Sets the author form elements above the subject.
    $form['author'] = array(
      '#weight' => -2,
    );
  }

  // Prepare default values for form elements.
  if ($is_admin) {
    $author = (!$comment->uid && $comment->name ? $comment->name : $comment->registered_name);
    $status = (isset($comment->status) ? $comment->status : COMMENT_NOT_PUBLISHED);
  }
  else {
    if ($user->uid) {
      $author = $user->name;
    }
    else {
      $author = ($comment->name ? $comment->name : '');
    }
    $status = (user_access('skip comment approval') ? COMMENT_PUBLISHED : COMMENT_NOT_PUBLISHED);
  }

  $date = '';
  if ($comment->cid) {
    $date = !empty($comment->date) ? $comment->date : format_date($comment->created, 'custom', 'Y-m-d H:i:s O');
  }

  // Add the author name field depending on the current user.
  if ($is_admin) {
    $form['author']['name'] = array(
      '#type' => 'textfield',
      '#title' => t('Authored by'),
      '#default_value' => $author,
      '#maxlength' => 60,
      '#size' => 30,
      '#description' => t('Leave blank for %anonymous.', array('%anonymous' => variable_get('anonymous', t('Anonymous')))),
      '#autocomplete_path' => 'user/autocomplete',
    );
  }
  elseif ($user->uid) {
    $form['author']['_author'] = array(
      '#type' => 'item',
      '#title' => t('Your name'),
      '#markup' => theme('username', array('account' => $user)),
    );
    $form['author']['name'] = array(
      '#type' => 'value',
      '#value' => $author,
    );
  }
  else {
    $form['author']['name'] = array(
      '#type' => 'textfield',
      '#title' => t('Your name'),
      '#default_value' => $author,
      '#required' => (!$user->uid && $anonymous_contact == COMMENT_ANONYMOUS_MUST_CONTACT),
      '#maxlength' => 60,
      '#size' => 30,
    );
  }

  // Add author e-mail and homepage fields depending on the current user.
  $form['author']['mail'] = array(
    '#type' => 'textfield',
    '#title' => t('E-mail'),
    '#default_value' => $comment->mail,
    '#required' => (!$user->uid && $anonymous_contact == COMMENT_ANONYMOUS_MUST_CONTACT),
    '#maxlength' => 64,
    '#size' => 30,
    '#description' => t('The content of this field is kept private and will not be shown publicly.'),
    '#access' => $is_admin || (!$user->uid && $anonymous_contact != COMMENT_ANONYMOUS_MAYNOT_CONTACT),
  );
  $form['author']['homepage'] = array(
    '#type' => 'textfield',
    '#title' => t('Homepage'),
    '#default_value' => $comment->homepage,
    '#maxlength' => 255,
    '#size' => 30,
    '#access' => $is_admin || (!$user->uid && $anonymous_contact != COMMENT_ANONYMOUS_MAYNOT_CONTACT),
  );

  // Add administrative comment publishing options.
  $form['author']['date'] = array(
    '#type' => 'textfield',
    '#title' => t('Authored on'),
    '#default_value' => $date,
    '#maxlength' => 25,
    '#size' => 20,
    '#access' => $is_admin,
  );
  $form['author']['status'] = array(
    '#type' => 'radios',
    '#title' => t('Status'),
    '#default_value' => $status,
    '#options' => array(
      COMMENT_PUBLISHED => t('Published'),
      COMMENT_NOT_PUBLISHED => t('Not published'),
    ),
    '#access' => $is_admin,
  );

  $form['subject'] = array(
    '#type' => 'textfield',
    '#title' => t('Subject'),
    '#maxlength' => 64,
    '#default_value' => $comment->subject,
    '#access' => variable_get('comment_subject_field_' . $node->type, 1) == 1,
    '#weight' => -1,
  );

  // Used for conditional validation of author fields.
  $form['is_anonymous'] = array(
    '#type' => 'value',
    '#value' => ($comment->cid ? !$comment->uid : !$user->uid),
  );

  // Add internal comment properties.
  foreach (array('cid', 'pid', 'nid', 'language', 'uid') as $key) {
    $form[$key] = array('#type' => 'value', '#value' => $comment->$key);
  }
  $form['node_type'] = array('#type' => 'value', '#value' => 'comment_node_' . $node->type);

  // Only show the save button if comment previews are optional or if we are
  // already previewing the submission.
  $form['actions'] = array('#type' => 'actions');
  $form['actions']['submit'] = array(
    '#type' => 'submit',
    '#value' => t('Save'),
    '#access' => ($comment->cid && user_access('administer comments')) || variable_get('comment_preview_' . $node->type, DRUPAL_OPTIONAL) != DRUPAL_REQUIRED || isset($form_state['comment_preview']),
    '#weight' => 19,
  );
  $form['actions']['preview'] = array(
    '#type' => 'submit',
    '#value' => t('Preview'),
    '#access' => (variable_get('comment_preview_' . $node->type, DRUPAL_OPTIONAL) != DRUPAL_DISABLED),
    '#weight' => 20,
    '#submit' => array('comment_form_build_preview'),
  );

  // Attach fields.
  $comment->node_type = 'comment_node_' . $node->type;
  $langcode = entity_language('comment', $comment);
  field_attach_form('comment', $comment, $form, $form_state, $langcode);

  return $form;
}
```

---
_Drupal 7.103 · [modules/comment/comment.module](https://github.com/drupal/drupal/blob/7.103/modules/comment/comment.module) · Licensed GPL-2.0-or-later (see LICENSE)._
